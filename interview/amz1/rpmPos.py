def posTargetValue(row, column, matrix, targetRPM):
    for i in range(row):
        for j in range(column):
            if matrix[i][j] > targetRPM:
                break
            if matrix[i][j] == targetRPM:
                return (i,j)
    return (-1,-1)
    