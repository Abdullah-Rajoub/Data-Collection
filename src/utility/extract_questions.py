def extract_questions(text):
    lines = text.split("\n")
    questions = []
    for line in lines:
        if line.startswith(
            ("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")
        ) and line.endswith("?"):
            question = line
            questions.append(question)
        elif line.endswith("?"):
            questions.append(line)
    return questions
