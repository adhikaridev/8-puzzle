def manhattan(current_index, goal_index):
    position = {0:(0,0),1:(1,0),2:(2,0),3:(0,1),4:(1,1),5:(2,1),6:(0,2),7:(1,2),8:(2,2)}
    x_position,y_position = position[current_index]
    x_goal,y_goal = position[goal_index]
    global distance
    distance += abs(x_position - x_goal) + abs(y_position - y_goal)
#print manhattan(8,1)
distance = 0
current_node = '724506831'
for i in range(8):
    manhattan(current_node.index(str(i+1)), i+1)
print distance