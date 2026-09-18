# OOP, SOLID & Design Patterns

`Weeks 14–17` · Low Level Design

## SOLID

```mermaid
graph TB
    S["S — Single Responsibility<br/>one reason to change"]
    O["O — Open/Closed<br/>open to extend, closed to modify"]
    L["L — Liskov Substitution<br/>a subtype must be usable as its base"]
    I["I — Interface Segregation<br/>many small interfaces > one fat one"]
    D["D — Dependency Inversion<br/>depend on ABSTRACTIONS, not concretions"]
```

### Liskov — the classic Rectangle/Square failure

```
  class Rectangle:  setWidth(w), setHeight(h)
  class Square(Rectangle):  setWidth also sets height  ← "a square IS a rectangle"

  def test(r: Rectangle):
      r.setWidth(5); r.setHeight(4)
      assert r.area() == 20        ✓ Rectangle
                                   ✗ Square gives 16

  → Square is NOT substitutable → inheritance was the wrong tool.
    Composition would have avoided it.
```

### Dependency Inversion in practice

```mermaid
graph LR
    subgraph Bad["VIOLATION"]
        A1[OrderService] -->|new MySQLRepo| B1[MySQLRepository]
    end
    subgraph Good["INVERTED"]
        A2[OrderService] --> I["«interface»<br/>OrderRepository"]
        B2[MySQLRepository] -.implements.-> I
        B3[InMemoryRepository] -.implements.-> I
    end
```

The payoff is testability: inject the in-memory one in tests.

## The patterns that actually get asked

```mermaid
graph TB
    C["CREATIONAL"] --> C1[Singleton]
    C --> C2[Factory / Abstract Factory]
    C --> C3[Builder]
    S["STRUCTURAL"] --> S1[Adapter]
    S --> S2[Decorator]
    S --> S3[Proxy]
    B["BEHAVIOURAL"] --> B1["Strategy ★"]
    B --> B2["Observer ★"]
    B --> B3["State ★"]
```

**Strategy, Observer and State** are the interview trio — know them cold.

### Strategy — swap the algorithm at runtime

```python
from abc import ABC, abstractmethod

class SplitStrategy(ABC):
    @abstractmethod
    def split(self, amount: float, users: list) -> dict: ...

class EqualSplit(SplitStrategy):
    def split(self, amount, users):
        share = amount / len(users)
        return {u: share for u in users}

class PercentSplit(SplitStrategy):
    def __init__(self, pct: dict): self.pct = pct
    def split(self, amount, users):
        return {u: amount * self.pct[u] / 100 for u in users}

class Expense:
    def __init__(self, amount, users, strategy: SplitStrategy):
        self.shares = strategy.split(amount, users)   # behaviour injected
```

Adding a new split type means **adding a class, not editing one** — that is Open/Closed in action.

### Observer — one change, many reactions

```mermaid
sequenceDiagram
    participant S as Subject (Order)
    participant A as EmailNotifier
    participant B as InventoryUpdater
    participant C as AnalyticsLogger
    S->>S: state changes (order placed)
    S->>A: notify()
    S->>B: notify()
    S->>C: notify()
    Note over S,C: the Subject does not know<br/>who is listening — add observers<br/>without touching it
```

### State — behaviour depends on the current state

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> MovingUp: request above
    Idle --> MovingDown: request below
    MovingUp --> Idle: arrived
    MovingDown --> Idle: arrived
    MovingUp --> MovingUp: more requests above
```

Replaces a sprawling `if/elif` on a state enum with one class per state.

## LLD case: Parking Lot

```mermaid
classDiagram
    class ParkingLot {
        -List~Floor~ floors
        +park(Vehicle) Ticket
        +unpark(Ticket) Fee
    }
    class Floor {
        -List~Spot~ spots
        +findSpot(VehicleType) Spot
    }
    class Spot {
        -SpotType type
        -bool occupied
    }
    class Vehicle {
        <<abstract>>
        -String plate
    }
    class Car
    class Bike
    class PricingStrategy {
        <<interface>>
        +calculate(Duration) Fee
    }
    ParkingLot "1" --> "*" Floor
    Floor "1" --> "*" Spot
    Vehicle <|-- Car
    Vehicle <|-- Bike
    ParkingLot --> PricingStrategy
```

**Talk through it in this order:** requirements → entities → relationships → interfaces for anything that varies (pricing, allocation) → then code.

The patterns fall out naturally: **Strategy** for pricing, **Factory** for vehicle creation, **Singleton** for the lot itself.

## Interview checklist

- [ ] All five SOLID with a bad example and the refactor
- [ ] Liskov via Rectangle/Square
- [ ] Strategy, Observer, State — code each from memory
- [ ] Composition over inheritance, with a case where inheritance broke
- [ ] Parking lot: requirements → class diagram → code, in 45 minutes
