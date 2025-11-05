words_file =open('CROSSWD.txt','r')

def more_than_20(words_file):
   for words in words_file:
        if  len(words) >= 22:
         return (words)
    

def has_no_e(word):
    for i in word:
        if "e" not in i:
            return False
        else: 
            return True
        
def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
        else: 
            return True
    

print(more_than_20(words_file))


