# Jarvis Voice Assistant

A simple voice-controlled assistant built in Python that can open websites, play YouTube videos, search the web, and respond to voice commands.

---

## Features

- Voice recognition using Google's speech recognition API.
- Text-to-speech responses with `pyttsx3`.
- Opens popular websites like Google, YouTube, WhatsApp.
- Plays requested videos on YouTube via YouTube Data API.
- Web searches using `googlesearch` and opens results in the browser.
- Listens continuously until you say "shut" to stop.

---

## Requirements

- Python 3.x
- `speech_recognition`
- `pyttsx3`
- `googlesearch-python`
- `google-api-python-client`
- `PyAudio` (for microphone access)
- A working microphone

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/michuishaan07/JARVIS.git
   cd JARVIS

2.Create and activate a virtual environment (optional but recommended):
   ```bash
python3 -m venv venv
source venv/bin/activate
 ```

3.Install dependencies:
  ```bash
pip install -r requirements.txt
 ```

4.Make sure you have a valid YouTube API key and replace the placeholder in the script.


## Usage
Speak commands such as:

"Open Google"

"Open YouTube"

"Open WhatsApp"

"Play [song or video name]"

Say "Jarvis" to activate

Say "shut" to exit the program
