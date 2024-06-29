from linked_list import Node, LinkedList
import union_intersection as uni

llist1 = LinkedList()
llist2 = LinkedList()

elements1 = [4,1,34,9,'se7en',9001,3.14159]
elements2 = [8,6,7,5,3,0,9]

for item in elements1:
    llist1.append(item)
    print(f'appending {item} to first LinkedList')

print(llist1.size())

for item in elements2:
    llist2.append(item)
    print(f'appending {item} to second LinkedList')

print(llist2.size())

print(str(llist1))
print(str(llist2))

uni.intersection(llist1, llist2)
