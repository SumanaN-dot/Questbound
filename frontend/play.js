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
    const res = await fetch(`${BACKEND_BASE}/session`, { method: "POST" });
    if (!res.ok) {
      console.warn("Failed to create backend session:", res.status);
      return;
    }
    const data = await res.json();
    sessionId = data.session_id;
    console.log("Backend session created:", sessionId);
  } catch (err) {
    console.warn("Backend unreachable, will use local responses:", err.message);
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

  // Try backend first
  if (sessionId) {
    try {
      const payload = {
        player_name: character.name || "Wanderer",
        action: text,
      };

      console.log("Sending to backend:", payload);
      const res = await fetch(`${BACKEND_BASE}/session/${sessionId}/action`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (res.ok) {
        const data = await res.json();
        console.log("Backend response:", data);
        const narrative = data.narrative || "The dungeon remains silent...";
        addToLog("dm", narrative);
        // Also show the roll result
        if (data.outcome) {
          const rollText = `[Roll: ${data.outcome.roll}, Success: ${data.outcome.success}, HP: ${data.state.hp}]`;
          console.log(rollText);
        }
        return;
      } else {
        console.warn("Backend action failed:", res.status);
        const errorText = await res.text();
        console.warn("Error details:", errorText);
      }
    } catch (err) {
      console.warn("Backend request failed:", err.message);
    }
  } else {
    console.warn("No session ID - backend not connected");
  }

  // Fallback to local response
  console.log("Using local fallback response");
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
