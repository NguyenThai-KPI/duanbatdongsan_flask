import pandas as pd
import os

def luu_du_lieu_dang_ky(ho_ten, du_an, sdt, email):

    du_lieu_moi = pd.DataFrame([{
        'Họ Và Tên': ho_ten,
        'Số Điện Thoại': sdt,
        'Email': email,
        'Dự Án Quan Tâm': du_an,
    }])

    file_excel = 'khach_hang_VIP.xlsx'
    file_csv = 'khach_hang.csv'

    if os.path.exists(file_excel):
        df_cu = pd.read_excel(file_excel)
        df_tong = pd.concat([df_cu, du_lieu_moi], ignore_index=True)
    else:
        df_tong = du_lieu_moi
    df_tong.to_excel(file_excel, index=False)
    df_tong.to_csv(file_csv, index=False, encoding='utf-8-sig')
    return True