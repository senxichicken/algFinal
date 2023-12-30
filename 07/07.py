from engine import Value

def loss_function(x, y, z):
    return (x - 1)**2 + (y - 2)**2 + (z - 3)**2

def gradient_descent(x, y, z, lr=0.01, max_iter=1000, tolerance=1e-6):
    for i in range(max_iter):
        loss = loss_function(x, y, z)
        loss.backward()

        # 檢查收斂性
        grad_norm = (x.grad**2 + y.grad**2 + z.grad**2)**0.5
        if grad_norm < tolerance:
            print(f"在第 {i+1} 次迭代後收斂。")
            break

        # 更新變量
        x.data -= lr * x.grad
        y.data -= lr * y.grad
        z.data -= lr * z.grad

        # 重置梯度以供下一次迭代使用
        x.grad = 0
        y.grad = 0
        z.grad = 0

        print(f"第 {i+1} 次迭代：損失 = {loss.data:.4f}, 梯度范數 = {grad_norm:.4f}, x = {x.data:.4f}, y = {y.data:.4f}, z = {z.data:.4f}")

    print("最終數值：x =", x.data, "，y =", y.data, "，z =", z.data)

# 初始化變量
x = Value(0.0)
y = Value(0.0)
z = Value(0.0)

# 使用梯度下降進行優化
gradient_descent(x, y, z)
