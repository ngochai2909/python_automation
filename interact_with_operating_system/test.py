import csv
import os
import re



# import datetime
#
# parent_dir = os.path.abspath(os.path.join(os.getcwd(),".."))
# os.chdir(parent_dir)
#
# timestamp = os.path.getmtime("file.txt")
# readable_time =  datetime.datetime.fromtimestamp(timestamp)
# #This code will provide the date and time for the file in an
# #easy-to-understand format
# print(readable_time)


# print(os.path.getsize("program.py"))

# users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
#  {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
#   {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
# keys = ["name", "username", "department"]
# with open('by_department.csv', 'w') as by_department:
#     writer = csv.DictWriter(by_department, fieldnames=keys)
#     writer.writeheader()
#     writer.writerows(users)

# print(re.search(r"cat|dog", "I like cats."))
# print(re.search(r"cat|dog", "I love dogs!"))
# print(re.search(r"cat|dog", "I like both dogs and cats."))
# print(re.findall(r"cats|dogs", "I like both dogs and cats."))


# def check_character_groups(text):
#   result = re.search(r"\w+ ", text)
#   return result is not None
#
#
# print(check_character_groups("One")) # False
# print(check_character_groups("123  Ready Set GO")) # True
# print(check_character_groups("username user_01")) # True
# print(check_character_groups("shopping_list: milk, bread, eggs.")) # False



# def check_sentence(text):
#     result = re.search(r"^[A-Z].*[.!?]$", text)
#     return result != None
#
# # Test cases
# print(check_sentence("Is this is a sentence?"))  # True
# print(check_sentence("is this is a sentence?"))  # False
# print(check_sentence("Hello"))  # False
# print(check_sentence("1-2-3-GO!"))  # False
# print(check_sentence("A star is born."))  # True

# result = re.search(r"\d+","this is my number: 123-234-123-123")
# print(result)
# def rearrange_name(name):
#   result = re.search(r"^(\w*) (\w.*)$", name)
#   if result is None:
#     return name
#   return "{} {}".format(result[2], result[1])
# name=rearrange_name("Nguyen Ngoc Hai")
# full_name = rearrange_name("Lucas Daniel")
# print(name)
# print(full_name)

text = "this is eeeeeeee"
result = re.search(r"[a-e]",text)


print(result)