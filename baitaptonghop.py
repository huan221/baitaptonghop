raw_input = "   nGuyen vaN aN  ;  2004   "

while True:
    print("\n===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if choice == "1":
        print("Dữ liệu gốc:", raw_input)

    elif choice == "2":
        # tách chuỗi
        parts = raw_input.split(";")
        
        name = parts[0].strip()
        year = parts[1].strip()

        # chuẩn hóa tên
        name = name.title()

        # tính tuổi
        age = 2026 - int(year)

        print("Họ tên:", name)
        print("Tuổi:", age)

    elif choice == "3":
        parts = raw_input.split(";")
        
        name = parts[0].strip().lower()
        year = parts[1].strip()

        # tách từng phần tên
        words = name.split()
        
        ho = words[0]
        ten_dem = words[1]
        ten = words[2]

        # tạo email
        email = ho[0] + ten_dem[0] + ten + "@company.com"

        # tạo ID
        member_id = ten.upper() + year[-2:]

        # in thẻ
        print("\n===== THẺ THÀNH VIÊN =====")
        print(f"Họ tên : {name.title()}")
        print(f"Email  : {email}")
        print(f"Mã ID  : {member_id}")
        print("==========================")

    elif choice == "4":
        print("Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")