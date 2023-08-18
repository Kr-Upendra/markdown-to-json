# from extract_data import extract_data_from_file

def prepare_options_json(options, correct_option):
    cur_opt = int(correct_option[-1])
    options_json = []
    for i, option in enumerate(options, start=1):
        is_correct = (i == cur_opt)
        option_json = {
            "content": option,
            "content_type": "MARKDOWN",
            "is_correct": is_correct,
            "multimedia": []
        }
        options_json.append(option_json)
    return {"options": options_json}


