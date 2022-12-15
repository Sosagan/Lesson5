def func(*a):
    sum = 0
    for i in a:
        sum += i
    print("Сумма: ", sum)
func(0, 5)
func(9, 8, 7, 6)
func(1, 2, 3, 4, 5, 6, 7, 8)