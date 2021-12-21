import random

#input name and question
while True:
    name = input('What is your name?\n')
    while True:
        question = input('Ask me anything:\n')
        answer = ['Yes- definitely', 'It is decidedly so', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']



        answer = random.choice(answer)
        if name == '':
            print('\n' + 'Question: ' + question + '\n')
        else:
            print('\n' + name + ' ' + 'asks: ' + question + '\n')
        if question == '':
            print('''There isn't anything to answer''')
        elif question.lower() == 'change name':
            break
        else:
            print('answer: ' + answer + '\n')hjgjhg