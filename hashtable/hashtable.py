class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key   = key
        self.value = value
        self.next  = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.storage   = [None] * capacity
        self.__true_size = 0
        self.min_size  = 8

    @property
    def capacity(self):
        return len(self.storage)

    @property
    def size(self):
        return self.__true_size

    def increase_size(self):
        self.__true_size += 1
        if self.__true_size / self.capacity >= 0.7:
            self.resize()

    def decrease_size(self):
        self.__true_size -= 1
        if self.__true_size / self.capacity <= 0.2:
            self.resize(1)

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        total = 0
        for b in key.encode():
            total ^= b
            total &= 0xffffffffffffffff
        return total

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        total = 5381
        for b in key.encode():
            total = total * 33 + b
        return total

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # index = self.fnv1(key) % self.capacity
        index = self.djb2(key) % self.capacity
        return index

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            # No node at the index? Create one
            self.storage[index] = HashTableEntry(key, value)
            self.increase_size()
        else:
            # There is a node? Now we must check if our key
            # is the same, or if we need to create a new node
            current_node = self.storage[index]
            while True:
                if current_node.key == key:
                    # If we find a node with our given key,
                    # Overwrite its value
                    current_node.value = value
                    return
                elif current_node.next is None:
                    # If we didn't find a node with our given key,
                    # Create one!
                    current_node.next = HashTableEntry(key, value)
                    self.increase_size()
                    return
                else:
                    # Otherwise, keep chaining down our nodes
                    current_node = current_node.next

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is not None:
            # If we find a node,
            # then chain down to find a node with the given key.
            previous_node = None
            current_node = self.storage[index]
            while current_node is not None:
                if current_node.key == key:
                    # If we find a node that matches the given key,
                    # remove the pointer from the previous node
                    current_node.value = None
                    if previous_node:
                        previous_node.next = current_node.next
                    self.decrease_size()
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next
        # No node with given key found? Error
        raise KeyError(f"Could not find key: \"{key}\"")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is not None:
            # If we find a node,
            # then chain down to find a node with the given key.
            current_node = self.storage[index]
            while current_node is not None:
                if current_node.key == key:
                    # If we find a node, return it!
                    return current_node.value
                else:
                    current_node = current_node.next
        # no node found? Return None
        return None

    def resize(self, grow_or_shrink=0):
        """
        Doubles or halves the capacity of the hash table and
        rehashes all key/value pairs.

            grow_or_shrink: 0 grow | 1 shrink
        """

        # Hold onto old storage so we can rehash our values
        old_storage = self.storage
        if grow_or_shrink == 1:
            self.storage = [None] * (self.capacity // 2)
        else:
            self.storage = [None] * self.capacity * 2
        # Reset our size so we start resizing at 0 again
        self.__true_size = 0
        for val in old_storage:
            if val is not None:
                # If our value exists,
                # we will rehash the node, AND all nodes connected to it
                current_node = val
                while current_node is not None:
                    self.put(current_node.key, current_node.value)
                    current_node = current_node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
