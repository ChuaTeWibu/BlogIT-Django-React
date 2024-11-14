import React from "react";
import Cookies from "js-cookie";
import jwtDecode from "jwt-decode";

// Hàm lấy thông tin người dùng từ token được lưu trữ trong cookie trình duyệt
function useUserData() {
    // Lấy giá trị của access token và refresh token từ cookie trình duyệt
    let access_token = Cookies.get("access_token");
    let refresh_token = Cookies.get("refresh_token");

    // Kiểm tra xem cả hai token đều có giá trị không
    if (access_token && refresh_token) {
        // Cả hai token đều có giá trị, thực hiện các bước tiếp theo
        // Lấy giá trị của refresh token
        const token = refresh_token;
        // Giải mã token để lấy thông tin người dùng
        const decoded = jwtDecode(token);

        // Trả về thông tin người dùng đã được giải mã từ token
        return decoded;
    } else {
        // Một hoặc cả hai token không có giá trị, xử lý lỗi hoặc chuyển hướng người dùng
        // Không thực hiện bất kỳ hành động nào cụ thể, nhưng có thể được sử dụng để xử lý lỗi
        // Ví dụ: hiển thị thông báo lỗi hoặc chuyển hướng người dùng đến trang đăng nhập
    }
}

// Xuất khẩu hàm useUserData dưới dạng hàm mặc định
export default useUserData;