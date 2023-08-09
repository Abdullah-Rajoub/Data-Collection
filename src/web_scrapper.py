import requests
from bs4 import BeautifulSoup
from utility.concatunation import *
from utility.extract_questions import extract_questions
import sys
import time

sys.path.insert(1, r"C:\Users\kinga\Desktop\scripts\src\models")
import pageInfo

sys.path.insert(1, r"C:\Users\kinga\Desktop\scripts\src\utility")
import concatunation

sys.path.insert(1, r"C:\Users\kinga\Desktop\scripts\src\api")
import gpt35_turbo

sys.path.insert(1, r"C:\Users\kinga\Desktop\scripts")
import JSON_creator_script

sys.path.insert(1, r"C:\Users\kinga\Desktop\scripts\src\utility")

import extract_questions

import os
import json
import datetime


def delete_elements(lst, indexes):
    new_lst = []
    for i in range(len(lst)):
        if i not in indexes:
            new_lst.append(lst[i])
    return new_lst


def create_json_file(name_of_file, questions, answers, pageType, URL):
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

    processed_questions = process_questions(questions)
    processed_answers = process_questions(answers)
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


urls = [
    "https://www.psu.edu.sa/en/jubilation-office",
    "https://www.psu.edu.sa/en/scholarship-office",
    "https://www.psu.edu.sa/en/compliance-office",
    "https://www.psu.edu.sa/en/writing-and-tutoring-center",
    "https://www.psu.edu.sa/en/project-management-office",
    "https://www.psu.edu.sa/en/evaluation-and-academic-accreditation-center",
    "https://www.psu.edu.sa/en/it-center",
    "https://www.psu.edu.sa/en/international-affairs",
    "https://www.psu.edu.sa/en/public-relations",
    "https://www.psu.edu.sa/en/quality-assurance",
    "https://www.psu.edu.sa/en/sp-dc",
    "https://www.psu.edu.sa/en/teaching-Learning",
    "https://www.psu.edu.sa/en/DTET",
]

#  "https://www.psu.edu.sa/en/TAC", done
#     "https://www.psu.edu.sa/en/center-statistics",done
# "https://www.psu.edu.sa/en/jubilation-office",
# "https://www.psu.edu.sa/en/scholarship-office",
# "https://www.psu.edu.sa/en/compliance-office",
# "https://www.psu.edu.sa/en/writing-and-tutoring-center",
# "https://www.psu.edu.sa/en/project-management-office",
# "https://www.psu.edu.sa/en/evaluation-and-academic-accreditation-center",
# "https://www.psu.edu.sa/en/it-center",
# "https://www.psu.edu.sa/en/international-affairs",
# "https://www.psu.edu.sa/en/public-relations",
# "https://www.psu.edu.sa/en/quality-assurance",
# "https://www.psu.edu.sa/en/sp-dc",
# "https://www.psu.edu.sa/en/teaching-Learning",
# "https://www.psu.edu.sa/en/DTET",


def remove_element(array, index):
    # Shift elements to the left starting from the given index
    for i in range(index, len(array) - 1):
        array[i] = array[i + 1]
    # Resize the array to remove the last element
    array.pop()


def tableCoversion(table):
    # an array that gives the posion that the data should repeat at, and how many times it should repeat/span
    rowSpans = []
    # Extract data from table
    table_data = []
    # this will be used to calculate the place of row spans in the table later
    numOfCoulmns = -1
    headRow = table.find("thead")
    row_data = []
    for headCell in headRow.find_all("th"):
        # getting the text inside the head cell
        cell_text = "".join(headCell.find_all(text=True))
        # gett the number of col span, by defualt it is 1
        colSpan = int(headCell.get("rowspan", 1))
        ## handling column span / if none existent still works
        numOfCoulmns -= colSpan - 1
        numOfCoulmns += 1
        row_data.extend([cell_text] * colSpan)
    table_data.append(row_data)
    ### table body work:
    for row in table.find_all("tbody"):
        for tr in row.find_all("tr"):
            row_data = []
            position_in_row = 0
            position_inside_span = 0
            # checking for any row spans from previous rows/ and filling up the rows accordingly
            counter = 0
            # just filling up the array with nones, will be replaced later with actual data
            # (avoid index out of bound )
            while counter <= numOfCoulmns:
                row_data.append(None)
                counter += 1
            for span in rowSpans:
                row_data[span["position_in_row"]] = span["cell_text"]
                span["span_amount"] -= 1
            for cell in tr.find_all("td"):
                cell_text = "".join(cell.find_all(text=True))
                # Handle row span (if 'rowspan' attribute is present) / col span
                rowspan = int(cell.get("rowspan", 1))
                colSpan = int(cell.get("colspan", 1))
                if rowspan > 1:
                    rowSpans.append(
                        {
                            "cell_text": cell_text,
                            "position_in_row": position_in_row,
                            "span_amount": rowspan,
                        }
                    )
                    row_data[position_in_row] = cell_text
                # row_data.extend([cell_text] * colSpan)
                original_index = position_in_row
                for span in rowSpans:
                    if (
                        position_in_row == span["position_in_row"]
                        and cell_text != span["cell_text"]
                    ):
                        position_in_row += 1
                        row_data[position_in_row] = cell_text
                        position_in_row += 1

                if position_in_row == original_index:
                    row_data[position_in_row] = cell_text
                    position_in_row += 1
            #
            while colSpan > 1:
                position_in_row += 1
                for span in rowSpans:
                    if (
                        position_in_row == span["position_in_row"]
                        and cell_text != span["cell_text"]
                    ):
                        position_in_row += 1
                row_data[position_in_row] = cell_text
                colSpan -= 1
            for span in rowSpans:
                if (span["span_amount"]) <= 1:
                    remove_element(rowSpans, position_inside_span)
                    position_inside_span -= 1
                position_inside_span += 1
            table_data.append(row_data)

    # Convert the table data to a string while preserving the structure
    table_string = ""
    for row in table_data:
        table_string += "\t".join(row) + "\n"
    return table_string


