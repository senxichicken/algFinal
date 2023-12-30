import math

f = lambda x: x**2 - 3*x + 1
df = lambda x: 2*x - 3

# 方法 1: 黃金分割
def golden_section_search(f, a, b, tolerance, max_iterations):
    alpha = (3 + math.sqrt(5)) / 2

    for i in range(max_iterations):
        c = b - (b - a) / alpha
        d = a + (b - a) / alpha

        if f(c) < f(d):
            b = d
        else:
            a = c

        if abs(b - a) < tolerance:
            return (a + b) / 2

    return None

# 方法 2: 牛頓
def newton_method(x0, f, df, iterations):
    x = x0
    for i in range(iterations):
        x = x - f(x) / df(x)
    return x

# 方法 3: 二分
def bisection_method(a, b, f, tolerance, max_iterations):
    if f(a) * f(b) > 0:
        print("Error: 函數在 a 和 b 的值上沒有異號。")
        return None

    iteration = 1
    while iteration <= max_iterations:
        c = (a + b) / 2

        if abs(f(c)) < tolerance:
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iteration += 1

    return None

a_bisection = 0
b_bisection = 2
tolerance_bisection = 1e-6

# 最大迭代
max_iterations_bisection = 20

# 初始值和迭代次數
x0_newton = 1
iterations_newton = 20

# 黃金分割法
result_golden = golden_section_search(f, a_bisection, b_bisection, tolerance_bisection, max_iterations_bisection)
print(f"方法 1 (黃金分割法) 的解：x = {result_golden}")

# 牛頓法
result_newton = newton_method(x0_newton, f, df, iterations_newton)
print(f"方法 2 (牛頓法) 的解：x = {result_newton}")

# 二分法
result_bisection = bisection_method(a_bisection, b_bisection, f, tolerance_bisection, max_iterations_bisection)
print(f"方法 3 (二分法) 的解：x = {result_bisection}")
