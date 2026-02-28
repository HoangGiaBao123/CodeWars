def friend(x):
    friend_list = []
    
    for friend in x:
        if len(friend) == 4:
            friend_list.append(friend)
    return friend_list
