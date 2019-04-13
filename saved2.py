
def up_switch(current_node, p):  # p is the position of zero
    temp = list(current_node[:])
    temp[p] = str(temp[p - 3])  # switching with up
    temp[p - 3] = '0'
    temp = "".join(temp)
    '''
    for item in list1:
        if item not in list2:
            list2.append(item)
    union = list2
    if temp not in union:   # append only if the node is not previously visited or enquued
        frontier_set.append(temp)
    '''
    if temp not in explored_set:
        if temp not in frontier_set:
            frontier_set.append(temp)


def down_switch(current_node, p):
    temp = list(current_node[:])
    temp[p] = str(temp[p + 3])  # switching with down
    temp[p + 3] = '0'
    temp = "".join(temp)
    '''
    for item in list1:
        if item not in list2:
            list2.append(item)
    union = list2
    if temp not in union:
        frontier_set.append(temp)
    '''
    if temp not in explored_set:
        if temp not in frontier_set:
            frontier_set.append(temp)


def left_switch(current_node, p):
    temp = list(current_node[:])
    temp[p] = str(temp[p - 1])  # switching with left
    temp[p - 1] = '0'
    temp = "".join(temp)
    '''
    for item in list1:
        if item not in list2:
            list2.append(item)
    union = list2
    if temp not in union:
        frontier_set.append(temp)
    '''
    if temp not in explored_set:
        if temp not in frontier_set:
            frontier_set.append(temp)


def right_switch(current_node, p):
    temp = list(current_node[:])
    temp[p] = str(temp[p + 1])  # switching with right
    temp[p + 1] = '0'
    temp = "".join(temp)
    '''
    for item in list1:
        if item not in list2:
            list2.append(item)
    union = list2
    if temp not in union:
        frontier_set.append(temp)
    '''
    if temp not in explored_set:
        if temp not in frontier_set:
            frontier_set.append(temp)


initial_state = '125340678'
goal_state = '012345678'
print 'Initial state: ', initial_state

frontier_set = []  # initializing frontier_set or queue
frontier_set.append(initial_state)  # assigning initial state to the frontier set
print 'Frontier set initially: ', frontier_set

explored_set = []  # initializing explored_set


nodes_expanded = -1  #initialized to 1 because the initial state is not actually an expanded node

while frontier_set:  # this while loop will run until there is element in frontier_set
    current_node = frontier_set[0]  # retrieving the front node/state
    explored_set.append(current_node)
    nodes_expanded = nodes_expanded + 1
    frontier_set = frontier_set[1:]  # dequeuing/removing the front node
    #print 'Current Node: ', current_node
    #print 'Frontier set after dequeuing: ', frontier_set
    #print 'Explored Set: ', explored_set

    if current_node == goal_state:
        print 'Goal found.'
        print 'nodes_expanded: ',nodes_expanded
        break
    else:
        print 'Goal not found.'

        position_of_zero = current_node.index('0')  # obtaining the index of zero/blank space

        if position_of_zero == 0:  # possible movements: down, right
            down_switch(current_node, position_of_zero)
            right_switch(current_node, position_of_zero)
            #print frontier_set

        if position_of_zero == 1:  # possible movements: down, left, right
            down_switch(current_node, position_of_zero)
            left_switch(current_node, position_of_zero)
            right_switch(current_node, position_of_zero)
            #print frontier_set

        if position_of_zero == 2:  # possible movements: down, left
            down_switch(current_node, position_of_zero)
            left_switch(current_node, position_of_zero)
            #print frontier_set

        if position_of_zero == 3:  # possible movements: up, down, right
            up_switch(current_node, position_of_zero)
            down_switch(current_node, position_of_zero)
            right_switch(current_node, position_of_zero)
            #print frontier_set

        if position_of_zero == 4:  # possible movements: up, down, left, right
            up_switch(current_node, position_of_zero)
            down_switch(current_node, position_of_zero)
            left_switch(current_node, position_of_zero)
            right_switch(current_node, position_of_zero)
            #print frontier_set

        if position_of_zero == 5:  # possible movements: up, down, left
            up_switch(current_node, position_of_zero)
            down_switch(current_node, position_of_zero)
            left_switch(current_node, position_of_zero)
            #print frontier_set

        if position_of_zero == 6:  # possible movements: up, right
            up_switch(current_node, position_of_zero)
            right_switch(current_node, position_of_zero)
            #print frontier_set

        if position_of_zero == 7:  # possible movements: up, left, right
            up_switch(current_node, position_of_zero)
            left_switch(current_node, position_of_zero)
            right_switch(current_node, position_of_zero)
            #print frontier_set

        if position_of_zero == 8:  # possible movements: up, left
            up_switch(current_node, position_of_zero)
            left_switch(current_node, position_of_zero)
            #print frontier_set

