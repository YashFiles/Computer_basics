from pyamaze import maze,agent,COLOR

def DFS(m):
    
    start=(m.rows,m.cols)
    explored = [start]
    frontier = [start]
    dfsPath={}
    
    while len(frontier)>0:
        currCell = frontier.pop()
        if currCell == (1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell = dfsPath[cell]
    return fwdPath



m= maze(10,10)
m.CreateMaze()
path=DFS(m)
a=agent(m,footprints=True)
m.tracePath({a:path})

#print(m.maze_map)

m.run()   
