# mysite
Một **project** có nhiều **application**. Project **mysite** có application **home**
### Thư mục code
- [home](home) // chứa code app home
  - [migratrions](home/migratrions)
  - [static](home/static) // chứa các file css, js, img
  - [teamplates](home/teamplates) // chứa file html
  - [admin.py](home/admin.py)
  - [apps.py](home/apps.py)
  - [models.py](home/models.py) // dùng để tương tác với database, có các class tương ứng các table
  - [tests.py](home/tests.py)
  - [urls.py](home/urls.py) // chứa các route của app home
  - [views.py](home/views.py) // là controller xử lý logic của các route trong file urls.py
- [mysite](mysite) // chứa code project mysite
  - [asgi.py](mysite/asgi,py)
  - [settings.py](mysite/settings.py) // chứa các cấu hình của project
  - [urls.py](mysite/urls.py)
  - [wsgi.py](mysite/wsgi.py)
  - [urls.py](mysite/urls.py) // chứa các route của project, có thể import các route của app home từ file urls.py trong thư mục home
- [db.sqlite3](db.sqlite3)
- [manage.py](manage.py)
### Luồng hoạt động
:point_right: Trình duyệt truy cập vào đường dẫn   
:point_right: Chạy vào file [/mysite/urls.py](mysite/urls.py)   
:point_right: Dựa vào url sẽ gọi đến file [/home/urls.py](home/urls.py)   
:point_right: Mỗi url sẽ gọi đến một hàm trong file [/home/views.py](home/views.py)   
:point_right: Các hàm xử lý logic, đọc dữ liệu từ database thông qua [/home/models.py](home/models.py) và render html từ các file trong [/home/teamples](home/teamplates)   
