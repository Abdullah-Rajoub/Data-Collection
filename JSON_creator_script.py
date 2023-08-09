import os
import json
import datetime


def create_json_file(name_of_file, questions, answers, pageType, URL):
    processed_questions = processed_answers(questions)
    processed_answers = processed_answers(answers)
    file_path = f"{name_of_file}.json"

    # Check if file exists, create it if not
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("[]")

    # Read existing data from file
    with open(file_path, "r") as f:
        existing_data = json.load(f)
    # questions array

    new_data = []
    answerIndex = -1
    for i in range(0, len(processed_answers), 1):
        answerIndex = answerIndex + 1
        for j in range(1):
            prompt1 = processed_questions[i]
            completion = processed_answers[answerIndex]
            new_data.append(
                {
                    "prompt": prompt1,
                    "completion": completion,
                    "URL": URL,
                    "pageType": pageType,
                    "date": datetime.date.today().strftime("%Y-%m-%d"),
                }
            )

    # Merge existing and new data
    all_data = existing_data + new_data

    # Write all data to file
    with open(file_path, "w") as f:
        json.dump(all_data, f, indent=2)

    def process_questions(question_string):
        # split the question string into individual lines
        lines = question_string.split("\n")
        # initialize an empty list to store the processed questions
        questions = []
        # iterate through each line
        for line in lines:
            # remove any numbering at the beginning of the line
            line = line.lstrip("0123456789. ")
            # remove any leading dash
            line = line.lstrip("- ")
            # add the processed question to the list of questions, if it's not an empty line
            if len(line) > 0:
                questions.append(line)
        # return the list of processed questions
        return questions


def process_questions(question_string):
    # split the question string into individual lines
    lines = question_string.split("\n")
    # initialize an empty list to store the processed questions
    questions = []
    # iterate through each line
    for line in lines:
        # remove any numbering at the beginning of the line
        line = line.lstrip("0123456789. ")
        # remove any leading dash
        line = line.lstrip("- ")
        # add the processed question to the list of questions, if it's not an empty line
        if len(line) > 0:
            questions.append(line)
    # return the list of processed questions
    return questions
