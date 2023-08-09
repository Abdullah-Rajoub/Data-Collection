import tiktoken


def concat_chunks(input_array):
    encoding = tiktoken.get_encoding("cl100k_base")
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    normal_length_output = []
    big_length_output = []
    current_string = ""

    for string in input_array:
        if (
            len(encoding.encode(current_string)) == 0
            and len(encoding.encode(string)) > 3000
        ):
            big_length_output.append(string)
        elif len(encoding.encode(current_string)) > 3000:
            big_length_output.append(current_string)
            current_string = string
        elif (
            len(encoding.encode(current_string)) + len(encoding.encode(string)) <= 3000
        ):
            current_string += string
        else:
            normal_length_output.append(current_string)
            current_string = string
    if len(encoding.encode(current_string)) > 3000:
        big_length_output.append(current_string)
    else:
        normal_length_output.append(current_string)
    if len(normal_length_output) == 1 and len(normal_length_output[0]) == 0:
        return {
            "normal_length_output": [],
            "big_length_output": big_length_output,
        }

    return {
        "normal_length_output": normal_length_output,
        "big_length_output": big_length_output,
    }


def concat_questions(input_array):
    encoding = tiktoken.get_encoding("cl100k_base")
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    normal_length_output = []
    big_length_output = []
    current_string = ""

    for string in input_array:
        if (
            len(encoding.encode(current_string)) == 0
            and len(encoding.encode(string)) > 500
        ):
            big_length_output.append(string)
        elif len(encoding.encode(current_string)) > 500:
            big_length_output.append(current_string)
            current_string = string + "\n"
        elif len(encoding.encode(current_string)) + len(encoding.encode(string)) <= 300:
            current_string += string + "\n"
        else:
            normal_length_output.append(current_string)
            current_string = string + "\n"
    if len(encoding.encode(current_string)) > 500:
        big_length_output.append(current_string)
    else:
        normal_length_output.append(current_string)
    return {
        "normal_length_output": normal_length_output,
        "big_length_output": big_length_output,
    }
