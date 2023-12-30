def df(f, p, k, step=0.01):
    """計算 f 在點 p 上對第 k 個變數的偏微分"""
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

def grad(f, p, step=0.01):
    """計算 f 在點 p 上的梯度"""
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, step)
    return gp

def gradientDescent(f, initial, lr=0.01, tol=1e-6, max_iter=1000, step=0.01):
    """梯度下降法尋找函數谷底"""
    point = initial.copy()

    for iteration in range(max_iter):
        fnow = f(point)
        gp = grad(f, point, step)
        temp = [point[i] - lr * gp[i] for i in range(len(point))]

        fneighbor = f(temp)

        if fneighbor < fnow:
            point = temp
            print('Point:', point, 'Function Value:', fneighbor)
        else:
            print(f"達到收斂條件，迭代次數: {iteration+1}")
            break

    return point, f(point)

# 測試
def example_function(x):
    return x[0]**2 + x[1]**2 + x[2]**2  # 替換成你想要優化的向量函數

initial_point = [2.0, 1.0, 3.0]  # 初始點
result_point, result_value = gradientDescent(example_function, initial_point)

print("最終結果：")
print("找到的點：", result_point)
print("函數值：", result_value)
