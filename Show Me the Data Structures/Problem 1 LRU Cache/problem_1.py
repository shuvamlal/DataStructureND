class double_node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

        
class LRU_Cache(object):
    
    def __init__(self, capacity):
        
        self.front = None
        self.rear = None
        self.hash_map = {}
        self.capacity = capacity
        self.current_size = 0
        
        
    def enqueue(self, node):
        if self.front is None:
            self.front = node
            self.rear = node    
        else:
            node.prev = self.front
            self.front.next = node
            self.front = node
        self.current_size += 1

    def dequeue(self, node):
        if self.front is None:
            return

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # if single node is present
        if not node.next and not node.prev:
            self.front = None
            self.rear = None
        
        if self.rear == node:
            self.rear = node.next
            self.rear.prev = None
        self.current_size -= 1
        return node



    def get(self, key):
        if key not in self.hash_map: # cache miss
            return -1
        
        node = self.hash_map[key]
        
        if self.front == node: # cache hit
            return node.value
        self.dequeue(node)
        self.enqueue(node)
        return node.value

    def set(self, key, value):
        if self.capacity <= 0:
            print("cache size is invalid")
            return None
    
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            
            if self.front != node:
                self.dequeue(node)
                self.enqueue(node)
        # when the cache is full      
        else:
            new_node = double_node(key, value)
            if self.current_size == self.capacity:
                del self.hash_map[self.rear.key]
                self.dequeue(self.rear)
            self.enqueue(new_node)
            self.hash_map[key] = new_node

# test case 1
our_cache=LRU_Cache(3)
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
our_cache.set(4,4)
cache_value = our_cache.get(4)    # Expected Value = 4
print(cache_value)
cache_value = our_cache.get(1)    # Expected Value = -1
print(cache_value)
our_cache.set(2,4)
cache_value = our_cache.get(2)    # Expected Value = 4
print(cache_value)
our_cache.set(5,5)
cache_value = our_cache.get(3)    # Expected Value = -1
print(cache_value)
cache_value = our_cache.get(5)    # Expected Value = 5
print(cache_value)
our_cache.set(2,6)
cache_value = our_cache.get(2)    # Expected Value = 6
print(cache_value)
our_cache.set(6,6)
cache_value = our_cache.get(4)    # Expected Value = -1
print(cache_value)
cache_value = our_cache.get(6)    # Expected Value = 6
print(cache_value)
our_cache.set(5,10)
our_cache.set(7,7)
print()

# Test case 2
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
cache_value = our_cache.get(1)       # returns 1
print(cache_value)
cache_value = our_cache.get(2)       # returns 2
print(cache_value)
cache_value = our_cache.get(9)       # return -1
print(cache_value)
print()

# Test case 3
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
cache_value = our_cache.get(1)       # returns 1
print(cache_value)
cache_value = our_cache.get(2)       # returns 2
print(cache_value)
cache_value = our_cache.get(3)       # return 3
print(cache_value)
cache_value = our_cache.get(5)       # return 5
print(cache_value)
our_cache.set(6, 6)
cache_value = our_cache.get(4)       # return -1
print(cache_value)
cache_value = our_cache.get(6)       # return 6
print(cache_value)
print()