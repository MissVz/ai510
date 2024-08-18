"""shopping_list.py

This assignment is to gain knowledge on Stack and Recursive functions.
A shopping list using Stack will be implemented for this exercise.
The program stores shopping items in both of simple array and linked list based stack.
Each storing mechanism is separated into different files, such as “simple_array_shopping_list_manager.py”
 or “linked_list_shopping_list_manager.py,” where each file contains FileNameClass classes with essential
 methods for data manipulation.
Note that “shopping_list.py” with the “main” method has already been provided (download attachment).

NOTE: You can choose either simple array approach OR linked list approach for the assignment.

"""

# file name: simple_array_shopping_list_manager.py
# class name: SimpleArrayShoppingListManagerClass
from simple_array_shopping_list_manager import SimpleArrayShoppingListManagerClass # type: ignore
# file name: linked_list_zip_list_manager.py
# class name: LinkedListZipListManagerClass
from linked_list_stack_shopping_list_manager import LinkedListStackShoppingListManagerClass # type: ignore
import time

item_list = ["apple", "banana", "milk", "bread", "butter", "cheese", "carrot", "pork", "beef", "mushroom", "fish"]

def main():
        print("\n\n------ Simple array ------")
        sa = SimpleArrayShoppingListManagerClass()

        #insert operation
        simple_array_insert_start_time = time.perf_counter()
        for i in range(len(item_list)):
                sa.insert_item(item_list[i])
        simple_array_insert_end_time = time.perf_counter()
        print("current list:\t", end = " ")
        sa.print_items()

        #time summary:
        saInsertOp = simple_array_insert_end_time - simple_array_insert_start_time
        print("-insert operation: %s\n\n" %(saInsertOp))

        print("------ Linked-List-Stack ------")
        lls = LinkedListStackShoppingListManagerClass()
        #insert operation
        linked_list_stack_insert_start_time = time.perf_counter()
        for i in range(len(item_list)):
                lls.insert_item(item_list[i])
        linked_list_stack_insert_end_time = time.perf_counter()
        print("current list:\t", end = " ")
        lls.print_items_from_top()

        print("last inserted item: \t %s" % lls.getLastItem())
        print("current list:\t", end = " ")
        lls.print_items_from_top()

        print("last removed item: \t %s" % lls.removeLastItem())
        print("current list:\t", end = " ")
        lls.print_items_from_top()

        print("current list from bottom:\t", end = " ")
        lls.print_items_from_bottom()

        #time summary:
        llInsertOp= linked_list_stack_insert_end_time - linked_list_stack_insert_start_time
        print("-insert operation: %s" %(llInsertOp))

if __name__ == "__main__":
        main()

