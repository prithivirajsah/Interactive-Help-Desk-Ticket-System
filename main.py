from ticket import Ticket
from data_structures import LinkedList, Stack, Queue, PriorityQueue
from dashboard import generate_dashboard

# Week 2: Recursive function for dependency check
def check_dependency(ticket, all_tickets):
    if not ticket.parent:
        return ticket.status == "closed"
    parent_ticket = next((t for t in all_tickets if t.ticket_id == ticket.parent), None)
    if not parent_ticket:
        return True
    if parent_ticket.status != "closed":
        return False
    return check_dependency(parent_ticket, all_tickets)

def get_valid_priority():
    while True:
        priority = input("Priority (normal/high): ").lower().strip()
        if priority in ["normal", "high"]:
            return priority
        print("❌ Invalid priority. Please enter 'normal' or 'high'.")

def get_valid_parent_id():
    while True:
        parent = input("Parent ticket ID (optional, press Enter to skip): ").strip()
        if not parent:
            return None
        if parent.isdigit():
            return int(parent)
        print("❌ Invalid ticket ID. Please enter a number or press Enter to skip.")

def get_valid_ticket_id(tickets):
    while True:
        try:
            ticket_id = int(input("Enter ticket ID: "))
            if any(t.ticket_id == ticket_id for t in tickets):
                return ticket_id
            print("❌ Ticket ID not found. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def main():
    tickets = []
    history = LinkedList()
    undo_stack = Stack()
    normal_queue = Queue()
    priority_queue = PriorityQueue()

    ticket_counter = 1

    print("🚀 Welcome to the Help Desk Ticket System!")
    print("This system demonstrates various data structures and algorithms.")

    while True:
        print("\n" + "="*50)
        print("🎫 HELP DESK TICKET SYSTEM")
        print("="*50)
        print("1. 📝 Create Ticket")
        print("2. ⚡ Process Next Ticket")
        print("3. ✅ Close Ticket")
        print("4. 🔄 Undo Last Action")
        print("5. 📊 Show Dashboard")
        print("6. 📜 Show History (Linked List)")
        print("7. 👤 Assign Agent to Ticket")
        print("8. 📋 Show Queue Status")
        print("0. 🚪 Exit")
        print("="*50)

        choice = input("Enter your choice (0-8): ").strip()

        if choice == "1":
            print("\n📝 CREATING NEW TICKET")
            print("-" * 30)
            
            title = input("Enter ticket title: ").strip()
            if not title:
                print("❌ Title cannot be empty.")
                continue
                
            description = input("Enter ticket description: ").strip()
            priority = get_valid_priority()
            parent = get_valid_parent_id()
            
            # Check if parent ticket exists
            if parent and not any(t.ticket_id == parent for t in tickets):
                print(f"❌ Parent ticket {parent} does not exist.")
                continue

            ticket = Ticket(ticket_counter, title, description, priority, parent)
            tickets.append(ticket)
            history.append(ticket)

            if priority == "high":
                priority_queue.enqueue(ticket)
                print(f"🔴 High priority ticket added to priority queue")
            else:
                normal_queue.enqueue(ticket)
                print(f"🟡 Normal priority ticket added to standard queue")

            undo_stack.push(("create", ticket))
            print(f"✅ Ticket {ticket_counter} created successfully!")
            print(f"   Title: {title}")
            print(f"   Priority: {priority}")
            print(f"   Parent: {parent if parent else 'None'}")
            ticket_counter += 1

        elif choice == "2":
            print("\n⚡ PROCESSING NEXT TICKET")
            print("-" * 30)
            
            if not priority_queue.is_empty():
                t = priority_queue.dequeue()
                print(f"🔴 Processing HIGH PRIORITY ticket:")
            elif not normal_queue.is_empty():
                t = normal_queue.dequeue()
                print(f"🟡 Processing NORMAL PRIORITY ticket:")
            else:
                print("❌ No tickets to process.")
                continue
                
            print(f"   ID: {t.ticket_id}")
            print(f"   Title: {t.title}")
            print(f"   Description: {t.description}")
            print(f"   Assigned to: {t.assigned_agent}")
            print(f"   Status: {t.status}")
            
            # Check dependencies
            if t.parent:
                parent_ticket = next((pt for pt in tickets if pt.ticket_id == t.parent), None)
                if parent_ticket and parent_ticket.status != "closed":
                    print(f"⚠️  Warning: Parent ticket {t.parent} is still open")

        elif choice == "3":
            print("\n✅ CLOSING TICKET")
            print("-" * 30)
            
            if not tickets:
                print("❌ No tickets exist to close.")
                continue
                
            ticket_id = get_valid_ticket_id(tickets)
            ticket = next((t for t in tickets if t.ticket_id == ticket_id), None)
            
            if ticket.status == "closed":
                print(f"❌ Ticket {ticket_id} is already closed.")
                continue
                
            if check_dependency(ticket, tickets):
                ticket.update_status("closed")
                undo_stack.push(("close", ticket))
                print(f"✅ Ticket {ticket_id} closed successfully!")
            else:
                print("❌ Cannot close ticket until parent is resolved.")
                parent_ticket = next((t for t in tickets if t.ticket_id == ticket.parent), None)
                if parent_ticket:
                    print(f"   Parent ticket {ticket.parent} status: {parent_ticket.status}")

        elif choice == "4":  # Undo feature
            print("\n🔄 UNDO LAST ACTION")
            print("-" * 30)
            
            if undo_stack.is_empty():
                print("❌ Nothing to undo.")
                continue
                
            action = undo_stack.peek()
            print(f"Last action: {action[0]} ticket {action[1].ticket_id}")
            
            confirm = input("Undo this action? (y/n): ").lower().strip()
            if confirm == 'y':
                action = undo_stack.pop()
                act, ticket = action
                if act == "create":
                    tickets.remove(ticket)
                    # Remove from appropriate queue
                    if ticket.priority == "high":
                        try:
                            priority_queue.queue.remove(ticket)
                        except ValueError:
                            pass
                    else:
                        try:
                            normal_queue.queue.remove(ticket)
                        except ValueError:
                            pass
                    print(f"🔄 Undo: Removed Ticket {ticket.ticket_id}")
                elif act == "close":
                    ticket.update_status("open")
                    print(f"🔄 Undo: Reopened Ticket {ticket.ticket_id}")
            else:
                print("Undo cancelled.")

        elif choice == "5":
            generate_dashboard(tickets)

        elif choice == "6":
            print("\n📜 TICKET HISTORY (Linked List)")
            print("-" * 40)
            history.display()

        elif choice == "7":
            print("\n👤 ASSIGN AGENT TO TICKET")
            print("-" * 30)
            
            if not tickets:
                print("❌ No tickets exist to assign.")
                continue
                
            ticket_id = get_valid_ticket_id(tickets)
            ticket = next((t for t in tickets if t.ticket_id == ticket_id), None)
            
            if ticket.status == "closed":
                print(f"❌ Cannot assign agent to closed ticket {ticket_id}.")
                continue
                
            agent = input("Enter agent name: ").strip()
            if agent:
                ticket.assign_agent(agent)
                undo_stack.push(("assign_agent", ticket, ticket.assigned_agent))
                print(f"✅ Agent '{agent}' assigned to ticket {ticket_id}")
            else:
                print("❌ Agent name cannot be empty.")

        elif choice == "8":
            print("\n📋 QUEUE STATUS")
            print("-" * 20)
            print(f"🔴 Priority Queue: {priority_queue.size()} tickets")
            print(f"🟡 Normal Queue: {normal_queue.size()} tickets")
            print(f"📚 Undo Stack: {len(undo_stack.stack)} actions")
            
            if not priority_queue.is_empty():
                print(f"\nNext high priority: {priority_queue.peek()}")
            if not normal_queue.is_empty():
                print(f"Next normal priority: {normal_queue.peek()}")

        elif choice == "0":
            print("\n👋 Thank you for using the Help Desk Ticket System!")
            print("This system demonstrated:")
            print("   • Lists & Matrices (Week 1)")
            print("   • Recursion (Week 2)")
            print("   • Functions & Loops (Week 3)")
            print("   • Linked Lists (Week 4)")
            print("   • Stacks & Queues (Week 5)")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 0-8.")

if __name__ == "__main__":
    main()