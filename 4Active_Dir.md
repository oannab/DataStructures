## Problem 4: Active Directory

**Requirement:**

* Write a function that provides an efficient look up of whether the user is in a group. 

**is_user_in_group()**
- Time complexity is given by the recursive calls and iterations performed. As it traverses recursively the entire hierarchy, inlcuding all subgroups to find the user. In this case 'n' is the total of groups and 'm' the average number of subgroups in each group - O(n+m)
- The space complexity is given by the recursive call stack - O(n), n is the number of children each group has. The space allocated for each group and its children increases linearly depending on potential depth of groups traversed. Worst-case - the function call stack can use memory proportional to the no of groups, users and recursion depth.
