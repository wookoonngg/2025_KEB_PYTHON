import random

drink_and_food = [ ["위스키", "초콜릿"], ["와인", "치즈"], ["소주", "삼겹살"],["고량주", "양꼬치"], ["사케", "광어회"], ["위스키", "낙곱새"]]



drinks_foods_dict = {drink: food for drink, food in drink_and_food}

drinks_foods_list = list(drinks_foods_dict.items())



while True:


    print("\n다음 술 중에 고르세요.")
    for idx, (drink, _) in enumerate(drinks_foods_list, start=1):  # 반복으로 위에 리스트 돌려서 메뉴 뽑음
        print(f"{idx}) {drink}")
ㅎㅅ
    print(f"{len(drinks_foods_list) + 1}) 아무거나") # 6번 랜덤 값

    print(f"{len(drinks_foods_list) + 2}) 종료") # 7번 종료 값

    menu = input("선택: ")

    if menu.isdigit():
        menu = int(menu)
        if 1 <= menu <= len(drinks_foods_list): # 1~5 번 까지 고르면
            drink, food = drinks_foods_list[menu - 1]
            print(f"{drink}에 어울리는 안주는 {food} 입니다")


        elif menu == len(drinks_foods_list) + 1:  # 6번 랜덤 값
            drink, food = random.choice(drinks_foods_list)
            print(f"{drink}에 어울리는 안주는 {food} 입니다")


        elif menu == len(drinks_foods_list) + 2:  # 7번 종료
            print("다음에 또 오세요!")
            break

