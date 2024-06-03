import pyttsx3 # type: ignore
import datetime
from chatterbot import ChatBot # type: ignore
from chatterbot.trainers import ChatterBotCorpusTrainer # type: ignore
from chatterbot.conversation import Statement # type: ignore
from chatterbot.trainers import ListTrainer # type: ignore




ChatBot= ChatBot("LEXI")


trainer=("ChatterBot.Corpus.english")
trainer= ListTrainer(ChatBot)
trainer.train([
 
    "hi, how are you today?",
    "I am fine, how are you?",
    "I am okay",
    "can you assist me",
    "how can I assist you?",
    "I am okay",
])



response= ChatBot.get_response('hi, how are you today?')
print("Bot response :",  response)

#    Bot_response_string=str(Bot_response)
  #  Bot_print=(Bot_response, Bot_response_string)
    #engine.say(Bot_print)
  #  engine.runAndWait()









