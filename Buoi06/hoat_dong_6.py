print("===== Bài tập 6.1 =====")
def giai_thua_de_quy(n):
    if n <= 1: # dieu kien dung
        return 1
    return n * giai_thua_de_quy(n - 1)
def giai_thua_lap(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
        return ket_qua
for i in [3, 5, 7]:
    print(f"{i}! Đệ quy =", giai_thua_de_quy(i))
    print(f"{i}! Vòng lặp =", giai_thua_lap(i))
    print()

print("\n===== Bài tập 6.2 =====")
def fibonacci_de_quy(n):
    if n <= 1: # dieu kien dung
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)
for i in range(10):
    print(fibonacci_de_quy(i), end=" ")
print()