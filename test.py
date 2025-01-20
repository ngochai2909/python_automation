import csv
import os
import datetime
from time import process_time_ns

# os.chdir("sub_dir")
# os.chdir("new_file")
# current_file = os.getcwd()
# directory = "new_file"
# list_file = os.listdir("new_file")
# for file in list_file:
#     full_name = os.path.join(current_file,directory,file)
#     if os.path.isdir(full_name):
#         print(f"{full_name} is a directory")
#     else:
#         print(f"{full_name} is a file")

#
# hosts = [["workstation.local","299.792.458"],["webserver.cloud","10.2.5.6"]]
# with open('hosts.csv','w') as hosts_csv:
#     writer = csv.writer(hosts_csv)
#     writer.writerows(hosts)

# string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
#
# # Tách chuỗi thành các phần 4 ký tự
# chunks = [string[i:i+1] for i in range(0, len(string), 1)]
#
# # In kết quả với dấu phẩy giữa các phần
# print("/n ".join(chunks))

#
# a = 1
# b = 1
# c = 2
# n = 3
# x_list = [i for i in range(a+1)]
# y_list = [i for i  in range(b+1)]
# z_list = [i for i in range(c+1)]
#
# list_all = [[x,y,z] for x in x_list for y in y_list for z in z_list]
#
# list_only = [i for i in list_all if sum(i) != n]
#
# # print(x_list, y_list ,z_list)
# print(list_only)

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     uniq_list = list(set(arr))
#     uniq_list.sort()
#     print(uniq_list[-2])

# records = [["c",10],["b",9],["a",10]]
#
# score = sorted(list(set(i[1] for i in records)))
#
# names = sorted([name[0] for name in records if name[1] == score[-1]])
# print(names)


if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record = [name,score]
        records.append(record)
    score = sorted(list(set(i[1] for i in records)))
    names = sorted([name[0] for name in records if name[1] == score[-3]])
    for name in names:
        print(name)
