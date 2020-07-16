# pip install SpeechRecognition
#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

#with sr.AudioFile('Voice001wav.wav') as source: #run with the audio file in spanish
#with sr.AudioFile('Lumumba1aac.wav') as source: #run with the audio file in french
with sr.AudioFile('MaximilienParyacc.wav') as source: #run with the audio file in english
    
    #audio_text = r.listen(source, timeout=3)
    audio_text = r.record(source)
    
    #audio = r.adjust_for_ambient_noise(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        #text = r.recognize_google(audio_text, show_all=True)
        #text = r.recognize_google(audio_text, language="es-ES")
        #text = r.recognize_google(audio_text, language="fr-FR")
        text = r.recognize_google(audio_text, language="en-EN")
        print('Converting audio transcripts into text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')