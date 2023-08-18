required_fields = ["question_id", "question_type", "question", "option1", "option2", "correct_options"]

def check_required_fields(data_dict):
    missing_fields = [field for field in required_fields if field not in data_dict]
    if missing_fields: 
        return "Please provide required fields:", ", ".join(missing_fields)
    else:
        return True
