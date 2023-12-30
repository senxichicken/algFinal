# 方法 1
def power2n_1(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_2a(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    return power2n_2a(n-1) + power2n_2a(n-1)

# 方法 2b：用遞迴
def power2n_2b(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    return 2 * power2n_2b(n-1)

# 方法 3：用遞迴+查表
dp = [None] * 10000

def power2n_3(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif dp[n]:
        return dp[n]
    else:
        dp[n] = power2n_3(n-1) + power2n_3(n-1)
        return dp[n]

# 測試方法 1
result_1 = power2n_1(3)
print(f"方法 1 的測試值: {result_1}")  

# 測試方法 2a
result_2a = power2n_2a(4)
print(f"方法 2a 的測試值: {result_2a}")  

# 測試方法 2b
result_2b = power2n_2b(5)
print(f"方法 2b 的測試值: {result_2b}") 

# 測試方法 3
result_3 = power2n_3(6)
print(f"方法 3 的測試值: {result_3}")  