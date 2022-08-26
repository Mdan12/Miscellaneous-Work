# Write a function in Python to check duplicate letters.
# It must accept a string, i.e., a sentence.
# The function should return True if the sentence has any word
# with duplicate letters, else return False. 

sentence = input("Please type in a sentence:\n")
sentence = sentence.replace(' ', '')

def duplicates(sentence):
    for letter in sentence:
        if sentence.count(letter) > 1:
            return True
    return False

result = duplicates(sentence)
if result:
    print ('True')
else:
    print('False')
