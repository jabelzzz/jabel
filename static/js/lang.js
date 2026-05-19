const translations = {
  en: {
    navigation: {
      about: "About me",
      skills: "Skills",
      projects: "Projects",
    },
    about: {
      title: "About me",
      lead: "Hi! I'm Jabel, I'm passionate about technology.<br><br>I've been working as a SysAdmin for over 5 years, where I've learned to design, implement, and maintain robust infrastructures (and solve problems when everything breaks down, which is almost just as important).<br><br>Additionally, I also have training and experience in backend development and I'm currently expanding my skills by learning the DevOps culture, which allows me to have a more comprehensive view of the entire software lifecycle.",
      secondary:
        "I like to stay up to date with new tools and trends, share ideas with the team and always look for practical and efficient solutions. In short: I'm curious, proactive and I enjoy both the terminal and a good coffee while debugging something that doesn't want to work.",
    },
    skills: {
      title: "Skills",
      backend: "Backend Development",
      frontend: "Frontend Development",
      devops: "SysAdmin & DevOps",
      databases: "Databases",
      cicd: "CI/CD & Tools",
    },
    projects: {
      title: "Projects",
    },
    profile: {
      role: "🧑🏻‍💻 SysAdmin & Backend Developer<br>📍 Gran Canaria 🇮🇨",
    },
  },
  es: {
    navigation: {
      about: "Sobre mí",
      skills: "Habilidades",
      projects: "Proyectos",
    },
    about: {
      title: "Sobre mí",
      lead: "¡Hola! Soy Jabel, soy un apasionado de la tecnología.<br /><br />Llevo más de 5 años trabajando como SysAdmin, donde he aprendido a diseñar, implementar y mantener infraestructuras sólidas (y a resolver problemas cuando todo se rompe, que es casi igual de importante).<br /><br />Además,también cuento con formación y experiencia en el desarrollo backend y actualmente estoy ampliando mis habilidades aprendiendo la cultura DevOps, lo que me permite tener una visión más completa de todo el ciclo de vida del software.",
      secondary:
        " Me gusta mantenerme al día con nuevas herramientas y tendencias, compartir ideas con el equipo y buscar siempre soluciones prácticas y eficientes. En pocas palabras: soy curioso, proactivo y disfruto tanto de la terminal como de un buen café mientras debuggeo algo que no quiere funcionar.",
    },
    skills: {
      title: "Habilidades",
      backend: "Desarrollo Backend",
      frontend: "Desarrollo Frontend",
      devops: "SysAdmin & DevOps",
      databases: "Bases de datos",
      cicd: "CI/CD & Tools",
    },
    projects: {
      title: "Proyectos",
    },
    profile: {
      role: "🧑🏻‍💻 SysAdmin / DevOps<br>📍 Gran Canaria 🇮🇨",
    },
  },
};

function initializeLanguage() {
  // Detect browser language
  const userLang = navigator.language.split("-")[0];
  const currentLang = userLang in translations ? userLang : "es";

  // Apply translations
  updateContent(currentLang);
}

function updateContent(lang) {
  const t = translations[lang];

  // Navigation links
  document.querySelectorAll(".nav-link").forEach((link) => {
    const section = link.getAttribute("href").slice(1);
    if (t.navigation[section]) {
      link.textContent = t.navigation[section];
    }
  });

  // About section
  const aboutSection = document.querySelector("#about");
  if (aboutSection) {
    aboutSection.querySelector(".title").textContent = t.about.title;
    aboutSection.querySelector(".lead-text").innerHTML = t.about.lead;
    aboutSection.querySelector(".secondary-text").textContent =
      t.about.secondary;
  }

  // Skills section
  const skillsSection = document.querySelector("#skills");
  if (skillsSection) {
    skillsSection.querySelector(".title").textContent = t.skills.title;
    skillsSection.querySelectorAll(".category-title").forEach((el) => {
      const category = el.getAttribute("data-category");
      if (t.skills[category]) {
        el.textContent = t.skills[category];
      }
    });
  }

  // Projects section
  const projectsSection = document.querySelector("#projects");
  if (projectsSection) {
    projectsSection.querySelector(".title").textContent = t.projects.title;
  }

  // Profile
  const profileRole = document.querySelector(".profile-role");
  if (profileRole) {
    profileRole.innerHTML = t.profile.role;
  }
}

// Initialize language on page load
document.addEventListener("DOMContentLoaded", initializeLanguage);
