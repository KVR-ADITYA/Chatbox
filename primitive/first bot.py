from chatterbot.trainers import ListTrainer
#this is actually the method used to train the chatbox
from chatterbot import ChatBot

print("Bot: Welcome to the Coustomer Care Service of XXXXXX Company.May I know your predicament")
bot= ChatBot('Test')

conv = open('chats.txt','r').readlines()
conv = open('chats_2.txt').readlines()
bot.set_trainer(ListTrainer)
#Sets the train
bot.train(conv)
while True:
    request = input('You: ')
    response = bot.get_response(request)
    print('Bot: ',response)

print("HAve a good day")