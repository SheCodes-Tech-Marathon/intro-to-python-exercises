"""

Bài 2: Viết chương trình tính giai thừa của một số nguyên N.
Input: 4
Output: 24

Input: 8
Output: 40320

"""


def main():
    n = int(input('Nhập n: '))
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print(factorial)
