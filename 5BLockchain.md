## Problem 5: BlockChain

**Requirement:**

* Simple implementation of blockchain data structure consisting of blocks linked together. Each block contains a times and data stamp, a hash to the previous block and its own hash.

**Block Class**
- space complexity of block instances created is O(1), as the blocks have predetermined attributes which are fixed for each instance. Constant amount of memory allocated for each block, regardless of no of instances created.

**calc_hash**
- calculates the hash of each block using SHA-256 constructor method
- Time complexity is linear O(1)
- space complexity is O(1), as the space required is constant to calculate the hashof the block


**BlockChain Class**
- space complexity is given by the chain list that stores instances of the Block Class - O(n), n is no of blocks stored

**add_block()**
- adds a new block to the chain
- takes its date & time stamp & previous hash as input 
- Time complexity is constatnt O(1)
- Space complexity is O(n), n is the no of new blocks created

**last_block()**
- returns most recent block on the blockchain 
- Time complexity is constant O(1)
- Space complexity is not significantly impact, as it returns a refernece to the last block, therefore no significant additional memory is required.

**check_valid()**
- iterated through the blockchain and verifies that each block's 'prev_hash' matches the hash of the previous block, otherwise returns invalid 
- Time complexity is O(n) as it iteraates trough the whole blockchain and checks for valid 'prev_hash'
- Space complexity is given by the iteration and comparison of each block's hash and previous hash - O(n), n is the no of blocks on the blockchain

- printing space complexity is O(n), where the space is proportional to the blocks on the chain.

**SUMMARY**
- Overall Time complexity is O(n) where n is the number of blocks on the blockchains. The overall complexity O(n) is given by the search operation even if the manipulation of block itself is constant
- Overall SPace complexity is O(n), n is no of blocks on the blockchain
