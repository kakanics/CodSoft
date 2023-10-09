import time
import random

greetings = ['hello', 'hi', 'hey!','hey']
keywords = ['weather', 'time', 'date', 'day', 'temperature', 'rain', 'sun', 'cloud', 'clouds', 'cloudy', 'wind', 'windy', 'snow', 'snowy', 'rainy', 'sunny', 'hot', 'cold', 'warm', 'freezing', 'boiling', 'freezing', 'warm', 'boiling']
intensions = {
    'question': ['what', 'how', 'why', 'when', 'where', 'who', 'which', 'whom', 'whose'],
    'positive': ['yes', 'yep', 'yeah', 'sure', 'ok', 'okay', 'fine', 'cool', 'understood', 'understand','great', 'awesome', 'fantastic', 'good', 'nice', 'sweet', 'yay'],
    'negative': ['no', 'nope', 'nah', 'not', 'never', 'dont', 'do not', 'dont know', 'do not know', 'dont understand', 'do not understand', 'dont get it', 'do not get it', 'dont know what you mean', 'do not know what you mean', 'dont know what you are saying', 'do not know what you are saying', 'dont know what you are talking about', 'do not know what you are talking about', 'dont know what you are talking', 'do not know what you are talking', 'dont know what you are talking about', 'do not know what you are talking about', 'dont know what you are talking', 'do not know what you are talking', 'dont know what you mean', 'do not know what you mean', 'dont know what you are saying', 'do not know what you are saying', 'dont know what you are talking about', 'do not know what you are talking about', 'dont know what you are talking', 'do not know what you are talking', 'dont know what you are talking about', 'do not know what you are talking about', 'dont know what you are talking', 'do not know what you are talking'],
    'thanks': ['thanks', 'thank you', 'thx', 'thnx', 'ty', 'thank you very much', 'thank you so much', 'thanks a lot', 'thanks a bunch', 'thanks a ton', 'thanks heaps', 'thanks loads', 'thanks loads'],
    'queryForWhatChatBotCanDo': ['what can you do', 'what are you capable of', 'what are your capabilities', 'what are your features', 'what are your functions', 'what are your functions', 'what are your abilities', 'what are you'],
    'Safety': ['can i go', 'should i go', 'is it safe', 'is it safe to go', 'is it safe to go outside', 'is it safe to go out', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now'],
    'firstPerson':['i', 'me', 'my', 'mine', 'myself'],
    'secondPerson':['you', 'your', 'yours', 'yourself'],
    'thirdPerson':['he', 'she', 'it', 'him', 'her', 'his', 'hers', 'its', 'they', 'them', 'their', 'theirs', 'himself', 'herself', 'itself', 'themselves'],
}
bye = ['bye', 'goodbye', 'see you later', 'see you soon', 'talk to you later', 'talk to you soon']
weathers = ['sunny', 'cloudy', 'rainy', 'windy', 'snowy', 'hot', 'cold', 'warm', 'freezing', 'boiling']

responses = {
    'greetings': ['Hello! How may I help you', 'Hi!', 'Hey! How are you?'],
    'question': ['I am a chatbot. I can help you with weather and time related queries.'],
    'positive': ['Great!', 'Awesome!', 'Fantastic!', 'Good!', 'Nice!', 'Sweet!', 'Yay!'],
    'negative': ['Oh no!', 'Oh dear!', 'Oh my!', 'Oh gosh!', 'Oh golly!', 'Oh wow!', 'Oh jeez!', 'sad to hear that'],
    'thanks': ['You are welcome!', 'No problem!', 'No worries!', 'My pleasure!', 'Anytime!'],
    'WhatAreYou': ['I am a chatbot. I can help you with weather and time related queries.'],
    'Safety': ['It is safe to go out.'],
    'Time': ['The time is ' + time.strftime("%H:%M:%S")],
    'Date': ['The date is ' + time.strftime("%d/%m/%Y")],
    'Day': ['Today is ' + time.strftime("%A")],
    'Weather': ['The weather today is ' + random.choice(weathers)],
    'bye': ['Bye!', 'Goodbye!', 'See you later!', "I'll miss you!", 'Have a nice day!', 'Pleasure talking to you!']
}

while True: 
    input = input()
    input = input.lower()
    flags = []
    for word in input.split(' '):
        if word in greetings:
            flags.append('greetings')

        #check key

        for intension in intensions:
            if word in intensions[intension]:
                flags.append(intension)

        if word in bye:
            flags.append('bye')
