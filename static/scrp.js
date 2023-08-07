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
      document.getElementById('response').innerText = data.answer;
  })
  .catch(error => {
      console.error('Error:', error);
  });
}