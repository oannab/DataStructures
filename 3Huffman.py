"""A. Huffman Encoding
Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:

Phase I - Build the Huffman Tree
A Huffman tree is built in a bottom-up approach.

First, determine the frequency of each character in the message. In our example, the following table presents the frequency of each character.
(Unique) Character	Frequency
A	7
B	3
C	7
D	2
E	6
Each row in the table above can be represented as a node having a character, frequency, 
left child, and right child. In the next step, we will repeatedly require to pop-out the 
node having the lowest frequency. Therefore, build and sort a list of nodes in the order 
lowest to highest frequencies. Remember that a list preserves the order of elements in which 
they are appended.
We would need our list to work as a priority queue, where a node that has lower frequency 
should have a higher priority to be popped-out. The following snapshot will help you 
visualize the example considered above:

Visualization of what we would like our priority queue to look like, with the lowest frequency 
node on the left, 'D'-2, followed by 'B'-3, 'E'-6, 'A'-7, and finally the highest frequency 
node on the right, 'C'-7.
Can you come up with other data structures to create a priority queue? How about using a 
min-heap instead of a list? You are free to choose from anyone.

Pop-out two nodes with the minimum frequency from the priority queue created in the above step.

Create a new node with a frequency equal to the sum of the two nodes picked in the above step. 
This new node would become an internal node in the Huffman tree, and the two nodes would become 
the children. The lower frequency node becomes a left child, and the higher frequency node becomes 
the right child. Reinsert the newly created node back into the priority queue.

Do you think that this reinsertion requires the sorting of priority queue again? If yes, then a 
min-heap could be a better choice due to the lower complexity of sorting the elements, every 
time there is an insertion.

Repeat steps #3 and #4 until there is a single element left in the priority queue. The snapshots 
below present the building of a Huffman tree.
Visualization of the steps described above to build a Huffman tree from a priority queue.
Visualization of repeating steps 3 and 4 above to create a Huffman tree.
For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child. 
See the final Huffman tree for our example:
The resulting Huffman tree from the given priority queue.

Phase II - Generate the Encoded Data
Based on the Huffman tree, generate unique binary code for each character of our string message. 
For this purpose, you'd have to traverse the path from root to the leaf node.
| (Unique) Character | Frequency | Huffman Code | |:-------------:|:-------------:| | D | 2 | 000 | | B | 3 | 001 | | E | 6 | 01 | | A | 7 | 10 | | C | 7 | 11 |

Points to Notice

Notice that the whole code for any character is not a prefix of any other code. Hence, 
the Huffman code is called a Prefix code.
Notice that the binary code is shorter for the more frequent character, and vice-versa.
The Huffman code is generated in such a way that the entire string message would now require a 
much lesser amount of memory in binary form.
Notice that each node present in the original priority queue has become a leaf node in the 
final Huffman tree.
This way, our encoded data would be 1010101010101000100100111111111111111000000010101010101
"""
"""B. Huffman Decoding
Once we have the encoded data, and the (pointer to the root of) Huffman tree, we can easily 
decode the encoded data using the following steps:

Declare a blank decoded string
Pick a bit from the encoded data, traversing from left to right.
Start traversing the Huffman tree from the root.
If the current bit of encoded data is 0, move to the left child, else move to the right 
child of the tree if the current bit is 1.
If a leaf node is encountered, append the (alphabetical) character of the leaf node to the 
decoded string.
Repeat steps #2 and #3 until the encoded data is completely traversed.
You will have to implement the logic for both encoding and decoding in the following template. 
Also, you will need to create the sizing schemas to present a summary.
"""
import sys
import heapq

#heapq module (priority queue)
#maintains a heap of items, where each item is a pair of values. Heapq compares

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None  

    def __lt__(self, other):
        return self.freq < other.freq     

def create_freq_table(data): # O(n) time complexity
    freq_table = {}
    for char in data: 
        if char in freq_table:
            freq_table[char] += 1 # count the frequency of each character
        else:
            freq_table[char] = 1 # add to dictionary and start counting frequency
    return freq_table        


def build_tree(freq_table): # O(n log n)
    priority_queue = []
    for char, freq in freq_table.items(): # O(n)
        node = HuffmanNode(char, freq)
        heapq.heappush(priority_queue, node) # O(log n) - push directly to heap 
           
    while len(priority_queue) > 1: # O(n log n) -> heap is O(log n)
        node1 = heapq.heappop(priority_queue) #pop out the first lowest. heapq compares the first element of the tuples. 
        node2 = heapq.heappop(priority_queue) #pop out the second
        sum_node = HuffmanNode(None, node1.freq + node2.freq) #create a new node with the sum of the 2 node - parent node of lowest-freq 2 current nodes
        sum_node.left = node1
        sum_node.right = node2
        heapq.heappush(priority_queue, sum_node) #maintains priority queue based on frequency    
    return priority_queue[0] #return the root node of the tree

 

