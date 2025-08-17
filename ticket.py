from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, title, description="", priority="normal", parent=None, assigned_agent="Unassigned"):
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.priority = priority  # "normal" or "high"
        self.status = "open"
        self.parent = parent  # for recursion check
        self.assigned_agent = assigned_agent
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"[{self.ticket_id}] {self.title} ({self.priority}) - {self.status} - {self.assigned_agent}"
    
    def update_status(self, new_status):
        self.status = new_status
        self.updated_at = datetime.now()
    
    def assign_agent(self, agent_name):
        self.assigned_agent = agent_name
        self.updated_at = datetime.now()