# 🎫 Interactive Help Desk Ticket System

A comprehensive command-line application that demonstrates various data structures and algorithms through a practical help desk ticket management system.

## 📋 Weekly Requirements Implementation

### 1: Lists & Matrices ✅
- **Dashboard Analytics**: 2D list implementation showing ticket statistics
- **Features**: Open vs. closed counts, priority breakdowns, agent workload
- **File**: `dashboard.py` - Generates comprehensive ticket analytics

### 2: Recursion ✅
- **Dependency Checking**: Recursive function to verify ticket dependencies
- **Features**: Ensures parent tickets are resolved before closing child tickets
- **File**: `main.py` - `check_dependency()` function

### 3: Functions & Loops ✅
- **Main Application**: Interactive menu system with input handling loops
- **Features**: User input validation, error handling, continuous operation
- **File**: `main.py` - Main application loop and helper functions

### 4: Linked Lists ✅
- **Ticket History**: Chronological storage of all tickets in linked list
- **Features**: Complete audit trail, ticket lookup by ID
- **File**: `data_structures.py` - `LinkedList` class

### 5: Stacks & Queues ✅
- **Queue**: Standard-priority tickets (FIFO processing)
- **Priority Queue**: High-priority tickets (processed first)
- **Stack**: Undo feature to revert last actions
- **File**: `data_structures.py` - `Queue`, `PriorityQueue`, `Stack` classes

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Running the System

1. **Interactive Mode** (Full application):
   ```bash
   python main.py
   ```

2. **Test Mode** (Verify weekly requirements):
   ```bash
   python test_system.py
   ```

## 🎯 System Features

### Core Functionality
- ✅ Create tickets with descriptions and priorities
- ✅ Process tickets based on priority (high priority first)
- ✅ Close tickets with dependency validation
- ✅ Assign agents to tickets
- ✅ Undo last actions (create, close, assign)
- ✅ Comprehensive dashboard with statistics
- ✅ Complete ticket history tracking

### Data Structures Used
- **Lists**: Ticket storage and 2D matrix for analytics
- **Linked Lists**: Chronological ticket history
- **Stacks**: Undo functionality
- **Queues**: Normal priority ticket processing
- **Priority Queues**: High priority ticket processing

### Advanced Features
- **Dependency Management**: Parent-child ticket relationships
- **Recursive Validation**: Ensures proper ticket closure order
- **Input Validation**: Robust error handling and user input validation
- **Real-time Statistics**: Live dashboard updates
- **Audit Trail**: Complete history of all system actions

## 📊 Dashboard Features

The analytics dashboard provides:
- Total ticket counts and resolution rates
- Priority breakdown (high vs. normal)
- Agent workload distribution
- Recent activity tracking
- Visual indicators for ticket status and priority

## 🔄 Undo System

The undo feature supports:
- **Create Actions**: Remove created tickets
- **Close Actions**: Reopen closed tickets
- **Agent Assignment**: Revert agent changes
- **Confirmation**: User confirmation before undoing

## 🧪 Testing

Run the test suite to verify all weekly requirements:
```bash
python test_system.py
```

This will test:
- Lists & matrices functionality
- Recursive dependency checking
- Functions and loops
- Linked list operations
- Stack and queue operations

## 📁 File Structure

```
helpdesk_system/
├── main.py              # Main application and menu system
├── ticket.py            # Ticket class definition
├── data_structures.py   # All data structure implementations
├── dashboard.py         # Analytics and dashboard generation
├── test_system.py       # Weekly requirements testing
└── README.md           # This documentation
```

## 💡 Usage Examples

### Creating a Ticket
1. Choose option 1 from the main menu
2. Enter ticket title and description
3. Select priority (normal/high)
4. Optionally specify parent ticket ID
5. Ticket is automatically added to appropriate queue

### Processing Tickets
1. Choose option 2 to process next ticket
2. High priority tickets are processed first
3. System shows ticket details and dependency warnings

### Managing Dependencies
- Create parent tickets first
- Child tickets cannot be closed until parent is resolved
- Recursive dependency checking ensures proper order

## 🎓 Learning Objectives

This system demonstrates:
- **Data Structure Implementation**: Custom implementations of linked lists, stacks, and queues
- **Algorithm Design**: Recursive functions and efficient data processing
- **Software Engineering**: Input validation, error handling, and user experience
- **System Design**: Modular architecture with clear separation of concerns

## 🔧 Customization

The system is designed to be easily extensible:
- Add new ticket fields in `ticket.py`
- Implement new data structures in `data_structures.py`
- Enhance dashboard analytics in `dashboard.py`
- Add new menu options in `main.py`

## 📝 Notes

- All data is stored in memory (no persistence)
- System resets when restarted
- Designed for educational demonstration of data structures
- Production use would require database integration

## 🤝 Contributing

This is an educational project demonstrating weekly programming concepts. Feel free to:
- Add new features
- Improve existing functionality
- Enhance the user interface
- Add more comprehensive testing

---

**Happy Coding! 🚀**
