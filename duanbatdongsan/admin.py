from flask import Blueprint, render_template, request, redirect, url_for, session

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dang-nhap', methods=['GET', 'POST'])
def dang_nhap():
    if request.method == 'POST':
        tai_khoan = request.form.get('tai_khoan')
        mat_khau = request.form.get('mat_khau')

        if tai_khoan == 'admin' and mat_khau == '123456':
            session['admin_da_dang_nhap'] = True
            return redirect(url_for('trang_quan_tri'))
        else:
            return "<h1>Sai tài khoản hoặc mật khẩu! Hãy quay lại.</h1>"

    return render_template('dang_nhap.html')

@admin_bp.route('/dang-xuat')
def dang_xuat():
    session.pop('admin_da_dang_nhap', None)
    return redirect(url_for('admin.dang_nhap'))