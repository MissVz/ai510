# Declare node class
class Node:
    # Define __init__ function
    # Parameter: data for the node
    def __init__(self, data):
        # Initialize the data to the specified value
        self.data = data
        # Initialize the next node to None (empty)
        self.next = None
        #print("Node __init__()")
        
# Declare Linked List class
class LinkedListStackShoppingListManagerClass:
    # Define __init__ function
    def __init__(self):
        # Initialize the head node to None (empty)
        self.head = None
        #print("LinkedListStackShoppingListManagerClass __init__()")
        
    # Define insert_item function to insert an item on the top of the stack
    # Parameter: item to insert into the stack
    def insert_item(self, item):
        # If the stack is empty (head is None),
        # set the item to insert as the head node
        if self.head == None:
            self.head=Node(item)
        # Else
        # Create a new node with the item to insert as the data
        # Set the current head node as the new node's next node
        # Set the new node as the head node
        else:
            newnode = Node(item)
            newnode.next = self.head
            self.head = newnode
        print(f"insert_item({item})")
        
    # Define is_list_empty function to check if the stack is empty
    def is_list_empty(self):
        # Check if the head node is None
        if self.head == None:
            print(f"is_list_empty({self.head})")
        # Then return True
            return True
        # Else return False
        else:
            return False

    # Define print_item_recursive_from_top method to print the items in the
    # stack recursively from the top
    # Parameter: currentNode to print
    def print_item_recursive_from_top(self, currentNode):
        #print("print_item_recursive_from_top()")
        # Base case: if the currentNode is None, return from the recursion
        if currentNode is None:
            return
        # Else
        else:        
        # Recursive case
            # Print the currentNode's data
            print(currentNode.data, end=" ")
            # Recursive call with the next node
            self.print_item_recursive_from_top(currentNode.next)

    # Define print_items_from_top function to call the 
    # print_item_recursive_from_top function
    def print_items_from_top(self):
        # Call print_item_recursive_from_top function with the head node
        #print("print_items_from_top()")
        if self.is_list_empty():
            print("Stack Underflow")
        else:
            print("[", end=" ")
            self.print_item_recursive_from_top(self.head)
            print("]")

    # Define print_item_recursive_from_bottom method to print the items in the
    # stack recursively from the bottom
    # Parameter: currentNode to print
    def print_item_recursive_from_bottom(self, currentNode):
        #print("print_item_recursive_from_bottom()")
        # Base case: if the currentNode is None, return from the recursion
        if currentNode is None:
            return
        # Else
        else:
        # Recursive case
            # Recursive call with the next node
            self.print_item_recursive_from_bottom(currentNode.next)
            # Print the currentNode's data
            print(currentNode.data, end=" ")
            
    # Define print_items_from_bottom function to call the 
    # print_item_recursive_from_bottom function
    def print_items_from_bottom(self):
        # Call print_item_recursive_from_bottom function with the head node
        #print("print_items_from_bottom()")
        if self.is_list_empty():
            print("Stack Underflow")
        else:
            print("[", end=" ")
            self.print_item_recursive_from_bottom(self.head)
            print("]")

    # Define getLastItem function to return the last item inserted into the
    # stack (peek operation)
    def getLastItem(self):
        #print("getLastItem()")
        # Check if the stack is empty
        # Return None
        if self.is_list_empty():
            return None
        # Else
        # Return the head node's data
        else:
            return self.head.data
        

    # Define removeLastItem function to remove the last item inserted into the
    # stack (pop operation)
    def removeLastItem(self):
        #print("removeLastItem()")
        # Check if the stack is empty
        # Then Return None
        if self.is_list_empty():
            return None
        # Else
        else:
            # Define the node to "pop" as the head node
            popped_node = self.head
            # Set the head node to the current head node's next node
            self.head = self.head.next
            # Set the popped node's next pointer to None
            popped_node.next = None
            # Return the popped node's data
            return popped_node.data