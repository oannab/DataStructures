
import random
from os.path import join
"""Problem 6: Union and Intersection
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B. For example, the intersection of A = [1, 2, 3] and B = [2, 3, 4] is [2, 3].

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.


"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None 

    def __str__(self): # O(n)
        curr_head = self.head
        out_string = ""
        while curr_head:
            out_string += str(curr_head.value) + " -> "
            curr_head = curr_head.next
        return out_string


    def append(self, value): # O(n)
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        curr_node  = Node(value)
        new_prev = node
        node.next = curr_node

    def size(self): # O(n)
        
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2): # O(n)
    # Your Solution Here
    u_set = set() # create a set with unique elemets from both lists

    curr_node = llist_1.head # traverse through the first list
    
    while curr_node: # O(n)
        u_set.add(curr_node.value) # add unique elements to the set
        curr_node = curr_node.next # move to the next node

    curr_node = llist_2.head # traverse through the second list
    
    while curr_node: # O(n)
        u_set.add(curr_node.value)
        curr_node = curr_node.next

    union_linked_list = LinkedList() # create a new linked list to store the union set of unique elemets
    for i in u_set:
        union_linked_list.append(i) # append the unique elements to the new linked list


    return union_linked_list


def intersection(llist_1, llist_2): # O(n)
    i_set = set() # create a set with unique elemets from first list in the beginnning

    cur_n = llist_1.head # traverse through the first list

    while cur_n: # O(n)
        i_set.add(cur_n.value) # add unique elements to the set
        cur_n = cur_n.next # move to the next node

    intersection_linked_list = LinkedList() # create a new linked list to store the intersection set of unqiue elemets    

    cur_n = llist_2.head # traverse through the second list
    while cur_n: # O(n)
        if cur_n.value in i_set: # if the element is in the set, add it to the intersection linked list
            intersection_linked_list.append(cur_n.value)
            i_set.remove(cur_n.value) 
# remove the element from the set to avoid duplicates as it willl no longer be present in set therefore even if coming across the same element again it will not be added into linkedlist() as it has no common denominator inside the set
        cur_n = cur_n.next


    if intersection_linked_list is None: # if the intersection linked list is empty, return None
        return "No intersection between the two lists"
    
    return intersection_linked_list        

# ---- base default tests ( Test 1 & Test 2 ) ----

## Test case 1

linked_list_1a = LinkedList()
linked_list_1b = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1a.append(i)

for i in element_2:
    linked_list_1b.append(i)

print (f"Test 1 - Union: {union(linked_list_1a,linked_list_1b)}")
print (f"Test 1 - Intersection: {intersection(linked_list_1a,linked_list_1b)}")

## Test case 2

linked_list_2a = LinkedList()
linked_list_2b = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_2a.append(i)

for i in element_2:
    linked_list_2b.append(i)

print (f"Test 2 - Union: {union(linked_list_2a,linked_list_2b)}")
print (f"Test 2 - Intersection: {intersection(linked_list_2a,linked_list_2b)}")


## ---- Test Cases 3 & 4 & 5 ----
## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 3  - Large Lists
linked_list_3a = LinkedList()
linked_list_3b = LinkedList()

# generate lists of 200 random integers between 0 and 500 each
e_3a = [random.randint(0, 500) for i in range(200)]
e_3b = [random.randint(0, 500) for i in range(200)]

for i in e_3a:
    linked_list_3a.append(i) # generate first linked list

for i in e_3b:
    linked_list_3b.append(i) # generate second linked list

print (f"Test 3 - Union: {union(linked_list_3a,linked_list_3b)}")
print (f"Test 3 - Intersection: {intersection(linked_list_3a,linked_list_3b)}")



## Test Case 4 - Empty Lists

linked_list_4a = LinkedList()   
linked_list_4b = LinkedList()

e_4a = []

e_4b = [random.randint(0, 100) for i in range(50)]

for i in e_4a:
    linked_list_4a.append(i)

for i in e_4b:
    linked_list_4b.append(i)    

print (f"Test 4 - Union: {union(linked_list_4a,linked_list_4b)}")
print (f"Test 4 - Intersection: {intersection(linked_list_4a,linked_list_4b)}")



## Test Case 5 - Strings

linked_list_5a = LinkedList()
linked_list_5b = LinkedList()

e_string1 = [''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(2)) for j in range(10)] # generate 10 random string series of length 2
e_string2 = [''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(2)) for j in range(10)] 

for i in e_string1:
    linked_list_5a.append(i)

for i in e_string2:
    linked_list_5b.append(i)

print (f"Test 5 - Union: {union(linked_list_5a,linked_list_5b)}")
print (f"Test 5 - Intersection: {intersection(linked_list_5a,linked_list_5b)}")


"""
References:
https://www.geeksforgeeks.org/union-and-intersection-of-two-linked-lists/

https://www.codingninjas.com/studio/library/union-and-intersection-of-two-linked-lists

https://www.codespeedy.com/find-union-and-intersection-of-two-linked-lists-in-python/

https://www.javatpoint.com/union-and-intersection-of-two-linked-lists

https://www.youtube.com/watch?v=D0X0BONOQhI
"""