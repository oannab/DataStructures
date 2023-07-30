## Problem 6: Union and Intersection of two LinkedLists

**Requirement:**

* Simple implementation of blockchain data structure consisting of blocks linked together. Each block contains a times and data stamp, a hash to the previous block and its own hash.

**calc_hash**
- calculates the hash of each block using SHA-256 constructor method
- Time complexity is linear O(1)

**add_block()**
- adds a new block to the chain
- takes its date & time stamp & previous hash as input 
- Time complexity is constatnt O(1)

**last_block()**
- returns most recent block on the blockchain 
- Time complexity is constant O(1)

**check_valid()**
- iterated through the blockchain and verifies that each block's 'prev_hash' matches the hash of the previous block, otherwise returns invalid 
- Time complexity is O(n) as it iteraates trough the whole blockchain and checks for valid 'prev_hash'

**SUMMARY**
- Overall Time complexity is O(n) where n is the number of blocks on the blockchains. The overall complexity O(n) is given by the search operation even if the manipulation of block itself is constant
