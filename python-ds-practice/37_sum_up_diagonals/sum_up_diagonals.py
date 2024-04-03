def sum_up_diagonals(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
        sum += matrix[i][-i-1]
    return sum