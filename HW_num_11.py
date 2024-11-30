import random
#START Question 1
bool_arr: list[bool] = [random.choice([True, False]) for _ in range(3)] #a
print(bool_arr)

if all(bool_arr):
    print("All values in the list are True.")
else:
    print("Not all values in the list are True.") #b

if any(bool_arr):
    print("The list contains at least one True.")
else:
    print("The list does not contain any True.") #c

print(not any(bool_arr)) #d

print(not all(bool_arr)) #e

num = [random.randint(-2, 2) for _ in range(5)] #f
print("Numeric list:", num)


print(num != 0 for num in num) #g

print(any(num != 0 for num in num)) # h

print(all(num == 0 for num in num)) #i

print(any(num == 0 for num in num)) #j
#END

#START Question 2
name_city= "Selin Introligator Israel"
print("Original string:", name_city)

print("Length of the string:", len(name_city)) # a

print("Uppercase string:", name_city.upper()) # b

print("Lowercase string:", name_city.lower()) # c

print("Starts with 'John':", name_city.startswith("Selin"))  # d

print("Ends with 'New York':", name_city.endswith("Israel"))  # e

parts = name_city.split()
print("Split into parts:", parts) # f

replaced_string = name_city.replace(" ", "*")
print("Replaced spaces with asterisks:", replaced_string)
print("Split replaced string:", replaced_string.split("*")) # g

print("Centered string:", name_city.center(50, "=")) # h

print("From 4th character to end:", name_city[3:]) # i

print("From start to 4th character:", name_city[:4]) # j

print("Even-indexed characters:", name_city[::2]) # k

print("Title case string:", name_city.title()) # l
#END

#START Question 3
# a
str_a = " day-fun "
print(str_a.strip())# a

str_b = "hello"
print(str_b.isalpha()) # b

str_c = "777"
print(str_c.isdigit()) # c

str_d = " "
print(str_d.isspace()) # d

char_list = ['A ', 'J ', 'N ', 'I ', 'N'] # e
print(''.join(char_list))

joined_with_star = '*'.join([char.strip() for char in char_list]) # f
print(joined_with_star)

str_g = "hELLo"
print("Does 'e' appear in 'hELLo':", 'e' in str_g.lower()) # g

user_input = input("Enter a word: ")
user = [char.upper() for char in user_input if char.isalpha()] # h
print("Uppercase letters from input:", user)

#END

