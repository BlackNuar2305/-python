def print_operation_table(operation, num_rows = 6, num_columns = 6):
    matrix = [[] for i in range(num_columns)]
    

    for i in range(num_rows):
        for j in range(num_columns):
            matrix[i].append(operation(i + 1, j + 1))
    return matrix



print(print_operation_table(lambda x, y: x * y))



