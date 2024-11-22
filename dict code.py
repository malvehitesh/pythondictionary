class CustomDict:
    def __init__(self):
        """Initialize an empty dictionary."""
        self.data = {}

    def add(self, key, value):
        """Add or update a key-value pair."""
        self.data[key] = value
        print(f"Added: {key} -> {value}")

    def get(self, key, default=None):
        """Retrieve the value for a given key. Return default if not found."""
        return self.data.get(key, default)

    def delete(self, key):
        """Remove a key-value pair."""
        if key in self.data:
            removed_value = self.data.pop(key)
            return f"Removed: {key} -> {removed_value}"
        else:
            return "Key not found"

    def popitem(self):
        """Remove and return the last inserted key-value pair."""
        if self.data:
            key, value = self.data.popitem()
            return f"Removed: {key} -> {value}"
        else:
            return "Dictionary is empty"

    def contains(self, key):
        """Check if a key exists in the dictionary."""
        return key in self.data

    def size(self):
        """Return the number of key-value pairs."""
        return len(self.data)

    def clear(self):
        """Remove all key-value pairs."""
        self.data.clear()
        return "Dictionary cleared"

    def keys(self):
        """Return all keys."""
        return list(self.data.keys())

    def values(self):
        """Return all values."""
        return list(self.data.values())

    def items(self):
        """Return all key-value pairs."""
        return list(self.data.items())

    def update(self, other_dict):
        """Update the dictionary with another dictionary or key-value pairs."""
        self.data.update(other_dict)
        return "Dictionary updated"

    def setdefault(self, key, default=None):
        """Return the value of a key. If the key does not exist, insert it with the default value."""
        return self.data.setdefault(key, default)

    def copy(self):
        """Return a shallow copy of the dictionary."""
        return self.data.copy()

    def fromkeys(self, keys, value=None):
        """Create a new dictionary from a sequence of keys with a specified value."""
        self.data = dict.fromkeys(keys, value)
        return self.data

    def display(self):
        """Print the entire dictionary."""
        return self.data


# Menu-based interaction
if __name__ == "__main__":
    custom_dict = CustomDict()

    while True:
        print("\nCustom Dictionary Operations Menu:")
        print("1. Add/Update a key-value pair")
        print("2. Get a value by key")
        print("3. Delete a key-value pair")
        print("4. Pop the last inserted item")
        print("5. Check if a key exists")
        print("6. Get dictionary size")
        print("7. Clear the dictionary")
        print("8. Display all keys")
        print("9. Display all values")
        print("10. Display all items")
        print("11. Update dictionary")
        print("12. Set default for a key")
        print("13. Copy dictionary")
        print("14. Create dictionary from keys")
        print("15. Display dictionary")
        print("16. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            key = input("Enter key: ")
            value = input("Enter value: ")
            custom_dict.add(key, value)

        elif choice == 2:
            key = input("Enter key: ")
            default = input("Enter default value (optional): ")
            print(custom_dict.get(key, default))

        elif choice == 3:
            key = input("Enter key to delete: ")
            print(custom_dict.delete(key))

        elif choice == 4:
            print(custom_dict.popitem())

        elif choice == 5:
            key = input("Enter key to check: ")
            print(f"Key exists: {custom_dict.contains(key)}")

        elif choice == 6:
            print(f"Size of dictionary: {custom_dict.size()}")

        elif choice == 7:
            print(custom_dict.clear())

        elif choice == 8:
            print("Keys:", custom_dict.keys())

        elif choice == 9:
            print("Values:", custom_dict.values())

        elif choice == 10:
            print("Items:", custom_dict.items())

        elif choice == 11:
            num_items = int(input("How many items to add to the dictionary? "))
            other_dict = {}
            for _ in range(num_items):
                key = input("Enter key: ")
                value = input("Enter value: ")
                other_dict[key] = value
            print(custom_dict.update(other_dict))

        elif choice == 12:
            key = input("Enter key: ")
            default = input("Enter default value: ")
            print(f"Value: {custom_dict.setdefault(key, default)}")

        elif choice == 13:
            copied_dict = custom_dict.copy()
            print("Copied Dictionary:", copied_dict)

        elif choice == 14:
            keys = input("Enter keys (comma-separated): ").split(",")
            value = input("Enter default value for keys: ")
            print(custom_dict.fromkeys(keys, value))

        elif choice == 15:
            print("Dictionary:", custom_dict.display())

        elif choice == 16:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
