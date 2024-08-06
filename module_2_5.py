def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        series = []
        for j in range(m):
            series.append(value)
        matrix.append(series)
    return matrix

result = get_matrix(4, 6, 7)
print(result)
