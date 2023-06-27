class Hashtable:
    def __init__(self):
        """
        Initialize the HashTable class.
        Args: None
        Returns: None
        """
        self.size = 100  # Size of the hash table
        self.table = [[] for _ in range(self.size)]  # Create an empty table with nested lists

    def _hash(self, key):
        """
        Hashes the key to determine the index in the table.
        Args: key (any): The key to be hashed.
        Returns: int: The index in the table for the given key.
        """
        return hash(key) % self.size

    def set(self, key, value):
        """
        Sets the key-value pair in the hash table, handling collisions as needed.
        If the key already exists, its value is replaced with the new value.
        Args:
            key (any): The key to be set.
            value (any): The value associated with the key.
        Returns: None
        """
        index = self._hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                entry[1] = value  # Update the value if the key already exists
                return
        self.table[index].append([key, value])  # Add a new key-value pair

    def get(self, key):
        """
        Retrieves the value associated with the given key from the hash table.
        Args: key (any): The key to retrieve the value for.
        Returns: any: The value associated with the key, or None if the key is not found.
        """
        index = self._hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]  # Return the value if the key exists
        return None  # Key not found

    def has(self, key):
        """
        Checks if the given key exists in the hash table.
        Args: key (any): The key to check for existence.
        Returns: bool: True if the key exists, False otherwise.
        """
        index = self._hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return True  # Key found
        return False  # Key not found

    def keys(self):
        """
        Retrieves a collection of keys in the hash table.
        Args: None
        Returns: list: A list of keys in the hash table.
        """
        keys = []
        for entries in self.table:
            for entry in entries:
                keys.append(entry[0])
        return keys

    def hash(self, key):
        """
        Computes the hash value for the given key.
        Args: key (any): The key to compute the hash value for.
        Returns: int: The hash value for the key.
        """
        return self._hash(key)
