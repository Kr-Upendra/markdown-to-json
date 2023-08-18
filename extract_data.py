import re

def extract_data_from_file(filename):
    content = open(filename, "r").read()
    questions = re.split(r'---END', content)

    question_dict = {}
    for question_text in questions[:-1]:
        lines = question_text.strip().split("\n")
        current_key = None 
        current_value = ""
        for line in lines: 
            if line.startswith("@"):
                if current_key is not None:
                    question_dict[current_key.lower()] = current_value.strip()
                current_key, current_value = line[1:].strip().split(":", 1)
            else:
                current_value += line + '\n'
        if current_key is not None:
            question_dict[current_key.lower()] = current_value.strip()

    return question_dict


