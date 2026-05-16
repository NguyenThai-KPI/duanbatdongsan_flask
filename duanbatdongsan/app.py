from flask import Flask, render_template, request, redirect, session, url_for
import csv

from thong_tin_chi_tiet import thong_tin_chi_tiet
from xu_ly_khach_hang import luu_du_lieu_dang_ky

app = Flask(__name__)
app.secret_key = 'batdongsan_bi_mat'


@app.route('/')
def trang_chu():
    danh_sach_du_an = []
    # ĐÃ ĐỔI ĐƯỜNG DẪN ĐỌC FILE VỀ DATABASE/SANPHAM.CSV
    try:
        with open('database/sanpham.csv', mode='r', encoding='utf-8') as file:
            doc_file = csv.reader(file)
            # Vì Tkinter lưu CSV không có header (dòng tiêu đề), ta phải đọc bằng index
            for row in doc_file:
                if len(row) >= 5:
                    danh_sach_du_an.append({
                        'MaDA': row[0],
                        'TenDuAn': row[1],
                        'Gia': row[2],
                        'SoLuong': row[3],
                        'ViTri': row[4]
                    })
    except FileNotFoundError:
        pass # Nếu chưa có file thì bỏ qua không báo lỗi

    return render_template('trang_chu.html', cac_du_an=danh_sach_du_an)

@app.route('/du-an/<ma_du_an>')
def chi_tiet_du_an(ma_du_an):
    du_an = thong_tin_chi_tiet.get(ma_du_an)
    if du_an:
        return render_template('chi_tiet.html', du_an=du_an)
    return "<h1>Dự án không tồn tại!</h1>", 404

@app.route('/dang-ky' , methods=['POST'])
def dang_ky():
    ho_ten = request.form.get('Họ_Tên')
    sdt = request.form.get('Số_Điện_Thoại')
    email = request.form.get('Email_Khách')
    du_an = request.form.get('Du_An_Quan_Tam')

    luu_du_lieu_dang_ky(ho_ten, sdt, email, du_an)
    return render_template('cam_on.html', ten_khach=ho_ten, ten_du_an=du_an)

if __name__ == '__main__':
    app.run(debug=True)