import asyncio
import edge_tts
import pygame
import speech_recognition as sr

pygame.mixer.init()

def speak(text):
    async def _speak():

        communicate =edge_tts.Communicate(
            text=str(text),
            voice="en-US-AriaNeural"
    )
        await communicate.save("voice.mp3")
    asyncio.run(_speak())

    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.unload()

def listen():
    recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)

    try:
        print("Recognizing...")
        command=recognizer.recognize_google(audio)
        return command.lower()
    except Exception:
        print("Sorry I couldn't understand")
        return ""
    
