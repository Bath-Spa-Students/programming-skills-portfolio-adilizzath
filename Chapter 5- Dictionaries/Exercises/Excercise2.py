#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 
#their meanings as values.

glossary={
    "variable":"A named storage location in memory used to store data.",
    "list":"An ordered collection of items,which can be of different data types",
    "conditional statement":"A statement that allows different code to execute based on their conditions.",
    "function":"A block of code that can be called to perform a specific task",
    "loop":"A control structure that repeats a set of statements as long as a specified condition."    
}

#print each word and its meaning neatly formatted with a newline each pair

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")