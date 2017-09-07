def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#this function isn't recursive, but demonstrates how you determine a palindrome
def isPalindrome(w):
    if w == w[::-1]:
        return True
    else:
        return False

###Enter your own recursive function to determine if a word is a palindrome


number = int(input('Enter an integer:'))
print(factorial(number))

#word = str(input('Enter a word:'))
#print(isPalindrome(word))
