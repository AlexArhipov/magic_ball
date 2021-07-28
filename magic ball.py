from random import *

print('Hello World, I am a magic ball, and I know the answer to any of your questions.')
answer = ["Undoubtedly", "A foregone conclusion", "No doubt", "Definitely yes", "You can be sure of this", "It seems to me - yes", "Most likely", "Good prospects", "Signs say - yes "," Yes "," It is not clear yet, try again "," Ask later "," Better not to tell "," Now you cannot predict "," Concentrate and ask again "," Don't even think "," My answer is no "," According to my information - no "," Prospects are not very good "," Very doubtful "]
while(True):
    ch = randint(0, 19)
    print('Ask your question or write "no" to exit') 
    guess = input()
    if guess == 'NO' or guess == 'No' or guess == 'no':
        break;
    print(answer[ch])
print('Come back if you have any questions!') 