
def hasVowel(list_):
    list_ = str(list_).lower()
    if 'a' in list_ or 'e' in list_ or 'i' in list_ or 'o' in list_ or 'u' in list_ :
        return True
    else:
        return False 

def vowel(l):
    l = str(l).lower()
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        return True
    else:
        return False
    
result = hasVowel("Hola")
print(result)
result = hasVowel("bbbbb")
print(result)

result = vowel("*")
print(result)
result = vowel("c")
print(result)

