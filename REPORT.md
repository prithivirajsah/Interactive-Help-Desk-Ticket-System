## Help Desk Ticket System — Final Report

### Introduction
Modern service organizations depend on disciplined ticket management to deliver responsive, transparent, and reliable support. This project implements an interactive Help Desk Ticket System as a command-line application, designed not only to be functional but also to illustrate foundational data structures and algorithms. The system models real operational needs—ticket creation, priority triage, assignment, dependency validation, and history tracking—while explicitly demonstrating lists, matrices, linked lists, stacks, queues, and recursion.

The implementation is intentionally lightweight and dependency-free, using Python’s standard library to prioritize clarity and educational value. Core modules encapsulate distinct concerns:
- `ticket.py` defines the domain model (`Ticket`) with metadata and mutators.
- `data_structures.py` contains clean, readable implementations of `LinkedList`, `Stack`, `Queue`, and a simple `PriorityQueue`.
- `dashboard.py` derives analytics from a 2D list representation of tickets to present totals, priority breakdowns, agent workload, and recent activity.
- `main.py` orchestrates interactive workflows, input validation, recursive dependency checks, and queue/undo coordination.
- `test_system.py` demonstrates weekly requirements and validates expected behaviors.

The result is a cohesive, modular system that supports interactive use and scripted demonstrations, enabling learners to connect theoretical CS concepts to a practical support scenario.

### Aims and Objectives
The project aims to build a practical yet pedagogical help desk ticketing solution that showcases core CS fundamentals through a realistic workflow.

- Educational objectives:
  - Demonstrate correct, readable implementations of key data structures:
    - Linked list for chronological ticket history
    - Stack for undo functionality
    - Queue for normal-priority ticket processing (FIFO)
    - Priority-aware queue for urgent tasks
  - Implement recursion to enforce hierarchical ticket dependency rules (parent tickets must be closed before children).
  - Provide a robust CLI with loops, helper functions, and input validation.
  - Generate real-time dashboard analytics using a 2D list snapshot of tickets.
  - Maintain a modular architecture for clarity and future extension.
  - Supply a test harness to validate and illustrate features by milestone.

- Functional objectives:
  - Create, process, close, and assign tickets with explicit priority and optional parent-child relationships.
  - Enforce dependency constraints on closure via a recursive check.
  - Maintain a full audit/history using a linked list.
  - Support undo for key operations to recover from mistakes.
  - Present live metrics: totals, open/closed counts, priorities, workloads, and recent activity.

### Expected Outcomes and Deliverables
- Functioning CLI application featuring:
  - Ticket creation with title, description, priority, and optional parent ID
  - Priority-aware processing (high before normal)
  - Recursive dependency validation prior to closure
  - Agent assignment workflow
  - Undo for creation and closure operations
  - Dashboard analytics with recent activity
  - Linked-list-based history display
- Modular codebase:
  - `ticket.py`, `data_structures.py`, `dashboard.py`, `main.py`, `test_system.py`, `README.md`
- Test script (`test_system.py`) demonstrating weekly requirements:
  - Lists & matrices (2D analytics)
  - Recursion (dependency checks)
  - Functions & loops (CLI and validation)
  - Linked lists (history)
  - Stacks & queues (undo, FIFO, priority)
- Documentation: `README.md` with usage instructions, learning objectives, and system overview.
- This report with methodology, risks and mitigations, milestones, tools, and screenshot placeholders.

### Project Risks, Threats, and Contingency Plans
- Input validation risks (invalid IDs, priority typos)
  - Contingency: Centralize validation (`get_valid_priority`, `get_valid_parent_id`, `get_valid_ticket_id`) and loop until valid entries are provided; guard conversions with try/except.
- Dependency rule violations (closing child before parent)
  - Contingency: Enforce via `check_dependency` recursion that traverses parent chains; demonstrate outcomes in `test_week2_recursion`.
- Priority handling errors (processing order incorrect)
  - Contingency: Distinct `PriorityQueue` abstraction and explicit tests showing enqueue/dequeue effects and order guarantees.
- Undo inconsistencies (queues/history out-of-sync)
  - Contingency: On undo of create, defensively remove from the correct queue; on undo of close, reopen ticket. Keep actions atomic and visible.
- Stateless runtime (no persistence across sessions)
  - Contingency: Clearly scope as educational; document an upgrade path to JSON/SQLite persistence if needed.
