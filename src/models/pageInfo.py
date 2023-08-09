class PageInfo:
    url = ""
    pageData = []
    pageType = ""
    questions = []
    answers = []
    tablesData = []

    def __init__(self, url, pageData, pageType, tablesData):
        self.url = url
        self.pageData = pageData
        self.pageType = pageType
        self.tablesData = tablesData

    def add_questions(self, questions_array):
        self.questions.extend(questions_array)

    def add_answers(self, answers_array):
        self.answers.extend(answers_array)
