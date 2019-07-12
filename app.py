import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json",'r'))
u_word=input("Enter a Word:")
new_word=u_word.lower()
def meaning(word):
    if word in data:
        return data[word]
    elif(len(get_close_matches(word,data.keys()))>0):
        match=get_close_matches(word,data.keys())
        print("Did you mean %s instead ?"%match[0].upper())
        while(True):
            user=input("Enter Y for Yes and N for No:")
            y_or_no=user.lower()
            if y_or_no=='y':
                print("Showing Result for %s"%match[0].upper())
                return data[match[0]]
                break
            elif y_or_no=='n':
                return "Word Doesn\'t Exist. Please Check the Word"
                break
            else:
                continue
    else:
        return "Word Doesn\'t Exist. Please Check the Word"
output=meaning(new_word)
if type(output)==list:
    for x in output:
        print(x)
else:
    print(output)
pass