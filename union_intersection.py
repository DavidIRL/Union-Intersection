from linked_list import Node, LinkedList

def union(llist1, llist2):
    items = str(llist1).split("->")+str(llist2).split("->")
    new_llist = LinkedList()
    for item in items:
        new_llist.append(item)

    return new_llist

def intersection(llist1, llist2):
    if not llist1 or not llist2:
        raise TypeError('Two non-empty LinkedLists must be provided')

    ll1 = str(llist1).split("->")
    ll2 = str(llist2).split("->")
    result = []
    output = LinkedList()

    for item in ll1:
        if item in ll2:
            result.append(item)

    for item in result:
        output.append(item)
    
    print(str(result))
    return result
            


    




