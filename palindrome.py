def palindrome(str1):
    if str1.lower() == (str1[::-1]).lower():
        return f'{str1} is palindrome string'
    return f'{str1} is not a palindrome string'

print(palindrome('racecar'))
