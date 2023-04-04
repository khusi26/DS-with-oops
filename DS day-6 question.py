#day-6 ds question-1
'''Write a python program that accepts a text and displays a 
string which contains the word with the largest frequency
 in the text and the 
frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose 
the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a 
single space between the words.
Perform case insensitive string comparisons wherever 
necessary'''

n = input().split(" ")
dict = {}
for i in n:
    i.lower()
    if(dict.get(i)):
        dict[i] += 1
    else:
        dict[i] = 1
m = list(dict.values())
maxvalue = max(m)
dictkeys = list(dict.keys())
result = dictkeys[0]
print(dict)
for i in dictkeys:
    if(dict.get(i) == maxvalue and len(i) > len(result)):
        result = i
print(result)

#question-2
'''Write a python function, check_anagram() which accepts two 
strings and returns True, if one string is an anagram of 
another string. 
Otherwise returns False.
The two strings are considered to be an anagram if they
 contain repeating characters but none of the characters repeat at the same position.
The length of the strings should be the same ,generate the python code
'''
'''
def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Sort both strings and compare them
    return sorted(str1) == sorted(str2) and str1 != str2
'''
#question-3
'''The number, 197, is called a circular prime because all
 rotations of the digits: 197, 971, and 719, are themselves
 prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 
13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of 
circular primes less than the given limit.'''
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s)):
            return False
        s = s[1:] + s[0]
    return True

def count_circular_primes(limit):
    count = 0
    for n in range(2, limit):
        if is_circular_prime(n):
            count += 1
    return count

limit = int(input("Enter a limit: "))
print("Number of circular primes below", limit, "is", count_circular_primes(limit))
'''

































