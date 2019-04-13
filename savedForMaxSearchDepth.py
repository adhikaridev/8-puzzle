import time
start_time = time.time()

def up_switch(current_node, p):  # p is the position of zero
    temp = list(current_node[:])
    temp[p] = str(temp[p - 3])  # switching with up
    temp[p - 3] = '0'
    temp.append('u')
    temp = "".join(temp)

    if temp[:9] not in set1:
        frontier_set.append(temp)
        set1.add(temp[:9])
    return temp

def down_switch(current_node, p):
    temp = list(current_node[:])
    temp[p] = str(temp[p + 3])  # switching with down
    temp[p + 3] = '0'
    temp.append('d')
    temp = "".join(temp)

    if temp[:9] not in set1:
        frontier_set.append(temp)
        set1.add(temp[:9])
    return temp

def left_switch(current_node, p):
    temp = list(current_node[:])
    temp[p] = str(temp[p - 1])  # switching with left
    temp[p - 1] = '0'
    temp.append('l')
    temp = "".join(temp)

    if temp[:9] not in set1:
        frontier_set.append(temp)
        set1.add(temp[:9])
    return temp

def right_switch(current_node, p):
    temp = list(current_node[:])
    temp[p] = str(temp[p + 1])  # switching with right
    temp[p + 1] = '0'
    temp.append('r')
    temp = "".join(temp)

    if temp[:9] not in set1:
        frontier_set.append(temp)
        set1.add(temp[:9])
    return temp

initial_state = '125340678'  # 618402735 125340678
goal_state = '012345678'
print 'Initial state: ', initial_state

frontier_set = []  # initializing frontier_set or queue
set1 = set()  # set for membership test of frontier_set
set1.add(initial_state)
print 'set1: ',set1

frontier_set.append(initial_state)  # assigning initial state to the frontier set
print 'Frontier set initially: ', frontier_set

explored_set = []  # initializing explored_set

nodes_expanded = -1  #initialized to 1 because the initial state is not actually an expanded node
path_to_goal = []
max_search_depth = 0
first = 0
leftmost_node = initial_state
while frontier_set:  # this while loop will run until there is element in frontier_set
    current_node = frontier_set[0]  # retrieving the front node/state
    explored_set.append(current_node)
    nodes_expanded = nodes_expanded + 1
    frontier_set = frontier_set[1:]  # dequeuing/removing the front node

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

        break
    else:
        print 'Goal not found.'

        position_of_zero = current_node.index('0')  # obtaining the index of zero/blank space

        if position_of_zero == 0:  # possible movements: down, right
            if current_node[-1] != 'u':
                returned_node = down_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'l':
                returned_node = right_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1

        if position_of_zero == 1:  # possible movements: down, left, right
            if current_node[-1] != 'u':
                returned_node = down_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'r':
                returned_node = left_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'l':
                returned_node = right_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1

        if position_of_zero == 2:  # possible movements: down, left
            if current_node[-1] != 'u':
                returned_node = down_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'r':
                returned_node = left_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1

        if position_of_zero == 3:  # possible movements: up, down, right
            if current_node[-1] != 'd':
                returned_node = up_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'u':
                returned_node = down_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'l':
                returned_node = right_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1

        if position_of_zero == 4:  # possible movements: up, down, left, right
            if current_node[-1] != 'd':
                returned_node = up_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'u':
                returned_node = down_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'r':
                returned_node = left_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'l':
                returned_node = right_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1

        if position_of_zero == 5:  # possible movements: up, down, left
            if current_node[-1] != 'd':
                returned_node = up_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'u':
                returned_node = down_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'r':
                returned_node = left_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1

        if position_of_zero == 6:  # possible movements: up, right
            if current_node[-1] != 'd':
                returned_node = up_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'l':
                returned_node = right_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1


        if position_of_zero == 7:  # possible movements: up, left, right
            if current_node[-1] != 'd':
                returned_node = up_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'r':
                returned_node = left_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'l':
                returned_node = right_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1

        if position_of_zero == 8:  # possible movements: up, left
            if current_node[-1] != 'd':
                returned_node = up_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1
            if current_node[-1] != 'r':
                returned_node = left_switch(current_node, position_of_zero)
                if current_node[:9] == leftmost_node:
                    leftmost_node = returned_node[:9]
                    max_search_depth += 1

        print leftmost_node
print 'Execution time: ',(time.time()-start_time)