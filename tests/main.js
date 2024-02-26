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
});
