import re
def check_web_address(text):
    # Biểu thức chính quy để kiểm tra tên miền hợp lệ
    pattern = r"^[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$"
    result = re.search(pattern, text)
    return result is not None

print(check_web_address("gmail.com"))           # True
print(check_web_address("www@google"))          # False
print(check_web_address("www.Coursera.org"))    # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True
