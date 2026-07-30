"""
Core deterministic random number generator engine.
Uses FNV-1a for string hashing and a Linear Congruential Generator (LCG)
for generating pseudo-random sequences based on a seed.
"""

def hash_seed(seed_str: str) -> int:
    """
    Hashes a string into an unsigned 32-bit integer using FNV-1a.
    This provides a reliable offset basis for the deterministic random generator.
    
    Args:
        seed_str (str): The input string to hash (e.g., a product ID).
        
    Returns:
        int: An unsigned 32-bit integer seed.
    """
    h = 2166136261  # FNV-1a 32-bit offset basis
    for char in seed_str:
        h ^= ord(char)
        # Emulate 32-bit multiplication (imul in JS)
        h = (h * 16777619) & 0xFFFFFFFF
    return h

class LCG:
    """
    Linear Congruential Generator (LCG) for deterministic pseudo-random number generation.
    Matches the specific constants used in the original JS engine:
    Multiplier: 1664525
    Increment: 1013904223
    """
    def __init__(self, seed: int):
        self.state = seed

    def next_float(self) -> float:
        """
        Advances the generator and returns a float in the range [0, 1).
        
        Returns:
            float: A pseudo-random float between 0 (inclusive) and 1 (exclusive).
        """
        # Emulate 32-bit integer overflow exactly like JavaScript
        self.state = ((self.state * 1664525) + 1013904223) & 0xFFFFFFFF
        return self.state / 0xFFFFFFFF

    def pick(self, items: list):
        """
        Picks a single item from a list deterministically.
        
        Args:
            items (list): The list to pick from.
            
        Returns:
            Any: The randomly picked item.
        """
        if not items:
            return None
        index = int(self.next_float() * len(items))
        return items[index]
