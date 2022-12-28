import googletrans
import speech_recognition
import gtts
import playsound

# print(googletrans.LANGUAGES)
input_lang = "ur"
output_lang = "en"

recognizer = speech_recognition.Recognizer() 
with speech_recognition.Microphone() as source:
    print("Speak Now!")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language=input_lang)
    print(text) 

translator = googletrans.Translator()
translation = translator.translate(text, dest=output_lang)
print(translation.text)
converted_audio = gtts.gTTS(translation.text, lang=output_lang)
converted_audio.save("64-reply.mp3")
playsound.playsound("64-reply.mp3")