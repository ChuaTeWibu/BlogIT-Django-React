// Import thư viện Moment.js với tên `moment`. Thư viện này giúp làm việc với thời gian, ngày tháng một cách dễ dàng và hiệu quả.
import moment from "moment";

// Định nghĩa hàm `Moment`, nhận vào một tham số `date` là ngày cần định dạng.
function Moment(date) {
    // Sử dụng moment để định dạng ngày `date` theo định dạng "DD MMM, YYYY."
    // - "DD" là ngày (ví dụ: 01, 02, ... 31)
    // - "MMM" là tháng viết tắt (ví dụ: Jan, Feb, ... Dec)
    // - "YYYY" là năm đầy đủ (ví dụ: 2023)
    return moment(date).format("DD MMM, YYYY.");
}

// Xuất hàm `Moment` để có thể sử dụng ở các phần khác trong mã nguồn.
export default Moment;
