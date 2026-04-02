def main():    
    matrix = [
        [131, 673, 234, 103,  18],
        [201,  96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524,  37, 331]
    ]

    size = len(matrix)
    best = [matrix[row][0] for row in range(size)]

    for col in range(1, size):
        column = [matrix[row][col] for row in range(size)]
        tmp = column[:]

        for i in range(size):
            column[i] += best[i] # right

            for j in range(0, i): # up
                if sum([best[j]]+tmp[j:i+1]) < column[i]:
                    column[i] = sum([best[j]]+tmp[j:i+1])

            for k in range(i, size): # bottom
                if sum([best[k]] +tmp[i:k+1]) < column[i]:
                    column[i] = sum([best[k]] +tmp[i:k+1])

        best = column
        #print(best)

    return min(best)

print(main())
