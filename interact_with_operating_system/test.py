import csv
import os
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

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

