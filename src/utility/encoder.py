import tiktoken


def string_token_counter(input_String):
    encoding = tiktoken.get_encoding("cl100k_base")
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return len(encoding.encode(input_String))


text = """
1. How are tuition fees paid?
2. Do tuition fees cover textbooks?
3. What services do tuition fees cover?
4. When are tuition fees payable?
5. How can a student withdraw from the university?
6. What happens if a student fails to register and pay tuition fees on time?
7. What are the tuition hour fees for Bachelor programs?
8. What are the tuition hour fees for Masters programs?
9. Is value-added VAT added for non-Saudi students?
10. Is there a sibling discount for undergraduate students?
11. What are the payment methods for tuition fees?
12. What is the biller code for Prince Sultan University?
13. What is the account/bill number for tuition fees?
14. What is the bank deposit information for tuition fees?
"""
