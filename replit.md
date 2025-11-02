# Mini-CRM System

## Overview

A Customer Relationship Management (CRM) system built with Python, demonstrating Object-Oriented Programming (OOP) principles. The system manages leads through various stages of the sales pipeline, from initial contact to conversion or loss. The application stores lead data in JSON format and provides search, listing, and CSV export capabilities.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Design Pattern

The system uses a **layered architecture** with clear separation of concerns:

1. **Model Layer** (`models.py`) - Domain objects using inheritance and polymorphism
2. **Repository Layer** (`repository.py`) - Data persistence abstraction
3. **Application Layer** (`crm_app.py`) - Business logic and user interaction

**Rationale**: This separation allows the domain logic to remain independent of storage mechanisms and user interfaces. Changes to data storage (e.g., switching from JSON to a database) would only require modifying the repository layer.

### Object-Oriented Design

**Inheritance Hierarchy**:
```
Contact (base class)
├── Lead (specialized contact with sales stage)
└── Customer (specialized contact with purchase history)
```

**Rationale**: The `Contact` base class provides common attributes (name, company, email, created date) and behaviors (validation, display formatting) shared by all contact types. `Lead` and `Customer` extend this with specialized attributes and override methods polymorphically.

**Polymorphism**: Methods like `to_dict()` and `get_display_info()` are overridden in child classes to include type-specific data while maintaining a consistent interface.

**Alternative Considered**: A single `Contact` class with type flags was considered but rejected because it would require conditional logic throughout the codebase and violate the Open/Closed Principle.

### Data Persistence Strategy

**Chosen Solution**: JSON file-based storage with in-memory operations

- Data stored in `data/leads.json`
- Full file read/write for each operation
- Simple dictionary serialization using `to_dict()` methods

**Rationale**: 
- **Pros**: Simple implementation, no external dependencies, human-readable data format, suitable for small datasets
- **Cons**: Not suitable for high-volume operations, no concurrent access control, entire dataset loaded into memory

**Alternative Considered**: SQLite database was considered but rejected to minimize dependencies and keep the codebase focused on OOP concepts rather than database management.

### Application State Management

**Encapsulation**: The `CRMApp` class encapsulates the application state and menu flow, holding a reference to the `LeadRepository` and managing the main event loop.

**Rationale**: This design isolates UI logic from business logic and data access, making it easier to add alternative interfaces (web, API) in the future.

### Stage Management

**Approach**: Predefined stage constants in the `Lead` class with validation

```python
STAGES = ["novo", "contatado", "qualificado", "convertido", "perdido"]
```

**Rationale**: Using class-level constants ensures consistency and prevents invalid stage values. The validation in `__init__` provides a fail-safe default ("novo") for invalid inputs.

### Search Implementation

**Linear Search**: Simple substring matching across name, company, and email fields

**Rationale**: 
- **Pros**: Simple to implement, works for small datasets, case-insensitive
- **Cons**: O(n) complexity, no fuzzy matching, no ranking

**Alternative for Future**: Could implement indexing or use a search library like Whoosh for larger datasets.

## External Dependencies

### Standard Library Only

The application uses only Python standard library modules:

- `json` - JSON serialization/deserialization for data persistence
- `csv` - CSV export functionality
- `datetime` - Timestamp management for lead creation dates
- `pathlib` - Cross-platform file path handling
- `typing` - Type hints for better code documentation

**Rationale**: Avoiding external dependencies keeps the project simple, portable, and easy to deploy. This is appropriate for an educational project demonstrating OOP concepts.

### File System Structure

```
project_root/
├── data/
│   ├── leads.json (runtime-generated)
│   └── leads.csv (export-generated)
├── models.py
├── repository.py
├── crm_app.py
└── main.py
```

**Data Directory**: Automatically created at runtime if it doesn't exist, using `Path.mkdir(exist_ok=True)`.

### No External Services

The system operates entirely locally with no:
- Database servers
- Web APIs
- Cloud services
- Authentication providers

This makes it ideal for learning and development without infrastructure dependencies.