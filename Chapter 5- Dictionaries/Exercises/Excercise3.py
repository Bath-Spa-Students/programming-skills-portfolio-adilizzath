# glossary of programming words and their meanings

glossary={
    "variable":"A named storage location in memory used to store data.",
    "list":"An ordered collection of items,which can be of different data types",
    "conditional statement":"A statement that allows different code to execute based on their conditions.",
    "function":"A block of code that can be called to perform a specific task",
    "loop":"A control structure that repeats a set of statements as long as a specified condition.",
    "dictionary":"A collection of key value pairs that can be used to store and retreive values",
    "tuple":"Immutable collection of elements",
    "string":"Sequence of characters enclosed in single or double quotes",
    "boolean":"A data type that represents True or False values",
    "method":"A function assosiated with an object of data type"
}

#print each word and its meaning neatly formatted with a newline each pair

for word,meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
