const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

let conversationHistory = [
    { role: "system", content: "You are a helpful assistant." }
];

function addMessage(message, isUser = false) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.classList.add(isUser ? 'user-message' : 'bot-message');
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function sendMessage() {
    const message = userInput.value.trim();
    if (message) {
        addMessage(message, true);
        userInput.value = '';

        try {
            const response = await fetch('http://localhost:11434/v1/chat/completions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    model: "llama3.1",
                    messages: [
                        ...conversationHistory,
                        { role: "user", content: message }
                    ]
                }),
            });

            if (!response.ok) {
                throw new Error('Failed to get response from Ollama server');
            }

            const data = await response.json();
            const botResponse = data.choices[0].message.content;
            addMessage(botResponse);

            // Update conversation history
            conversationHistory.push({ role: "user", content: message });
            conversationHistory.push({ role: "assistant", content: botResponse });

        } catch (error) {
            console.error('Error:', error);
            addMessage('Sorry, there was an error processing your request.');
        }
    }
}

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});