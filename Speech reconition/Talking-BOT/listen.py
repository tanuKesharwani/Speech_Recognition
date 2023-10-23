from email.mime import audio
import speech_recognition as sr


def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1

        audio = r.listen(source,0,3) # r.listen(source ,0,2)after every two second the computer recognize what you say
        
    try:
        print("Recognizing...")

        query = r.recognize_google(audio,language="en-in") #calling the variable named audio
        print(f"you said:{query}")

    except:
        return ""
    query = str(query)
    return query.lower()

# Listen()