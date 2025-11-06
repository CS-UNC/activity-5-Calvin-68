words_file =open('CROSSWD.txt','r')

def more_than_20(words_file):
    result = []
    for item in words_file:
        word = item.strip('\n')
        if len(word) > 20:
            result.append(word)
    return result
            

    
def has_no_e(word):
    item = str(word)
    return 'e' in item.lower()
        


def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
        else: 
            return True
    


