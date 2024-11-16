# BlogIT-Django-React

Xây dựng hệ thống Server dựa trên MVT của Django-RestFrameWork và Client dựa trên ReactJS

--Khoi dong Backend
py -3.11 -m venv venv

venv\Scripts\activate

## Run Server

py manage runserver

### Khi sử dụng Django Rest Framework (DRF), bạn sẽ phải tự định nghĩa các phương thức HTTP và tự ánh xạ dữ liệu từ ORM (Object-Relational Mapping) theo cách thủ công. Điều này có nghĩa là bạn cần phải viết các lớp view và phương thức xử lý các yêu cầu HTTP (GET, POST, PUT, DELETE, v.v.), cũng như tự quản lý việc chuyển đổi giữa dữ liệu cơ sở dữ liệu (ORM) và các định dạng dữ liệu trả về (thường là JSON).

--Khoi dong Frontend
npm install yarn --global
npm install vite --global

#### khỏi cần chạy

npm create vite@latest . -- --template react

<!-- -- Copy noi dung tu file trong config sang package.json de tai toan bo thu vien va version cua react --> khoi can lam

-- Sau do chay cau lenh <yarn> tren Terminal

## run Client

yarn dev
