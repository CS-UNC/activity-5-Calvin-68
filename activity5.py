# CROSSWD.txt =open('CROSSWD.txt','r')

def more_than_20(file):
    result = []
    wordfile = open(file, 'r')
    for items in wordfile:
        word = items.rstrip('\n')
        if len(word) > 20:
            result.append(word)
    return result
    
def has_no_e(word):
    item = str(word)
    return 'e' not in item.lower()
        

def uses_only(word, letters):
    allowed = set(letters)
    return all(characters in allowed for characters in word)
    
def all_uses_only(file, letters):
    result = []
    opened_file = open(file, 'r')
    for line in opened_file:
        words = line.split()
        for word in words:
            if uses_only(word, letters):
                result.append(word)
    return result