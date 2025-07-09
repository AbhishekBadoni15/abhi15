def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row += [last_row[j] + last_row[j+1] for j in range(len(last_row) - 1)]
            row.append(1)
        triangle.append(row)
    return triangle

for row in pascal_triangle(5):
    print(row)


