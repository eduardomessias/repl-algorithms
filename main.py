
print('Binary tree')

from algorithms.binary_tree import BinaryTree
import random

tree = BinaryTree()

for i in range(0, 10):
    tree.add(random.randint(1, 100))

print ('tree.traverse(): ' + str(tree.traverse()))

node = tree.search(10)

if node == None:
    print('tree.search(10): Not found')
else:
    print('tree.search(10): Found')

print ('Linked list')

from algorithms.linked_list import LinkedList

list = LinkedList()

for i in range(0, 10):
    list.add(random.randint(1, 100))

print ('list.head: ' + str(list.head.value))
print ('list.tail: ' + str(list.tail.value))
print ('list.traverse(): ' + str(list.traverse()))

list.sort()
print ('list.sort(): ' + str(list.traverse()))

node = list.search(10)

if node == None:
    print('list.search(10): Not found')
else:
    print('list.search(10): Found')

print ('Binary gap')
from algorithms.binary_gap import binary_gap


n = 8875000
print ('input: ' + str(n))
print (binary_gap(n))
