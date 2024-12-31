# 1. Tạo một Dictionary
# Bài tập: Tạo một dictionary lưu thông tin cá nhân của bạn, bao gồm:
# Tên
# Tuổi
# Nghề nghiệp
# Địa chỉ
# In từng key và value của dictionary.
from operator import truediv

from more_itertools.more import permutation_index

information = {
    "name":"hai",
    "age":23,
    "professional":"developer",
    "address":"vietnam"
}
for key,value in information.items():
    print(f"{key}:{value}")

#  2.Kiểm tra Sự Tồn Tại của Key
# Bài tập: Viết một chương trình kiểm tra xem key "age" có tồn tại trong dictionary không.
def check_age_exist(person):
    if person["age"]:
        return True
    return False

# 3. Đếm Số Lượng Key
# Bài tập: Viết một hàm nhận vào một dictionary và trả về số lượng key trong đó.
sample_dict = {"a": 1, "b": 2, "c": 3}
def count_key(dictionary):
    count = 0
    for item in dictionary:
        count += 1
    return count



# 4. Cập nhật Giá trị
# Bài tập: Tạo một dictionary lưu thông tin sản phẩm
product = {"name": "Laptop", "price": 1500, "stock": 5}
product["stock"] = 10
product["price"] = 1400


# 5 Lấy Giá trị Mặc định
# Bài tập: Viết một chương trình lấy giá trị của một key trong dictionary. Nếu key không tồn tại, trả về giá trị mặc định "Not Found".
person = {"name": "Alice", "age": 25}

def check_key(dictionary,key):
    if(dictionary[key]):
        print(dictionary[key])
    else:
        print("Not Found")

