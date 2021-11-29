#Q12) Program to find the count of each vowel in a string(use dictionary)

vowels = 'aeiou'

ip_str = 'Hello, welcome to the magic world of python?'


ip_str = ip_str.casefold()


count = {}.fromkeys(vowels,0)


for char in ip_str:
   if char in count:
       count[char] += 1

print(count)