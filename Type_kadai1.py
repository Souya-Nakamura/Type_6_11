for num in range(1, 101):
    string = ''

    # ここから記述
    # numの値が15の倍数の時にFizzBuzzを出力する
    if num % 15 == 0:
        print("FizzBuzz\n")
    
    # numの値が3の倍数かつ5の倍数でないときにFizzを出力する
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz\n")
    
    # numの値が5の倍数かつ3の倍数でないときにBuzzを出力する
    if num % 5 == 0 and num % 3 != 0:
        print("Buzz\n")

    # 3と5の倍数以外はそのままnumの値を出力する
    print(num)
    # ここまで記述

    print(string)