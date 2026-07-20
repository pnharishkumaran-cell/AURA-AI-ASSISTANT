import webbrowser
from datetime import datetime
import os
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
    elif "Open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "date" in command:
        date=get_date()
        print(date)
        speak(date)

    elif "open calculater" in command:
        speak("Opening calculater")
        os.system("calc")
    elif "exit" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        ("ask anything")