// OPEN MODALS
function openModal(id) {
  document.getElementById(id).style.display = "block";
}

// CLOSE MODALS
function closeModal(id) {
  document.getElementById(id).style.display = "none";
}

// CLOSE WHEN CLICKING OUTSIDE MODAL
window.addEventListener("click", (event) => {
  document.querySelectorAll(".modal").forEach((modal) => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });
});

// LOGIN FORM HANDLER
document.getElementById("loginForm")?.addEventListener("submit", (e) => {
  e.preventDefault();
  alert("The Dungeon recognizes you... enter wisely.");
});

// SIGNUP FORM HANDLER
document.getElementById("signupForm")?.addEventListener("submit", (e) => {
  e.preventDefault();
  alert("Your fate has been bound to the Dungeon.");
});

// OPTIONAL: HERO BUTTON FLAVOR (non-breaking)
document
  .querySelector(".hero .blood-btn")
  ?.addEventListener("click", () => {
    console.log("A new journey begins...");
  });

