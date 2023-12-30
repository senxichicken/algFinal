def conflict(state, nextX):    
    nextY = len(state)
    return any(abs(state[i] - nextX) in (0, nextY - i) for i in range(nextY))

def queens(n, state=()):
    if len(state) == n: 
        return [()]
    ans = []
    for pos in range(n):
        if not conflict(state, pos):
            ans += [(pos,)+ result for result in queens(n, state + (pos,))]
    return ans



def visualize(state):
    vis=['.'*len(state)] * len(state)
    for i ,item in enumerate(state):
        vis[i]=vis[i][:item]+"Q"+vis[i][item+1:]
    return vis

n = 8
solutions = queens(n)
for solution in solutions:
    print("解法:")
    for row in visualize(solution):
        print(row)
    print("\n")