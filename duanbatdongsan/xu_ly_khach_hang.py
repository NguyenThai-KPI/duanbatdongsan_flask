import pandas as pd
import os


def luu_du_lieu_dang_ky(ho_ten, sdt, email, du_an):  # Đã sắp xếp lại thứ tự biến cho chuẩn với app.py
    du_lieu_moi = pd.DataFrame([{
        'MaKH': '',  # Để trống mã KH để Admin tự điền sau trên Desktop
        'TenKH': ho_ten,
        'SDT': sdt,
        'Email': email,
        'DiaChi': du_an  # Tạm lưu tên dự án quan tâm vào cột Địa chỉ để khớp với format Desktop
    }])

    # ÉP ĐƯỜNG DẪN LƯU VÀO THƯ MỤC DATABASE
    file_excel = 'database/khach_hang_VIP.xlsx'
    file_csv = 'database/khach_hang.csv'

    # Tạo thư mục database nếu chưa có
    if not os.path.exists('database'):
        os.makedirs('database')

    if os.path.exists(file_excel):
        df_cu = pd.read_excel(file_excel)
        df_tong = pd.concat([df_cu, du_lieu_moi], ignore_index=True)
    else:
        df_tong = du_lieu_moi

    df_tong.to_excel(file_excel, index=False)
    # Không dùng index=False để Pandas không đẻ thêm cột số thứ tự
    df_tong.to_csv(file_csv, index=False, encoding='utf-8-sig')
    return True