#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  const burgerMenu = document.querySelector('.home-burger-menu');
  const mobileMenu = document.querySelector('.home-mobile-menu');
  const menuCloseIcon = document.querySelector('.home-menu-close');

  // Add click event listener to burger menu
  burgerMenu.addEventListener('click', function () {
    toggleMobileMenu();
  });

  // Add click event listener to menu close icon
  menuCloseIcon.addEventListener('click', function () {
    // Hide the mobile menu
    mobileMenu.style.display = 'none';
  });

  // Attach event listeners for delete buttons
  const deleteButtons = document.querySelectorAll('.close');
  deleteButtons.forEach((button) => {
    button.addEventListener('click', function () {
      const healthStatusId = parseInt(
        this.getAttribute('data-health-status-id'),
        10
      );
      deleteEntry(healthStatusId);
    });
  });

  // Function to toggle mobile menu
  function toggleMobileMenu() {
    // Check if the mobile menu is currently hidden
    if (mobileMenu.style.display === 'none' || !mobileMenu.style.display) {
      // Display the mobile menu
      mobileMenu.style.display = 'block';
    } else {
      // Hide the mobile menu
      mobileMenu.style.display = 'none';
    }
  }

  // Function to delete an entry
  function deleteEntry(healthStatusId) {
    fetch('/delete-entry', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ healthStatusId: healthStatusId }),
    })
      .then(() => {
        // Remove the deleted entry directly from the DOM
        const deletedEntry = document.getElementById(`entry-${healthStatusId}`);
        if (deletedEntry) {
          deletedEntry.remove();
        }
      })
      .catch((error) => {
        console.error('Error deleting entry:', error);
      });
  }

  // Ensure deleteEntry is available in the global scope
  window.deleteEntry = deleteEntry;
});
