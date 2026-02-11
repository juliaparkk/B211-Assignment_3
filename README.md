# B211-Assignment_3
# a Which species of irises are most similar/are least similar? 
# Least similar: Setosa
Setosa separates itself in every major dimension:
- Petal length is extremely small (around 1.4–1.7 cm in your first rows), while the overall median is 4.29 cm.
- Petal width is also tiny (≈0.20–0.40 cm), compared to the overall median of 1.37 cm.
- Sepal width tends to be larger than the other species (your sample shows 3.52 cm vs. overall mean 3.08 cm).
- The strong negative correlations involving sepal width (–0.515 with petal length, –0.460 with petal width) reflect this pattern: setosa has wide sepals but very small petals.
These traits place setosa far from the other two species in the measurement space.

# Most similar: Versicolor and Virginica
Versicolor and virginica overlap heavily in the variables that show the strongest correlations:
- Petal length and width are strongly positively correlated (0.943), and both species fall on the “large petal” end of the spectrum.
- Versicolor in your sample: petal length ≈ 4.0–4.8 cm
- Virginica in your sample: petal length ≈ 5.0–5.7 cm
- Sepal length for both species is in the 5.8–6.9 cm range, close to the overall mean of 5.77 cm.
- Sepal width for both species clusters near the overall mean (≈3.0 cm).
- Because their measurements fall along the same ranges—and because the variables with the strongest correlations (petal length and width) differ only moderately between them— versicolor and virginica form a pair that is much more similar to each other than either is to setosa.

# Purpose
This project provides a clear, maintainable structure for modeling domain entities with well-defined responsibilities, attributes, and behaviors. It emphasizes readability, testability, and separation of concerns.

# Class Design and Implementation
The project follows a simple object-oriented design:
- **Data classes** hold state and simple validation.
- **Service classes** encapsulate business logic.
- **Repository classes** abstract persistence and storage concerns.
Each class is designed with a single responsibility and explicit interfaces to reduce coupling and improve maintainability.

# Classes
# `BaseEntity`
**Purpose:** Common base for all domain objects.
**Attributes**
- `id: str` — Unique identifier.
**Methods**
- `__init__(id: str)` — Initializes the entity.
- `__repr__()` — Returns a concise debug representation.

# `User`
**Purpose:** Represents an application user.
**Attributes**
- `name: str` — Display name.
- `email: str` — Unique email address.
- `is_active: bool` — Indicates whether the user is active.
**Methods**
- `activate()` — Sets `is_active` to `True`.
- `deactivate()` — Sets `is_active` to `False`.
- `update_email(new_email: str)` — Validates and updates `email`.

# `UserService`
**Purpose:** Encapsulates user-related business rules.
**Attributes**
- `repository: UserRepository` — Data access dependency.
**Methods**
- `register_user(name: str, email: str)` — Creates and persists a new user.
- `disable_user(user_id: str)` — Deactivates an existing user.

# `UserRepository`
**Purpose:** Abstracts data storage.
**Attributes**
- `storage: dict[str, User]` — In-memory storage.
**Methods**
- `save(user: User)` — Persists the user.
- `get(user_id: str)` — Retrieves a user by id.
- `delete(user_id: str)` — Removes a user.

## Limitations
- In-memory storage only; no database integration.
- Minimal validation; email format checks are basic.
- No concurrency control or transaction support.
- No role-based access control or permission checks.
