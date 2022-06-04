# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    "variable":"A binding which is used to reference a value",
    "hoisting": "A concept in JavaScript whereby the V8 engine stores all functions before running a script",
    "array": "A data structure which stores data within square brackets",
    "tag":" A is a building block in HTML",
    "expression":"An expression is a line of code which evaluates to give a value"
}

print(f"variable: {glossary['variable']}")
print(f"hoisting: {glossary['hoisting']}")
print(f"array: {glossary['array']}")
print(f"tag: {glossary['tag']}")
print(f"expression: {glossary['expression']}")
