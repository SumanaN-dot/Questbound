const gameLog = document.getElementById("game-log");
const input = document.getElementById("player-input");

// Load character with safe fallback
let character = null;
try {
  const saved = localStorage.getItem("playerCharacter");
  character = saved ? JSON.parse(saved) : null;
} catch (e) {
  console.warn("Failed to parse character from localStorage:", e);
  character = null;
}

if (!character) {
  character = { name: "Wanderer", class: "Adventurer" };
}

// Backend configuration
const BACKEND_BASE = "http://127.0.0.1:8000";
let sessionId = null;

// Initialize backend session on page load
async function initializeSession() {
  try {
    console.log("Attempting to create backend session...");
    const res = await fetch(`${BACKEND_BASE}/session`, { method: "POST" });
    if (!res.ok) {
      console.error("❌ Failed to create backend session. Status:", res.status);
      console.error("Response:", await res.text());
      return;
    }
    const data = await res.json();
    sessionId = data.session_id;
    console.log("✅ Backend session created:", sessionId);
  } catch (err) {
    console.error("❌ Backend unreachable:", err.message);
    console.error("Is the backend running on http://127.0.0.1:8000 ?");
    sessionId = null;
  }
}

// Initialize on load
initializeSession();

async function sendPrompt() {
  const text = input.value.trim();
  if (!text) return;

  addToLog("player", text);
  input.value = "";

  console.log("\n=== ACTION ATTEMPT ===");
  console.log("Action:", text);
  console.log("Session ID:", sessionId);

  // Try backend first
  if (!sessionId) {
    console.warn("❌ No session ID - backend not connected. Using fallback.");
    setTimeout(() => {
      const response = generateMockResponse(text);
      addToLog("dm", response);
    }, 600);
    return;
  }

  try {
    const payload = {
      player_name: character.name || "Wanderer",
      action: text,
    };

    console.log("📤 Sending to backend:", payload);
    const res = await fetch(`${BACKEND_BASE}/session/${sessionId}/action`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    console.log("📥 Backend response status:", res.status);

    if (res.ok) {
      const data = await res.json();
      console.log("✅ Backend returned data:", data);
      const narrative = data.narrative || "The dungeon remains silent...";
      console.log("Using narrative:", narrative);
      addToLog("dm", narrative);
      // Also show the roll result
      if (data.outcome) {
        const rollText = `[Roll: ${data.outcome.roll}/${data.outcome.difficulty}, Success: ${data.outcome.success}, HP: ${data.state.hp}]`;
        console.log(rollText);
      }
      return;
    } else {
      console.error("❌ Backend error status:", res.status);
      const errorText = await res.text();
      console.error("Error details:", errorText);
    }
  } catch (err) {
    console.error("❌ Backend request failed:", err.message);
    console.error(err);
  }

  // Fallback to local response
  console.warn("⚠️ Falling back to local mock response");
  setTimeout(() => {
    const response = generateMockResponse(text);
    addToLog("dm", response);
  }, 600);
}

function addToLog(type, text) {
  const p = document.createElement("p");
  p.className = type === "player" ? "player-text" : "dm-text";
  p.textContent = text;
  gameLog.appendChild(p);

  gameLog.scrollTop = gameLog.scrollHeight;
}

// Fallback AI logic (local response when backend is down)
function generateMockResponse(playerText) {
  return `The Dungeon Master considers your action carefully.\n\nAs a ${character.class}, your instincts guide you. The dungeon reacts to "${playerText}", and something stirs in the darkness...`;
}
