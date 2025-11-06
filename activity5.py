words_file =open('CROSSWD.txt','r')

def more_than_20(file):
    result = []
    words_file =open('CROSSWD.txt','r')
    for item in words_file:
        word = item.strip('\n')
        if len(word) >= 20:
            result.append(word)
    return result
            
print(more_than_20('CROSSWD.txt'))
    
def has_no_e(word):
    item = str(word)
    return 'e' not in item.lower()
        
print(has_no_e('allegory'))

def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
        else: 
            return True
    


