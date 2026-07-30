from typing import Any, Optional

class Node:
    """
    A node in the doubly linked list used by the LRU Cache.
    """
    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class LRUCache:
    """
    Custom Least Recently Used (LRU) Cache implementation.
    Uses a combination of a Hash Map (dict) and a Doubly Linked List
    to achieve O(1) time complexity for both get and put operations.
    """
    def __init__(self, capacity: int = 100):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.cache = {}  # Map key -> Node
        
        # Dummy head and tail to simplify edge cases
        self.head = Node("head", None)
        self.tail = Node("tail", None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: Node):
        """Removes an existing node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node

    def _add_node_to_head(self, node: Node):
        """Adds a node right after the dummy head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node

    def get(self, key: str) -> Optional[Any]:
        """
        Retrieves a value from the cache.
        Moves the accessed node to the head of the list (most recently used).
        
        Args:
            key: The key to look up.
            
        Returns:
            The cached value if it exists, otherwise None.
        """
        if key in self.cache:
            node = self.cache[key]
            # Move to front
            self._remove_node(node)
            self._add_node_to_head(node)
            return node.value
        return None

    def put(self, key: str, value: Any):
        """
        Adds or updates a value in the cache.
        If the cache exceeds capacity, the least recently used item is evicted.
        
        Args:
            key: The key to store.
            value: The value to cache.
        """
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_node_to_head(node)
        else:
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node_to_head(new_node)
            
            # Check capacity and evict LRU if needed
            if len(self.cache) > self.capacity:
                # The LRU node is right before the tail
                lru_node = self.tail.prev
                if lru_node and lru_node != self.head:
                    self._remove_node(lru_node)
                    del self.cache[lru_node.key]
