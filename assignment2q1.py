# # incremental = range(1, 6)
# # decremental = range(4, 0, -1)
# for i in range(1, 2):
#     for k in range(1, 6):
#         print('*' * k)
#         # print(['*' * k for k in range(4, 0, -1)])
#     for k in range(4, 0, -1):
#         print('*' * k)
            
# # for i in range(1, 2):
# #     for k in range(4, 0, -1):
# #         print('*' * k)
        
    
# # for i in range(2, 13):
# #     for k in range(1, 13):
# #         print(f'{i} by {k} = ', k * i )
for i in range(9):
    for k in range(6):
        if (k == 0 and i < 1) or (i ==1 and k < 2) or (i == 2 and k < 3) or (i == 3 and k < 4) or (i == 4 and k < 5) or (i == 5 and k < 4) or (i == 6 and k < 3) or (i == 7 and k < 2) or (i == 8 and k < 1) or i== 0:
            print('*', end=' ')
            
        else:
            print(' ', end=' ') 
    print()