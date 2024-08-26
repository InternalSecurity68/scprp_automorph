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
username = ""  # Roblox username or "me"
name_tag = ""
rank_tag = ""
# Accessory List:
# Use the list if you want to keep track of what ID is what
accessories_id = ""  # Format: 1234567890,1234567890,1234567890, etc...
startergears = ""
team = ""
can_random_kill = True
max_health = 100
scale = 1
basekit = False # If True, uses Site-68's basekit to clear your existing avatar of all accessories
permanent = True # If True, uses the perm- prefix in commands for a permantent character.
mod = True # If True, assumes you have mod permissions to morph yourself.
tntag = False # If True, hides NAME tag from display
trtag = False # If True, hides RANK tag from display
faceid = ""
color_ntag = ""  # Format: RRR GGG BBB
color_rtag = ""  # Format: RRR GGG BBB

# Settings
command_prefix = ":"
chat_start_keybind = "/"
send_message_keybind = "return"
delay = 0.0  # Delay between each command sent in SECONDS
interval = 0.0  # Delay of steps when sending individual commands in SECONDS.
user_choice = "random" # Set this string value to either 'random' or the name of a specific outfit

outfits = {
    "OutfitName": (000, 000)  # Replace with the classic clothing accessories in the format: (ShirtID, PantsID)
}

def select_outfit(choice):
    if choice.lower() == 'random':
        return random.choice(list(outfits.items()))
    return choice, outfits.get(choice) or random.choice(list(outfits.items()))

outfit_name, chosen_outfit = select_outfit(user_choice)
print(f"Chosen outfit: {outfit_name}")

# Command mapping
command_map = {
    "shirt": "permshirt" if permanent else "shirt",
    "morph": "permmorph" if permanent else "morph",
    "hat": "permhat" if permanent else "hat",
    "ntag": "permntag" if permanent else "ntag",
    "rtag": "permrtag" if permanent else "rtag",
    "cntag": "permcntag" if permanent else "cntag",
    "crtag": "permcrtag" if permanent else "crtag",
    "tntag": "permtrtag" if permanent else "tntag",
    "trtag": "permtrtag" if permanent else "trtag",
    "face": "permface" if permanent else "face",
    "maxhealth": "permmaxhealth" if permanent else "maxhealth",
    "scale": "permscale" if permanent else "scale",
    "canrk": "permcanrk" if permanent else "canrk"
}

# Building the command list
commands = [
    f"{command_prefix}clearstartergear {username}",
    f"{command_prefix}unpermall {username}",
    f"{command_prefix}{command_map['shirt']} {username} {chosen_outfit[0]} {chosen_outfit[1]}"
]

optional_commands = [
    (basekit, f"{command_prefix}{command_map['morph']} {username} basekit"),
    (accessories_id, f"{command_prefix}{command_map['hat']} {username} {accessories_id}"),
    (tntag, f"{command_prefix}{command_map['tntag']} {username} true"),
    (trtag, f"{command_prefix}{command_map['trtag']} {username} true"),
    (faceid, f"{command_prefix}{command_map['face']} {username} {faceid}"),
    (name_tag, f"{command_prefix}{command_map['ntag']} {username} {name_tag}"),
    (rank_tag, f"{command_prefix}{command_map['rtag']} {username} {rank_tag}"),
    (team, f"{command_prefix}team {username} {team}"),
    (color_ntag, f"{command_prefix}{command_map['cntag']} {username} {color_ntag}"),
    (color_rtag, f"{command_prefix}{command_map['crtag']} {username} {color_rtag}"),
    (max_health != 100, f"{command_prefix}{command_map['maxhealth']} {username} {max_health}"),
    (max_health != 100, f"{command_prefix}heal {username}"),
    (scale != 1, f"{command_prefix}{command_map['scale']} {username} {scale}"),
    (can_random_kill, f"{command_prefix}{command_map['canrk']} {username} true"),
    (startergears, f"{command_prefix}startergear {username} {startergears}")
]

# Append optional commands if the condition is met
commands += [cmd for cond, cmd in optional_commands if cond]

def send_command(command):
    pyperclip.copy(command)
    autoit.win_activate("Roblox")
    time.sleep(interval)
    pyautogui.press(chat_start_keybind)
    time.sleep(interval)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(interval)
    keyboard.send("enter")

def main():
    start_time = time.time()
    if mod:
        send_command("/c system")
    for command in commands:
        print(command)
        if mod:
            send_command(command)
            time.sleep(delay)
    if mod:
        pyautogui.press(chat_start_keybind)
        pyautogui.press('backspace')
    pyperclip.copy("a")
    end_time = time.time()  # Record the end time
    duration = end_time - start_time
    print(f"Total execution time: {duration:.2f} seconds")
    print("Morphing Finished! Input any key to exit...")
    input()

if __name__ == "__main__":
    main()
