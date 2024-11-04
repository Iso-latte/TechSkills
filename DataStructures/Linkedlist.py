

class Node:
    def __init__(self, data): # Constructor
        self.data = data # Assign data
        self.next = None # Assign next to None

class LinkedList:
    def __init__(self):
        self.head = Node() # Set the head to a node with no data

    def append(self, data):
        new_node = Node(data) # Create a new node with the data
        current = self.head # Set the current node to the head
        while current.next is not None: # While the current node has a next node
            current = current.next # Set the current node to the next node
        current.next = new_node # Set the next node to the new node

    def length(self):
        current = self.head # Set the current node to the head
        total = 0 # Set the total to 0
        while current.next is not None: # While the current node has a next node
            total += 1 # Increment the total
            current = current.next # Set the current node to the next node
        return total # Return the total
    
    def display(self):
        elements = [] # Create a list to store the elements
        current = self.head # Set the current node to the head
        while current.next is not None: # While the current node has a next node
            current = current.next # Set the current node to the next node
            elements.append(current.data) # Append the data of the current node to the list
        print(elements) # Print the list

    def get(self, index): # Get the data at a specific index
        if index >= self.length():   # If the index is greater than the length of the linked list
            print("ERROR: 'Get' Index out of range!") # Print an error message
            return None # Return None
        current_index = 0  # Set the current index to 0
        current = self.head # Set the current node to the head
        while True: # Infinite loop 
            current = current.next # Set the current node to the next node
            if current_index == index:  # If the current index is equal to the index
                return current.data # Return the data of the current node
            current_index += 1  # Increment the current index

    def remove(self, index): # Erase the node at a specific index
        if index >= self.length(): # If the index is greater than the length of the linked list
            print("ERROR: 'Erase' Index out of range!") # Print an error message
            return None # Return None
        current_index = 0 # Set the current index to 0
        current = self.head # Set the current node to the head
        while True: # Infinite loop
            last_node = current # Set the last node to the current node
            current = current.next # Set the current node to the next node
            if current_index == index: # If the current index is equal to the index
                last_node.next = current.next # Set the next node of the last node to the next node of the current node
                return 
            current_index += 1
        
    def insert(self, index, data): # Insert a node at a specific index
        if index >= self.length(): # If the index is greater than the length of the linked list
            print("ERROR: 'Insert' Index out of range!") # Print an error message
            return 
        if index < 0: # If the index is less than 0
            print("ERROR: 'Insert' Index out of range!") # Print an error message
            return
        new_node = Node(data) # Create a new node with the data
        current_index = 0 # Set the current index to 0
        current = self.head # Set the current node to the head
        while True: # Infinite loop
            last_node = current # Set the last node to the current node
            current = current.next # Set the current node to the next node
            if current_index == index: # If the current index is equal to the index
                last_node.next = new_node # Set the next node of the last node to the new node
                new_node.next = current # Set the next node of the new node to the current node
                return 
            current_index += 1 # Increment the current index