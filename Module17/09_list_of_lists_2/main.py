nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nice_list = [nice_list[i][j][k] for i in range(len(nice_list))
            for j in range(len(nice_list[0]))
            for k in range(len(nice_list[0][0]))]
print(nice_list)