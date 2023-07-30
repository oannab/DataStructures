"""
Problem 5: Blockchain
Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. 
Each block contains some information and how it is connected related to 
the other blocks in the chain. Each block contains a cryptographic hash 
of the previous block, a timestamp, and transaction data. 
For our blockchain we will be using a SHA-256 hash, 
the Greenwich Mean Time when the block was created, 
and text strings as the data.

Use your knowledge of linked lists and hashing to create a 
blockchain implementation.

Block chain with 3 blocks, 'Block 0', 'Block 1' which refers 
to 'Block 0', and 'Block 2' which refers to 'Block 1'
We can break the blockchain down into three main parts.

First is the information hash"""

import hashlib

import datetime

#We do this for the information we want to store in the blockchain 
# such as transaction time, data, and information like the previous chain.

#The next main component is the block on the blockchain

class Block: 

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None

    def calc_hash(self):  # O(1)
        # concatenate the timestamp, data, and previous_hash
        # hash the result
        sha = hashlib.sha256()

        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)

        encoded_str = hash_str.encode('utf-8')
        
        sha.update(encoded_str)

        return sha.hexdigest()

class BlockChain:

    def __init__(self):
        self.chain = []
        # Genesis block is the first block in the chain
        self.add_block(datetime.datetime.utcnow(), "Genesis Block")

    def add_block(self, timestamp, data): # O(1)
        if len(self.chain) == 0:
            previous_hash = 0
        else:
            previous_hash = self.chain[-1].hash 
        
        block = Block(timestamp, data, previous_hash)
        self.chain.append(block)
        return block



    def last_block(self): # O(1)
        return self.chain[-1]    

    def check_valid(self): # O(n)
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i-1].hash:
                return False # If the previous hash of a block doesn't match the hash of the previous block, the chain is invalid

        return True    

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or 
# very large values

## Test Case 1
blockchain = BlockChain()
blockchain.add_block(f"Test 1: {datetime.datetime.utcnow()}", "Transaction 1")

## Test Case 2
blockchain.add_block(f"Test 2: {datetime.datetime.utcnow()}", "Transaction 1")


## Test Case 3
blockchain.add_block(f"Test 3: {datetime.datetime.utcnow()}", "")


# Print the blockchain
for block in blockchain.chain: # O(n)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print()

# Check if the blockchain is valid
print("Is Blockchain Valid?", blockchain.check_valid())



"""
References:
https://www.geeksforgeeks.org/how-is-blockchain-different-from-a-linked-list/
https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
https://github.com/mchrupcala/blockchain-walkthrough
https://www.educative.io/answers/how-to-create-a-simple-blockchain-with-python

"""