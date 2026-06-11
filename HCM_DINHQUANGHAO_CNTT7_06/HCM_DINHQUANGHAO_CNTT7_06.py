meeting = [
    {
        'ID': 'BK001',
        'ten_phong': 'Phòng Thảo Luận A',
        'ten_nguoi_dat': 'Phòng marketing',
        'gio_bat_dau': 9,
        'gio_ket_thuc': 12,
        'tong_thoi_gian': 3,
        'phan_loai': 'Tiêu chuẩn'
    }
]


def booking_show():
    if not meeting:
        print('Hiện tại không có cuộc họp nào')
        return

    print('-' * 130)
    print('{:10} {:25} {:25} {:15} {:15} {:15} {:20}'.format(
        'ID',
        'Tên phòng',
        'Người đặt',
        'Bắt đầu',
        'Kết thúc',
        'Tổng giờ',
        'Phân loại'
    ))
    print('-' * 130)

    for item in meeting:
        print('{:10} {:25} {:25} {:15} {:15} {:15} {:20}'.format(
            item['ID'],
            item['ten_phong'],
            item['ten_nguoi_dat'],
            item['gio_bat_dau'],
            item['gio_ket_thuc'],
            item['tong_thoi_gian'],
            item['phan_loai']
        ))


def sig_meeting():
    id_BK = input('Nhập mã BK: ').strip()

    if not id_BK:
        print('Mã BK không được để trống!')
        return

    for item in meeting:
        if item['ID'] == id_BK:
            print('Mã BK đã tồn tại!')
            return

    name_meeting = input('Nhập tên phòng họp: ').strip()
    if not name_meeting:
        print('Tên phòng không được để trống!')
        return

    name_order = input('Nhập tên người đặt: ').strip()
    if not name_order:
        print('Tên người đặt không được để trống!')
        return

    hour_start = int(input('Nhập giờ bắt đầu (0-23): '))
    hour_end = int(input('Nhập giờ kết thúc (0-23): '))

    if hour_start >= hour_end:
        print('Giờ kết thúc phải lớn hơn giờ bắt đầu!')
        return

    tong_thoi_gian = hour_end - hour_start

    if 8 <= hour_start < 17:
        phan_loai = 'Tiêu chuẩn'
    elif 17 <= hour_start < 22:
        phan_loai = 'Ngoài giờ'
    else:
        phan_loai = 'Đặc biệt'

    meeting.append({
        'ID': id_BK,
        'ten_phong': name_meeting,
        'ten_nguoi_dat': name_order,
        'gio_bat_dau': hour_start,
        'gio_ket_thuc': hour_end,
        'tong_thoi_gian': tong_thoi_gian,
        'phan_loai': phan_loai
    })

    print('Đăng ký phòng họp thành công!')

def update_booking():
    booking_id = input('Nhập mã BK cần cập nhật: ').strip()

    for item in meeting:
        if item['ID'] == booking_id:

            ten_phong = input(
                f"Tên phòng mới ({item['ten_phong']}): "
            ).strip()

            ten_nguoi_dat = input(
                f"Tên người đặt mới ({item['ten_nguoi_dat']}): "
            ).strip()

            gio_bat_dau = int(
                input(f"Giờ bắt đầu mới ({item['gio_bat_dau']}): ")
            )

            gio_ket_thuc = int(
                input(f"Giờ kết thúc mới ({item['gio_ket_thuc']}): ")
            )

            if gio_bat_dau >= gio_ket_thuc:
                print('Giờ kết thúc phải lớn hơn giờ bắt đầu!')
                return

            tong_thoi_gian = gio_ket_thuc - gio_bat_dau

            if 8 <= gio_bat_dau < 17:
                phan_loai = 'Tiêu chuẩn'
            elif 17 <= gio_bat_dau < 22:
                phan_loai = 'Ngoài giờ'
            else:
                phan_loai = 'Đặc biệt'

            item['ten_phong'] = ten_phong
            item['ten_nguoi_dat'] = ten_nguoi_dat
            item['gio_bat_dau'] = gio_bat_dau
            item['gio_ket_thuc'] = gio_ket_thuc
            item['tong_thoi_gian'] = tong_thoi_gian
            item['phan_loai'] = phan_loai

            print('Cập nhật thành công!')
            return

    print('Không tìm thấy mã BK!')


def delete_booking():
    booking_id = input('Nhập mã BK cần xóa: ').strip()

    for item in meeting:
        if item['ID'] == booking_id:
            meeting.remove(item)
            print('Xóa thành công!')
            return

    print('Không tìm thấy mã BK!')

def search_booking():
    booking_id = input('Nhập mã BK cần tìm: ').strip()

    for item in meeting:
        if item['ID'] == booking_id:
            print(item)
            return

    print('Không tìm thấy cuộc họp!')

def show_total_hour():
    if not meeting:
        print('Không có dữ liệu')
        return

    total = 0

    for item in meeting:
        total += item['tong_thoi_gian']

    print(f'Tổng thời lượng sử dụng của tất cả cuộc họp: {total} giờ')

def menu():
    while True:
        print('\n===== QUẢN LÝ PHÒNG HỌP =====')
        print('1. Hiển thị danh sách cuộc họp')
        print('2. Đăng ký phòng họp')
        print('3. Cập nhật cuộc họp')
        print('4. Xóa cuộc họp')
        print('5. Tìm cuộc họp theo mã BK')
        print('6. Thống kê thời lượng')
        print('7. Phân loại cuộc họp')
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
                print('Thoát chương trình')
                break
            case _:
                print('Lỗi: Vui lòng nhập đúng chức năng')


menu()