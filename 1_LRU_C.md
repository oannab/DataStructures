### 1 - LRU CACHE (Least Recently Used) ###
* data structure that maintains a fixed size cache and removes the least recently used item when capacity is exceeded.

**class LRU CACHE (Object)** 
- create the object cache 
- 'cache' dictionary is used to store nodes

**get()**
- retrieve the value based on the dictionary 'key' provided - if exists - O(1)
- if exists, the current node is moved to the front of the linked list - O(1)

**set()**
- if the requested key exists, its current node value is updated and  moved to the front of the linked list - O(1)
- if the 'key' does not exist in the dictionary, a new 'key-value' pair is added to dictionary - a new node is created - O(1)
- the new node is added to the front of the linked list and stored in cache/dictionary - O(1)

**move_to_front()**
- if node anywhere in in the list, except the front, it moves the specified node at the front of linked list - constant time O(1)
- no action if node already at the front - O(1)

**move_to_front()**
- if tails does not exist/None, no action - O(1)
- if tail is the only node in the list, current head and tail is updated with this node - O(1)
- if multiple nodes, tail is udated, and the removed node is detached from the linked list - constant time O(1)


*Space Complexity*
- the complexity is given by the capacity a cache can hold
- the cache capacity is fixed, created with the instance of cache, predefined at the beginning. This determines the max elements that can be stored. 
- The space in the cache is used by the linked list nodes and dictionary and remains constant once the cached is initializes. 

- The Doubly Linked List Nodes - each node takes a constant amount of memory to store pointers & values - O(1). The memory used by nodes is constant regardless of cache capacity. Therefore, if cache is full, the space complexity of nodes is proportional and constant to the size of cache / its capacity O(capacity). T

- The Dictionary Cache Space - is used to store the key/value pairs, keys correspond to the cache keys and values correspond to the cache nodes.  Each key/value use constant O(1) amount of memory - therefore it is dependant of the cache size and the actual size a node (the doubly linked list nodes) will take based on the class attribute 

- Total SPace complexity is constant O(1) - both the linked list nodes and the dictionary have constant space complexity O(1) in terms of memory required per node/element. Once the cache is initialized, its capacity doesn't change. It is not dependent on input data or number of elements, it is only determined by the maximum capacity of the cache.
