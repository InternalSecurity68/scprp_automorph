import pyautogui
import time
import autoit
import keyboard
import random
import pyperclip

# User and outfit settings
# To include quotation marks within the display tags, put \" inside
# For example, the code for "Cloud" would be:
# name_tag = "\"Cloud\""
username = "" # Roblox username or "me"
name_tag = ""
rank_tag = ""
# Accessory list:
accessories_id = "" # Format: 1234567890,1234567890,1234567890, etc...
startergears = ""
team = ""
can_random_kill = True
max_health = 100
scale = 1
basekit = False
permanent = True
mod = True
trtag = False
faceid = ""
color_ntag = "" # Format: RRR GGG BBB
color_rtag = "" # Format: RRR GGG BBB

# Settings
command_prefix = ":"
chat_start_keybind = "/"
send_message_keybind = "return"
delay = 0.0  # Delay between each command
interval = 0.0  # Interval between command execution

outfits = {
    "OutfitName": (000, 000) # Replace the 000 with the classic clothing accessories in the format: (ShirtID, PantsID)
}

# Set this string value to either 'random' or the name of a specific outfit
user_choice = "random"

# The script below allows for automatic morphing, using the keyboard to maximize speed.
def select_outfit(choice):
    if choice.lower() == 'random':
        outfit_name, outfit_ids = random.choice(list(outfits.items()))
    else:
        outfit_name = choice
        outfit_ids = outfits.get(choice)
        if outfit_ids is None:
            print(f"No outfit found with the name '{choice}'. Selecting a random outfit instead.")
            outfit_name, outfit_ids = random.choice(list(outfits.items()))
    return outfit_name, outfit_ids

outfit_name, chosen_outfit = select_outfit(user_choice)
print(f"Chosen outfit: {outfit_name}")

command_map = {
    "shirt": ("permshirt", "shirt"),
    "morph": ("permmorph", "morph"),
    "hat": ("permhat", "hat"),
    "ntag": ("permntag", "ntag"),
    "rtag": ("permrtag", "rtag"),
    "cntag": ("permcntag", "cntag"),
    "crtag": ("permcrtag", "crtag"),
    "trtag": ("permtrtag", "trtag"),
    "face": ("permface", "face"),
    "maxhealth": ("permmaxhealth", "maxhealth"),
    "scale": ("permscale", "scale"),
    "canrk": ("permcanrk", "canrk")
}

commands = [
    f"{command_prefix}clearstartergear {username}",
    f"{command_prefix}permdamagemultiplier {username} 2",
    f"{command_prefix}unpermall {username}",
    f"{command_prefix}{command_map['shirt'][0 if permanent else 1]} {username} {chosen_outfit[0]} {chosen_outfit[1]}"
]

if basekit:
    commands.append(f"{command_prefix}{command_map['morph'][0 if permanent else 1]} {username} basekit")
if accessories_id:
    commands.append(f"{command_prefix}{command_map['hat'][0 if permanent else 1]} {username} {accessories_id}")
if trtag:
    commands.append(f"{command_prefix}{command_map['trtag'][0 if permanent else 1]} {username} true")
if faceid:
    commands.append(f"{command_prefix}{command_map['face'][0 if permanent else 1]} {username} {faceid}")
if name_tag:
    commands.append(f"{command_prefix}{command_map['ntag'][0 if permanent else 1]} {username} {name_tag}")
if rank_tag:
    commands.append(f"{command_prefix}{command_map['rtag'][0 if permanent else 1]} {username} {rank_tag}")
if team:
    commands.append(f"{command_prefix}team {username} {team}")
if color_ntag:
    commands.append(f"{command_prefix}{command_map['cntag'][0 if permanent else 1]} {username} {color_ntag}")
if color_rtag:
    commands.append(f"{command_prefix}{command_map['crtag'][0 if permanent else 1]} {username} {color_rtag}")
if max_health != 100:
    commands.append(f"{command_prefix}{command_map['maxhealth'][0 if permanent else 1]} {username} {max_health}")
    commands.append(f"{command_prefix}heal {username}")
if scale != 1:
    commands.append(f"{command_prefix}{command_map['scale'][0 if permanent else 1]} {username} {scale}")
if can_random_kill:
    commands.append(f"{command_prefix}{command_map['canrk'][0 if permanent else 1]} {username} true")
if startergears:
    commands.append(f"{command_prefix}startergear {username} {startergears}")

def send_command(command):
    pyperclip.copy(command)
    autoit.win_activate("Roblox")
    pyautogui.press(chat_start_keybind)
    time.sleep(delay)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(delay)
    keyboard.send("enter")

def main():
    if mod:
        send_command("/c system")
    for command in commands:
        print(command)
        if mod:
            send_command(command)
            time.sleep(interval)
    if mod:
        pyautogui.press(chat_start_keybind)
        pyautogui.press('backspace')
    pyperclip.copy("a")
    print("Morphing Finished! Input any key to exit...")
    input()

if __name__ == "__main__":
    main()
