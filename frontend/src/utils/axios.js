// Import thư viện Axios để thực hiện các yêu cầu HTTP. Axios là một thư viện JavaScript phổ biến cho mục đích này.
import axios from 'axios';

// Tạo một instance của Axios và lưu vào biến 'apiInstance'. Instance này sẽ có các cấu hình cụ thể.
const apiInstance = axios.create({
    // Thiết lập URL cơ sở cho instance này. Tất cả các yêu cầu thực hiện bằng instance này sẽ bắt đầu với URL này.
    baseURL: 'http://127.0.0.1:8000/api/v1/',

    // Thiết lập thời gian chờ cho các yêu cầu từ instance này. Nếu một yêu cầu mất hơn 5 giây để hoàn thành, yêu cầu đó sẽ bị hủy.
    timeout: 5000, // Thời gian chờ là 5 giây

    // Định nghĩa các headers sẽ được thêm vào mọi yêu cầu thực hiện từ instance này. Việc này thường dùng để chỉ định kiểu dữ liệu gửi đi và kiểu dữ liệu muốn nhận về.
    headers: {
        'Content-Type': 'application/json', // Yêu cầu sẽ gửi dữ liệu dưới dạng JSON.
        Accept: 'application/json', // Yêu cầu mong đợi nhận dữ liệu phản hồi dưới dạng JSON.
    },
});

// Xuất biến 'apiInstance' để có thể được sử dụng trong các phần khác của mã nguồn. Các mô-đun khác có thể import và sử dụng instance này để thực hiện các yêu cầu API.
export default apiInstance;
