import nltk
nltk.download('words')
import string

#---------------------------------------
english_words = nltk.corpus.words.words()
print(len(english_words))
#---------------------------------------

#Encrypt
def encrypt(sentence, key):
    alphabetSTR = string.ascii_lowercase
    alphabet_list = list(alphabetSTR)

    result = ''

    for char in sentence:
        alph = 0
        if not char.isalpha() : 
            if char ==' ' : 
                result += char
            continue

        char = char.lower()
        alph += alphabet_list.index(char) + key
        alphabet = alph % 26
        result += alphabet_list[alphabet]

    return result

#---------------------------------------
#Decrypt
def decrypt(string, key):
    return encrypt(string, -key)

#---------------------------------------
def break_code(string):
    broken = [] # this array has the appended decrypeted version
    for i in range(26):
        trial = decrypt(string,i)
        broken.append(trial)
    
#---------------------------------------
    def words_count(sentence):
        sentence_words = sentence.split()
        eng_count = 0

        for word in sentence_words:
            if word.lower() in english_words:
                eng_count += 1

        return eng_count
#---------------------------------------
    def maybe(sentences):
        maximum = 0
        maximum_sentence = ''

        for sentence in sentences:
            if words_count(sentence) > maximum:
                maximum_sentence = sentence
                maximum = words_count(sentence)
        return maximum_sentence

    return maybe(broken)

#---------------------------------------

if __name__ == "__main__":
    print( encrypt('emnv', 7) )
    print(break_code('Sd gkc dro locd yp dswoc, sd gkc dro gybcd yp dswoc'))