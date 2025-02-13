my_fruits = []
while True:
    print("\n🔹 과일 관리 시스템 🔹")
    print("1. 추가")
    print("2. 수정")
    print("3. 삭제")
    print("4. 조회")
    print("5. 검색")
    print("6. 종료")

    choice = input("메뉴 선택: ")
    if choice == "1":
        item = input("추가할 과일을 작성해주세요:")
        my_fruits.append(item)
        print(f"{item} 추가 되었습니다.")
    elif choice == "2":
        index = int(input("수정할 인덱스 번호를 설정해주세요"))
        if 0 <= index < len(my_fruits):
            oldItem = my_fruits[index]
            newItem = input("수정할 과일을 작성해주세요:")
            my_fruits[index] = newItem
            print(f"{index} 번째 값이 {oldItem}에서 {newItem}으로 변경되었습니다.")
        else:
            print("유효하지 않는 값입니다.")
    elif choice == "3":
        item = input("삭제할 값을 입력하세요")
        if item in my_fruits:
            my_fruits.remove(item)
        else:
            print("값이 리스트에 없습니다.")

    elif choice == "4":
        print(f"현재 my_fruits : {my_fruits}")


    elif choice == "5":
        item = input("검색할 값을 입력하세요")
        if item in my_fruits:
            print(f"값이 리스트에 있습니다. : {my_fruits[my_fruits.index(item)]}")
        else:
            print("값이 리스트에 없습니다.")
    elif choice == "6":
        print("프로그램을 종료합니다.")
        break