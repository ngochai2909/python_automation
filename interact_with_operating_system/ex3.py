import os


def parent_directory():
    # Tạo đường dẫn tương đối tới thư mục cha
    relative_parent = os.path.join(os.getcwd(), "..")

    # Chuyển đổi đường dẫn thành tuyệt đối
    absolute_parent = os.path.abspath(relative_parent)

    # Trả về đường dẫn tuyệt đối của thư mục cha
    return absolute_parent


print(parent_directory())
