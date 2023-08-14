**Requirement**
* A. Huffman Encoding
- Phase I - Build the Huffman Tree - A Huffman tree is built in a bottom-up approach.
- Phase II - Generate the Encoded Data
* B. Huffman Decoding
- implement the logic for both encoding and decoding 

* 

**create_freq_table**
- Time complexity is O(n), where n is the length of input data
- Iterates trough the input data and build the dictionary adding the frequency as value to each character
- Space Complexity - O(n), n is the no of unique elems in the input data. The method only creates a freq table dictionary to store chars frequency.


**build_tree**
- The priority Queue - Heap - merges nodes with lowest frequency. The priority queue is a binary heapwhich is O(log n) due to insertion and deletion
- Time complexity: O(n log n), where n is the number of unique characters in the input data. Running time is directly proportional to the input size due to the heapq.heappush() operation being performed n times, and each operation takes O(log n) time.
- The while loop iterates through the priority queue, performing O(log n) heap operations for each element (in the worst case, all elements). Hence, the overall time complexity is O(n log n).
- Space Complexity is given by the priority queue instances -HuffmanNodes- nodes in the tree. 
- Worst case scenario is the no of nodes in the trees is the same as no of unique chars in the input data - O(n), n is no of unique chars


**huffman_encoding()**
- Linear Time complexity: O(n log n), where n is the length of the input data.
- The function first calls create_freq_table(data) with a time complexity of O(n) and space complexity of O(n), n is no of elems stored in dictionary. 
- Then, it calls build_tree(freq_table), which has a time complexity of O(n log n). Traversing the Huffman tree to generate the codes has a time complexity of O(n), as each character is traversed once to build the corresponding Huffman code.
- Space complexity - O(n), is given by unique elems, but the traversal (computational memory required) can also contribute to the space complexity


**huffman_decoding**
- Linear Time complexity: O(n), where n is the length of the encoded data.
- The decoding process requires traversing the Huffman tree for each bit in the encoded data. I
- Worst case - each bit corresponds to a unique character in the original data. Since the Huffman tree has n nodes (where n is the number of unique characters), the time complexity for decoding is O(n).
- Space required for the Huffman Tree is proportional to the height of the tree which is O(log n), n is the unique chars.
- SPace required for decoding is proportional to the encoded data - O(n), n is the length of encoded data
- Overall Space complexity is O(log n) + O(n), which is overall worst case O(n)

**Summary**
* Overall time complexity of Huffman encoding() and decoding() is O(n log n), where n is the length of input data. 
* Overall space complexity is O(n), given by the frequency table and Huffman Tree, n is number of unique chars in the input data.
