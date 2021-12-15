def simple_text_editor(ops_list):
    s = ""
    actions = []
    
    for op in ops_list:
        op = op.split()

        if len(op) == 1:
            s = actions.pop()
            continue
        
        # action 1: append
        if op[0] == '1':
            actions.append(s)
            s += op[1]
        # action 2: delete
        elif op[0] == '2':
            actions.append(s)
            s = s[:int(op[1]) * -1]
        # action 3: print
        elif op[0] == '3':
            print(s[int(op[1])-1])
        # invalid action
        else:
            raise ValueError("Invalid action number")


if __name__ == '__main__':
    # get input
    num_ops = input()
    ops_list = []
    for row in range(int(num_ops)):
        ops_list.append(input())

    # run function
    simple_text_editor(ops_list)