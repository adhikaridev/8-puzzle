import time
import resource
start_time = time.time()

def up_switch(current_node, p):  # p is the position of zero
    s = current_node[:]
    p = p - 3
    temp = "".join((s[:p], s[p + 3], s[p + 1:p + 3], s[p], s[p + 3 + 1:]))
    temp = temp.__add__('u')
    global max_search_depth
    if len(temp[9:]) > max_search_depth :
        max_search_depth = len(temp[9:])
    global y
    if temp[:9] not in set1:
        frontier_set[y] = temp
        y = y + 1
        set1.add(temp[:9])

def down_switch(current_node, p):
    s = current_node[:]
    temp = "".join((s[:p], s[p + 3], s[p + 1:p + 3], s[p], s[p + 3 + 1:]))
    temp = temp.__add__('d')
    global max_search_depth
    if len(temp[9:]) > max_search_depth :
        max_search_depth = len(temp[9:])
    global y
    if temp[:9] not in set1:
        frontier_set[y] = temp
        y = y + 1
        set1.add(temp[:9])

def left_switch(current_node, p):
    s = current_node[:]
    p = p - 1
    temp = "".join((s[:p], s[p + 1], s[p + 1:p + 1], s[p], s[p + 1 + 1:]))
    temp = temp.__add__('l')
    global max_search_depth
    if len(temp[9:]) > max_search_depth :
        max_search_depth = len(temp[9:])
    global y
    if temp[:9] not in set1:
        frontier_set[y] = temp
        y = y + 1
        set1.add(temp[:9])

def right_switch(current_node, p):
    s = current_node[:]
    temp = "".join((s[:p], s[p + 1], s[p + 1:p + 1], s[p], s[p + 1 + 1:]))
    temp = temp.__add__('r')
    global max_search_depth
    if len(temp[9:]) > max_search_depth :
        max_search_depth = len(temp[9:])
    global y
    if temp[:9] not in set1:
        frontier_set[y] = temp
        y = y + 1
        set1.add(temp[:9])

initial_state = '125340678'  # 618402735 125340678   864213570
goal_state = '012345678'
print 'Initial state: ', initial_state

frontier_set = {}  # initializing frontier_set or queue
set1 = set()  # set for membership test of frontier_set
set1.add(initial_state)
x = 0
y = 1
frontier_set[x] = initial_state  # assigning initial state to the frontier set
print 'Frontier set initially: ', frontier_set

#explored_set = []  # initializing explored_set
nodes_expanded = -1  #initialized to 1 because the initial state is not actually an expanded node
path_to_goal = []
max_search_depth = 0
while frontier_set:  # this while loop will run until there is element in frontier_set
    current_node = frontier_set[x]  # retrieving the front node/state
    del frontier_set[x]
    x = x + 1
    #explored_set.append(current_node)
    nodes_expanded = nodes_expanded + 1
    #frontier_set = frontier_set[1:]  # dequeuing/removing the front node

    if current_node[:9] == goal_state:
        print 'Goal found.'
        print 'Goal: ',current_node
        for move in current_node[9:]:
            if move=='u':
                path_to_goal.append('Up')
            if move=='d':
                path_to_goal.append('Down')
            if move=='l':
                path_to_goal.append('Left')
            if move=='r':
                path_to_goal.append('Right')
        print 'path_to_goal: ',path_to_goal
        l = len(path_to_goal)
        print 'cost_of_path: ',l
        print 'nodes_expanded: ',nodes_expanded
        print 'search_depth: ',l
        print 'max_search_depth: ',max_search_depth
        print 'running_time: ',(time.time() - start_time)
        print 'max_ram_usage: ',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024.0*1024)

        break
    else:
        print 'Goal not found.'

        position_of_zero = current_node.index('0')  # obtaining the index of zero/blank space

        if position_of_zero == 0:  # possible movements: down, right
            if current_node[-1] != 'u':
                down_switch(current_node, position_of_zero)
            if current_node[-1] != 'l':
                right_switch(current_node, position_of_zero)


        if position_of_zero == 1:  # possible movements: down, left, right
            if current_node[-1] != 'u':
                returned_node = down_switch(current_node, position_of_zero)
            if current_node[-1] != 'r':
                returned_node = left_switch(current_node, position_of_zero)
            if current_node[-1] != 'l':
                right_switch(current_node, position_of_zero)


        if position_of_zero == 2:  # possible movements: down, left
            if current_node[-1] != 'u':
                down_switch(current_node, position_of_zero)

            if current_node[-1] != 'r':
                left_switch(current_node, position_of_zero)


        if position_of_zero == 3:  # possible movements: up, down, right
            if current_node[-1] != 'd':
                up_switch(current_node, position_of_zero)

            if current_node[-1] != 'u':
                down_switch(current_node, position_of_zero)

            if current_node[-1] != 'l':
                right_switch(current_node, position_of_zero)


        if position_of_zero == 4:  # possible movements: up, down, left, right
            if current_node[-1] != 'd':
                up_switch(current_node, position_of_zero)

            if current_node[-1] != 'u':
                down_switch(current_node, position_of_zero)

            if current_node[-1] != 'r':
                left_switch(current_node, position_of_zero)

            if current_node[-1] != 'l':
                right_switch(current_node, position_of_zero)


        if position_of_zero == 5:  # possible movements: up, down, left
            if current_node[-1] != 'd':
                up_switch(current_node, position_of_zero)

            if current_node[-1] != 'u':
                down_switch(current_node, position_of_zero)

            if current_node[-1] != 'r':
                left_switch(current_node, position_of_zero)


        if position_of_zero == 6:  # possible movements: up, right
            if current_node[-1] != 'd':
                up_switch(current_node, position_of_zero)

            if current_node[-1] != 'l':
                right_switch(current_node, position_of_zero)



        if position_of_zero == 7:  # possible movements: up, left, right
            if current_node[-1] != 'd':
                up_switch(current_node, position_of_zero)

            if current_node[-1] != 'r':
                left_switch(current_node, position_of_zero)

            if current_node[-1] != 'l':
                right_switch(current_node, position_of_zero)


        if position_of_zero == 8:  # possible movements: up, left
            if current_node[-1] != 'd':
                up_switch(current_node, position_of_zero)

            if current_node[-1] != 'r':
                left_switch(current_node, position_of_zero)

