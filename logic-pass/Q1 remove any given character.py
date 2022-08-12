def remove_given_character(string,char):
    return string.replace(char,'') if char in string else f"{char} is not in the String"
print(remove_given_character(input('Enter your string: '),input('Enter character to replace: ')))
