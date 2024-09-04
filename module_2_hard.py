def code(n):
    result = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            sum_ = i + j
            if n % sum_ == 0:
                result.append(i)
                result.append(j)
    return result

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = code(n)
    print("Нужный пароль:",*result)
else:
    print("Число должно быть в диапазоне от 3 до 20.")