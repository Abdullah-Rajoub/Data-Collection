def eliminate_strings(arr):
    # Display all strings in the console
    for i, s in enumerate(arr):
        print(f"{i+1}: {s}")

    # Prompt user for indices of strings to eliminate
    to_eliminate = input(
        "What questions do you want to eliminate from the array? (Give your inputs in the following format: 1, 2, 3, 7)\n"
    )
    to_eliminate = [int(idx) - 1 for idx in to_eliminate.split(",")]

    # Generate output array with elements at specified indices eliminated
    output = [s for i, s in enumerate(arr) if i not in to_eliminate]

    return output


input_arr = [
    "What is your name?",
    "What is your favorite color?",
    "What is your favorite food?",
    "What is your favorite animal?",
    "What is your favorite book?",
    "What is your favorite movie?",
    "What is your favorite hobby?",
]

output_arr = eliminate_strings(input_arr)

# Example user input: "2,5,6,7,1"
# Corresponding array elements: element at indexes 1, 4, 5, 6, and 0
# Expected output: ["What is your favorite color?", "What is your favorite book?"]
#                  ["What is your name?", "What is your favorite food?", "What is your favorite animal?", "What is your favorite hobby?"]
print(output_arr)