- Console-only dashboard may be perceived as limited
  - Contingency: Provide structured, readable output and instructions for capturing screenshots; document potential future visualization (matplotlib, web UI).

### Methodology
- Requirements mapping:
  - Model real help desk tasks: creation, triage, assignment, dependency enforcement, audit trail, and undo.
  - Align weekly academic themes with cohesive features for a single integrated application.

- Architecture and modules:
  - Domain model (`ticket.py`): stores identifiers, content, status, priority, agent, timestamps; provides `update_status` and `assign_agent` for controlled state changes.
  - Data structures (`data_structures.py`):
    - `LinkedList` with a `Node` type, `append`, `display`, and `get_ticket_by_id`
    - `Stack` with `push`, `pop`, `peek`, `is_empty`
    - `Queue` and `PriorityQueue` with `enqueue`, `dequeue`, `peek`, and `size`
  - Application logic (`main.py`): interactive menu, input helpers, dependency check, and coordination between queues, undo stack, and history list.
  - Analytics (`dashboard.py`): construct a 2D list snapshot `[[status, priority, assigned_agent], ...]` and compute totals, resolution rate, priority distribution, per-agent workload, and recent activity.
  - Tests (`test_system.py`): runnable demonstrations for each weekly theme, showing outputs and order of operations.

- Algorithmic decisions:
  - Recursion for dependency validation is succinct and ensures correctness by climbing parent references until it reaches a root or a non-closed ancestor.
  - Priority queue implemented via list insertion keeps code minimal and readable for educational purposes while ensuring urgent tickets are handled first.
  - Linked list emphasizes pointer traversal and ordered history without over-engineering.
  - Stack captures LIFO semantics for undo, which maps naturally to the user mental model.

- User experience and ergonomics:
  - Clear, consistent menu with numbered options and separators for readability.
  - Friendly error messages and reprompts for invalid input.
  - Non-disruptive dashboard access and informative summaries on exit.

- Validation approach:
  - Combination of scripted tests and manual runs. Tests illustrate typical sequences and edge cases; manual runs encourage exploration (multiple tickets, nested dependencies, different priorities).

### Resource Requirements
- Runtime: Python 3.6+ (no external dependencies)
- Hardware: Any modern computer capable of running Python (macOS, Windows, Linux)
- Software: Terminal/shell, text editor/IDE (Cursor, VS Code, PyCharm), optional Git
- Skills: Basic Python proficiency and familiarity with data structures and CLI workflows
- Time: ~1–2 weeks for implementation and documentation, with optional extensions for persistence and richer dashboards

### Work Breakdown Structure / Milestones
- Milestone 1: Project setup and domain model (Day 1–2)
  - Initialize repository
  - Implement `Ticket` with attributes and mutators
  - Establish coding conventions, docstrings, and module boundaries
- Milestone 2: Data structures (Day 2–3)
  - Implement `LinkedList` and `Node`
  - Implement `Stack`, `Queue`, `PriorityQueue`
  - Sanity tests for core operations (append, push/pop, enqueue/dequeue)
- Milestone 3: CLI and validation (Day 3–5)
  - Build menu loop and helper functions for validation
  - Implement ticket creation, enqueue by priority, and history append
- Milestone 4: Processing and dependencies (Day 5–6)
  - Implement next-ticket processing and detail display
  - Implement and enforce `check_dependency` recursion for closures
- Milestone 5: Undo and assignment (Day 6–7)
  - Implement undo for create and close
  - Add agent assignment with validation and bookkeeping
- Milestone 6: Dashboard and analytics (Day 7–8)
  - Implement 2D list analytics; compute counts, resolution rate, workloads
  - Add recent activity ordered by `updated_at`
- Milestone 7: Tests and documentation (Day 8–9)
  - Implement `test_system.py` demonstrations
  - Write `README.md` for usage and learning objectives
- Milestone 8: Review and polish (Day 9–10)
  - Manual QA, edge cases, and documentation review
  - Prepare report and capture screenshots

### Tools and Technologies Used
- Language: Python 3.6+
- Standard library only (no third-party dependencies)
- Terminal-based interface for portability and focus
- Git for version control (optional but recommended)
- Editor/IDE: Cursor or any Python-aware editor
- Testing: Custom demonstration script `test_system.py`

### Dashboard (Images & screenshots of all pages made, with captions, descriptions, and proper formatting)
Replace the `src` paths with your own screenshot files after capturing the terminal output. Suggested location: `docs/images/`.

