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
