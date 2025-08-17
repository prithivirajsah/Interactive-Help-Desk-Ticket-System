# Linked List Node
class Node:
    def __init__(self, ticket):
        self.ticket = ticket
        self.next = None

# Linked List for chronological history
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, ticket):
        new_node = Node(ticket)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        if not temp:
            print("No tickets in history.")
            return
        while temp:
            print(temp.ticket)
            temp = temp.next
    
    def get_ticket_by_id(self, ticket_id):
        temp = self.head
        while temp:
            if temp.ticket.ticket_id == ticket_id:
                return temp.ticket
            temp = temp.next
        return None


# Stack for undo feature
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None


# Queue for normal priority
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, ticket):
        self.queue.append(ticket)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if self.queue:
            return self.queue[0]
        return None


# Priority Queue for high-priority tickets
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, ticket):
        # High priority tickets go to the front
        if ticket.priority == "high":
            self.queue.insert(0, ticket)
        else:
            self.queue.append(ticket)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if self.queue:
            return self.queue[0]
        return None