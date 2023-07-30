### 1. LRU CACHE ###
# doubly linked list to store the cache. 
#Moves most recently used nodes to the front of the list.

#add_to_front()

#remove_from_back()
#append() # appends specified node to the end of the list

#remove() # removes most recently used node from the list

#move_to_front() # moves specified node to the front of the list

#All operations must take O(1) time.

""" """


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
        self.cache = {} # dictionary to store the nodes
        

    def get(self, key): #time complexity is O(1)
               
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1
        
        node = self.cache[key] # get the node from the cache
        self.move_to_front(node) # move the node to the front of the list
        return node.value 
            
#
    def set(self, key, value): # time complexity is O(1)
        # add a new key-value pair to cache
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            node = self.cache[key] # get the node from the cache
            node.value = value # update the value of the node
            self.move_to_front(node) # move the node to the front of the list
        else:
            if self.size >= self.capacity :
                self.remove_from_back() # remove the node from the back of the list

                print('self.size', self.size)
            #add new value at the beginning of the list
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.move_to_front(new_node)
            
            
            #self.append(node) # append the node to the end of the list
            
            print(new_node)


    def move_to_front(self, node): #time complexity is O(1)
        # move the node to the front of the list
        if node == self.head:
            return
        
        print('self.head', self.head)

        if node == self.tail: # if the node is the tail
            self.tail = self.tail.prev # update the tail
            if self.tail:
                self.tail.next = None # update the tail
            print('self.tail', self.tail)
            print('self.tail.next', self.tail.next)    
        else:
            if node.prev:
                node.prev.next = node.next # update the prev node
                print('node.prev.next', node.prev.next)
            if node.next:    
                node.next.prev = node.prev # update the next 
                print('node.next.prev', node.next.prev )
        
        node.prev = None
        if self.head:
            self.head.prev = node
            print('self.head.prev', self.head.prev)
        node.next = self.head
        self.head = node

        print('self.head', self.head)


    def remove_from_back(self): #time complexity is O(1)
        # remove the node from the back of the list
        if self.tail == None:
            return
        print('self.tail', self.tail)
        if self.tail.prev == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        print('self.tail', self.tail)


"""    def append(self, node): #time complexity is O(1)
        #append the node to the end of the list
        if self.head == None:
            self.head = node
            self.tail = node
            return"""
        
        


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

our_cache = LRU_Cache(1)

our_cache.set(1, 'd');

our_cache.get(1)       # returns 'd'

our_cache.set(2, 'o');   

our_cache.get(1)       # returns -1 - gets removed

our_cache.get(2)       # returns 'o'

# should return -1 because cache reached it's capacity and 3 was the least recently used entry

## Test Case 2

our_cache = LRU_Cache(0)

our_cache.set(1, 1);

our_cache.set(2, 2);

## Test Case 3

our_cache = LRU_Cache(-1)

our_cache.set(1, 1);    

our_cache.set(2, 2);    