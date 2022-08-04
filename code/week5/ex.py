"""

Tạo một class có tên là StringUtilities, các bài tập sẽ tương ứng với các method có trong class đấy.

Bài 1: Viết chương trình nhận một câu và trả lại một câu được viết ngược lại.
Input: sentence = Adam and Eve
Output: Eve and Adam

Input: sentence = A clear blue sky
Output: sky blue clear A

Input: sentence = Lady
Output: Lady

=========================================================

Bài 2: Viết chương trình nhận vào một câu in ra độ dài của từ dài nhất. Nếu chuỗi rỗng hay không hợp lệ thì in ra là 0.
Input: sentence = I like ice cream
Output: 5

Input: sentence = in the nick of time
Output: 4

Input: sentence = ''
Output: 0

=========================================================

Bài 3: Viết chương trình kiểm tra chuỗi các dấu ngoặc có hợp lệ hay không. Các dấu ngoặc bao gồm: “(“, “)”, “[“, “]”, “{“, “}”.
Input: string = {()}[]
Output: True

Input: string = {(
Output: False

Input: string = [(])
Output: False

=========================================================

Bài 4: Viết chương trình loại bỏ các khoảng trắng có trong câu ấy.
Input: string = A very lovely day
Output: Averylovelyday

Input: string = So      much           space
Output: Somuchspace

=========================================================

Bài 5: Viết chương trình nhập vào một chuỗi và in ra một chuỗi sắp xếp theo thứ tự tăng dần theo bảng chữ cái. Chuỗi được sắp xếp không bao gồm các dấu cách (whitespaces)
Input: string = old mcdonald had a farm
Output: aaaacddddfhllmmnoor

"""


class StringUtilities:
    def reverse_sentence(self, sentence: str) -> str:
        pass

    def longest_word_length(self, sentence: str) -> int:
        pass

    def is_valid_parentheses(self, string: str) -> bool:
        pass

    def remove_white_spaces(self, string: str) -> str:
        pass

    def sort_string(self, string: str) -> str:
        pass

