// Nhập hàm 'create' từ thư viện 'zustand'
import { create } from 'zustand';

// Nhập hàm 'mountStoreDevtool' từ thư viện 'simple-zustand-devtools'
import { mountStoreDevtool } from 'simple-zustand-devtools';

// Tạo một cửa hàng Zustand tùy chỉnh có tên 'useAuthStore' bằng cách sử dụng hàm 'create'
const useAuthStore = create((set, get) => ({
    // Định nghĩa biến trạng thái 'allUserData' và khởi tạo nó thành null
    allUserData: null, // Sử dụng biến này để lưu trữ tất cả dữ liệu người dùng

    // Định nghĩa biến trạng thái 'loading' và khởi tạo nó thành false
    loading: false,

    // Định nghĩa hàm 'user' trả về một đối tượng với dữ liệu liên quan đến người dùng
    user: () => ({
        user_id: get().allUserData?.user_id || null,
        username: get().allUserData?.username || null,
    }),

    // Định nghĩa hàm 'setUser' cho phép thiết lập biến trạng thái 'allUserData'
    setUser: (user) => set({ allUserData: user }),

    // Định nghĩa hàm 'setLoading' cho phép thiết lập biến trạng thái 'loading'
    setLoading: (loading) => set({ loading }),

    // Định nghĩa hàm 'isLoggedIn' kiểm tra xem 'allUserData' không phải là null
    isLoggedIn: () => get().allUserData !== null,
}));

// Gắn DevTools chỉ trong môi trường phát triển
if (import.meta.env.DEV) {
    mountStoreDevtool('Store', useAuthStore);
}

// Xuất 'useAuthStore' để sử dụng trong các phần khác của ứng dụng
export { useAuthStore };