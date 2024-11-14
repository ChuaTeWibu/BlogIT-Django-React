// Import thư viện SweetAlert2 với tên `Swal`. Thư viện này giúp tạo các thông báo (alert) hiện đại, tùy chỉnh được.
import Swal from "sweetalert2";

// Định nghĩa hàm `Toast` để hiển thị thông báo dạng toast với các tham số `icon`, `title`, và `text`.
function Toast(icon, title, text) {
    // Tạo một instance `Toast` sử dụng `Swal.mixin`, thiết lập các tùy chọn cấu hình mặc định.
    const Toast = Swal.mixin({
        toast: true,                // Kiểu thông báo là toast, tức là một thông báo nhỏ hiện lên góc màn hình.
        position: "top",            // Đặt vị trí của thông báo ở phía trên màn hình.
        showConfirmButton: false,   // Ẩn nút xác nhận để thông báo tự động biến mất.
        timer: 1500,                // Thời gian hiển thị thông báo là 1500ms (1.5 giây).
        timerProgressBar: true,     // Hiển thị thanh tiến trình thời gian còn lại của thông báo.
    });

    // Trả về một thông báo với biểu tượng, tiêu đề và nội dung được tùy chỉnh bởi các tham số đầu vào.
    return Toast.fire({
        icon: icon,  // Biểu tượng của thông báo (ví dụ: 'success', 'error', 'info').
        title: title, // Tiêu đề của thông báo.
        text: text,   // Nội dung phụ của thông báo.
    });
}

// Xuất hàm `Toast` để có thể được sử dụng ở các phần khác của mã nguồn.
export default Toast;
