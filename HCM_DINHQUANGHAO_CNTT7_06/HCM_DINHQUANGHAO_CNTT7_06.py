meeting = [
    {
        'ID': 'BK001',
        'ten_phong': 'Phòng Thảo Luận A',
        'ten_nguoi_dat': 'Phòng Marketing',
        'gio_bat_dau': 9,
        'gio_ket_thuc': 12,
        'tong_thoi_gian': 3,
        'phan_loai': 'Tiêu chuẩn'
    }
]


def xep_loai(tong_gio):
    if tong_gio < 2:
        return 'Ngắn'
    elif tong_gio < 4:
        return 'Tiêu chuẩn'
    elif tong_gio < 6:
        return 'Dài'
    else:
        return 'Quá tải (Cần xem xét lại)'


def booking_show():
    if not meeting:
        print('Hiện tại không có cuộc họp nào')
        return

    print('-' * 130)
    print('{:10} {:25} {:25} {:15} {:15} {:15} {:25}'.format(
        'ID', 'Tên phòng', 'Người đặt',
        'Bắt đầu', 'Kết thúc',
        'Tổng giờ', 'Phân loại'
    ))
    print('-' * 130)

    for item in meeting:
        print('{:10} {:25} {:25} {:15} {:15} {:15} {:25}'.format(
            item['ID'],
            item['ten_phong'],
            item['ten_nguoi_dat'],
            item['gio_bat_dau'],
            item['gio_ket_thuc'],
            item['tong_thoi_gian'],
            item['phan_loai']
        ))


def sig_meeting():
    id_BK = input('Nhập mã BK: ').strip().upper()

    for item in meeting:
        if item['ID'] == id_BK:
            print('Mã BK đã tồn tại!')
            return

    ten_phong = input('Nhập tên phòng họp: ').strip()
    ten_nguoi_dat = input('Nhập tên người đặt: ').strip()

    try:
        gio_bat_dau = int(input('Nhập giờ bắt đầu (0-24): '))
        gio_ket_thuc = int(input('Nhập giờ kết thúc (0-24): '))
    except ValueError:
        print('Giờ phải là số!')
        return

    if not (0 <= gio_bat_dau <= 24 and 0 <= gio_ket_thuc <= 24):
        print('Giờ phải nằm trong khoảng 0-24')
        return

    if gio_bat_dau >= gio_ket_thuc:
        print('Giờ kết thúc phải lớn hơn giờ bắt đầu!')
        return

    tong_thoi_gian = gio_ket_thuc - gio_bat_dau
    phan_loai = xep_loai(tong_thoi_gian)

    meeting.append({
        'ID': id_BK,
        'ten_phong': ten_phong,
        'ten_nguoi_dat': ten_nguoi_dat,
        'gio_bat_dau': gio_bat_dau,
        'gio_ket_thuc': gio_ket_thuc,
        'tong_thoi_gian': tong_thoi_gian,
        'phan_loai': phan_loai
    })

    print('Đăng ký phòng họp thành công!')


def update_booking():
    booking_id = input('Nhập mã BK cần cập nhật: ').strip().upper()

    for item in meeting:
        if item['ID'] == booking_id:

            ten_phong = input(
                f"Tên phòng mới ({item['ten_phong']}): "
            ).strip()

            ten_nguoi_dat = input(
                f"Tên người đặt mới ({item['ten_nguoi_dat']}): "
            ).strip()

            try:
                gio_bat_dau = int(
                    input(f"Giờ bắt đầu mới ({item['gio_bat_dau']}): ")
                )

                gio_ket_thuc = int(
                    input(f"Giờ kết thúc mới ({item['gio_ket_thuc']}): ")
                )
            except ValueError:
                print('Giờ phải là số!')
                return

            if gio_bat_dau >= gio_ket_thuc:
                print('Giờ kết thúc phải lớn hơn giờ bắt đầu!')
                return

            tong_thoi_gian = gio_ket_thuc - gio_bat_dau
            phan_loai = xep_loai(tong_thoi_gian)

            item['ten_phong'] = ten_phong or item['ten_phong']
            item['ten_nguoi_dat'] = ten_nguoi_dat or item['ten_nguoi_dat']
            item['gio_bat_dau'] = gio_bat_dau
            item['gio_ket_thuc'] = gio_ket_thuc
            item['tong_thoi_gian'] = tong_thoi_gian
            item['phan_loai'] = phan_loai

            print('Cập nhật thành công!')
            return

    print('Không tìm thấy mã BK!')


def delete_booking():
    booking_id = input('Nhập mã BK cần xóa: ').strip().upper()

    for item in meeting:
        if item['ID'] == booking_id:

            confirm = input(
                'Bạn có chắc muốn xóa? (Y/N): '
            ).upper()

            if confirm == 'Y':
                meeting.remove(item)
                print('Xóa thành công!')
            else:
                print('Đã hủy thao tác!')

            return

    print('Không tìm thấy mã BK!')


def search_booking():
    booking_id = input('Nhập mã BK cần tìm: ').strip().upper()

    for item in meeting:
        if item['ID'] == booking_id:
            print('\nThông tin cuộc họp:')
            for k, v in item.items():
                print(f'{k}: {v}')
            return

    print('Không tìm thấy cuộc họp!')


def show_total_hour():
    if not meeting:
        print('Không có dữ liệu')
        return

    tong_gio = sum(item['tong_thoi_gian'] for item in meeting)

    ngan = sum(1 for i in meeting if i['phan_loai'] == 'Ngắn')
    tieu_chuan = sum(1 for i in meeting if i['phan_loai'] == 'Tiêu chuẩn')
    dai = sum(1 for i in meeting if i['phan_loai'] == 'Dài')
    qua_tai = sum(
        1 for i in meeting
        if i['phan_loai'] == 'Quá tải (Cần xem xét lại)'
    )

    print('\n===== THỐNG KÊ =====')
    print(f'Tổng số giờ sử dụng: {tong_gio}')
    print(f'Cuộc họp ngắn: {ngan}')
    print(f'Cuộc họp tiêu chuẩn: {tieu_chuan}')
    print(f'Cuộc họp dài: {dai}')
    print(f'Cuộc họp quá tải: {qua_tai}')


def menu():
    while True:
        print('\n===== QUẢN LÝ PHÒNG HỌP =====')
        print('1. Hiển thị danh sách cuộc họp')
        print('2. Đăng ký phòng họp')
        print('3. Cập nhật cuộc họp')
        print('4. Xóa cuộc họp')
        print('5. Tìm cuộc họp theo mã BK')
        print('6. Thống kê thời lượng')
        print('7. Lọc theo phân loại')
        print('8. Thoát')

        choice = input('Chọn chức năng: ')

        match choice:
            case '1':
                booking_show()
            case '2':
                sig_meeting()
            case '3':
                update_booking()
            case '4':
                delete_booking()
            case '5':
                search_booking()
            case '6':
                show_total_hour()
            case '7':
                print('')
            case '8':
                print('Bạn đã thoát chương trình!')
                break
            case _:
                print('Vui lòng chọn từ 1-8')


menu()