- How to capture:
  - Run `python main.py` and navigate to each feature.
  - On macOS: Shift+Cmd+4 to capture the relevant terminal area.
  - Save files with descriptive names and consistent dimensions for readability.

- Figure 1: Main Menu
  - Description: Initial interface listing all available operations.
  - Screenshot: ![Main menu](docs/images/main_menu.png)
  - Caption: Figure 1. Main menu of the Help Desk Ticket System showing core actions.

- Figure 2: Creating a Ticket
  - Description: Prompts for title, description, priority, and optional parent; enqueues accordingly.
  - Screenshot: ![Create ticket](docs/images/create_ticket.png)
  - Caption: Figure 2. Ticket creation flow with validation and queue placement.

- Figure 3: Processing Next Ticket
  - Description: Priority-aware processing; high-priority items are dequeued first.
  - Screenshot: ![Process ticket](docs/images/process_next_ticket.png)
  - Caption: Figure 3. Processing the next available ticket with priority and dependency cues.

- Figure 4: Closing a Ticket with Dependency Check
  - Description: Validates recursively whether all ancestors are closed before allowing closure.
  - Screenshot: ![Close ticket](docs/images/close_ticket_dependency.png)
  - Caption: Figure 4. Attempting to close a child ticket triggers recursive dependency checks.

- Figure 5: Undo Last Action
  - Description: Shows the top of the undo stack; supports undoing create and close actions.
  - Screenshot: ![Undo action](docs/images/undo_last_action.png)
  - Caption: Figure 5. Undoing the most recent action to recover from user error.

- Figure 6: Assign Agent to Ticket
  - Description: Assigns an agent to an open ticket and records the change.
  - Screenshot: ![Assign agent](docs/images/assign_agent.png)
  - Caption: Figure 6. Assigning an agent for ownership and workload tracking.

- Figure 7: Show Dashboard
  - Description: Displays totals, priority breakdown, agent workloads, and recent activity.
  - Screenshot: ![Dashboard](docs/images/dashboard_overview.png)
  - Caption: Figure 7. Dashboard metrics derived from a 2D list snapshot.

- Figure 8: Ticket History (Linked List)
  - Description: Chronological history traversal via singly linked list.
  - Screenshot: ![Linked list history](docs/images/history_linked_list.png)
  - Caption: Figure 8. Ticket history maintained as a linked list.

- Figure 9: Queue Status
  - Description: Queue sizes, peeked next items, and undo stack size.
  - Screenshot: ![Queue status](docs/images/queue_status.png)
  - Caption: Figure 9. Overview of queue metrics and next-in-line tickets.

- Figure 10: Exit Summary
  - Description: Summary of educational focus areas shown upon exit.
  - Screenshot: ![Exit summary](docs/images/exit_summary.png)
  - Caption: Figure 10. Exit screen summarizing featured data structures.

### Conclusion
This Help Desk Ticket System fulfills its dual role as a practical CLI workflow and a didactic showcase of data structures and algorithms. The codebase intentionally favors clarity over complexity: a simple `PriorityQueue` implementation, a readable recursion for dependency checks, and a straightforward `LinkedList` for history make the system approachable for learners while remaining useful for scenario-based demonstrations. The CLI promotes discoverability through numbered options and consistent prompts, while analytics offer immediate feedback about system state.

Though intentionally minimal in scope, the architecture invites extensions. Adding persistence (e.g., JSON files or SQLite) would enable durable sessions and reporting over time. A richer dashboard—potentially with charts—or a web interface could broaden stakeholder appeal and interactivity. Role-based access control and SLA tracking could further align the system with production environments. These enhancements can be added incrementally thanks to the current modular design without disrupting the educational clarity of the core features.

Overall, the project demonstrates how foundational CS concepts—lists, matrices, linked lists, stacks, queues, and recursion—map directly to real-world problem solving in support operations. The result is a cohesive, testable, and extensible learning artifact that balances correctness, readability, and practical relevance.

---

Appendix: Running and Testing
- Interactive mode: `python main.py`
- Test demonstrations: `python test_system.py`
- Code structure:
  - `main.py` — menu and orchestration
  - `ticket.py` — domain model
  - `data_structures.py` — linked list, stack, queue, priority queue
  - `dashboard.py` — analytics and dashboard
  - `test_system.py` — milestone demonstrations

Word count note: This report targets approximately 2,500 words (excluding figures and any future references), with emphasis on clarity and alignment to the implemented system.
