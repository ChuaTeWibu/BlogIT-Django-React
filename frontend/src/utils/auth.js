// Import hàm hook `useAuthStore` từ tệp '../store/auth' để quản lý trạng thái đăng nhập
import { useAuthStore } from "../store/auth";

// Import thư viện axios để thực hiện các yêu cầu HTTP
import axios from "./axios";

// Import jwt_decode để giải mã JSON Web Tokens
import jwt_decode from "jwt-decode";

// Import thư viện Cookies để quản lý cookie trong trình duyệt
import Cookies from "js-cookie";

// Import thư viện Swal (SweetAlert2) để hiển thị các thông báo dạng toast
import Swal from "sweetalert2";

// Cấu hình thông báo toast toàn cục bằng Swal.mixin
const Toast = Swal.mixin({
    toast: true,
    position: "top",
    showConfirmButton: false,
    timer: 1500,
    timerProgressBar: true,
});

// Hàm để xử lý đăng nhập người dùng
export const login = async (email, password) => {
    try {
        // Thực hiện yêu cầu POST để lấy token của người dùng
        const { data, status } = await axios.post("user/token/", {
            email,
            password,
        });

        // Nếu yêu cầu thành công (mã trạng thái 200), thiết lập người dùng đã xác thực và hiển thị thông báo thành công
        if (status === 200) {
            setAuthUser(data.access, data.refresh);

            // Hiển thị thông báo thành công dạng toast
            Toast.fire({
                icon: "success",
                title: "Signed in successfully",
            });
        }

        // Trả về dữ liệu và không có lỗi
        return { data, error: null };
    } catch (error) {
        // Xử lý lỗi và trả về thông tin lỗi
        return {
            data: null,
            error: error.response.data?.detail || "Something went wrong",
        };
    }
};

// Hàm để xử lý đăng ký người dùng mới
export const register = async (full_name, email, password, password2) => {
    try {
        // Thực hiện yêu cầu POST để đăng ký người dùng mới
        const { data } = await axios.post("user/register/", {
            full_name,
            email,
            password,
            password2,
        });

        // Đăng nhập người dùng mới và hiển thị thông báo thành công
        await login(email, password);

        // Hiển thị thông báo đăng ký thành công
        Toast.fire({
            icon: "success",
            title: "Signed Up Successfully",
        });

        // Trả về dữ liệu và không có lỗi
        return { data, error: null };
    } catch (error) {
        // Xử lý lỗi và trả về thông tin lỗi
        return {
            data: null,
            error: error.response.data || "Something went wrong",
        };
    }
};

// Hàm để xử lý đăng xuất người dùng
export const logout = () => {
    // Xóa token truy cập và token làm mới khỏi cookie, đặt lại trạng thái người dùng và hiển thị thông báo thành công
    Cookies.remove("access_token");
    Cookies.remove("refresh_token");
    useAuthStore.getState().setUser(null);

    // Hiển thị thông báo đăng xuất thành công
    Toast.fire({
        icon: "success",
        title: "You have been logged out.",
    });
};

// Hàm để thiết lập người dùng đã xác thực khi tải trang
export const setUser = async () => {
    // Lấy token truy cập và token làm mới từ cookie
    const accessToken = Cookies.get("access_token");
    const refreshToken = Cookies.get("refresh_token");

    // Kiểm tra nếu token không tồn tại
    if (!accessToken || !refreshToken) {
        return;
    }

    // Nếu token truy cập hết hạn, làm mới nó; nếu không, thiết lập người dùng đã xác thực
    if (isAccessTokenExpired(accessToken)) {
        const response = await getRefreshToken(refreshToken);
        setAuthUser(response.access, response.refresh);
    } else {
        setAuthUser(accessToken, refreshToken);
    }
};

// Hàm để thiết lập người dùng đã xác thực và cập nhật trạng thái người dùng
export const setAuthUser = (access_token, refresh_token) => {
    // Đặt token truy cập và token làm mới vào cookie với ngày hết hạn
    Cookies.set("access_token", access_token, {
        expires: 1, // Token truy cập hết hạn sau 1 ngày
        secure: true,
    });

    Cookies.set("refresh_token", refresh_token, {
        expires: 7, // Token làm mới hết hạn sau 7 ngày
        secure: true,
    });

    // Giải mã token truy cập để lấy thông tin người dùng
    const user = jwt_decode(access_token) ?? null;

    // Nếu có thông tin người dùng, cập nhật trạng thái người dùng; nếu không, đặt trạng thái tải là false
    if (user) {
        useAuthStore.getState().setUser(user);
    }
    useAuthStore.getState().setLoading(false);
};

// Hàm để làm mới token truy cập bằng token làm mới
export const getRefreshToken = async () => {
    // Lấy token làm mới từ cookie và thực hiện yêu cầu POST để làm mới token truy cập
    const refresh_token = Cookies.get("refresh_token");
    const response = await axios.post("user/token/refresh/", {
        refresh: refresh_token,
    });

    // Trả về token truy cập mới
    return response.data;
};

// Hàm để kiểm tra xem token truy cập có hết hạn không
export const isAccessTokenExpired = (accessToken) => {
    try {
        // Giải mã token truy cập và kiểm tra nếu nó đã hết hạn
        const decodedToken = jwt_decode(accessToken);
        return decodedToken.exp < Date.now() / 1000;
    } catch (err) {
        // Trả về true nếu token không hợp lệ hoặc đã hết hạn
        return true;
    }
};
