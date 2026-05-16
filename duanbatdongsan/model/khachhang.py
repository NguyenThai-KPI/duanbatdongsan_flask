import csv

class KhachHang:
    def __init__(self, file_path="database/khach_hang.csv"):
        self.file_path = file_path

    def list(self, page=1, page_size=100):
        danh_sach = []
        try:
            # Đọc dữ liệu từ file CSV của khách hàng
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    # Đảm bảo dòng có đủ 5 cột dữ liệu
                    if len(row) >= 5:
                        kh = {
                            "MaKH": row[0],
                            "TenKH": row[1],
                            "SDT": row[2],
                            "Email": row[3],
                            "DiaChi": row[4]
                        }
                        danh_sach.append(kh)
        except Exception as e:
            print(f"Lỗi đọc kho khách hàng: {e}")

        return {"data": danh_sach}