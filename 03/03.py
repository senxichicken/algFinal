def permutations(arr):
    result = []

## 用遞迴
    def generate(current, remaining):
        if not remaining:
            result.append(current.copy())
            return

        for i, num in enumerate(remaining):
            current.append(num)
            generate(current, remaining[:i] + remaining[i+1:])
            current.pop()

    generate([], arr)
    return result

def print_permutations(arr, arr_name):
    print(f"{arr_name}的所有排列:")
    perms = permutations(arr)
    for perm in perms:
        print(perm)
    print()

arr_2 = [0, 1]
arr_3 = [0, 1, 2]
arr_4 = [0, 1, 2, 3]

print_permutations(arr_2, "arr_2")
print_permutations(arr_3, "arr_3")
print_permutations(arr_4, "arr_4")
