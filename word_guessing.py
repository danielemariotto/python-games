# ENG: In this game, there is a list of words present, out of which our interpreter will choose 1 random word. The user first has to input their names and then, will be asked to guess any alphabet. If the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet. The user will be given 12 turns(which can be changed accordingly) to guess the complete word.
# ITA: In questo gioco è presente un elenco di parole, tra le quali il nostro programma sceglierà 1 parola a caso. L'utente deve prima inserire il proprio nome e poi gli verrà chiesto di indovinare una lettera qualsiasi. Se la parola casuale contiene quella lettera, verrà mostrata come output (con il posizionamento corretto), altrimenti il programma chiederà di indovinare un'altra lettera. L'utente avrà a disposizione 12 turni (che possono essere modificati di conseguenza) per indovinare la parola completa.

import random

words = ['book', 'car', 'house', 'dog', 'computer', 'city', 'tree', 'phone', 'beach', 'food', 'music', 'movie', 'chair', 'school', 'friend', 'job', 'water', 'sun', 'moon', 'star']

word_index = random.randint(0, len(words)-1)

word = words[word_index]

wordcopy = word
attempts = 1
max_attempts = 12
words_guessed = '_'*len(word)
position_list = []
print('In this game you have to guess a word')
name = input('Enter your name: ')
print(f'You have {max_attempts} available tries to find the word')
print('   ')
print('You will send me letters (one a time) that you think is in the word. I will tell you if is inside the word or not. If correct, I will tell you also the position of the letter in the word')
print('   ')
while attempts <= max_attempts:
    print('   ')
    letter = input(f'Attempt number {attempts}. \n{name}, enter a letter do you think is in the word: ')
    if letter in word:
        position = word.index(letter)
        wordcopy = wordcopy[:position] + '-' +  wordcopy[position+1:] # replace the letter with a '-'
        words_guessed= words_guessed[:position] + letter + words_guessed[position+1:] # replace the '_' with the letter

        position_list.append(position)

        # if the letter is present more than once in the word
        while letter in wordcopy:
            position = wordcopy.index(letter) # find the position of the letter in the copy of the word
            position_list.append(position)
            wordcopy = wordcopy[:position] + '-' + wordcopy[position+1:] # replace the letter with a '-'
            words_guessed= words_guessed[:position] + letter + words_guessed[position+1:] # replace the '_' with the letter
        else:
            position_list=[]

        if len(position_list)>0: # if the letter is present more than once in the word
            print(f'Correct. The letter {letter} is in these positions:', position_list)
        else: # if the letter is present only once in the word
            print(f'Correct. The letter {letter} is in position:', position)
        print('words_guessed: ', words_guessed)
        position_list=[]
        if words_guessed==word:
            break
    else:
        if attempts == max_attempts:
            print(f'I am sorry. That letter is not in the word. You have 1 more try. Last retry.')
        else:
            print(f'I am sorry. That letter is not in the word. You still has {attempts} tries. Retry.')
    attempts+= 1

if words_guessed==word:
    print(f'Congrats, you guessed the word, that is \'{word}\'')
else:
    print('Sorry, but you lost the game')