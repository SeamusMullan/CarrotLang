# CarrotLang

Welcome to CarrotLang, a modern and intuitive programming language designed for clarity, simplicity, and power. CarrotLang brings together the best features of conventional programming while introducing innovative concepts to enhance developer experience.

## Syntax Definitions

### 0. General Rules
- CarrotLang does not enforce indentation, but each line of code must perform a single operation.

**Valid CarrotLang code example:**
```carrot
immutable people = ["john", "mary"]
print(people[0])
```

**Invalid CarrotLang code example:**
```carrot
immutable people = ["john", "mary"] print(people[0])
```

### 1. Readable Declarations
- `immutable` for unchangeable constants.
- `mutable` for changeable variables.
- `changeable` for variables that might become immutable during compilation.

```carrot
immutable MAX_SCORE = 100
mutable playerName = "Player1"
changeable playerLevel = 20
willWin = Yes  // Uses 'changeable' by default
```

### 2. Elegant Control Flow
- `when` for conditional checks.
- `but when` for else-if scenarios.
- `otherwise` for else conditions.

```carrot
when score > 50 then
print("You're winning!")
but when score > 25 then
print("doing ok...")
otherwise
print("Try harder!")
```

### 3. Function Definitions
- Use `task` for defining functions.
- `returns` keyword for specifying return types.

```carrot
task calculateTotal(a, b) {
return a + b
}

task Multiply(a, b) returns Number {
return a * b
}
```

### 4. Array Indexing
- Arrays start at index 0.
- Negative indexing supported for reverse access.

```carrot
immutable numbers = [1, 2, 3]
print(numbers[1])  // prints 2
print(numbers[-2]) // prints 2
```

### 5. Looping Constructs
- `repeat times` for fixed iterations.
- `iterate over * with *` for collection traversal.

```carrot
repeat 5 times {
print("Hello")
}

iterate over collection with element {
print(element)
}

iterate over accounts with data {
print(data.name)
}
```

### 6. Comments
- `note` for single-line comments.
- `explain` for multi-line comments.

```carrot
note This is a single-line comment

explain {
This block explains the following code
}
```

### 7. Error Handling
- `attempt` and `rescue` for try-catch blocks.
- `always` for code that always executes regardless of errors.

```carrot
attempt {
// code that might throw an error
} rescue (error) {
print("An error occurred: " + error)
} always {
// Cleanup or finalization code
}
```

### 8. Custom Operators
- Define custom operators for enhanced readability.

```carrot
operator <+> (a, b) {
return a.concat(b)
}
```

### 9. Type Annotations
- Optional type annotations for clarity.
```carrot
mutable score: Number = 0
immutable name: String = "CarrotCoder"
```

### 10. Module System
- `include` and `export` keywords for module management.

- **Single Module Import:**
```carrot
include "mathModule"
```

- **Multiple Module Import:**
```carrot
immutable requirements = ["mathModule", "fancyModule", "dumbModule"]
include requirements
```

- **Selective Module Import:**
```carrot
include requirements except requirements[2]
```

- **Module Removal:**
```carrot
forget about "mathModule"
forget about requirements[1]
```

---

## Additional Features in CarrotLang

- **Types**: CarrotLang supports a variety of types for different purposes:
  - `Number` (Integers, Floats, Doubles)
  - `Boolean` (`yes` or `no`, case-insensitive)
  - `String` (treated as `Char` when length is 1)
  - `Nothing` (similar to `Null`)
  - `Chance` (percentage probability)
  - `Currency` (with on-the-fly conversion)
  - `VectorN` (N-dimensional vector)
  - `GridN` (N-dimensional square matrix)
  - `GridXY` (X rows, Y columns matrix)
  - `UID` (Unique identifier)
  - `Date` (Date in DD/MM/YYYY format)
  - `GeoLocation` (using Lat, Lng)

All types in CarrotLang can be created as instances
```carrot
note a 50% chance using the Chance type
immutable prob: Chance = Chance(50)

note the location of The Spire in Dublin using the GeoLocation type
immutable theSpire: GeoLocation = GeoLocation(53.3498, 6.2603)

explain{
    a budget for a company using the Currency type
    All currency types use the ISO code to represent a currency
    see https://en.wikipedia.org/wiki/ISO_4217
}
immutable budget: Currency = Currency(1000000, EUR)
```

- **Exclamation Marks**: All statements in CarrotLang end with an exclamation mark for emphasis and clarity.

```carrot
print("Hello, CarrotLang")!
```

- **Immutable Data**: CarrotLang supports immutable data structures to ensure data integrity.

```carrot
immutable constantData = ["fixed", "values"]!
```

- **Open Source**: CarrotLang is an open-source project, welcoming contributions from the developer community worldwide.

---

For more information, examples, and resources, visit the [CarrotLang official repository](https://github.com/CarrotLang/CarrotLang).