import sys
import time
import resource
start_time = time.time()

def bfs(board):
    initial_state = board  # 618402735 125340678   864213570
    goal_state = '012345678'

    frontier_set = {}  # initializing frontier_set or queue
    set1 = set()  # set for membership test of frontier_set
    set1.add(initial_state)
    x = 0
    y = 1
    frontier_set[x] = initial_state  # assigning initial state to the frontier set

    # explored_set = []  # initializing explored_set
    nodes_expanded = -1  # initialized to 1 because the initial state is not actually an expanded node
    path_to_goal = []
    global max_search_depth

    def up_switch(current_node, p):  # p is the position of zero
        s = current_node[:]
        p = p - 3
        temp = "".join((s[:p], s[p + 3], s[p + 1:p + 3], s[p], s[p + 3 + 1:]))
        temp = temp.__add__('u')
        global max_search_depth
        if len(temp[9:]) > max_search_depth:
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
        if len(temp[9:]) > max_search_depth:
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
        if len(temp[9:]) > max_search_depth:
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
        if len(temp[9:]) > max_search_depth:
            max_search_depth = len(temp[9:])
        global y
        if temp[:9] not in set1:
            frontier_set[y] = temp
            y = y + 1
            set1.add(temp[:9])


    while frontier_set:  # this while loop will run until there is element in frontier_set
        current_node = frontier_set[x]  # retrieving the front node/state
        del frontier_set[x]
        x = x + 1
        # explored_set.append(current_node)
        nodes_expanded = nodes_expanded + 1
        # frontier_set = frontier_set[1:]  # dequeuing/removing the front node

        if current_node[:9] == goal_state:
            for move in current_node[9:]:
                if move == 'u':
                    path_to_goal.append('Up')
                if move == 'd':
                    path_to_goal.append('Down')
                if move == 'l':
                    path_to_goal.append('Left')
                if move == 'r':
                    path_to_goal.append('Right')
            print 'path_to_goal: ', path_to_goal
            l = len(path_to_goal)
            print 'cost_of_path: ', l
            print 'nodes_expanded: ', nodes_expanded
            print 'search_depth: ', l
            print 'max_search_depth: ', max_search_depth
            print 'running_time: ', (time.time() - start_time)
            print 'max_ram_usage: ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024.0 * 1024)
            with open('output.txt', 'w') as f:
                f.write('path_to_goal: ')
                f.write(str(path_to_goal))
                f.write('\n')
                f.write('cost_of_path: ')
                f.write(str(l))
                f.write('\n')
                f.write('nodes_expanded: ')
                f.write(str(nodes_expanded))
                f.write('\n')
                f.write('search_depth: ')
                f.write(str(l))
                f.write('\n')
                f.write('max_search_depth: ')
                f.write(str(max_search_depth))
                f.write('\n')
                f.write('running_time: ')
                f.write(str(round((time.time() - start_time),8)))
                f.write('\n')
                f.write('max_ram_usage: ')
                f.write(str(round((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024.0 * 1024)),8)))

            break
        else:

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

