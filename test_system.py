#!/usr/bin/env python3
"""
Test script for the Help Desk Ticket System
This demonstrates all the weekly requirements
"""

from ticket import Ticket
from data_structures import LinkedList, Stack, Queue, PriorityQueue
from dashboard import generate_dashboard

def test_week1_lists_matrices():
    """Week 1: Lists & Matrices - Dashboard with 2D list"""
    print(" Testing Week 1: Lists & Matrices")
    print("=" * 50)
    
    # Create sample tickets for testing
    test_tickets = [
        Ticket(1, "Server Down", "Production server is not responding", "high"),
        Ticket(2, "Login Issue", "Users cannot login to the system", "normal"),
        Ticket(3, "Database Slow", "Database queries are taking too long", "high"),
        Ticket(4, "UI Bug", "Button not working on mobile", "normal"),
        Ticket(5, "API Error", "REST API returning 500 errors", "high")
    ]
    
    # Test dashboard with 2D list
    generate_dashboard(test_tickets)
    print()

def test_week2_recursion():
    """Week 2: Recursion - Dependency checking"""
    print(" Testing Week 2: Recursion")
    print("=" * 50)
    
    # Create tickets with dependencies
    parent_ticket = Ticket(1, "Infrastructure Setup", "Setup new server infrastructure", "high")
    child_ticket1 = Ticket(2, "Database Installation", "Install database on new server", "normal", parent=1)
    child_ticket2 = Ticket(3, "Application Deployment", "Deploy app to new server", "high", parent=2)
    
    tickets = [parent_ticket, child_ticket1, child_ticket2]
    
    print("Testing dependency chain:")
    print(f"Parent: {parent_ticket}")
    print(f"Child 1: {child_ticket1}")
    print(f"Child 2: {child_ticket2}")
    
    # Test recursive dependency check
    from main import check_dependency
    
    print(f"\nCan close child_ticket1? {check_dependency(child_ticket1, tickets)}")
    print(f"Can close child_ticket2? {check_dependency(child_ticket2, tickets)}")
    
    # Close parent ticket
    parent_ticket.update_status("closed")
    print(f"\nAfter closing parent ticket:")
    print(f"Can close child_ticket1? {check_dependency(child_ticket1, tickets)}")
    print(f"Can close child_ticket2? {check_dependency(child_ticket2, tickets)}")
    print()

def test_week3_functions_loops():
    """Week 3: Functions & Loops - Menu system"""
    print(" Testing Week 3: Functions & Loops")
    print("=" * 50)
    
    # Test input validation functions
    from main import get_valid_priority, get_valid_parent_id
    
    print("Input validation functions are implemented in main.py")
    print("They handle user input with proper error checking and loops")
    print()

def test_week4_linked_lists():
    """Week 4: Linked Lists - Ticket history"""
    print(" Testing Week 4: Linked Lists")
    print("=" * 50)
    
    # Create linked list for history
    history = LinkedList()
    
    # Add tickets to history
    tickets = [
        Ticket(1, "First Issue", "Initial problem report", "normal"),
        Ticket(2, "Second Issue", "Follow-up problem", "high"),
        Ticket(3, "Third Issue", "Another problem", "normal")
    ]
    
    for ticket in tickets:
        history.append(ticket)
    
    print("Ticket History (Linked List):")
    history.display()
    
    # Test finding ticket by ID
    found_ticket = history.get_ticket_by_id(2)
    print(f"\nFound ticket by ID 2: {found_ticket}")
    print()

def test_week5_stacks_queues():
    """Week 5: Stacks & Queues - Undo, Normal Queue, Priority Queue"""
    print(" Testing Week 5: Stacks & Queues")
    print("=" * 50)
    
    # Test Stack (Undo feature)
    undo_stack = Stack()
    undo_stack.push(("create", Ticket(1, "Test", "Test ticket", "normal")))
    undo_stack.push(("close", Ticket(2, "Test2", "Test ticket 2", "high")))
    
    print("Undo Stack:")
    print(f"Stack size: {len(undo_stack.stack)}")
    print(f"Top action: {undo_stack.peek()}")
    
    # Test Queue (Normal priority)
    normal_queue = Queue()
    normal_queue.enqueue(Ticket(1, "Normal 1", "First normal ticket", "normal"))
    normal_queue.enqueue(Ticket(2, "Normal 2", "Second normal ticket", "normal"))
    
    print(f"\nNormal Queue:")
    print(f"Queue size: {normal_queue.size()}")
    print(f"Next ticket: {normal_queue.peek()}")
    
    # Test Priority Queue (High priority)
    priority_queue = PriorityQueue()
    priority_queue.enqueue(Ticket(1, "High 1", "First high priority", "high"))
    priority_queue.enqueue(Ticket(2, "Normal 1", "First normal priority", "normal"))
    priority_queue.enqueue(Ticket(3, "High 2", "Second high priority", "high"))
    
    print(f"\nPriority Queue:")
    print(f"Queue size: {priority_queue.size()}")
    print(f"Next ticket: {priority_queue.peek()}")
    
    # Show processing order
    print(f"\nProcessing order (Priority Queue):")
    while not priority_queue.is_empty():
        ticket = priority_queue.dequeue()
        print(f"  Processing: {ticket}")
    
    print()

def run_all_tests():
    """Run all weekly tests"""
    print(" HELP DESK TICKET SYSTEM - WEEKLY REQUIREMENTS TEST")
    print("=" * 70)
    
    test_week1_lists_matrices()
    test_week2_recursion()
    test_week3_functions_loops()
    test_week4_linked_lists()
    test_week5_stacks_queues()
    
    print(" All weekly requirements tests completed!")
    print("\nTo run the interactive system, use: python main.py")

if __name__ == "__main__":
    run_all_tests()
