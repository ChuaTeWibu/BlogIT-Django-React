// Import các hook 'useEffect' và 'useState' từ React.
// 'useEffect' để thực hiện các hiệu ứng phụ, và 'useState' để quản lý trạng thái cục bộ trong thành phần.
import { useEffect, useState } from "react";

// Import hàm 'setUser' từ tiện ích xác thực người dùng để kiểm tra và thiết lập người dùng.
import { setUser } from "../utils/auth";

// Định nghĩa thành phần 'MainWrapper' là một thành phần chức năng nhận prop 'children'.
const MainWrapper = ({ children }) => {
  // Khởi tạo biến trạng thái 'loading' và gán giá trị ban đầu là 'true', nghĩa là trang đang trong trạng thái tải.
  const [loading, setLoading] = useState(true);

  // Sử dụng 'useEffect' để thực hiện các hiệu ứng phụ sau khi thành phần được render lần đầu tiên (mounted).
  useEffect(() => {
    // Định nghĩa một hàm bất đồng bộ 'handler' để xử lý các tác vụ xác thực.
    const handler = async () => {
      // Đặt trạng thái 'loading' là 'true' để biểu thị rằng dữ liệu đang được tải.
      setLoading(true);

      // Thực hiện kiểm tra xác thực người dùng một cách bất đồng bộ thông qua hàm 'setUser'.
      await setUser();

      // Sau khi xác thực hoàn tất, đặt trạng thái 'loading' thành 'false' để ngừng chế độ tải.
      setLoading(false);
    };

    // Gọi hàm 'handler' ngay sau khi thành phần được render lần đầu.
    handler();
  }, []); // Mảng rỗng để chỉ gọi 'useEffect' khi thành phần được mount.

  // Hiển thị nội dung con (children) nếu quá trình tải hoàn tất (loading là false).
  // Nếu đang tải (loading là true), không hiển thị nội dung nào.
  return <>{loading ? null : children}</>;
};

// Xuất thành phần 'MainWrapper' để có thể sử dụng trong các phần khác của ứng dụng.
export default MainWrapper;
