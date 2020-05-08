import hashlib
import time

class Block:
    def __init__(self, data, timestamp=None, prev_hash=None):
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = prev_hash
        self.hash = self.calc_hash(data)
        self.next=None
      
    def calc_hash(self,data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')    # data will be encoded
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.head = None
        
    def add_block(self,data):
        timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.localtime())
        
        if self.head is None:    # first block of the chain
            self.head = Block(data, timestamp,0)
            return
        else:    # Move the node to the last
            node = self.head
            while node.next:
                node = node.next
            prev_hash=node.hash
            node.next = Block(data, timestamp, prev_hash)
            return


    def print_blockchain(self):
        if self.head is None:
            print("Empty chain")
        else:
            node=self.head
            if node.next.previous_hash != node.hash:
                printf("hash is of another type")
            else:
                while node:    
                    print(node.timestamp)
                    print(node.data)
                    print(node.previous_hash)
                    node = node.next

b1 = BlockChain()

b1.add_block("Block 1")
b1.add_block("Block 2")
b1.add_block("Block 3")
b1.print_blockchain()
# answer
# Thu, 23 Apr 2020 01:33:16 PM India Standard Time
# Block 1
# 0
# Thu, 23 Apr 2020 01:33:16 PM India Standard Time
# Block 2
# 8eb412d817c7762cbd93dd64982b163e9b75ab1e4b584052b2c675247a7a9c22
# Thu, 23 Apr 2020 01:33:16 PM India Standard Time
# Block 3
# 3098ea9817bca09fad1817836acace069f4a63fafdf7e981b6d2330ef1295a10
print()
#test case 2
b2= BlockChain()
b2.print_blockchain()
# answer
# Empty chain
print()
#test case 3
b3=BlockChain()
b3.add_block("Block Chain head")
b3.add_block("")
b3.add_block("tail of the block chain")
b3.print_blockchain()
# answer
# Thu, 23 Apr 2020 01:35:09 PM India Standard Time
# Block Chain head
# 0
# Thu, 23 Apr 2020 01:35:09 PM India Standard Time

# e42b20c56d234e855931a9e495fe9fcb4314c9824a5facc5c4a5405852f23eef
# Thu, 23 Apr 2020 01:35:09 PM India Standard Time
# tail of the block chain
# e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855