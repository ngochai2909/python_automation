# ex1
list_number = [1,2,3,4,5]
number_2nd = list_number[2]
number_4th = list_number[4]


# ex2
fruits = ['apple', 'banana', 'cherry']
# Replace the 2nd element with 'orange' and append 'grape' to the list.
fruits.insert(2,"orange")
fruits.append('grape')


#ex3
def loops_function(elements):
    print( [element for element in elements])

# ex4

list_numbers = [2, 7, 3, 8, 10]
count = 0
for number in list_numbers:
    count += number
max_number = max(list_numbers)


# ex5
new_tuple = (1, 2, 3, 4, 5)
converted_list = list(new_tuple)
converted_list.append(6)
converted_tuple = tuple(converted_list)
