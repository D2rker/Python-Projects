let btn = document.querySelector("#btn");
let content = document.querySelector("#content");
let voice = document.querySelector("#voice");

function speak(text) {
    let text_speak = new SpeechSynthesisUtterance(text);
    text_speak.rate = 1;
    text_speak.pitch = 1;
    text_speak.volume = 1;
    text_speak.lang = "hi-GB";
    window.speechSynthesis.speak(text_speak);
}

function wishMe() {
    let day = new Date();
    let hours = day.getHours();
    if (hours >= 0 && hours < 12) {
        speak("Good Morning Sir");
    } else if (hours >= 12 && hours < 16) {
        speak("Good afternoon Sir");
    } else {
        speak("Good Evening Sir");
    }
}

let speechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition = new speechRecognition();

recognition.onresult = (event) => {
    let currentIndex = event.resultIndex;
    let transcript = event.results[currentIndex][0].transcript;
    content.innerText = transcript;
    takeCommand(transcript.toLowerCase());
};

btn.addEventListener("click", () => {
    recognition.start();
    voice.style.display = "block";
    btn.style.display = "none";
});

async function takeCommand(message) {
    voice.style.display = "none";
    btn.style.display = "flex";

    if (message.includes("hello") || message.includes("hey")) {
        speak("Hello sir, what can I help you with?");
    } else if (message.includes("who are you")) {
        speak("I am your virtual assistant, created by Ayush Sir.");
    } else if (message.includes("open youtube")) {
        speak("Opening YouTube...");
        window.open("https://youtube.com/", "_blank");
    } else if (message.includes("open google")) {
        speak("Opening Google...");
        window.open("https://google.com/", "_blank");
    } else if (message.includes("open facebook")) {
        speak("Opening Facebook...");
        window.open("https://facebook.com/", "_blank");
    } else if (message.includes("time")) {
        let time = new Date().toLocaleString(undefined, { hour: "numeric", minute: "numeric" });
        speak(`The time is ${time}`);
    } else if (message.includes("date")) {
        let date = new Date().toLocaleString(undefined, { day: "numeric", month: "short" });
        speak(`Today's date is ${date}`);
    } else {
        // Fallback to ChatGPT for other questions
        const chatResponse = await askChatGPT(question);
        speak(chatResponse);
    }
}

async function askChatGPT(question) {
    const apiKey = "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"; // Replace with your actual OpenAI API key
    const apiUrl = "https://api.openai.com/v1/completions";

    const requestBody = {
        model: "text-davinci-003", // Use "gpt-3.5-turbo" if supported
        prompt: question,
        max_tokens: 100,
        temperature: 0.7,
    };

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`,
            },
            body: JSON.stringify(requestBody),
        });

        const data = await response.json();
        if (data.choices && data.choices.length > 0) {
            return data.choices[0].text.trim();
        } else {
            return "I'm sorry, I couldn't get an answer to that.";
        }
    } catch (error) {
        console.error("Error calling ChatGPT:", error);
        return "I'm sorry, I couldn't get an answer right now. Please try again later.";
    }
}
