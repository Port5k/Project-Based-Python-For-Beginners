# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = {
    "variable":"A binding which is used to reference a value",
    "hoisting": "A concept in JavaScript whereby the V8 engine stores all functions before running a script",
    "array": "A data structure which stores data within square brackets",
    "tag":" A is a building block in HTML",
    "expression":"An expression is a line of code which evaluates to give a value"
}

for term, meaning in glossary.items():
    print(f"{term.title()}: {meaning}")