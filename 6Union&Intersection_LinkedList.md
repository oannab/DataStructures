## Problem 6: Union and Intersection of two LinkedLists

**Requirement:**

1. Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

2. You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code. (source: Original Udacity Text)
""
**Overall Summary:**
For both Union & Intersection, the elements are added to a set(), prior to be appended and transformed into Linked Lists. This method is used to allow for an iterable sequence of distinct elements.

**Node Class**
- SPace complexity is constant O(1), regardless of number of node instances created. The attributes of a node remain the same and are predefined for each node, therefore constant.

**LinkedList Class**
- Space complexity is constant O(1) - space required is contsnat for method attributes that are attached to the node instances



**Union:**
- Traverse through the first list and second list of given elements and add the unique elements to a set() - O(n)
- Takes the set list of the union of both lists and converts the list to a linked list - O(n)
- Space complexity is O(n), n is the total number of elements in both linked lists. Space is linear, dependant on legth of linked lists. The storage of the unique elements from both linked lists contributes to the space complexity and is proportional to no of unique elems.
- The time complexity to determine the union of two lists is O(n) since the main operations are converting the lists to sets, which takes linear time, and then converting the result set back to a linked list, which also takes linear time of O(n)

**Intersection:**
- Traverse through the first list of given elements and add the unique elements to a set() - O(n)
- Traverse through the second list of given elements and checks if the element is in the set() and if True, it adds it to the LinkedList intersection list - O(n) + O(n) = O(2n) = O(n)
- Removes the element from the set if found within the seond list - O(n)
- Takes the set list of the union of both lists and converts the list to a linked list - O(n)
- Time complexity  - to determine the intersection of two linked lists is O(n). The primary operation involves creating a set() from the first list, which takes linear time, and then checking the second list against the dictionary to find common elements, also taking linear time of O(n)
- Space complexity is given by new linked list created to store the intersection of unique chars of the 2  input lists - O(n), n is the number of elems in the first linked list.


- For both scenarios, best and worst-case, the time complexity is O(n) for both the union and intersection functions. The main operations involve iterating through the elements of the given lists to convert them to sets and then converting the results back to linked lists. The space complexity remains O(n) as well, considering the sets and the new linked lists that contain all unique elements.
- Overall Space complexity is O(n), n is the total no of stored elements in both operations.
