menu1 = 0
menu2 = 0
menu3 = 0
total = 0
menu = 0

while menu != 4 :
    print("==== 슈먼 카페 ====")
    print("1. 아메리카노 : 2000원")
    print("2. 카페라떼 : 2500원")
    print("3. 마끼야또 : 3000원")
    print("4. 주문종료\n")
    
    menu = int(input("메뉴를 입력해주세요 => "))
    if menu == 0 or menu > 4 :
        print("잘못 입력되었습니다. 다시 입력해주세요.")
        
        print("\n**** 총 주문내역 ****")
        print("1. 아메리카노 : %d잔" % menu1)
        print("2. 카페라떼 : %d잔" % menu2)
        print("3. 마끼야또 : %d잔" % menu3)
        print("총금액 : %d원\n" % total)
        continue
    elif menu == 4 :
        break
        
    num = int(input("수량을 입력해주세요 => "))

    if menu == 1:
        menu1 += num
        total += num*2000
    elif menu == 2:
        menu2 += num
        total += num*2500 
    elif menu == 3:
        menu3 += num
        total += num*3000
        
    print("\n**** 총 주문내역 ****")
    print("1. 아메리카노 : %d잔" % menu1)
    print("2. 카페라떼 : %d잔" % menu2)
    print("3. 마끼야또 : %d잔" % menu3)
    print("총금액 : %d원\n" % total)

print("주문을 종료합니다.")
        
print("\n**** 총 주문내역 ****")
print("1. 아메리카노 : %d잔" % menu1)
print("2. 카페라떼 : %d잔" % menu2)
print("3. 마끼야또 : %d잔" % menu3)
print("총금액 : %d원" % total)
