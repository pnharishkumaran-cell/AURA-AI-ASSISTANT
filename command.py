import webbrowser
from datetime import datetime
import os
import pyautogui
from speech import speak
from datetime import datetime

def get_date():
    today=datetime.now().strftime("%d %B %Y")
    return f"today date is {today}"


def process_command(command):
    if "open youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening google")
        webbrowser.open("https://www.google.com")
    elif "time" in command:
        current = datetime.now().strftime("%I:%M %p")
        print(f"The current time is {current}")
        speak(f"The curren time is {current}")
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "date" in command:
        date=get_date()
        print(date)
        speak(date)
    elif "search" in command:
        search=command.replace("search","").strip()
        speak(f"searching {search}")
        webbrowser.open(f"https://www.google.com/results?search_query={search} ")
    elif "open camera" in command:
        speak("opening camera")
        os.system("start microsoft.windows.camera:")
    elif "take screenshot" in command:
        speak("Taking screenshot")
        screenshot=pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("screenshot saved successfully")

    elif "search youtube for " in command:
        query=command.replace(f"search youtube for","").strip()
        speak(f"searching youtube for {query}")
        webbrowser.open (f"https://www.youtube.com/results?search_qeary={query} ")


    elif "open calculater" in command:
        speak("Opening calculater")
        os.system("calc")
    elif "exit" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        ("ask anything")