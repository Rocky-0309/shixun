#练习题1
def is_prime(num):
    """判断一个数是否为素数"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("1到100之间的素数：")
primes = [num for num in range(1, 101) if is_prime(num)]
print(primes)

#练习题2

# 初始化前两项
fibonacci = [0, 1]

# 计算剩余的18项
for i in range(2, 20):
    next_num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_num)

print("\n斐波那契数列前20项：")
print(fibonacci)

#练习题3
total = 0
num = 1

while num <= 10000:
    # 检查条件：能被3整除或能被5整除，但不能被15整除
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        total += num
    num += 1

print(f"\n1-10000之间满足条件的数的和：{total}")