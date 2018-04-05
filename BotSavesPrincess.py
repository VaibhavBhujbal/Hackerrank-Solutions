#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    p0 = grid[0][0] == 'p'
    p1 = grid[0][n-1] == 'p'
    p2 = grid[n-1][n-1] == 'p'
    p3 = grid[n-1][0] == 'p'
    up_down = True
    left_right = True
    if p1:
        left_right = False
    elif p2:
        up_down = False
        left_right = False
    elif p3:   
         up_down = False   
    
    x = (n-1)//2
    
    str1 = ''
    if up_down:
        str1+='UP\n'* x
    else:
        str1+='DOWN\n'* x
    
    if left_right:
        str1+='LEFT\n'* x
    else:
        str1+='RIGHT\n'* x 
    
    print(str1)
    
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)