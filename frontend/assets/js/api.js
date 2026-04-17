const API_BASE_URLS = [
  "https://career-guidance-backend-0g7p.onrender.com",
  "http://localhost:5000/api/v1"
];

function getToken() {
  return localStorage.getItem("token");
}

async function apiRequest(path, method = "GET", body = null, secured = false) {
  const headers = { "Content-Type": "application/json" };
  if (secured && getToken()) headers.Authorization = `Bearer ${getToken()}`;
  let lastError = null;
  for (const baseUrl of API_BASE_URLS) {
    try {
      const response = await fetch(`${baseUrl}${path}`, {
        method,
        headers,
        body: body ? JSON.stringify(body) : null
      });
      const text = await response.text();
      const data = text ? JSON.parse(text) : {};
      if (!response.ok) {
        return {
          success: false,
          message: data.message || `Request failed with status ${response.status}`
        };
      }
      return data;
    } catch (error) {
      lastError = error;
    }
  }
  return {
    success: false,
    message: "Unable to connect to backend server. Please start Flask API."
  };
}
