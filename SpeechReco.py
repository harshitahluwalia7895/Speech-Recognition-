import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as Source:
    print('Speak Anything: ')
    audio = r.listen(Source)
    try:
        text = r.recognize_google(audio)
        print('You just said : {}'.format(text))
    except:
        print('Sorry Could not recognise your Voice !!')