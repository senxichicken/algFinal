import random

def neighbor(f, p, h=0.01):
    """找尋鄰近點"""
    q = p.copy()
    i = random.randint(0, len(p)-1)  # 隨機選擇一個維度
    q[i] += random.uniform(-h, h)    # 在該維度上進行小幅度隨機變動
    return q, f(*q)

def hillClimbing(f, dimensions, h=0.01, max_iterations=10000):
    """爬山演算法尋找局部極大值"""
    p = [random.uniform(-10, 10) for _ in range(dimensions)]  # 初始點
    fnow = f(*p)  # 目前高度
    failCount = 0

    for _ in range(max_iterations):
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:
            fnow = f1
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount += 1

    return p, fnow

# 測試
def example_function(x, y, z):
    return -1 * (x**2 + y**2 + z**2)

result = hillClimbing(example_function, dimensions=3)
print("最終結果：", result)
