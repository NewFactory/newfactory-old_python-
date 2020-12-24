  function menuToggle()
  {
    const toggleMenu = document.querySelector('.toggle');
    toggleMenu.classList.toggle('active');
    const section = document.querySelector('section');
    section.classList.toggle('active');
  }
