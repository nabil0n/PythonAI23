def josephus(items,k):
    order = []
    current_index = -1
    while len(order) < len(items):
        steps = 0
        while steps < k:
            current_index = (current_index + 1) % len(items)
            if items[current_index] is not None:
                steps += 1
        order.append(items[current_index])
        items[current_index] = None
    return order


print(josephus(["C","o","d","e","W","a","r","s"], 4)) #,['e', 's', 'W', 'o', 'C', 'd', 'r', 'a']

print(josephus([1, 2, 3, 4, 5, 6, 7], 3))
