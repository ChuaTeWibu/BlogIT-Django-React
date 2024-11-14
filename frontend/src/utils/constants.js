// Import mô-đun `UserData` từ đường dẫn `../views/plugin/UserData`. `UserData` có thể là một hàm hoặc một thành phần chứa thông tin người dùng.
import UserData from "../views/plugin/UserData";

// Định nghĩa hằng số `API_BASE_URL` là URL cơ sở cho các yêu cầu API của ứng dụng.
export const API_BASE_URL = "http://127.0.0.1:8000/api/v1/";

// Định nghĩa hằng số `SERVER_URL` là URL của server backend. Hữu ích để liên kết trực tiếp với backend khi cần.
export const SERVER_URL = "http://127.0.0.1:8000";

// Định nghĩa hằng số `CLIENT_URL` là URL của client. Hữu ích khi cần tham chiếu URL của frontend, chẳng hạn trong quá trình xác thực.
export const CLIENT_URL = "http://localhost:5173";

// Định nghĩa hằng số `PAYPAL_CLIENT_ID` là ID của client PayPal, được dùng khi tích hợp cổng thanh toán PayPal. Ở đây, giá trị là "test" để kiểm thử.
export const PAYPAL_CLIENT_ID = "test";

// Định nghĩa ký hiệu tiền tệ `CURRENCY_SIGN`, ở đây là đô-la Mỹ.
export const CURRENCY_SIGN = "$";

// Lấy `user_id` từ đối tượng trả về của `UserData()`, nếu có.
export const userId = UserData()?.user_id;

// Lấy `teacher_id` từ đối tượng trả về của `UserData()`, nếu có.
export const teacherId = UserData()?.teacher_id;

// In `teacherId` ra console để kiểm tra giá trị, giúp xác thực rằng `teacherId` đã được lấy đúng từ `UserData`.
console.log(teacherId);
