function saveCharacter() {
  const selectedClass = document.querySelector('input[name="class"]:checked');

  if (!selectedClass) {
    alert("Choose a class before entering the dungeon.");
    return;
  }

  const stats = {
    strength: Number(document.getElementById("str").value),
    dexterity: Number(document.getElementById("dex").value),
    intelligence: Number(document.getElementById("int").value),
    charisma: Number(document.getElementById("cha").value),
  };

  const totalPoints = Object.values(stats).reduce((a, b) => a + b, 0);

  if (totalPoints > 27) {
    alert("You have assigned too many stat points. Max is 27.");
    return;
  }

  const character = {
    name: "Adventurer",  // Default name; can be enhanced later
    class: selectedClass.value,
    stats
  };

  localStorage.setItem("playerCharacter", JSON.stringify(character));

  // Navigate to the game
  alert("Your fate is sealed.");
  window.location.href = "play.html";
}