def dfs(board):
    initial_state = board  # 618402735  864213570  125340678
    goal_state = '012345678'

    frontier_set = {}  # initializing frontier_set or queue
    set1 = set()  # set for membership test of frontier_set
    set1.add(initial_state)
    frontier_set[0] = initial_state  # assigning initial state to the frontier set

    # explored_set = []  # initializing explored_set
    # set2 = set() #for explored_set
    nodes_expanded = -1  # initialized to 1 because the initial state is not actually an expanded node
    path_to_goal = []
    def up_switch(current_node, p):  # p is the position of zero
        s = current_node[:]
        p = p - 3
        temp = "".join((s[:p], s[p + 3], s[p + 1:p + 3], s[p], s[p + 3 + 1:]))
        temp = temp.__add__('u')
        global max_search_depth
        if len(temp[9:]) > max_search_depth:
            max_search_depth = len(temp[9:])
        global x
        if temp[:9] not in set1:
            frontier_set[x] = temp
            x = x + 1
            set1.add(temp[:9])

    def down_switch(current_node, p):
        s = current_node[:]
        temp = "".join((s[:p], s[p + 3], s[p + 1:p + 3], s[p], s[p + 3 + 1:]))
        temp = temp.__add__('d')
        global max_search_depth
        if len(temp[9:]) > max_search_depth:
            max_search_depth = len(temp[9:])
        global x
        if temp[:9] not in set1:
            frontier_set[x] = temp
            x = x + 1
            set1.add(temp[:9])

    def left_switch(current_node, p):
        s = current_node[:]
        p = p - 1
        temp = "".join((s[:p], s[p + 1], s[p + 1:p + 1], s[p], s[p + 1 + 1:]))
        temp = temp.__add__('l')
        global max_search_depth
        if len(temp[9:]) > max_search_depth:
            max_search_depth = len(temp[9:])
        global x
        if temp[:9] not in set1:
            frontier_set[x] = temp
            x = x + 1
            set1.add(temp[:9])

    def right_switch(current_node, p):
        s = current_node[:]
        temp = "".join((s[:p], s[p + 1], s[p + 1:p + 1], s[p], s[p + 1 + 1:]))
        temp = temp.__add__('r')
        global max_search_depth
        if len(temp[9:]) > max_search_depth:
            max_search_depth = len(temp[9:])
        global x
        if temp[:9] not in set1:
            frontier_set[x] = temp
            x = x + 1
            set1.add(temp[:9])


    while frontier_set:  # this while loop will run until there is element in frontier_set
        global x
        global max_search_depth
        current_node = frontier_set[x - 1]  # retrieving the front node/state
        nodes_expanded = nodes_expanded + 1
        del frontier_set[x - 1]  # popping a node
        x = x - 1
        if current_node[:9] == goal_state:
            for move in current_node[9:]:
                if move == 'u':
                    path_to_goal.append('Up')
                if move == 'd':
                    path_to_goal.append('Down')
                if move == 'l':
                    path_to_goal.append('Left')
                if move == 'r':
                    path_to_goal.append('Right')
            print 'path_to_goal: ', path_to_goal
            l = len(path_to_goal)
            if l < max_search_depth:
                max_search_depth = max_search_depth - 1
            print 'cost_of_path: ', l
            print 'nodes_expanded: ', nodes_expanded
            print 'search_depth: ', l
            print 'max_search_depth: ', max_search_depth
            print 'running_time: ', (time.time() - start_time)
            print 'max_ram_usage: ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024.0 * 1024)

            with open('output.txt', 'w') as f:
                f.write('path_to_goal: ')
                f.write(str(path_to_goal))
                f.write('\n')
                f.write('cost_of_path: ')
                f.write(str(l))
                f.write('\n')
                f.write('nodes_expanded: ')
                f.write(str(nodes_expanded))
                f.write('\n')
                f.write('search_depth: ')
                f.write(str(l))
                f.write('\n')
                f.write('max_search_depth: ')
                f.write(str(max_search_depth))
                f.write('\n')
                f.write('running_time: ')
                f.write(str(round((time.time() - start_time), 8)))
                f.write('\n')
                f.write('max_ram_usage: ')
                f.write(str(round((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024.0 * 1024)),8)))
            break
        else:

            position_of_zero = current_node.index('0')  # obtaining the index of zero/blank space

            if position_of_zero == 0:  # possible movements: right, down
                if current_node[-1] != 'l':
                    right_switch(current_node, position_of_zero)
                if current_node[-1] != 'u':
                    down_switch(current_node, position_of_zero)

            if position_of_zero == 1:  # possible movements: right, left, down
                if current_node[-1] != 'l':
                    right_switch(current_node, position_of_zero)
                if current_node[-1] != 'r':
                    left_switch(current_node, position_of_zero)
                if current_node[-1] != 'u':
                    down_switch(current_node, position_of_zero)

            if position_of_zero == 2:  # possible movements:  left, down
                if current_node[-1] != 'r':
                    left_switch(current_node, position_of_zero)
                if current_node[-1] != 'u':
                    down_switch(current_node, position_of_zero)

            if position_of_zero == 3:  # possible movements: right, down, up
                if current_node[-1] != 'l':
                    right_switch(current_node, position_of_zero)
                if current_node[-1] != 'u':
                    down_switch(current_node, position_of_zero)
                if current_node[-1] != 'd':
                    up_switch(current_node, position_of_zero)

            if position_of_zero == 4:  # possible movements: right, left, down, up
                if current_node[-1] != 'l':
                    right_switch(current_node, position_of_zero)
                if current_node[-1] != 'r':
                    left_switch(current_node, position_of_zero)
                if current_node[-1] != 'u':
                    down_switch(current_node, position_of_zero)
                if current_node[-1] != 'd':
                    up_switch(current_node, position_of_zero)

            if position_of_zero == 5:  # possible movements: left, down, up
                if current_node[-1] != 'r':
                    left_switch(current_node, position_of_zero)
                if current_node[-1] != 'u':
                    down_switch(current_node, position_of_zero)
                if current_node[-1] != 'd':
                    up_switch(current_node, position_of_zero)

            if position_of_zero == 6:  # possible movements: right, up
                if current_node[-1] != 'l':
                    right_switch(current_node, position_of_zero)
                if current_node[-1] != 'd':
                    up_switch(current_node, position_of_zero)

            if position_of_zero == 7:  # possible movements: right, left, up
                if current_node[-1] != 'l':
                    right_switch(current_node, position_of_zero)
                if current_node[-1] != 'r':
                    left_switch(current_node, position_of_zero)
                if current_node[-1] != 'd':
                    up_switch(current_node, position_of_zero)

            if position_of_zero == 8:  # possible movements: up, left
                if current_node[-1] != 'r':
                    left_switch(current_node, position_of_zero)
                if current_node[-1] != 'd':
                    up_switch(current_node, position_of_zero)

