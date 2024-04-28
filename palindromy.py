def palindrome(word):
    """
    Checks if word given as argumrent is a palindrome (True) or not (False). 
    """
    i = len(word)
    x = 0
    y = i-1
    if i > 1:
        while word[x] == word[y]:
            x +=1
            y -=1
            if x >= y:
                return True
        else:  
            return False    
    else: 
        return False
print(palindrome("kajak"))