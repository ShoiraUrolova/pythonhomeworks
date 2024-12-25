# NUmber data type
#1
number = float(input("Enter a float number: "))
rounded_number=round(number, -2)
print("Rounded number:", rounded_number)
2
a = float(input("Emter a float number1: "))
b = float(input("Emter a float number2: "))
c = float(input("Emter a float number3: "))
eng_katta = max(a,b,c)
eng_kichik = min(a,b,c)
print("eng katta:", eng_katta)
print("eng kichik:", eng_kichik)
#3
kilometers = float(input("enter a float number:"))
meters = kilometers*1000
centimeters = meters*100
print("km to m", meters)
print("km to cm", centimeters)
#4
num1 = int(input("enter bo'linuvchi="))
num2 = int(input("enter bo'luvchi="))
bulinma = num1 // num2
qoldiq = num1 % num2
print("bo'linma:", bulinma)
print("qoldiq", qoldiq)
#5
celcius = float(input("enter the temperature in celcius:"))
fahrenheit = (celcius * 9/5)+32
print("fahrenheit:", fahrenheit)
#6
number = int(input("enter a number:"))
the_last_digit = number % 10
print("the last digit=", the_last_digit)
#7
number = int(input("enter a number:"))
qoldiq = number % 2 
if qoldiq == 0:
   print("even")
else:
     print("odd")


### string questions
#1
year_of_birth = int(input("enter a year"))
age = 2024 - year_of_birth
print("age:", age)
#2




#3
word = str(input("enter string: "))
length = len(word)
print ("legth of the word:", length)
print(word.upper())
print(word.lower())
#4
string = str(input("enter a string: "))
cleaned_string = string.replace(" ", "").lower()
reversed_string = cleaned_string[:: -1]
if cleaned_string==reversed_string:
   print("the string is palindrome")
else:
    print("the string is not palindrome")
#5
string = str(input("enter a sting: ")) 
vowels="aeiou"
consonants= "wrtypsdfghjklzxcvbnmq"
vowel_count =0
consonant_count =0
for char in string.lower():
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
        return vowel_count , consonant_count
print("the number of vowels: ", vowel_count)
print("the number of consonant:", consonant_count)
#6
main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")
if contains(substring, main_string):
    print(f'"{main_string}" contains "{substring}".')
else:
    print(f'"{main_string}" does not contain "{substring}".')
#7
sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the replacement word: ")
updated_sentence = sentence.replace(word_to_replace, replacement_word)
print("Updated sentence:", updated_sentence)
#8
string= str(input("enter a string"))
if string:
    first_char = user_input[0]
    last_char = user_input[-1]
    print(f"The first character is: {first_char}")
    print(f"The last character is: {last_char}")
else:
    print("You entered an empty string!")
#9
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)
#10
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words in the sentence:", word_count)
# 11
user_input = input("Enter a string: ")
contains_digits = any(char.isdigit() for char in user_input)
if contains_digits:
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")
#12
words = input("Enter a list of words separated by space: ").split()
separator = input("Enter the separator character: ")
joined_string = separator.join(words)
print("Joined string:", joined_string)
# 13
user_input = input("Enter a string: ")
no_spaces = user_input.replace(" ", "")
print("String without spaces:", no_spaces)
# 14
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1 == string2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")
#15
sentence = input("Enter a sentence: ")
words = sentence.split()
acronym = ''.join(word[0].upper() for word in words)
print("Acronym:", acronym)
#16
user_input = input("Enter a string: ")
character_to_remove = input("Enter the character to remove: ")
modified_string = user_input.replace(character_to_remove, "")
print("String after removal:", modified_string)
#17
user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
modified_string = ''.join('*' if char in vowels else char for char in user_input)
print("String after replacing vowels:", modified_string)
#18
user_input = input("Enter a string: ")
start_word = input("Enter the word the string should start with: ")
end_word = input("Enter the word the string should end with: ")
if user_input.startswith(start_word) and user_input.endswith(end_word):
    print("the sentence is started with:", start_word)
    print("the sentance is ended with: ", end_word)
else:
    print("the sentence is not started with: ", start_word)
    print("the sentance is not ended with: ", end_word)

### boolean data type
#1
username = input("Enter your username: ")
password = input("Enter your password: ")
if username and password:
    print("Both username and password are provided.")
else:
    print("Username and password cannot be empty.")
#2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
are_equal = (num1 == num2)
print("it is:", are_equal)
#3
num = int(input("Enter a number: "))
is_positive_and_even = (num > 0) and (num % 2 == 0)
print("Is the number positive and even:", is_positive_and_even)
#4
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
are_all_different = (num1 != num2) and (num1 != num3) and (num2 != num3)
print("Are all three numbers different:", are_all_different)
#5
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
have_same_length = len(string1) == len(string2)
print("Do the strings have the same length:", have_same_length)
#6
number = int(input("Enter a number: "))
is_divisible_by_3_and_5 = (number % 3 == 0) and (number % 5 == 0)
print("Is the number divisible by both 3 and 5:", is_divisible_by_3_and_5)
