// Import thư viện Axios để thực hiện các yêu cầu HTTP.
import axios from 'axios';

// Import các hàm liên quan đến xác thực từ tệp `auth` để xử lý việc làm mới token và kiểm tra token có hết hạn không.
import { getRefreshToken, isAccessTokenExpired, setAuthUser } from './auth';

// Import `API_BASE_URL` từ tệp `constants` để sử dụng làm URL cơ sở cho các yêu cầu.
import { API_BASE_URL } from './constants';

// Import thư viện `js-cookie` để quản lý cookie trong trình duyệt.
import Cookies from 'js-cookie';

// Định nghĩa hàm `useAxios`, hàm này tạo một instance của Axios đã được cấu hình tùy chỉnh.
const useAxios = () => {
    // Lấy access token và refresh token từ cookie.
    const accessToken = Cookies.get('access_token');
    const refreshToken = Cookies.get('refresh_token');

    // Tạo một instance của Axios với URL cơ sở và thêm access token vào headers mặc định.
    const axiosInstance = axios.create({
        baseURL: API_BASE_URL, // Đặt URL cơ sở cho tất cả các yêu cầu từ instance này.
        headers: { Authorization: `Bearer ${accessToken}` }, // Đặt header Authorization để chứa access token.
    });

    // Thêm một interceptor cho các yêu cầu của instance.
    axiosInstance.interceptors.request.use(async (req) => {
        // Kiểm tra nếu access token còn hạn
        if (!isAccessTokenExpired(accessToken)) {
            return req; // Nếu còn hạn, trả về yêu cầu gốc.
        }

        // Nếu access token đã hết hạn, thực hiện làm mới token
        const response = await getRefreshToken(refreshToken);

        // Cập nhật trạng thái xác thực với access token và refresh token mới.
        setAuthUser(response.access, response.refresh);

        // Cập nhật lại header Authorization của yêu cầu với access token mới.
        req.headers.Authorization = `Bearer ${response?.data?.access}`;
        return req; // Trả về yêu cầu đã được cập nhật.
    });

    return axiosInstance; // Trả về instance Axios tùy chỉnh đã cấu hình.
};

// Xuất hàm `useAxios` để các thành phần khác có thể sử dụng.
export default useAxios;
