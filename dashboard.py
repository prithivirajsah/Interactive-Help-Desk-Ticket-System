def generate_dashboard(tickets):
    if not tickets:
        print("\n📊 Ticket Dashboard")
        print("No tickets found.")
        return
    
    # 2D List: [[status, priority, assigned_agent]]
    data = [[t.status, t.priority, t.assigned_agent] for t in tickets]

    # Basic counts
    open_count = sum(1 for row in data if row[0] == "open")
    closed_count = sum(1 for row in data if row[0] == "closed")
    high_priority = sum(1 for row in data if row[1] == "high")
    normal_priority = sum(1 for row in data if row[1] == "normal")
    
    # Agent statistics
    agent_stats = {}
    for row in data:
        agent = row[2]
        if agent not in agent_stats:
            agent_stats[agent] = {"open": 0, "closed": 0}
        if row[0] == "open":
            agent_stats[agent]["open"] += 1
        else:
            agent_stats[agent]["closed"] += 1

    print("\n" + "="*50)
    print("📊 TICKET DASHBOARD")
    print("="*50)
    
    # Overall statistics
    print(f"\n📈 OVERALL STATISTICS:")
    print(f"   Total Tickets: {len(tickets)}")
    print(f"   Open Tickets: {open_count}")
    print(f"   Closed Tickets: {closed_count}")
    print(f"   Resolution Rate: {(closed_count/len(tickets)*100):.1f}%" if tickets else "0%")
    
    # Priority breakdown
    print(f"\n🎯 PRIORITY BREAKDOWN:")
    print(f"   High Priority: {high_priority}")
    print(f"   Normal Priority: {normal_priority}")
    
    # Agent workload
    print(f"\n👥 AGENT WORKLOAD:")
    for agent, stats in agent_stats.items():
        total = stats["open"] + stats["closed"]
        print(f"   {agent}: {stats['open']} open, {stats['closed']} closed (Total: {total})")
    
    # Recent activity (last 5 tickets)
    print(f"\n🕒 RECENT ACTIVITY:")
    recent_tickets = sorted(tickets, key=lambda x: x.updated_at, reverse=True)[:5]
    for ticket in recent_tickets:
        status_icon = "🟢" if ticket.status == "open" else "🔴"
        priority_icon = "🔴" if ticket.priority == "high" else "🟡"
        print(f"   {status_icon} {priority_icon} [{ticket.ticket_id}] {ticket.title}")
    
    print("="*50)