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




// OPTIONAL: HERO BUTTON FLAVOR (non-breaking)
document
  .querySelector(".hero .blood-btn")
  ?.addEventListener("click", () => {
    console.log("A new journey begins...");
  });

