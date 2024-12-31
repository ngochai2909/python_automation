# ex6:Remove duplicates from a list:
numbers = [1, 2, 2, 3, 4, 4, 5]
new_number = set(numbers)


# ex7: Find common elements in two lists:
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
list_3 = set(list_1 + list_2)


# ex8:Sort a list of tuples ( chưa làm được )
tuple_list =  [(1, 'c'), (2, 'a'), (3, 'b')]
sorted_tuple = sorted(tuple_list, key=lambda x:x[1])




# ex9 : Flatten a nested list
list_1 = [[1, 2], [3, 4], [5, 6]]
# for i in list_1:
#     print((e for e in i )
#
#

# ex10: Find the second largest number
list_4 = [10, 20, 4, 45, 99]
list_4.sort()
