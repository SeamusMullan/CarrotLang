# CarrotLang


## Syntax Definitions

1. **Readable Declarations**: Use clear and descriptive keywords for variable declarations to make the code more readable. For instance:
- `immutable` for constants that cannot change.
- `mutable` for variables that can change.
- `changeable` for variables that might change in compilation. If they don't change, they get made immutable. 
- If no declaration is made, changeable is assumed

```carrot
immutable MAX_SCORE = 100
mutable playerName = "Player1"
changeable playerLevel = 20
willWin = Yes note this uses changeable
```

2. **Elegant Control Flow**: Instead of traditional `if-else` statements, use more natural language-like constructs.
- `when` for conditions.
- `but when` for else-if statements
- `otherwise` for else statements.

```carrot
when score > 50 then
print("You're winning!")
but when score > 25 then
print("doing ok...")
otherwise
print("Try harder!")
```

3. **Function Definitions**: Use `task` to define functions, making it clear that functions perform specific tasks.
```carrot
task calculateTotal(a, b) {
return a + b
}
```

Tasks can be forced to return a type by using `returns`
```carrot
task Multiply(a, b) returns Number {
return a * b
}
```

4. **Array Indexing**: Start array indexing from 0
```carrot
immutable numbers = [1, 2, 3]
print(numbers[1])  note prints 2
```

Arrays can also be indexed backwards
```carrot
print(numbers[-2]) note prints 2
```

5. **Looping Constructs**: Simplify loops with readable keywords.
- `repeat times` for a specific number of iterations.
- `iterate over * with *` for iterating through collections.

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

6. **Comments**: Use `note` for single-line comments and `explain` for block comments to make code documentation more conversational.
```carrot
note This is a single-line comment

explain {
This is a block comment
explaining the following code block
}
```

7. **Error Handling**: Use `attempt` and `rescue` for try-catch blocks, making them more understandable.
```carrot
attempt {
note code that might throw an error
} rescue (error) {
print("An error occurred: " + error)
}
```

Use `always` after an attempt-rescue block for code that should always run

```
attempt{
note Risky code
} rescue (error) {
print(error)
} always {
note Do extra things here
}
```

8. **Custom Operators**: Allow users to define their own operators for specific operations, enhancing readability and functionality.
```carrot
operator <+> (a, b) {
return a.concat(b)
}
```

9. **Type Annotations**: Include optional type annotations for variables to help with clarity and debugging.
```carrot
mutable score: Number = 0
immutable name: String = "CarrotCoder"
```

All the possible types in CarrotLang are listed below
- Number (Integers, Floats or Doubles)
- Booleans (using `yes` or `no` caps-insensitive)
- String (Character when length of 1)
- Nothing (similar to Null)
- Chance (represents a percentage chance)
- Currency (can be converted to different currencies on the fly)
- VectorN (N dimensional Vector)
- GridN (N dimensional square matrix)
- GridXY (X row, Y col dimensional matrix)
- UID (Unique variable that cannot equal any other variable at runtime)

10. **Module System**: Use `include` and `export` keywords for importing
```carrot
include "mathModule"
```

When importing multiple modules, you can use a list instead

```carrot
immutable requirements = ["mathModule", "fancyModule" "dumbModule"]
include requirements
```

To only include specific modules you can specifiy elements to exclude
```carrot
include requirements except requirements[2]
```

You can also remove modules after they have been used using `forget about`
```carrot
forget about requirements[1]
```