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


def check_character_groups(text):
  result = re.search(r"\w+ ", text)
  return result is not None


print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
