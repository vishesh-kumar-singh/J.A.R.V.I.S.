import sys
import os

# Get the project root directory
project_root = os.path.abspath('C:/My Stuff/Programming/Projects/JARVIS')
sys.path.append(project_root)

import screen_brightness_control as sbc
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
from Basic_Functionalities.Speaking_Ability import speak

def set_brightness(level):
    """
    Set the screen brightness to the specified level.

    Args:
        level (int): Brightness level (0-100).

    Raises:
        ValueError: If the level is outside the range of 0 to 100.
    """
    try:
        if not (0 <= level <= 100):
            raise ValueError("Brightness level must be between 0 and 100.")
        
        sbc.set_brightness(level)
        print(f"Brightness set to {level}%")
        speak("As you wish, sir!")
    except ValueError as ve:
        print(f"Invalid brightness level: {ve}")
        speak(f"Invalid brightness level: {ve}")
    except sbc.ScreenBrightnessError as sbe:
        print(f"Error adjusting brightness: {sbe}")
        speak(f"Error adjusting brightness: {sbe}")
    except Exception as e:
        print(f"Unexpected error occurred while setting brightness: {e}")
        speak(f"Unexpected error occurred while setting brightness: {e}")

import subprocess

def set_volume(level):
    try:
        # Check if the level is within the acceptable range (0-100)
        if not (0 <= level <= 100):
            raise ValueError("Volume level must be between 0 and 100.")

        # Construct the command to set the volume using NirCmd
        command = f"nircmd.exe setsysvolume {int((level / 100) * 65535)}"

        # Run the command using subprocess
        subprocess.run(command, check=True, shell=True)
        print(f"Volume set to {level}%")
        speak("As you wish, sir!")
        
    except ValueError as ve:
        print(f"Invalid volume level: {ve}")
        speak(f"Invalid volume level: {ve}")
    except subprocess.CalledProcessError as cpe:
        print(f"Error running NirCmd: {cpe}")
        speak(f"Error running NirCmd: {cpe}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        speak(f"Unexpected error occurred: {e}")
def mute():
    command = f"nircmd.exe mutesysvolume 1"
    # Run the command using subprocess
    subprocess.run(command, check=True, shell=True)
def unmute():
    command = f"nircmd.exe mutesysvolume 0"
    # Run the command using subprocess
    subprocess.run(command, check=True, shell=True)

def screen_saver():
    command = f"nircmd.exe screensaver"
    # Run the command using subprocess
    subprocess.run(command, check=True, shell=True)

def turn_off_monitor():
    command = f"nircmd.exe monitor off"
    # Run the command using subprocess
    subprocess.run(command, check=True, shell=True)

def switch_off():
    command = f"nircmd.exe exitwin poweroff"
    # Run the command using subprocess
    subprocess.run(command, check=True, shell=True)
