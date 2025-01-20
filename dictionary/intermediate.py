# 6.Tần số Ký tự
# Bài tập: Viết một chương trình đếm số lần xuất hiện của mỗi ký tự trong một chuỗi và lưu kết quả trong dictionary.
text = "hello"
statis = {}
for i in text:
    statis[i] = text.count(i)

# 7.Lọc Dictionary
numbers = {"a": 1, "b": 3, "c": 2, "d": 5}
new_numbers = {}
for key, value in numbers.items():
    if value != 2:
        new_numbers[key] = value

#8. Hợp hai Dictionaries
# Bài tập: Viết một chương trình hợp hai dictionaries. Nếu key trùng lặp, cộng giá trị của chúng.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4,"d":12}
for key, value in dict2.items():
    if key in dict1:
        dict1[key] += value
    else:
        dict1[key] = value

# 9.Tạo Dictionary Từ Hai Danh sách
# Bài tập: Cho hai danh sách: một danh sách tên và một danh sách điểm, hãy ghép chúng thành một dictionary.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
combine =dict( zip(names, scores))


