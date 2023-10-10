import time
import random

greetings = ['hello', 'hi', 'hey!','hey']
keywords = ['weather', 'time', 'date', 'day', 'temperature', 'rain', 'sun', 'cloud', 'clouds', 'cloudy', 'wind', 'windy', 'snow', 'snowy', 'rainy', 'sunny', 'hot', 'cold', 'warm', 'freezing', 'boiling', 'freezing', 'warm', 'boiling']
intensions = {
    'question': ['what', 'how', 'why', 'when', 'where', 'who', 'which', 'whom', 'whose', 'tell'],
    'positive': ['yes', 'yep', 'yeah', 'sure', 'ok', 'okay', 'fine', 'cool', 'understood', 'understand','great', 'awesome', 'fantastic', 'good', 'nice', 'sweet', 'yay'],
    'negative': ['no', 'nope', 'nah', 'not', 'hate', 'sad', 'bad', 'awful', 'terrible', 'never', 'dont', 'do not', 'dont know', 'do not know', 'dont understand', 'do not understand', 'dont get it', 'do not get it', 'dont know what you mean', 'do not know what you mean', 'dont know what you are saying', 'do not know what you are saying', 'dont know what you are talking about', 'do not know what you are talking about', 'dont know what you are talking', 'do not know what you are talking', 'dont know what you are talking about', 'do not know what you are talking about', 'dont know what you are talking', 'do not know what you are talking', 'dont know what you mean', 'do not know what you mean', 'dont know what you are saying', 'do not know what you are saying', 'dont know what you are talking about', 'do not know what you are talking about', 'dont know what you are talking', 'do not know what you are talking', 'dont know what you are talking about', 'do not know what you are talking about', 'dont know what you are talking', 'do not know what you are talking'],
    'thanks': ['thanks', 'thank you', 'thx', 'thnx', 'ty', 'thank you very much', 'thank you so much', 'thanks a lot', 'thanks a bunch', 'thanks a ton', 'thanks heaps', 'thanks loads', 'thanks loads'],
    'queryForWhatChatBotCanDo': ['what can you do', 'what are you capable of', 'what are your capabilities', 'what are your features', 'what are your functions', 'what are your functions', 'what are your abilities', 'what are you'],
    'Safety': ['can i go', 'should i go', 'is it safe', 'is it safe to go', 'is it safe to go outside', 'is it safe to go out', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now', 'is it safe to go out today', 'is it safe to go out tomorrow', 'is it safe to go out tonight', 'is it safe to go out this evening', 'is it safe to go out this morning', 'is it safe to go out this afternoon', 'is it safe to go out now'],
    'firstPerson':['i', 'me', 'my', 'mine', 'myself'],
    'secondPerson':['you', 'your', 'yours', 'yourself'],
    'thirdPerson':['he', 'she', 'it', 'him', 'her', 'his', 'hers', 'its', 'they', 'them', 'their', 'theirs', 'himself', 'herself', 'itself', 'themselves'],
}
bye = ['bye', 'goodbye', 'stop', 'see you later', 'see you soon', 'talk to you later', 'talk to you soon']
weathers = ['sunny', 'cloudy', 'rainy', 'windy', 'snowy', 'hot', 'cold', 'warm', 'freezing', 'boiling']

responses = {
    'greetings': ['Hello! How may I help you', 'Hi!', 'Hey! How are you?'],
    'question': ['I am a chatbot. I can help you with weather and time related queries.'],
    'whatAreYou': ['I am a chatbot. I can help you with weather and time related queries.'],
    'positive': ['Great!', 'Awesome!', 'Fantastic!', 'Good!', 'Nice!', 'Sweet!', 'Yay!'],
    'negative': ['Oh no!', 'Oh dear!', 'Oh my!', 'Oh gosh!', 'Oh golly!', 'Oh wow!', 'Oh jeez!', 'sad to hear that'],
    'thanks': ['You are welcome!', 'No problem!', 'No worries!', 'My pleasure!', 'Anytime!'],
    'safety': ['It is safe to go out.'],
    'time': ['The time is ' + time.strftime("%H:%M:%S")],
    'date': ['The date is ' + time.strftime("%d/%m/%Y")],
    'day': ['Today is ' + time.strftime("%A")],
    'weather': ['The weather today is ' + random.choice(weathers)],
    'randomResponse': ['I am not sure what you mean. Can you please rephrase that?', 'I am not sure what you are saying. Can you please rephrase that?', 'I am not sure what you are talking about. Can you please rephrase that?', 'I am not sure what you mean. Can you please rephrase that?', 'I am not sure what you are saying. Can you please rephrase that?', 'I am not sure what you are talking about. Can you please rephrase that?', 'I am not sure what you mean. Can you please rephrase that?', 'I am not sure what you are saying. Can you please rephrase that?', 'I am not sure what you are talking about. Can you please rephrase that?'],
    'askForhealth':['How are you feeling today?'],
    'answerAboutHealth':['I am great'],
    'bye': ['Bye!', 'Goodbye!', 'See you later!', "I'll miss you!", 'Have a nice day!', 'Pleasure talking to you!']
}

while True: 
    UserInput = input('you: ')
    UserInput = UserInput.lower()
    flags = []
    exit = False
    for sentence in UserInput.split(','):
        flag=[]
        for word in sentence.split(' '):
            if word in greetings:
                flag.append('greetings')

            if word in keywords:
                flag.append(word)

            for intension in intensions:
                if word in intensions[intension]:
                    flag.append(intension)

            if word in bye:
                flag.append('bye')
        flags.append(flag)
    responded = False
    for respond in flags:
        print ('chatbot: ', end='')
        if 'greetings' in respond:
            print(random.choice(responses['greetings']))
            responded = True
        if 'question' in respond:
            if 'whatAreYou' in respond:
                print(random.choice(responses['whatAreYou']))
            if 'weather' in respond:
                print(random.choice(responses['weather']))
            if 'time' in respond:
                print(random.choice(responses['time']))
            if 'date' in respond:
                print(random.choice(responses['date']))
            if 'day' in respond:
                print(random.choice(responses['day']))
            if 'secondPerson' in respond:
                print(random.choice(responses['answerAboutHealth']))              
                print(random.choice(responses['askForhealth']))              
            responded = True
        if 'Safety' in respond:
            print(random.choice(responses['Safety']))
            responded = True
        if 'positive' in respond and not 'question' in respond:
            print(random.choice(responses['positive']))
            responded = True
        if 'negative' in respond and not 'question' in respond:
            print(random.choice(responses['negative']))
            responded = True
        if 'thanks' in respond:
            print(random.choice(responses['thanks']))
            responded = True
        if 'whatAreYou' in respond:
            print(random.choice(responses['whatAreYou']))
            responded = True
        if 'safety' in respond:
            print(random.choice(responses['safety']))
            responded = True
        if 'time' in respond:
            print(random.choice(responses['time']))
            responded = True
        if 'date' in respond:
            print(random.choice(responses['date']))
            responded = True
        if 'day' in respond:
            print(random.choice(responses['day']))
            responded = True
        if 'bye' in respond:
            print(random.choice(responses['bye']))
            responded = True
            exit=True
        if 'askForhealth' in respond:
            print(random.choice(responses['askForhealth']))
            responded = True
    if responded == False:
        print(random.choice(responses['randomResponse']))
        responded = True
    if exit:
        break