class Dequeue:

    def __init__(self):
        self.dequeue = []

    def display_dequeue(self):
        print(self.dequeue)

    def insert_front(self,element):
        self.dequeue.insert(0,element)

    def insert_rear(self,element):
        self.dequeue.append(element)

    def is_empty(self):
        return True if len(self.dequeue)==0 else False

    def remove_first(self):
        return None  if self.is_empty() else self.dequeue.pop(0)

    def remove_last(self):
        return None  if self.is_empty() else self.dequeue.pop()

dq = Dequeue()
element = None
def menus():
    while True:
        print("1. Insert Element at the Front")
        print("2. Insert Element at the Rear")
        print("3. Delete Element at the front")
        print("4. Delete Element at the Rear")
        print("5. Exit")
        choice = int(input("Enter a choice: "))
        if choice == 1:
            print("\n Inserting Element at the front...\n")
            element = input("Enter the element to be inserted:")
            dq.insert_front(element)
            dq.display_dequeue()
        elif choice == 2:
            print("\n Inserting Element at the Rear...\n")
            element = input("Enter the element to be inserted:")
            dq.insert_rear(element)
            dq.display_dequeue()
        elif choice == 3:
            print("\n Deleting Element at the front...\n")
            dq.remove_first()
            dq.display_dequeue()
        elif choice == 4:
            print("\n Deleting Element at the rear...\n")
            dq.remove_last()
            dq.display_dequeue()
        elif choice == 5:
            break;
        else:
            print("Enter a valid choice")
menus()