def ast(board):
    def manhattan(node):
        node = node[:9]
        distance = 0
        position = {0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (0, 1), 4: (1, 1), 5: (2, 1), 6: (0, 2), 7: (1, 2), 8: (2, 2)}
        for i in range(8):
            current_index = node.index(str(i + 1))
            goal_index = i + 1
            x_position, y_position = position[current_index]
            x_goal, y_goal = position[goal_index]
            distance += abs(x_position - x_goal) + abs(y_position - y_goal)
        return distance

    def up_switch(current_node, p):  # p is the position of zero
        s = current_node[:]
        p = p - 3
        temp = "".join((s[:p], s[p + 3], s[p + 1:p + 3], s[p], s[p + 3 + 1:]))
        temp = temp.__add__('u')
        heuristic = manhattan(temp)
        path_to_n = len(temp[9:])
        total_cost_to_goal = heuristic + path_to_n

        if temp[:9] not in set2:
            if temp[:9] not in set1:
                frontier_set[temp] = total_cost_to_goal
                set1.add(temp[:9])
            else:
                for key in frontier_set:
                    if key[:9] == temp[:9]:
                        value = frontier_set[key]
                        special_key = key
                if total_cost_to_goal < value:
                    del frontier_set[special_key]
                    frontier_set[temp] = total_cost_to_goal

        global max_search_depth
        if len(temp[9:]) > max_search_depth:
            max_search_depth = len(temp[9:])

    def down_switch(current_node, p):
        s = current_node[:]
        temp = "".join((s[:p], s[p + 3], s[p + 1:p + 3], s[p], s[p + 3 + 1:]))
        temp = temp.__add__('d')

        heuristic = manhattan(temp)
        path_to_n = len(temp[9:])
        total_cost_to_goal = heuristic + path_to_n

        if temp[:9] not in set2:
            if temp[:9] not in set1:
                frontier_set[temp] = total_cost_to_goal
                set1.add(temp[:9])
            else:
                for key in frontier_set:
                    if key[:9] == temp[:9]:
                        value = frontier_set[key]
                        special_key = key
                if total_cost_to_goal < value:
                    del frontier_set[special_key]
                    frontier_set[temp] = total_cost_to_goal

        global max_search_depth
        if len(temp[9:]) > max_search_depth:
            max_search_depth = len(temp[9:])

    def left_switch(current_node, p):
        s = current_node[:]
        p = p - 1
        temp = "".join((s[:p], s[p + 1], s[p + 1:p + 1], s[p], s[p + 1 + 1:]))
        temp = temp.__add__('l')
        heuristic = manhattan(temp)
        path_to_n = len(temp[9:])
        total_cost_to_goal = heuristic + path_to_n
        if temp[:9] not in set2:
            if temp[:9] not in set1:
                frontier_set[temp] = total_cost_to_goal
                set1.add(temp[:9])
            else:
                for key in frontier_set:
                    if key[:9] == temp[:9]:
                        value = frontier_set[key]
                        special_key = key
                if total_cost_to_goal < value:
                    del frontier_set[special_key]
                    frontier_set[temp] = total_cost_to_goal
        global max_search_depth
        if len(temp[9:]) > max_search_depth:
            max_search_depth = len(temp[9:])

    def right_switch(current_node, p):
        s = current_node[:]
        temp = "".join((s[:p], s[p + 1], s[p + 1:p + 1], s[p], s[p + 1 + 1:]))
        temp = temp.__add__('r')
        heuristic = manhattan(temp)
        path_to_n = len(temp[9:])
        total_cost_to_goal = heuristic + path_to_n

        if temp[:9] not in set2:
            if temp[:9] not in set1:
                frontier_set[temp] = total_cost_to_goal
                set1.add(temp[:9])
            else:
                for key in frontier_set:
                    if key[:9] == temp[:9]:
                        value = frontier_set[key]
                        special_key = key
                if total_cost_to_goal < value:
                    del frontier_set[special_key]
                    frontier_set[temp] = total_cost_to_goal
        global max_search_depth
        if len(temp[9:]) > max_search_depth:
            max_search_depth = len(temp[9:])

    initial_state = board  # 618402735 125340678   864213570
    goal_state = '012345678'

    frontier_set = {}  # initializing frontier_set or queue
    set1 = set()  # set for membership test of frontier_set
    set1.add(initial_state)
    set2 = set()
    frontier_set[initial_state] = 0  # assigning initial state to the frontier set

    # explored_set = []  # initializing explored_set
    nodes_expanded = -1  # initialized to 1 because the initial state is not actually an expanded node
    path_to_goal = []
    while frontier_set:  # this while loop will run until there is element in frontier_set
        current_node = min(frontier_set, key=frontier_set.get)
        del frontier_set[current_node]
        nodes_expanded = nodes_expanded + 1
        set2.add(current_node[:9])
        if current_node[:9] == goal_state:
            for move in current_node[9:]:
                if move == 'u':
                    path_to_goal.append('Up')
                if move == 'd':
                    path_to_goal.append('Down')
                if move == 'l':
                    path_to_goal.append('Left')
                if move == 'r':
                    path_to_goal.append('Right')
            print 'path_to_goal: ', path_to_goal
            l = len(path_to_goal)
            print 'cost_of_path: ', l
            print 'nodes_expanded: ', nodes_expanded
            print 'search_depth: ', l
            print 'max_search_depth: ', max_search_depth
            print 'running_time: ', (time.time() - start_time)
            print 'max_ram_usage: ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024.0 * 1024)
            with open('output.txt', 'w') as f:
                f.write('path_to_goal: ')
                f.write(str(path_to_goal))
                f.write('\n')
                f.write('cost_of_path: ')
                f.write(str(l))
                f.write('\n')
                f.write('nodes_expanded: ')
                f.write(str(nodes_expanded))
                f.write('\n')
                f.write('search_depth: ')
                f.write(str(l))
                f.write('\n')
                f.write('max_search_depth: ')
                f.write(str(max_search_depth))
                f.write('\n')
                f.write('running_time: ')
                f.write(str(round((time.time() - start_time), 8)))
                f.write('\n')
                f.write('max_ram_usage: ')
                f.write(str(round((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024.0 * 1024)),8)))
            break
        else:
            position_of_zero = current_node.index('0')  # obtaining the index of zero/blank space

            if position_of_zero == 0:  # possible movements: down, right
                if current_node[-1] != 'u':
                    down_switch(current_node, position_of_zero)
                if current_node[-1] != 'l':
                    right_switch(current_node, position_of_zero)

            if position_of_zero == 1:  # possible movements: down, left, right
                if current_node[-1] != 'u':
                    down_switch(current_node, position_of_zero)
                if current_node[-1] != 'r':
                    left_switch(current_node, position_of_zero)
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

method = sys.argv[1]
arg_board = sys.argv[2]
board = ''
i = 0
for item in arg_board:
    if (i%2) == 0:
        board = board.__add__(item)
    i += 1

if method == 'bfs':
    max_search_depth = 0
    x = 0
    y = 1
    bfs(board)

if method == 'dfs':
    max_search_depth = 0
    x = 1
    dfs(board)
if method == 'ast':
    max_search_depth = 0
    ast(board)