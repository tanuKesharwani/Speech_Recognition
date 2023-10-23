import pyttsx3 


def say(Text):
    engine = pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id) # 1 for girl and 0 for boy

    engine.setProperty('rate',120) #it define on what speed the voice gives output

    print("   ")
    print(f"chotu:{Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("   ")

# say("hello i am chutki")