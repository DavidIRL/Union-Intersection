from linked_list import Node, LinkedList


ll1 = LinkedList()
ll2 = LinkedList()

elements1 = [4,1,34,9,'se7en',9001,3.14159]
elements2 = [8,6,7,5,3,0,9]

for item in elements1:
    ll1.append(item)
    print(f'appending {item} to first LinkedList')

print(ll1.size())

for item in elements2:
    ll2.append(item)
    print(f'appending {item} to second LinkedList')

print(ll2.size())

print(str(ll1), str(ll2))
