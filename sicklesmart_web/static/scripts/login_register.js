document.addEventListener('DOMContentLoaded', function () {
  const loginButton = document.querySelector('.home-login');
  const registerButton = document.querySelector(
    '.home-btn-group button:not(.home-login)'
  );

  // Add click event listener to login button
  loginButton.addEventListener('click', function () {
    // Redirect to the login page
    window.location.href = 'login';
  });

  // Add click event listener to register button
  registerButton.addEventListener('click', function () {
    // Redirect to the register page
    window.location.href = 'register';
  });
});
