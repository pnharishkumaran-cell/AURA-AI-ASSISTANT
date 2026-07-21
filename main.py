from speech import speak,listen
from command import process_command
from ai import ask_ai
from greeting import wish
print("====================")
print("      AURA AI       ")
print("====================")

print("Starting AI assistant......")
greeting=wish()

speak(f"{greeting}, I am Aura, How can i help you ")


while True:
    command=listen()

    if command =="":
        continue
    print("You :",command)

    if "exit" in command:
        speak("Goodbye have a nice day")
        break

    if "open youtube" in command or"open google"in command or "time" in command or "date" in command or "open notepad " in command or "open calculator" in command or "open camera" in command or "search youtube for" in command or "search" in command or "take screenshot" in command:
        process_command(command)

    else:
        try:

            response=ask_ai(command)
            print("Aura :",response)
            speak(response)
        except Exception as e:
            print("Error :", e)
            print("Sorry i couldn't get response from the AI")
