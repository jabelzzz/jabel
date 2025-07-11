function initializeNavigation() {
  const navLinks = document.querySelectorAll(".nav-link");
  const sections = document.querySelectorAll(".section");

  // Hide all sections except the first one
  sections.forEach((section, index) => {
    if (index !== 0) section.style.display = "none";
  });

  // Handle navigation
  navLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const targetId = link.getAttribute("href").slice(1);

      // Update active state of links
      navLinks.forEach((l) => l.classList.remove("active"));
      link.classList.add("active");

      // Show/hide sections with animation
      sections.forEach((section) => {
        if (section.id === targetId) {
          section.style.display = "block";
          section.style.animation = "fadeIn 0.3s ease";
        } else {
          section.style.display = "none";
        }
      });
    });
  });
}
