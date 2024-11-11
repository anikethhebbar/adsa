#Write a program for implementing the following operations of stack S and also find the amortized cost if a sequence of n following operations are performed on a data structure:
# Push(S, x)
# Pop(S)
# Multipop(S, k) using user inputs

class Stack:
    def __init__(self):
        self.stack = []
        self.cost = 0  # Track amortized cost

    def push(self, x):
        self.stack.append(x)
        self.cost += 1  # Cost of push is 1

    def pop(self):
        if not self.is_empty():
            self.cost += 1  # Cost of pop is 1
            return self.stack.pop()
        else:
            return None

    def multipop(self, k):
        popped_elements = []
        pops = min(k, len(self.stack))  # Can't pop more than stack size
        self.cost += pops  # Cost is number of actual pops
        for _ in range(pops):
            popped_elements.append(self.pop())
        return popped_elements

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def get_amortized_cost(self):
        return self.cost

# Get user inputs
stack = Stack()
while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop") 
    print("3. Multipop")
    print("4. Print stack size")
    print("5. Print amortized cost")
    print("6. Exit")
    
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        x = int(input("Enter element to push: "))
        stack.push(x)
        print(f"Pushed {x} to stack")
    
    elif choice == 2:
        popped = stack.pop()
        if popped is not None:
            print(f"Popped element: {popped}")
        else:
            print("Stack is empty")
    
    elif choice == 3:
        k = int(input("Enter number of elements to pop: "))
        popped = stack.multipop(k)
        print(f"Popped elements: {popped}")
    
    elif choice == 4:
        print(f"Stack size: {stack.size()}")
    
    elif choice == 5:
        print(f"Amortized cost of operations: {stack.get_amortized_cost()}")
    
    elif choice == 6:
        break
    
    else:
        print("Invalid choice!")