function appendChat(sender, message) {
  var chatContainer = document.getElementById('chatContainer');
  var chatDiv = document.createElement('div');
  chatDiv.classList.add('chat-card', 'card');

  var chatCardBody = document.createElement('div');
  chatCardBody.classList.add('card-body');

  var chatMessage = document.createElement('p');
  chatMessage.classList.add('card-text');

  // Menghilangkan "Chatbot" dan "You" dari chat
  if (sender !== 'Chatbot' && sender !== 'You') {
      chatMessage.innerHTML = "<strong>" + sender + ":</strong> " + message;
  } else {
      chatMessage.innerText = message;
  }

  chatCardBody.appendChild(chatMessage);
  chatDiv.appendChild(chatCardBody);

  // Cek apakah pesan dari user atau chatbot
  if (sender === 'You') {
      chatDiv.classList.add('user-message');
  } else if (sender === 'Chatbot') {
      chatDiv.classList.add('chatbot-message');
  }

  chatContainer.appendChild(chatDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

function getAnswer() {
  // Get user input
  var question = document.getElementById('question').value;

  // Call API or use Ajax to get the response from the backend
  fetch('/get_response', {
      method: 'POST',
      body: JSON.stringify({ question: question }),
      headers: {
          'Content-Type': 'application/json'
      }
  })
  .then(response => response.json())
  .then(data => {
      // Update the response element with the chatbot's answer
      appendChat('You', question);
      appendChat('Chatbot', data.answer);

      // Clear input field
      document.getElementById('question').value = '';
  })
  .catch(error => {
      console.error('Error:', error);
  });
}

 // Fungsi untuk memulai percakapan dengan kalimat awal
 function startChat() {
  var welcomeMessage = "Halo, perkenalkan namaku Tensibot!! Gimana kabar kamu hari ini?";
  appendChat('Chatbot', welcomeMessage);
}
startChat();