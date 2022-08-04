"""

Bài 1: Viết chương trình cho người dùng nhập sở thích của mình 3 lần, sở thích ấy sẽ được đưa vào trong một list và in list ấy ra màn hình.
Input: Đá bóng
Chạy
Nghe nhạc
Output: [“Đá bóng”, “Chạy", “Nghe nhạc"]

"""


def main():
    hobbies = []
    for _ in range(3):
        hobby = input('Hãy nhập sở thích: ')
        hobbies.append(hobby)

    print(hobbies)
