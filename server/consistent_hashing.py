import hashlib
import bisect

class ConsistentHashing:
    def __init__(self, num_replicas=3):
        self.num_replicas = num_replicas
        self.ring = []
        self.nodes = {}

    def _hash(self, key): 

# key.encode('utf-8'):
#       Converts the key string to UTF-8 encoded bytes.

# hashlib.sha256(...):
#       Creates a SHA-256 hash object from the encoded key.

# .hexdigest():
#       Returns the hash as a string of hexadecimal digits.

# int(..., 16):
#       Converts the hexadecimal string to an integer, using base 16.

        return int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node):
        for i in range(self.num_replicas):
            node_hash = self._hash(f"{node}-{i}")
            # print("node vale " f"{node}-{i}", node_hash)
            bisect.insort(self.ring, node_hash)
            self.nodes[node_hash] = node
# bisect.insort() performs two main operations:
#       It finds the correct insertion point for the new element using binary search.
#       It inserts the element at that position, shifting other elements as necessary.

# bisect.insort(self.ring, node_hash) -----node_hash is the element to insert inside the self.ring


    def get_node(self, key):
        key_hash = self._hash(key)
        idx = bisect.bisect(self.ring, key_hash)
        if idx == len(self.ring):
            idx = 0
        return self.nodes[self.ring[idx]]
# The bisect.bisect() function (also known as bisect.bisect_right()) is used to find the insertion 
# point for a new element in a sorted list. Here's an explanation of how it works:

# Purpose: bisect.bisect() finds the index where an element should be inserted in a sorted list
# to maintain the list's order.

# idx = bisect.bisect(self.ring, key_hash) ---- in this, we get the index, where key_hash would be placed if its not in
# the list already, if it is already present, its index would be returned.