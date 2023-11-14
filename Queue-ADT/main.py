import time
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty: Cannot dequeue")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty: Cannot peek")
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self.front
            while current:
                print(current.data, end=" <- ")
                current = current.next
            print()

    def clear(self):
        self.reset()

    def reverse(self):
        prev = None
        current = self.front
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.front, self.rear = self.rear, self.front

# Helper functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_and_clear():
    time.sleep(2)
    clear_screen()

# Interactive Queue
queue = Queue()
clear_screen()

while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display Queue")
    print("5. Clear Queue")
    print("6. Reverse Queue")
    print("7. Check Size")
    print("8. Check if Empty")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        data = input("Enter the data to enqueue: ")
        queue.enqueue(data)
        print(f"{data} has been enqueued.")
    elif choice == '2':
        try:
            data = queue.dequeue()
            print(f"Dequeued item: {data}")
        except IndexError as e:
            print(e)
    elif choice == '3':
        try:
            data = queue.peek()
            print(f"Front item: {data}")
        except IndexError as e:
            print(e)
    elif choice == '4':
        queue.display()
    elif choice == '5':
        queue.clear()
        print("Queue has been cleared.")
    elif choice == '6':
        queue.reverse()
        print("Queue has been reversed.")
    elif choice == '7':
        print(f"Queue size: {queue.size()}")
    elif choice == '8':
        if queue.is_empty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")
    elif choice == '9':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
    
    wait_and_clear()
