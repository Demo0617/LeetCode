while True:
    try:
        m, n= map(int, input().split())
        maze = []
        for i in range(m):
            maze.append(list(map(int, input().split())))
        def walk(x, y, pos=[(0,0)]):
            if x + 1 < m and maze[x+1][y] == 0:
                if (x+1, y) not in pos:
                    walk(x+1, y, pos+[(x+1, y)])
            if x - 1 >= 0 and maze[x-1][y] == 0:
                if (x-1, y) not in pos:
                    walk(x-1, y, pos+[(x-1,y)])
            if y + 1 < n and maze[x][y+1] == 0:
                if (x, y+1) not in pos:
                    walk(x, y+1, pos+[(x, y+1)])
            if y - 1 >= 0 and maze[x][y-1] == 0:
                if (x, y-1) not in pos:
                    walk(x, y-1, pos+[(x, y-1)])
            if x == m-1 and y == n-1:
                for p in pos:
                    print('({},{})'.format(p[0],p[1]))
        walk(0, 0, [(0, 0)])
    except:
        break


