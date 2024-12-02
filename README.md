# Jarvis - Your AI Virtual Assistant 🚀

Jarvis is a smart virtual assistant built in Python, capable of performing various tasks such as opening websites, playing music, fetching weather information, answering queries using Wikipedia, and much more! Additionally, Jarvis integrates Gemini's AI capabilities to handle complex queries when no direct match is found in the codebase.

## Features

- **Website Access**: Open any website by simply speaking its name.
- **Music Player**: Play songs from your local music library file.
- **Weather Information**: Get current weather updates for any city.
- **Wikipedia Search**: Search for any topic and get summarized results.
- **Google Search**: Search for anything on Google and get the top results.
- **YouTube Search**: Look up videos on YouTube with ease.
- **Current Time**: Get the current time based on your system's time zone.
- **Gemini AI Integration**: Handles complex or undefined queries using Gemini AI (requires a Google API key).

## Requirements

Ensure you have the following installed:

- Python 3.8+
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository to your local machine:
   git clone https://github.com/imSyedMoinUddin/jarvis-virtual-assistant.git

2. Install the required packages:
   pip install -r requirements.txt

3. Add the necessary API keys:
   - Replace `"Your_Api_Key"` in the code with:
     - Your Google API key (for Gemini functionality).
     - Your OpenWeatherMap API key (for weather data).

   Alternatively, create a `.env` file in the root directory with the following structure:

   GOOGLE_API_KEY=your_google_api_key_here
   OPENWEATHERMAP_API_KEY=your_openweathermap_api_key_here

4. Run the program:
   python main.py

## How to Use

1. **Run the assistant**:
   - Once the assistant starts, you can interact with it by speaking

2. **Commands you can try**:
   - **Open a website**:
     Open Google
   - **Play music**:
     Speak Play then
     [song name]
     (The song should be in your music library file)
   - **Get weather information**:
   - Speak Weather then:
     Weather in [city name]
   - **Search Wikipedia**:
   - Speak Wikipedia then speak:
     Tell me about [topic]
   - **Google search**:
     Search Google for [query]
   - **YouTube search**:
     Search YouTube for [query]
   - **Current time**:
     What's the time?
   - **Complex queries**:
     - If your query doesn’t match any predefined commands, Jarvis will use Gemini AI to provide an answer.

3. **Stop the assistant**:
   - You can exit the assistant at any time by speaking:
     "Exit"

## API Keys Configuration

### Google API Key
To use Gemini AI, you need a valid Google API key. Get your API key from the [Google Cloud Console](https://console.cloud.google.com/).

### OpenWeatherMap API Key
For weather-related queries, obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

Replace `"Your_Api_Key"` placeholders in the code or set up a `.env` file as shown above.

## Directory Structure

```
jarvis/ (You Folder Name)
│
├── main.py              # Main application script
├── musicLibrary.py      # File Containing a dictionary in python for your favourite songs
├── requirements.txt     # Python package requirements
├── README.md            # Documentation (this file)
└── .env (optional)      # File for storing API keys securely
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance Jarvis's functionality.
