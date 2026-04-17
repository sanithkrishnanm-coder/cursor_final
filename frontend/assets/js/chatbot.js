function appendChatMessage(container, text, type) {
  const bubble = document.createElement("div");
  bubble.className = `chat-bubble ${type === "user" ? "chat-user" : "chat-bot"}`;
  bubble.textContent = text;
  container.appendChild(bubble);
  container.scrollTop = container.scrollHeight;
}

async function sendChatMessage() {
  const input = document.getElementById("chat-input");
  const messagesEl = document.getElementById("chat-messages");
  const statusEl = document.getElementById("chat-status");
  const message = input.value.trim();
  if (!message) return;

  appendChatMessage(messagesEl, message, "user");
  input.value = "";
  statusEl.textContent = "Assistant is typing...";
  const data = await apiRequest("/chat/message", "POST", { message }, true);
  if (data.success) {
    appendChatMessage(messagesEl, data.data.reply, "bot");
    statusEl.textContent = "Online";
  } else {
    appendChatMessage(messagesEl, data.message || "Unable to process request.", "bot");
    statusEl.textContent = "Offline";
  }
}

async function loadChatSuggestions() {
  const suggestionsEl = document.getElementById("chat-suggestions");
  const data = await apiRequest("/chat/suggestions");
  if (!data.success) return;
  suggestionsEl.innerHTML = "";
  data.data.forEach((item) => {
    const btn = document.createElement("button");
    btn.className = "chip btn-outline";
    btn.textContent = item;
    btn.type = "button";
    btn.addEventListener("click", () => {
      document.getElementById("chat-input").value = item;
      sendChatMessage();
    });
    suggestionsEl.appendChild(btn);
  });
}

function initChatbotPage() {
  const messagesEl = document.getElementById("chat-messages");
  appendChatMessage(
    messagesEl,
    "Hi! I am your Career Guidance Assistant. Ask about careers, mentors, bookings, or goals.",
    "bot"
  );
  loadChatSuggestions();

  document.getElementById("chat-send-btn").addEventListener("click", sendChatMessage);
  document.getElementById("chat-input").addEventListener("keydown", (event) => {
    if (event.key === "Enter") sendChatMessage();
  });
}
