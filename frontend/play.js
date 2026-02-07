const gameLog = document.getElementById("game-log");
const input = document.getElementById("player-input");

// Load character
const character = JSON.parse(localStorage.getItem("playerCharacter"));

function sendPrompt() {
  const text = input.value.trim();
  if (!text) return;

  addToLog("player", text);
  input.value = "";

  // Placeholder AI response
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

// TEMP AI logic (replace later)
function generateMockResponse(playerText) {
  return `The Dungeon Master considers your action carefully.

As a ${character.class}, your instincts guide you. The dungeon reacts to "${playerText}", and something stirs in the darkness...`;
}