def huffman_encoding(data): # O(n log n)
    if data is None:
        return "", None
    elif not data:  # Check if the data is an empty string
        return "", HuffmanNode(None, 0) # 0 is the frequency of the 'None' value

    freq_table = create_freq_table(data) # create the frequency table - O(n) and n is the length of input data the f() needs to traverse
    node = build_tree(freq_table) # the frequency table is the input data to create the tree - O(n log n) where n is the length of tree and logn is the levels of the tree the n in O(N logn) needs to traverse

    huffman_codes = {} # dictionary to store huffman codes for each character in the input data
    stack = [(node, "")] # traverse the tree iteratively and mark the frequency. The tuple elements are at the 'current_node' and its 'frequency' 
    while stack: # O(n) where n is the number of unique items in the input data
        current_node, code = stack.pop() # with each iteration remove the current_node from the stack
        if current_node.char is not None:  # if current_node is not a leaf node
            huffman_codes[current_node.char] = code # update the dictionary
        else:
            stack.append((current_node.left, code + "0")) # traverse and add the left child '0' to the code
            stack.append((current_node.right, code + "1")) # traverse and add the right leaaf '1' to the code

    encoded_data = "".join(huffman_codes[char] for char in data) # binary representation of the data

    return encoded_data, node # node is the root



def huffman_decoding(encoded_data, tree): # O(n) 
    if not encoded_data or tree is None:
        return ""
    decoded_data = ""
    current_node = tree
    for bit in encoded_data:
        if bit not in encoded_data:
            raise TypeError ("Null Input")
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":#
            current_node = current_node.right
        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = tree
    return decoded_data
    

if __name__ == "__main__":
    codes = {}

# Example usage:
message = "AAAAAAABBBCCCCCCCDDEEEEEE"
encoded_message, huffman_tree = huffman_encoding(message)
print("Encoded Message:", encoded_message)
print("Decoded Message:", huffman_decoding(encoded_message, huffman_tree))

# Test Case 0 - Default
print('test 0')
a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # sys.getsizeof() eturns the size of any object in bytes.
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

## Test Case 1
print('test 1')
a_large_sentence = "The bird is the word and this sentence is so so so so so so so so so sos so so sos ossossososoososso long"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_large_sentence)))
print ("The content of the data is: {}\n".format(a_large_sentence))

encoded_data, tree = huffman_encoding(a_large_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))


# Test Case 2
print('test 2')
a_null_sentence = None

print("The size of the data is: {}\n".format(sys.getsizeof(a_null_sentence)))
print("The content of the data is: {}\n".format(a_null_sentence))

encoded_data, tree = huffman_encoding(a_null_sentence)

if encoded_data:
    print("The size of the encoded data is: {} bytes\n".format(sys.getsizeof(int(encoded_data, base=2)) // 8))
    print("The content of the encoded data is: {}\n".format(encoded_data))
else:
    print("The encoded data is empty.")

decoded_data = huffman_decoding(encoded_data, tree)

print("The size of the decoded data is: {} bytes\n".format(sys.getsizeof(decoded_data)))
print("The content of the decoded data is: {}\n".format(decoded_data))


# Test Case 3
print('test 3')
empty_sentence = ""

print("The size of the data is: {}\n".format(sys.getsizeof(empty_sentence)))
print("The content of the data is: {}\n".format(empty_sentence))

encoded_data, tree = huffman_encoding(empty_sentence)

if encoded_data:
    print("The size of the encoded data is: {} bytes\n".format(sys.getsizeof(int(encoded_data, base=2)) // 8))
    print("The content of the encoded data is: {}\n".format(encoded_data))
else:
    print("The encoded data is empty.")

decoded_data = huffman_decoding(encoded_data, tree)

if decoded_data:
    print("The size of the decoded data is: {} bytes\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))
else:
    print("The decoded data is empty.")

"""
references:
https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
https://stackoverflow.com/questions/55446613/not-supported-between-instances-of-str-and-node
https://blog.finxter.com/python-__lt__-magic-method/
https://stackoverflow.com/questions/63164064/unable-to-understand-lt-method
https://www.kosbie.net/cmu/fall-15/15-112/notes/notes-data-compression.html
https://www.programiz.com/dsa/huffman-coding
https://en.wikipedia.org/wiki/Huffman_coding
https://www.javatpoint.com/huffman-coding-using-python
https://stackoverflow.com/questions/55876342/difference-between-ologn-and-onlognhttps://stackoverflow.com/questions/55876342/difference-between-ologn-and-onlogn
https://www.youtube.com/watch?v=dM6us854Jk0
"""
