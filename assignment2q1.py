# incremental = range(1, 6)
# decremental = range(4, 0, -1)
for i in range(1, 2):
    for k in range(1, 6):
        print('*' * k)
        # print(['*' * k for k in range(4, 0, -1)])
    for k in range(4, 0, -1):
        print('*' * k)
            
# for i in range(1, 2):
#     for k in range(4, 0, -1):
#         print('*' * k)
        
    
# for i in range(2, 13):
#     for k in range(1, 13):
#         print(f'{i} by {k} = ', k * i )
        