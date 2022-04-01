# mysite
Một **project** có nhiều **application**. Project **mysite** có application **home**
### Thư mục code
- home // chứa code app home
  - migratrions
  - static // chứa các file css, js, img
  - teamplates // chưa file html
  - admin.py
  - apps.py
  - models.py
  - tests.py
  - urls.py // chứa các route của app home
  - views.py // là controller xử lý logic của các route trong file urls.py
- mysite // chứa code project mysite
  - asgi,py
  - settings.py // chứa các cấu hình của project
  - urls.py
  - wsgi.py
  - urls.py // chứa các route của project, có thể import các route của app home từ file urls.py trong thư mục home
- db.sqlite3
- manage.py
### Luồng hoạt động
:point_right: Trình duyệt truy cập vào đường dẫn   
:point_right: Chạy vào file /mysite/urls.py   
:point_right: Dựa vào url sẽ gọi đến file /home/urls.py   
:point_right: Mỗi url sẽ gọi đến một hàm trong file /home/views.py   
:point_right: Các hàm xử lý logic, đọc dữ liệu từ database thông qua /home/models.py và render html từ các file trong /home/teamples   
