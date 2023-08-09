import openai
import requests
import json
import sys
import time

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, r"C:\Users\kinga\Desktop\scripts\src\utility")
import concatunation

URL = "https://api.openai.com/v1/chat/completions"


# This function takes a text, and generate the prompt used for questions generation
def PROMPT_FOR_QUESTIONS_GENRATION(text):
    QUESTIONS_PROMPT = "Forget about all previous instructions.\n Prtend to be a copywriter with 6 years of experience working for Prince Sultan University. Create a list of questions from the text provided. Provide as many questions as possible about the text. Don't include any questions outside the text provided.\nHere is the text:\n"
    return QUESTIONS_PROMPT + text


# This function creates a prompt to answer the question from text
def PROMPT_FOR_ANSWERS_GENRATION(questions, text):
    return f"Forget about all previous instructions.\n Prtend to be a copywriter with 6 years of experience answering questions about Prince Sultan University.\nAnswer all questions. Explain everything in your answer, and give complete Sentences as an answer. The answers should be from the text provided. Give only factual answers. If the text doesn't have the answer, respond with 'There is no answer in the text'.\nHere are the questions:\n {questions}\nHere is the text:\n{text}.\n Show only the answers in the output"


def PROMPT_FOR_QUESTION_VARATIONS(questions):
    return f"Forget about all previous instructions.\nPrtend to be a copywriter with 6 years of experience working for Prince Sultan Unitveristy. Show the original questions and two paraphrases for each question, but keep the same meaning for the questions.\n Here are the questions:\n{questions}\nShow the output in the following format.\nExample input:\n1.What is your name?\nExample output:\n1. What is your name?\n- Can you tell me your name?\n- Can you tell me what your name is?"


def PROMPT_FOR_ANSWERS_VARATIONS(answers):
    return f"Prtend to be a copywriter with 6 years of experience working for Prince Sultan.\nShow the original sentence and two paraphrases for each sentence, without changing the meaning of the sentence!\nHere are the sentences:\n{answers}\nShow the output in the following format.\nExample input:\n1. The apple is red\nExample output:\n1. The apple is red\n- The color of the apple is red\n- red is the color of the apple "


def PROMPT_FOR_TABLES_QUESTIONS_GENERATION(text):
    return f"Forget about all previous instructions.\n Generate as many questions as possible about the table provided. Here is the table with a bit of explanation before the table:\n{text}\nThe output should follow this format:\n1. [First question]\n2. [Second question]\n3. [third question]\n..."


###### First Step #########
def createListOfQuestions(text):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": PROMPT_FOR_QUESTIONS_GENRATION(text=text),
            }
        ],
        "temperature": 0.5,
        "n": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "max_tokens": 900,
    }
    response = requests.post(URL, headers=headers, json=payload, stream=False)

    # Tapping into the questions returned in the response
    return json.loads(response.text)["choices"][0]["message"]["content"]


def createListOfAnswers(questions_chunks, text):
    answers = ""
    for questions in questions_chunks:
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": PROMPT_FOR_ANSWERS_GENRATION(
                        questions=questions, text=text
                    ),
                }
            ],
            "temperature": 0.9,
            "n": 1,
            "stream": False,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "max_tokens": 600,
        }
        response = requests.post(URL, headers=headers, json=payload, stream=False)
        answer = json.loads(response.text)["choices"][0]["message"]["content"]
        answers = answers + answer
        print(answers)
    return answers


def createVarationsOfQuestions(questions):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": PROMPT_FOR_QUESTION_VARATIONS(questions=questions),
            }
        ],
        "temperature": 0.3,
        "n": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "max_tokens": 2900,
    }
    response = requests.post(URL, headers=headers, json=payload, stream=False)
    # Tapping into the questions varations returned in the response
    return json.loads(response.text)["choices"][0]["message"]["content"]


def createVarationsOfAnswers(answers):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": PROMPT_FOR_ANSWERS_VARATIONS(answers=answers),
            }
        ],
        "temperature": 0.3,
        "n": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "max_tokens": 2900,
    }
    response = requests.post(URL, headers=headers, json=payload, stream=False)
    # Tapping into the answers varation returned in the response
    return json.loads(response.text)["choices"][0]["message"]["content"]


def createListOfQuesTionsFromTable(text):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": PROMPT_FOR_TABLES_QUESTIONS_GENERATION(text=text),
            }
        ],
        "temperature": 0.7,
        "n": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "max_tokens": 900,
    }
    response = requests.post(URL, headers=headers, json=payload, stream=False)

    # Tapping into the questions returned in the response
    return json.loads(response.text)["choices"][0]["message"]["content"]


openai.api_key = "Put your own key"
question_generator_tokens = 80
answer_generator_tokens = 700
messages = [
    {
        "role": "system",
        "content": "Pretend to be a copywriter for Prince Sultan University",
    },
]


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}",
}
# Extract the response and the length of completion
# text = """
# Article 5
# Undergraduate study follows the academic level system.
# Undergraduate study comprises a minimum of eight levels.
# The duration of an academic level is one semester.
# Students are promoted successively from one academic level to another, in accordance with the promotion rules.
# The Rules of Implementation for Article 5
# The student is responsible for understanding and following academic rules and regulations including graduation requirements. Guidance and assistance from academic advisors does not relieve the student of this responsibility. Therefore, every student should be thoroughly familiar with all academic regulations pertaining to the granting of academic degrees. He/She regularly should familiarize him/herself with new academic regulations; in this regard he/she may consult the department chairman or the academic advisor regarding these regulations.
# The financial rules and regulations stated in Appendix D must be followed.
# The University assigns an academic advisor to each student for assistance in matters that relate to academic progress, such as:
# Selecting the academic major that best suits the student’s preferences and capabilities.
# Understanding and interpreting the academic regulations.
# Informing the student of the sequence of the required and elective courses and suggesting suitable elective courses.
# Following up on the academic progress of the student.
# Assisting in early registration and the various stages of registration.
# Assisting in course substitution, if and when necessary.
# The academic advisor is chosen from the faculty members of the department or the college. The academic advisor for the PYP students is the director of the PYP or someone appointed by him/her or acting on his/her behalf.
# """
# questions = createListOfQuestions(text=text)
# questions_chunks = concatunation.concat_questions(questions)["normal_length_output"]
# answers = createListOfAnswers(text=text, questions_chunks=questions_chunks)
# questionsVarations = createVarationsOfQuestions(questions=questions)
# answersVarations = createVarationsOfAnswers(answers=answers)
