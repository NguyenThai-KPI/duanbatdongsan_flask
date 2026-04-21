from flask import Flask, render_template, request, redirect
import csv
import pandas as pd
import os
app = Flask(__name__)


# 1. TUYẾN ĐƯỜNG GỐC (TRANG CHỦ HỆ THỐNG)
@app.route('/')
def trang_chu():
    danh_sach_du_an = []
    # Đọc file CSV
    with open('du_an.csv', mode='r', encoding='utf-8') as file:
        doc_file = csv.DictReader(file)
        for dong in doc_file:
            danh_sach_du_an.append(dong)

    # Hiển thị danh sách 3 dự án
    return render_template('trang_chu.html', cac_du_an=danh_sach_du_an)


thong_tin_chi_tiet = {
    'DA01': {
        'ten': 'Aria Bay',
        'slogan': 'GIAI ĐIỆU TRÊN TẦNG KHÔNG',
        'vi_tri_title': 'VỊ TRÍ HÀNG GHẾ ĐẦU VỊNH KỲ QUAN',
        'quy_mo': '2 HECTA',
        'tang': '40 TẦNG NỔI',
        'tong_can': '2314 CĂN HỘ',
        'anh_nen': 'bg-halong.jpg.png',
        # Dữ liệu Tiện ích
        'tien_ich': [
            {'ten': 'Hồ Bơi ROOFTOP Bốn Mùa', 'mo_ta': 'Trải nghiệm thư giãn sang trọng', 'anh': 'ho-boi.jfif'},
            {'ten': 'Elite Fitness Center', 'mo_ta': 'Trang thiết bị tối tân, HLV chuyên nghiệp',
             'anh': 'phong-tap.jfif'},
            {'ten': 'Nhà Hàng Á - Âu', 'mo_ta': 'Tinh hoa ẩm thực đa quốc gia', 'anh': 'amthuc-a-au.jfif'}
        ],
        # Dữ liệu Sản phẩm
        'san_pham': [
            {'ten': 'Căn hộ Studio', 'dien_tich': '35m2', 'gia': 'Từ 1.5 Tỷ', 'anh': 'can-ho-studio.jpeg'},
            {'ten': 'Căn hộ 2 Phòng Ngủ', 'dien_tich': '65m2', 'gia': 'Từ 2.8 Tỷ', 'anh': 'can-ho-2phong.jpeg'},
            {'ten': 'Căn hộ 1 Phòng ngủ', 'dien_tich': '62m2', 'gia': 'Từ 2.1 Tỷ', 'anh': 'can-ho-1phong.jpeg'}
        ]
    },
    'DA02': {
        'ten': 'Sun Grand City',
        'slogan': 'KIỆT TÁC BÊN VỊNH BÃI CHÁY',
        'vi_tri_title': 'TÂM ĐIỂM KẾT NỐI DU LỊCH',
        'quy_mo': '1.5 HECTA',
        'tang': '35 TẦNG NỔI',
        'tong_can': '1500 CĂN HỘ',
        'anh_nen': 'vitri-ngoi.jfif',
        'tien_ich': [
            {'ten': 'Bể bơi ốc đảo', 'mo_ta': 'Nghỉ dưỡng chuẩn resort 5 sao', 'anh': 'ho-boi-1.jpg'},
            {'ten': 'Sun Gym Club', 'mo_ta': 'Phòng tập hiện đại view biển', 'anh': 'gym-1.png'},
            {'ten:' 'Nhà hàng quốc tế & Buffet': 'Ẩm thực đa quốc gia & không gian bar hiện đại', 'anh': 'amthuc-a-au.jfif'}
        ],
        'san_pham': [
            {'ten': 'Căn hộ 1 Phòng Ngủ', 'dien_tich': '45m2', 'gia': 'Từ 2 Tỷ', 'anh': 'can-ho-1phong.jpeg'},
            {'ten': 'Căn hộ 2 Phòng Ngủ', 'dien_tich': '75m2', 'gia': 'Từ 3.5 Tỷ', 'anh': 'can-ho-2phong.jpeg'},
            {'ten': 'Căn hộ Dual Key', 'dien_tich': '90m2', 'gia': 'Từ 4.2 Tỷ', 'anh': 'can-ho-3phong.jpg'}

        ]
    },
    'DA03': {
        'ten': 'Vinhomes Dragon Bay',
        'slogan': 'BIỂU TƯỢNG THỊNH VƯỢNG HÒN GAI',
        'vi_tri_title': 'ĐỊA THẾ TỰA SƠN HƯỚNG THỦY',
        'quy_mo': '3.2 HECTA',
        'tang': '25 TẦNG NỔI',
        'tong_can': '3000 CĂN HỘ',
        'anh_nen': 'tamnhin-aria.jpg',
        'tien_ich': [
            {'ten': 'Bến du thuyền', 'mo_ta': 'Đẳng cấp thượng lưu', 'anh': 'halong-aria.webp'},
            {'ten': 'Vincom Plaza', 'mo_ta': 'Thiên đường mua sắm sầm uất', 'anh': 'nha-hang-1.jpg'},
            {'ten': 'Bệnh viện Vinmec', 'mo_ta': 'Chăm sóc sức khỏe tiêu chuẩn quốc tế', 'anh': 'nha-hang-2.jpg'}
        ],
        'san_pham': [
            {'ten': 'Căn hộ 2 Phòng Ngủ', 'dien_tich': '68m2', 'gia': 'Từ 3.2 Tỷ', 'anh': 'can-ho-2phong.jpeg'},
            {'ten': 'Căn hộ 3 Phòng Ngủ', 'dien_tich': '90m2', 'gia': 'Từ 4.5 Tỷ', 'anh': 'can-ho-3phong.jpg'},
            {'ten': 'Shophouse Khối Đế', 'dien_tich': '120m2', 'gia': 'Từ 14 Tỷ', 'anh': 'thap-bieutuong.jfif'}
        ]
    }
}


# 2. Tuyến đường xử lý chung (Chỉ dùng 1 template)
@app.route('/du-an/<ma_du_an>')
def chi_tiet_du_an(ma_du_an):
    # Tìm dữ liệu tương ứng với mã dự án
    du_an = thong_tin_chi_tiet.get(ma_du_an)

    if du_an:
        # "Bơm" dữ liệu vào file chi_tiet.html
        return render_template('chi_tiet.html', du_an=du_an)
    return "<h1>Dự án không tồn tại!</h1>", 404

@app.route('/dang-ky' , methods=['POST'])
def su_ly_dang_ky():
    ho_ten = request.form.get('Họ_Tên')
    sdt = request.form.get('Số_Điện_Thoại')
    email = request.form.get('Email_Khách')
    du_an = request.form.get('Du_An_Quan_Tam')

    du_lieu_moi = pd.DataFrame([{
        'Họ Và Tên': ho_ten,
        'Số Điện Thoại': sdt,
        'Email': email,
        'Dự Án Quan Tâm': du_an,
    }])

    ten_file = 'khach_hang_VIP.xlsx'

    if os.path.exists(ten_file):
        df_cu = pd.read_excel(ten_file)
        df_tong = pd.concat([df_cu, du_lieu_moi], ignore_index=True)
    else:
        df_tong = du_lieu_moi
    df_tong.to_excel(ten_file, index=False)
    return render_template('cam_on.html', ten_khach=ho_ten, ten_du_an=du_an)

if __name__ == '__main__':
    app.run(debug=True)