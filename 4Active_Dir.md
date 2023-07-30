## Problem 5: Union and Intersection of two LinkedLists

**Requirement:**

* Write a function that provides an efficient look up of whether the user is in a group. 

**is_user_in_group()**
- Time complexity is given by the recursive calls and iterations performed. As it traverses recursively the entire hierarchy, inlcuding all subgroups to find the user. In this case 'n' is the total of groups and 'm' the average number of subgroups in each group.
 - O(n+m)