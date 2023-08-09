import os
import json
import datetime
import sys

sys.path.append("C:\Users\kinga\Desktop\scripts\utility")

from extract_questions.py import *


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


# example usage
question_string = """
1. What are the graduation requirements for students at Prince Sultan University?
- What conditions must be met for a student to graduate from Prince Sultan University?
- What are the criteria that students must fulfill to obtain a degree from Prince Sultan University?

2. What is the minimum cumulative and major GPA required for graduation?
- What is the minimum combined GPA that a student needs to have in order to graduate?
- What is the minimum GPA required for a student's major in order to graduate?

3. Can a student with a low cumulative GPA still graduate? How?
- Is it possible for a student with a low cumulative GPA to still obtain a degree?
- What options are available for students with a low cumulative GPA who want to graduate?

4. What is the process for recalculation of a student's cumulative GPA?
- How is a student's cumulative GPA recalculated?
- What steps are taken to recalculate a student's GPA at Prince Sultan University?

5. What are the rules governing the recalculation of the cumulative GPA?
- What policies govern the recalculation of a student's GPA at Prince Sultan University?
- What regulations dictate how a student's cumulative GPA is recalculated?

6. Can changes be made to academic records after the graduation documents have been issued?
- Is it possible to make changes to academic records after a student has graduated?
- What is the policy for altering academic records after graduation at Prince Sultan University?
"""
answers_string = """
1. Students must successfully complete all graduation requirements according to the degree plan, and have a cumulative GPA of at least a pass.
- In order to graduate, students need to fulfill all the requirements specified in their degree plan and maintain a minimum cumulative GPA that is considered passing.
- A passing cumulative GPA and the completion of all requirements listed in the degree plan are necessary for graduation.

2. The minimum cumulative and major GPA required for graduation is 2.00 or higher (out of 4.00).
- A minimum cumulative and major GPA of 2.00 or higher (out of 4.00) is required for graduation.
- Graduation necessitates achieving a minimum cumulative and major GPA of 2.00 or higher (out of 4.00).

3. If a student has passed the required courses but has a low cumulative GPA, the College Council may specify appropriate courses for the student to complete in order to improve their GPA.
- In case a student has passed the mandatory courses but has a low cumulative GPA, the College Council has the authority to identify relevant courses for the student to take to improve their GPA.
- If a student has completed the necessary courses but has a low cumulative GPA, they may be required to take additional courses as recommended by the College Council to improve their GPA.

4. A student may request a recalculation of their cumulative GPA if they have successfully completed all the courses required for obtaining the degree. The request is based on the recommendation of the departmental council, in coordination with the Admission and Registration Deanship and the approval of the College Council, provided that the new GPA does not exceed 2.00 (out of 4.00) after recalculation.
- Students who have successfully completed all the courses required for their degree may request a recalculation of their cumulative GPA. Such a request is subject to the approval of the departmental council, Admission and Registration Deanship, and College Council, and provided that the new GPA does not exceed 2.00 (out of 4.00).
- After successfully completing all the mandatory courses, students may ask for their cumulative GPA to be recalculated, subject to approval from the departmental council, Admission and Registration Deanship, and College Council, with the new GPA not to exceed 2.00 (out of 4.00).

1. The rules governing the recalculation of the cumulative GPA include: excluding a grade earned previously in any completed course if the student has repeated the course successfully and earned a grade of D or higher, excluding certain grades (F, DN, WF, D and D+) from the total number of credits used to calculate the student's cumulative GPA, excluding a maximum of 24 credits when calculating the cumulative GPA, indicating the courses that have been excluded from the calculation of the GPA by a special mark in the academic record, and clearly indicating the cumulative GPA after excluding the grades of the repeated courses.
- The regulations for recalculating the cumulative GPA involve: removing the previously earned grade for any course if the student repeats and earns a grade of D or higher, excluding specific grades (F, DN, WF, D, and D+) from the calculation of the cumulative GPA, disregarding up to 24 credits when determining the cumulative GPA, marking the courses that have been excluded from the GPA calculation in the student's academic record, and displaying the cumulative GPA after eliminating the repeated course grades.
- The rules that apply to recalculating the cumulative GPA require that grades earned previously in any completed course be excluded if the student repeats the course successfully and earns a grade of D or higher, that certain grades (F, DN, WF, D, and D+) are not counted towards the cumulative GPA, that a maximum of 24 credits can be excluded when calculating the cumulative GPA, that a special mark is used in the academic record to indicate the courses that have been excluded from the GPA calculation, and that the cumulative GPA is displayed after eliminating the grades of the repeated courses.

2. No changes to academic records are allowed under any circumstances after the graduation documents have been issued.
- Academic records cannot be altered after graduation documents have been released, without exception.
- Once graduation documents have been issued, academic records may not be modified under any circumstances.

"""
questions = process_questions(question_string)
print("the length of the questions generated is")
print(len(questions))

answers = process_questions(answers_string)
print("the length of the answers generated is")
print(len(answers))


# Set file path and name
file_path = "output.json"

# Check if file exists, create it if not
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("[]")

# Read existing data from file
with open(file_path, "r") as f:
    existing_data = json.load(f)
# questions array


def remove_duplicates(input_list):
    return list(set(input_list))


print(len(questions))
print(len(answers))
new_data = []
answerIndex = -1
for i in range(0, len(questions), 1):
    answerIndex = answerIndex + 1
    for j in range(1):
        prompt1 = questions[i]
        completion = answers[answerIndex]
        new_data.append(
            {
                "prompt": prompt1,
                "completion": completion,
                "URL": "https://www.psu.edu.sa/en/graduation-guidelines",
                "pageType": "admision/Rules&Regulations/Graduation",
                "date": datetime.date.today().strftime("%Y-%m-%d"),
            }
        )

# Merge existing and new data
all_data = existing_data + new_data

# Write all data to file
with open(file_path, "w") as f:
    json.dump(all_data, f, indent=2)
