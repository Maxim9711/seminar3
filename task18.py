#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


from random import randrange

N = int(input("N: "))
A = [randrange(1000) for i in range(N)]
print(A)

X = int(input("X: "))


different = abs(X - A[0])
index = 0
for i in range(1, N):
    count = abs(X - A[i])
    if count < different:
        different = count
        index = i

print(f"close value {A[index]}")
