from collections import Counter

def repeated_char(string,char):
    return f"{char} is repeated {Counter(string)[char]} times" if char in string else f'{char} is not in String'
print(repeated_char('haya','k'))