#Function
import datetime
from speak import say
import wikipedia
import pywhatkit
def Time():
    time=datetime.datetime.now().strftime("%H:%M")
    say(time)

def Date():
    date = datetime.date.today()
    say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    say(day)

def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()
    elif "day" in query:
        Day()


#input function


    

def InputExecution(tag,query):
    if "wikipedia" in tag:
        name = str(query).replace("who is ","").replace("about","").replace("what is","").replace("deatils about","")
        result = wikipedia.summary(name)
        say(result)
    
    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        pywhatkit.search(query)


