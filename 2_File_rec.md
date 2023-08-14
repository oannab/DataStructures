## Exercise 2 - File Search Recursion

**find_files()**
**search_files()**
- takes a 'suffix' argument - a string representing the file name extension to search for 
- iterates trough files and directories - O(n)
- Check file extension matches the given suffix -O(1)
- Adding the match file path to the list - O(n)
- Best case scenario is O(1) if the specified file contains no files/directories and the returned list is empty.
- Worst case scenario  is O(n) when the specified path contains large files and subdirectories, as the f() needs to traverse all.

- space complexity is given by the recursion of the f() - O(n), n is the total number of files/directories found during traversal. With each recursive call, we store local variables and return addresses. 
- The recursion grows linearly: 
    - start at root to search for suffix. files and subdirs are added to the files list. 
    - From there, recursively search inside each subdir and add its diles/subdirs with files to files list.
    - after all sudirs are explored and added to files list, exit traversal.
- the depth of the recursion is given by the directory structure and number of nested subdirectories. each traversal stores the subdirs and files found and added to the files list - O(n), n is the number of files and dirs stored. The space used by the function call stack and local variables increases with th depth 

**Time / Space Complexity**
- Overall time complexity is O(n)
- Space complexity is O(n), n is no of files and subdirs. The space used by the function call stack and local variables increases with the depth of dirs traversed. Linear relationship between memory used and no of elems traversed.

_References:_
_https://stackoverflow.com/questions/61255507/time-and-space-complexity-of-a-file-recursion-algorithm_
