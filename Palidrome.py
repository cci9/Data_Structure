def palindrome(string):
    startIndex = 0
    endIndex = len(string) - 1
    while endIndex > startIndex:
        if string[startIndex] == string[endIndex]:
            startIndex = startIndex + 1
            endIndex = endIndex - 1
            if startIndex <= endIndex:
                print('Yes, it is a palidrome')
                break
        else:
            print('Not a palidrome')
            break

def is_palindrome(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        return True
    return False

def is_palindrome_python(string):
    return string == ''.join(string[::-1])

test = 'mamt'
palindrome(test)
print(is_palindrome(test))
print(is_palindrome_python(test))
