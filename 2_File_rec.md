## Exercise 2 - File Search Recursion

**find_files()**
**search_files()**
- takes a 'suffix' argument - a string representing the file name extension to search for 
- iterates trough files and directories - O(n)
- Check file extension matches the given suffix -O(1)
- Adding the match file path to the list - O(n)
- Best case scenario is O(1) if the specified file contains no files/directories and the returned list is empty.
- Worst case scenario  is O(n) when the specified path contains large files and subdirectories, as the f() needs to traverse all.

**Summary**
* Overall time complexity is O(n)