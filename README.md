# Music Bot

This is a Discord music bot built using Python and the `discord.py` library. It allows users to play music in voice channels with simple commands, making it a fun and interactive addition to any server.

## Features
- Join a voice channel and play music from YouTube.
- Adjust the volume of the music to suit your preferences.
- Simple and intuitive commands for controlling the bot.

## Setup Instructions

### Prerequisites
Before you begin, ensure you have the following installed on your system:

1. **Python**: Make sure Python 3.8 or higher is installed. You can download it from [python.org](https://www.python.org/).
2. **Homebrew** (for macOS): If you're on macOS, install Homebrew by following the instructions at [brew.sh](https://brew.sh/).
3. **Opus Library**: The Opus library is required for voice functionality. Install it using Homebrew with the command `brew install opus`.
4. **FFmpeg**: FFmpeg is needed for audio processing. Install it using Homebrew with the command `brew install ffmpeg`.

### Installation
1. Clone this repository or download the source code as a ZIP file and extract it.
2. Open a terminal and navigate to the project directory using the `cd` command.
3. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
1. Create a file named `token_config.py` in the same directory as `msb.py`.
2. Open `token_config.py` and add your Discord bot token in the following format:
   ```python
   TOKEN = "your_discord_bot_token_here"
   ```
   Replace `your_discord_bot_token_here` with the actual token for your bot.

## How to Use
1. Start the bot by running the following command in your terminal:
   ```bash
   python3 msb.py
   ```
2. Use the following commands in your Discord server to interact with the bot:
   - `!start <channel_id>`: Make the bot join a voice channel. Replace `<channel_id>` with the ID of the voice channel.
   - `!play <url>`: Play music from a YouTube URL. Replace `<url>` with the link to the YouTube video.
   - `!volume <0-100>`: Adjust the volume of the music. Provide a value between 0 and 100.

## Common Errors and Fixes

### 1. `Opus is not loaded`
   - **Cause**: The Opus library is not installed or the path is incorrect.
   - **Fix**: Ensure Opus is installed using Homebrew and update the path in `msb.py` if necessary.

### 2. `FFmpeg not found`
   - **Cause**: FFmpeg is not installed.
   - **Fix**: Install FFmpeg using Homebrew with the command `brew install ffmpeg`.

### 3. `Invalid channel ID`
   - **Cause**: The provided channel ID is incorrect or the bot lacks permissions to join the channel.
   - **Fix**: Double-check the channel ID and ensure the bot has the necessary permissions to join voice channels.

### 4. `Bot is not connected to a voice channel`
   - **Cause**: The bot is not in a voice channel.
   - **Fix**: Use the `!start` command to make the bot join a voice channel before attempting to play music.

## License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.