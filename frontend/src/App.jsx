// Import các thành phần từ react-router-dom và các component khác trong dự án
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import Index from './views/core/'; // Component trang chủ
import MainWrapper from '../src/layouts/MainWrapper'; // Layout bao quanh ứng dụng

// Định nghĩa component chính của ứng dụng
function App() {
  return(
    <>
      {/* BrowserRouter dùng để cung cấp tính năng điều hướng cho ứng dụng */}
      <BrowserRouter>
        {/* MainWrapper bao quanh ứng dụng, có thể chứa layout chung như menu hoặc footer */}
        <MainWrapper>
          {/* Routes chứa các tuyến đường của ứng dụng */}
          <Routes>
            {/* Route xác định một đường dẫn và component sẽ hiển thị khi vào đường dẫn đó */}
            <Route path='/' element={<Index/>}/>
          </Routes>
        </MainWrapper> 
      </BrowserRouter>
    </>
  )
}

// Xuất component App để có thể sử dụng ở file khác
export default App;
