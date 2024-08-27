# SCP: Roleplay Auto-Morph Script

This Python script automatically morphs your character in the Roblox game [SCP: Roleplay](https://www.roblox.com/games/5041144419/SCP-Roleplay). Whether you're roleplaying as a specific character or switching between outfits, this script streamlines the process by automating the very boring part of having to copy and paste your commands manually.

## How It Works
The script copies each command to the clipboard using the `pyperclip` library. This ensures that commands are accurately and quickly inserted into the game's command prompt. _I purposely didn't use the `pyautogui` library due to it cutting off the commands and there was no noticeable time improvement when switching between the two._ This highly customizable, allowing you to specify character details and morph preferences, whether permanent or temporary, and to choose or randomize outfits.

- **Libraries Used:** `pyautogui`, `autoit`, `keyboard`, `time`, `random`, `pyperclip`

## Features

- Adjustible settings for your character/morph and general settings on the backend.
- Switch between `perm-` and non-permanent morph commands.
- Automatically runs ``unpermall`` and ``clearstartergear`` after each execution for quick changing of character.
- Modify the delay between commands for faster or slower morphing. Default delay is `0` seconds.
- Ability to add multiple outfits and select one at random or choose a specific outfit.
- Restores last entry of clipboard post-execution.
- The script supports a variety of morph-related commands, including:
  - `:ntag`
  - `:rtag`
  - `:hats`
  - `:shirt`
  - `:startergear`
  - `:team`
  - `:canrk`
  - `:maxhealth`
  - `:scale`
  - `:tntag`
  - `:trtag`
  - `:faceid`
  - `:cntag`
  - `:crtag`
  - `:skin`
-  And lastly, a timer to benchmark how fast the morphing process took.
  - _The script executes at approximately 1.3 commands per second under optimal conditions._

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `pyautogui`
  - `autoit`
  - `keyboard`
  - `pyperclip`

You can install the required libraries using the command prompt:
```bash
pip install pyautogui autoit keyboard pyperclip
```

## Usage

1. **Configure the Script:**
   - Open the script in a text editor and fill in your character's settings (e.g., username, outfit, team).
   - Set your preferences for permanent morphs, morph speed, and outfit selection.

2. **Run the Script:**
   - Ensure Roblox is open and you are in the SCP: Roleplay game.
   - Run the script using Python. The script will automatically execute the necessary commands to morph your character based on your configuration.

3. **In-Game Behavior:**
   - The script interacts with Roblox by simulating key presses and clipboard actions. **Do not multitask while the script is running to avoid disrupting the process.**

4. **Completion:**
   - Once the script finishes executing, it will prompt you to press any key to exit. Your character should be fully morphed according to your settings.

## Disclaimer

Use this script responsibly and in accordance with Roblox's Terms of Service. The creators of this script are not responsible for any actions taken by Roblox or other players as a result of using this script.
