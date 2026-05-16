import csv


class SanPham:
    def __init__(self, file_path="database/sanpham.csv"):
        self.file_path = file_path

    def list(self, page=1, page_size=100):
        danh_sach = []
        try:
            # Đọc dữ liệu bằng thư viện csv chuẩn
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    # Đảm bảo dòng có đủ 5 cột dữ liệu
                    if len(row) >= 5:
                        sp = {
                            "MaDA": row[0].strip(),
                            "TenDuAn": row[1].strip(),
                            "gia": row[2].strip(),
                            "soluong": row[3].strip(),
                            "ViTri": row[4].strip()
                        }
                        danh_sach.append(sp)
        except Exception as e:
            print(f"Lỗi đọc kho sản phẩm: {e}")

        return {"data": danh_sach}