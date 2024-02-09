# functions for main algorithm


def is_even(x):
    return x % 2 == 0


def is_sublist(sublist, list):
    if sublist == list:
        return True
    elif sublist == []:
        return True
    elif len(sublist) > len(list):
        return False
    else:
        i = 0
        result = False
        while i < len(list) and not result:
            if sublist[0] == list[i]:
                j = 1
                check = True
                while j < len(sublist) and i + j < len(list) and check:
                    if sublist[j] == list[i + j]:
                        j += 1
                    else:
                        check = False
                
                if j == len(sublist):
                    result = True
            
            if not result:
                i += 1
        
        return result


def calculate_reward(buffer_list, sequence_list, reward_list):
    reward = 0
    for i in range(len(sequence_list)):
        if is_sublist(sequence_list[i], buffer_list):
            reward += reward_list[i]
    
    return reward
