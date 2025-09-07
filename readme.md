# Nexa: Your Personal Voice Assistant

Nexa is a personal voice assistant built with Python, designed to be a simple yet effective tool for everyday tasks. Inspired by popular assistants like Alexa and Google Assistant, Nexa uses speech recognition to understand your commands and responds with a synthesized voice. It leverages the Google Gemini API for general queries, allowing for intelligent and conversational interactions.

Features

    Voice Activation: Activate Nexa by simply saying the wake word "nexa".

    Web Navigation: Open common websites like Google, YouTube, and Facebook with voice commands.

    Music Playback: Play your favorite songs from a predefined list in MusicLibrary.py.

    News Updates: Get the latest news headlines using the News API.

    Intelligent Responses: Powered by the Gemini 2.0 Flash API, Nexa can handle a variety of questions and commands beyond its core functions.

How It Works

Nexa listens for a wake word and then processes the subsequent command using Google's speech recognition technology. Based on the command, it can perform various actions, from opening a web browser to fetching news headlines. For general queries, the command is sent to the Gemini API, and Nexa reads the generated response back to you.

Prerequisites

To run this project, you'll need the following:

    Python: Version 3.10 or higher.

    Environment Variables:

        Google Gemini API Key: Obtain a key from Google AI Studio. The environment variable name is 

        API_KEY.

News API Key: Obtain a key from the News API website. The environment variable name is 

newsapi.

Installation

    Clone the repository:
    Bash

git clone <your-repository-url>
cd nexa-voice-assistant

Create and activate a virtual environment (recommended):
Bash

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

Install the required packages:
Bash

pip install -r requirements.txt

Set up environment variables:
Create a 

.env file in the project root directory and add your API keys.

Code snippet

    API_KEY=<your_gemini_api_key>
    newsapi=<your_newsapi_key>

Usage

    Run the main script:
    Bash

    python main.py

    Wait for the "initializing nexa.." message, and then say the wake word "nexa" to activate the assistant.

    Once activated, the assistant will respond with "hi, I am nexa," and you can give a command.

Examples of Commands:

    "open google"

    "open youtube"

    "open facebook"

    "play march": Plays a song from the MusicLibrary.py file.

    "news": Reads the latest news headlines from the US.

    "What is the weather like today?": A general question that will be handled by Gemini.

Project Structure

    main.py: The core script that handles voice recognition, command processing, and assistant logic.

    client.py: Manages the interaction with the Google Gemini API.

    MusicLibrary.py: A simple dictionary containing song names and their corresponding YouTube URLs.

    .env: The file where your API keys are stored securely.

requirements.txt: Lists all the necessary Python libraries for the project.

Contributing

Feel free to fork the repository, make improvements, and submit pull requests.

    Add more commands: Extend the ProcessCommand function in main.py.

    Improve speech functionality: Experiment with different text-to-speech libraries or parameters.

    Enhance Gemini integration: Refine the system instructions in client.py for more tailored responses.

License

This project is open-source and available under the MIT License.