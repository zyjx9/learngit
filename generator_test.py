def triangles():
    results = []
    for i in range(10): 
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = results[i - 1][j - 1] + results[i - 1][j]
        results.append(row)
        yield row


if __name__ == '__main__':
    results = list(triangles())
    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')