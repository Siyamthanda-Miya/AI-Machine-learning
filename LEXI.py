import pyttsx3 # type: ignore
import datetime
from chatterbot import ChatBot # type: ignore
from chatterbot.trainers import ChatterBotCorpusTrainer # type: ignore
from chatterbot.conversation import Statement # type: ignore



#aquires training data from the database
ChatBot= ChatBot("LEXI")

trainer= ChatterBotCorpusTrainer(ChatBot)
trainer.train("chatterbot.corpus,english")

def Wishuser():
    hour=datetime.datetime.now().hour

    if hour>=0 and hour<12:
        engine.say(f"Good Morning, {user}")
        print("Good Morning")

    elif hour>=12 and hour<16:
        engine.say(f"Good Afternoon, {user}")
        print("Good Afternoon")

    else:
        engine.say(f"Good Evening, {user}")
        print("Good Evening")


#pyttsx3 initialization and settings
engine = pyttsx3.init()
voices = engine.getProperty('rate')
engine.setProperty('rate', 160)
voices_list = engine.getProperty('voices')
engine.setProperty('voice', voices_list[1].id)


engine.say("Hey there!, what's your name,friend?.")
engine.runAndWait()



#user name input
user=input("Enter name :")

#Lexi greets the user based on the time of the day, using the user's name
Wishuser()
engine.runAndWait()

engine.say("lets chat.")
engine.runAndWait()




while True:
    query=input(f"{user}    :")

    response= ChatBot.get_response(query)
    print(ChatBot.get_response(Statement(text=query, search_text=query)))
    engine.say(response)
    engine.runAndWait()
 









