import gtts
import playsound

text = input("Enter something here: ")
sound = gtts.gTTS(text, lang="en")

sound.save("62-voice.mp3")
playsound.playsound("62-voice.mp3")