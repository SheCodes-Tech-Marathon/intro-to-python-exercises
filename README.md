# SheCodes Tech Marathon Exercises

## Công việc cần làm

Bạn sẽ cần làm đủ số lượng bài tập theo từng tuần học.
Bạn sẽ truy cập vào thư mục code để làm bài tập.
Với những thư mục hay file khác bạn không được tự ý thay đổi thông tin, tránh việc ảnh hưởng đến bộ test case để test bài tập của bạn.

## Yêu cầu

Trong máy bạn sẽ cần cài đặt những thành phần sau:

- Python
- Git

## Hướng dẫn setup

Trước khi bắt đầu, tải bài tập xuống máy bằng lệnh:

```sh
git clone git@github.com:SheCodes-Tech-Marathon/intro-to-python-exercises.git
```

Nếu như bạn không có git, bạn có thể tải bài tập dưới dạng file zip qua github.

Sau khi cài đặt xong, bạn sẽ cần cài đặt các thư viện cần thiết cho bộ test:

- Với Windows:

```sh
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

- Với MacOS/Linux:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Hướng dẫn chạy test kiểm tra đúng sai của chương trình

Sau khi bạn hoàn thành bài tập và chạy thử để kiểm tra, bạn cần chạy bộ test để kiểm tra với những trường hợp khác mà bọn mình chuẩn bị. Bạn sẽ cần chạy lệnh sau:

- Nếu bạn muốn chạy bộ test cho tất cả bài tập:

```sh
pytest
```

- Nếu bạn muốn chạy bộ test chỉ cho bài tập bạn đang làm:

```sh
pytest tests/test_week[tuần]/test_week[tuần]_ex[bài tập].py
Ví dụ:
pytest tests/test_week1/test_week1_ex1.py
```
