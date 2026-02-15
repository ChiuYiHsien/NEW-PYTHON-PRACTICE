str1, str2 = "python", "drgon"

print("aa" not in str1)

len_str1 = len(str1)
len_str2 = len(str2)
if len_str1 != len_str2:
    print("The length of the two strings are not equal.")


first_name = "Yi-Hsien"
last_name = "Chiu"
# %s is a placeholder for string, and the values are passed in a tuple after the % operator.
print("My name is %s %s" % (first_name, last_name))
print("My name is {} {}" .format(first_name, last_name))  # .format() method
print(f"My name is {first_name} {last_name}")  # f-string

challenge = "I am enjoying 30 days of python"
# index() method returns the index of the first occurrence of the specified value.
print(challenge.index("30"))

print(challenge.find("30"))
print(challenge.find("chiu"))

web = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator.
print(" | ".join(web))

strings = ["Thirty", "Days", "Of", "Python"]
print(strings[0] + " " + strings[1] + " " + strings[2] + " " + strings[3])


test = "coding for all coding "
print(test.strip("coding "))
print(test.swapcase())
print(test.capitalize())
print(test.title()) # 8
print(test.split()[0])
print(test.find("coding"))
print(test[-1])
print(test.index("c"))
print(test.replace("coding", "python"))

test2 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(test2.split(", "))

str1 = 'You cannot end a sentence with because because because is a conjunction'
print(str1.index("because"))
print(str1.rindex("because"))
print(str1.replace("because because because ", ""))

list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(list1))

print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")