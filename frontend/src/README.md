1. Thư mục utils
Bắt đầu với các tiện ích (utils), vì chúng cung cấp các hàm cơ bản và cấu hình chung mà các phần khác của dự án sẽ sử dụng.

constants.js:

Đây là tệp nên viết đầu tiên. Nó định nghĩa các hằng số cấu hình như URL API (API_BASE_URL, SERVER_URL, CLIENT_URL, PAYPAL_CLIENT_ID, CURRENCY_SIGN), mà các tệp khác sẽ tham chiếu đến. Điều này giúp bạn dễ dàng cập nhật hoặc quản lý các thông số cấu hình một cách tập trung.
auth.js:

Sau đó, bạn có thể viết auth.js, chứa các hàm quản lý xác thực như login, register, logout, và setUser. Các hàm này sẽ gọi API (dựa trên constants.js) để thực hiện đăng nhập, đăng ký, xác thực người dùng và quản lý phiên làm việc.
axios.js:

Kế đến là axios.js, tệp này tạo một instance của Axios với cấu hình cơ bản (dùng API_BASE_URL từ constants.js) để gọi API. Cấu hình này giúp các tệp khác không cần thiết lập lại URL hoặc các thông số khi gọi API.
useAxios.js:

useAxios.js được xây dựng sau auth.js và axios.js. Đây là một hook để sử dụng Axios có tích hợp cơ chế làm mới (refresh) token khi token hết hạn. Hook này sẽ gọi các hàm từ auth.js để lấy token mới khi cần.
2. Thư mục store
auth.js:
Tiếp theo là auth.js trong thư mục store, tệp này lưu trữ trạng thái xác thực người dùng bằng cách sử dụng thư viện quản lý trạng thái như zustand. Nó cung cấp các trạng thái như isLoggedIn, user, và setUser để các thành phần trong ứng dụng có thể truy cập và cập nhật trạng thái đăng nhập của người dùng.
3. Thư mục plugin
Các tệp trong plugin là các tiện ích bổ sung, cung cấp các hàm và thành phần hỗ trợ cho ứng dụng.

Moment.js:

Tệp này chứa hàm Moment, dùng thư viện moment để định dạng ngày tháng. Viết tệp này sau khi thiết lập các phần chính trong utils và store, để có thể sử dụng ở nhiều nơi nếu cần định dạng ngày tháng trong ứng dụng.
Toast.js:

Toast.js chứa hàm Toast, dùng thư viện sweetalert2 để hiển thị thông báo dạng toast cho người dùng. Tệp này có thể dùng chung cho các thông báo thành công, thất bại, hoặc cảnh báo.
useUserData.js:

Tệp này có thể cung cấp một hook để lấy thông tin người dùng, chẳng hạn user_id hoặc teacher_id. Tệp này thường được sử dụng sau khi đã có auth.js và các tiện ích chính khác, để lấy dữ liệu người dùng trong ứng dụng.
4. Thư mục layouts
Các thành phần trong layouts là những thành phần cấu trúc giúp định hình cách ứng dụng hiển thị và điều hướng giữa các trang.

#MainWrapper.jsx:
    ##MainWrapper.jsx là thành phần bọc ngoài (wrapper) giúp xác thực người dùng trước khi hiển thị nội dung. Thành phần này sẽ gọi hàm setUser từ auth.js trong utils để kiểm tra phiên làm việc và cập nhật trạng thái đăng nhập của người dùng. Viết MainWrapper.jsx sau khi hoàn tất utils và store để đảm bảo nó có thể gọi và kiểm tra xác thực người dùng.
#PrivateRoute.jsx:
    ##PrivateRoute.jsx dùng để bảo vệ các route cần xác thực, chỉ cho phép người dùng đã đăng nhập truy cập vào. Thành phần này sử dụng useAuthStore để kiểm tra trạng thái đăng nhập và điều hướng người dùng đến trang đăng nhập nếu chưa xác thực. Tệp này sẽ cần thiết lập trước các hàm xác thực và store, để kiểm tra và điều hướng người dùng đúng cách.
Tổng kết thứ tự viết mã hợp lý
Viết các cấu hình và hàm tiện ích cơ bản trong utils:

constants.js
auth.js
axios.js
useAxios.js
Thiết lập trạng thái xác thực trong store:

auth.js
Viết các tiện ích bổ sung trong plugin:

Moment.js
Toast.js
useUserData.js
Xây dựng các thành phần bố cục layouts để bảo vệ route và xác thực người dùng:

MainWrapper.jsx
PrivateRoute.jsx