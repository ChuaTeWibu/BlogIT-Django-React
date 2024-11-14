// Import thành phần 'Navigate' từ thư viện 'react-router-dom'. Thành phần này dùng để điều hướng đến các đường dẫn khác trong ứng dụng.
import { Navigate } from "react-router-dom";

// Import hàm 'useAuthStore' từ một store xác thực (auth store) tùy chỉnh.
import { useAuthStore } from "../store/auth";

// Định nghĩa thành phần 'PrivateRoute' dưới dạng một thành phần chức năng (functional component) nhận vào một prop 'children'.
const PrivateRoute = ({ children }) => {
  // Sử dụng hook 'useAuthStore' để kiểm tra trạng thái xác thực của người dùng.
  // Có vẻ như đang sử dụng một thư viện quản lý trạng thái như 'zustand' hoặc 'mobx-state-tree' để quản lý trạng thái đăng nhập.
  const loggedIn = useAuthStore((state) => state.isLoggedIn)();

  // Kiểm tra nếu người dùng đã đăng nhập, thì hiển thị thành phần con (children).
  // Nếu người dùng chưa đăng nhập, điều hướng họ đến trang đăng nhập.
  return loggedIn ? <>{children}</> : <Navigate to="/login" />;
};

// Xuất thành phần 'PrivateRoute' để có thể sử dụng trong các phần khác của ứng dụng.
export default PrivateRoute;
