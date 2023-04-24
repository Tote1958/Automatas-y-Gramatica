def counter(text):
    #text = text.translate(str.maketrans('', '', chars))
    text = text.translate(str.maketrans('', '', ''.join(chars)))
    words.append(text)
    word = words[-1].split(' ')
    '''print(words)
    print(word)'''
    for i in word:
        i = i.lower()
        if not i in new_words:
            new_words.append(i)
            repetitions.append(1)
        else:
            repetitions[new_words.index(i)] = repetitions[new_words.index(i)] + 1

words = []
repetitions = []
new_words = []
max = 0
#chars = '.,!"():1234567890'
chars = ['.', ',', '!', '"', '\n', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')', ':', ';', "'"]

with open('Ej_d.txt', encoding='UTF-8') as file:
    line = file.readlines()
    for i in line:
        counter(i)

for i in repetitions:
    if i > max:
        max = i
        max_word = new_words[repetitions.index(i)]
print(new_words)
print(repetitions)
print('Palabra más repetida: ', max_word, ' Se repitió ', max, ' veces.')