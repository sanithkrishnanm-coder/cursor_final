function navTemplate() {
  const token = localStorage.getItem("token");
  const userRaw = localStorage.getItem("user");
  let user = null;
  try {
    user = userRaw ? JSON.parse(userRaw) : null;
  } catch (error) {
    user = null;
  }
  const isLoggedIn = Boolean(token && user);
  const isAdmin = isLoggedIn && user.role === "admin";

  const authLinks = isLoggedIn
    ? `
      <a href="dashboard.html">Dashboard</a>
      <a href="profile.html">Profile</a>
      ${isAdmin ? `<a href="admin.html">Admin</a>` : ""}
      <a href="#" id="logout-link">Logout</a>
    `
    : `<a href="login.html">Login</a>`;

  return `
    <header>
      <nav>
        <a class="logo" href="index.html">CareerGuidance</a>
        <div class="nav-links">
          <a href="careers.html">Careers</a>
          <a href="mentors.html">Mentors</a>
          <a href="chatbot.html">Chatbot</a>
          ${authLinks}
        </div>
      </nav>
    </header>
  `;
}

function mountLayout(title, content) {
  document.body.innerHTML = `
    ${navTemplate()}
    <div class="container">
      <h1 class="page-title">${title}</h1>
      ${content}
    </div>
    <footer>Career Guidance Platform</footer>
  `;
  const logoutLink = document.getElementById("logout-link");
  if (logoutLink) {
    logoutLink.addEventListener("click", function (event) {
      event.preventDefault();
      localStorage.removeItem("token");
      localStorage.removeItem("user");
      window.location.href = "login.html";
    });
  }
}