def findingLists(tags):
    text = ""
    for tag in tags:
        if tag.name in ["ul", "ol"]:
            text = text + findingLists(tag)
        else:
            text = text + f"- {tag.text.strip()}\n"
    return text


def coverting_links(a_tag):
    if "href" in a_tag:
        link_text = a_tag["href"]
        if "#" in link_text:
            return "You can find more infomation on Prince Sultan University website at: https://www.psu.edu.sa/en"
        else:
            return link_text
    else:
        return ""


text_chunks = []
listOfPages = []
table_text_chunks = []
for url in urls:
    text_chunks = []
    table_text_chunks = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    target_div = soup.find("div", {"class": "col_two_third nobottommargin col_last"})

    for chunk in target_div.find_all(
        [
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "ul",
            "ol",
            "p",
            "table",
            "q",
            "abbr",
            "address",
            "a",
            "br",
        ],
    ):
        if chunk.name in ["ul", "ol"]:
            text_chunks.append(findingLists(chunk) + "\n")
        elif chunk.name == "table":
            table_text_chunks.append(f"{text_chunks.pop()}{tableCoversion(chunk) }")
        elif chunk.name == "a":
            text_chunks.append(coverting_links(chunk) + "\n")
        elif chunk.name == "br":
            text_chunks.append("\n")
        else:
            text_chunks.append(chunk.text.strip() + "\n")
    newPageInfo = pageInfo.PageInfo(
        url=url,
        pageData=concat_chunks(text_chunks)["normal_length_output"],
        pageType=input(f"Give a page type to this page: {url}\n-->  "),
        tablesData=concat_chunks(table_text_chunks)["normal_length_output"],
    )
    listOfPages.append(newPageInfo)

for page in listOfPages:
    for data_chunk in page.pageData:
        questions = gpt35_turbo.createListOfQuestions(text=data_chunk)
        print(f"the questions are:\n {questions}")

        questions_list = extract_questions.extract_questions(questions)
        user_input = input(
            "Enter the INDEX of questions to be deleted (comma-separated): "
        )
        elements_to_delete = [int(x) for x in user_input.split(",")]

        new_lst = delete_elements(questions_list, elements_to_delete)
        print(f"the new questins are:\n{new_lst}")
        questions_chunks = concatunation.concat_questions(new_lst)[
            "normal_length_output"
        ]
        answers = gpt35_turbo.createListOfAnswers(
            text=data_chunk, questions_chunks=questions_chunks
        )
        time.sleep(60)
        questionsVarations = gpt35_turbo.createVarationsOfQuestions(questions=new_lst)
        answersVarations = gpt35_turbo.createVarationsOfAnswers(answers=answers)
        time.sleep(60)
        create_json_file(
            questions=questionsVarations,
            answers=answersVarations,
            URL=page.url,
            pageType=page.pageType,
            name_of_file="test",
        )
    for data_chunk in page.tablesData:
        questions = gpt35_turbo.createListOfQuesTionsFromTable(text=data_chunk)
        print(f"the questions are:\n {questions}")
        # time.sleep(30)
        questions_list = extract_questions.extract_questions(questions)
        user_input = input(
            "Enter the number of questions to be deleted (comma-separated): "
        )
        elements_to_delete = [int(x) for x in user_input.split(",")]

        new_lst = delete_elements(questions_list, elements_to_delete)
        print(f"the new questins are:\n{new_lst}")
        questions_chunks = concatunation.concat_questions(new_lst)[
            "normal_length_output"
        ]
        answers = gpt35_turbo.createListOfAnswers(
            text=data_chunk, questions_chunks=questions_chunks
        )
        time.sleep(60)
        questionsVarations = gpt35_turbo.createVarationsOfQuestions(questions=new_lst)
        answersVarations = gpt35_turbo.createVarationsOfAnswers(answers=answers)
        time.sleep(60)
        create_json_file(
            questions=questionsVarations,
            answers=answersVarations,
            URL=page.url,
            pageType=page.pageType,
            name_of_file="test",
        )
