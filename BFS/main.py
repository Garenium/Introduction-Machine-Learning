#Dictionary source: https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json 
from collections import deque
import json

language_alphabets = {
    'en': 'abcdefghijklmnopqrstuvwxyz',
}

def print_word(word):
    print(word[0],'\n')

    print(word[1])

def bfs(word, dictionary, language_alphabet):
    #A queue has is a list with tuples word and the path visited 
    #We use a tuple to keep track of valid words in case of a spelling error
    #I chose dequue because it's faster than SimpleQueue
    queue = deque([(word, [])])
    #Basically a list but must have unique elements
    visited = set([word])
    while not len(queue) == 0:
        curr_word, path = queue.popleft()
        if curr_word in dictionary:
            #returning a tuple
            return (curr_word, dictionary[curr_word], path)
        for i in range(len(curr_word)):
            #Breadth first search
            for char in language_alphabet:
                #if curr_word is dog 
                #new_word = '' + a + 'og'
                new_word = curr_word[:i] + char + curr_word[i+1:]
                if new_word in dictionary and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, path + [(curr_word, new_word)]))
    return None

f = open('dictionary.json')
word_dict = json.load(f)
# print(type(word_dict)) #<class 'dict'>

language = input("What languages are you interested (en)? ")
if(language == ""): language = "en"
else: exit()

word_input = input("Type a word: ").lower()

word = bfs(word_input, word_dict, language_alphabets[language])

if(not word==None):
    print_word(word)

# print(bfs(word.lower(), word_dict, language_alphabets[language]))

# list_r = [1,2,3]
# print(list_r)