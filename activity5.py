# CROSSWD.txt =open('CROSSWD.txt','r')

def more_than_20(file):
    result = []
    wordfile = open(file, 'r')
    for items in wordfile:
        word = items.rstrip('\n')
        if len(word) > 20:
            result.append(word)
    return result

print(more_than_20('CROSSWD.txt'))
    
def has_no_e(word):
    item = str(word)
    return 'e' not in item.lower()
        
print(has_no_e('allegory'))

def uses_only(word, letters):
    allowed = set(letters)
    return all(characters in allowed for characters in word)
    