my_user_dict = {}
while True:
    print("\n🔹 딕셔너리(회원번호) 관리 시스템 🔹")
    print("1. 추가")
    print("2. 수정")
    print("3. 삭제")
    print("4. 조회")
    print("5. 검색")
    print("6. 종료")

    choice = input("메뉴 선택: ")

    if choice == "1":
        name = input("추가할 회원 이름 입력 해주세요:")
        userNo = int(input("추가할 회원 번호를 입력 해주세요:"))
        my_user_dict[name] = userNo
        print(f"{name} 회원님이 추가 되었습니다.")

    elif choice == "2":
        name = input("수정할 이름을 입력 해주세요")
        if name in my_user_dict.keys():
            old_userNo = my_user_dict[name]
            newUserNo = int(input("수정할 번호를 입력해주세요"))
            my_user_dict[name] = newUserNo
            print(f"{name} 회원님의 번호가 {old_userNo}에서 {newUserNo}으로 변경되었습니다.")
        else:
            print("유효하지 않는 값입니다.")

    elif choice == "3":
        name = input("삭제할 이름을 입력하세요")
        if name in my_user_dict.keys():
            del my_user_dict[name]
            print(f"{name}회원님이 삭제 되었습니다.")
        else:
            print("회원님이 존재하지 없습니다.")

    elif choice == "4":
        for key, value in my_user_dict.items():
            print(f"{key}님 , 회원번호: {value}")

    elif choice == "5":
        name = input("검색할 이름을 입력하세요")
        if name in my_user_dict.keys():
            print(f"{my_user_dict[name]}회원님이 존재합니다.")
        else:
            print(f"{my_user_dict[name]}회원님이 없습니다.")

    elif choice == "6":
        print("프로그램을 종료합니다.")
        break