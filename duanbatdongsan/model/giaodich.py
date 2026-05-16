import csv

class GiaoDich:
    def __init__(self, file_path="database/giao_dich.csv"):
        self.file_path = file_path

    def list(self, page=1, page_size=100):
        danh_sach = []
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 6:
                        gd = {
                            "MaGD": row[0],
                            "MaKH": row[1],
                            "MaDA": row[2],
                            "Ngay": row[3],
                            "SoTien": row[4],
                            "TrangThai": row[5] # VD: Đã cọc, Đã thanh toán, Hủy
                        }
                        danh_sach.append(gd)
        except Exception as e:
            print(f"Lỗi đọc kho giao dịch: {e}")
        return {"data": danh_sach}