import json
from check_required import check_required_fields
from options_json import prepare_options_json
from extract_data import extract_data_from_file
from remove_pre_options import remove_items



if __name__ == "__main__":
    default_filename = "input.md" # Replace it with your desired readme file

    question_list = extract_data_from_file(default_filename)  ## Getting extracted question list from file

    # Extracted options so that I can create list of options
    option1 = question_list["option1"]
    option2 = question_list["option2"]
    option4 = question_list["option3"]
    option3 = question_list["option4"]
    correct_options = question_list["correct_options"]
    options_list = [option1, option2, option3, option4]

    options = prepare_options_json(options_list, correct_options) # This simply prepare options json

    result = check_required_fields(question_list) # for checking if required fields are in file or not

    if result == True:
        filtered_questions = remove_items(question_list)  # Cause I have created options so I don't need to pre options list

        tag_elements = filtered_questions["tag_names"] # Get tag names from questions so that it can be created as a list
        tags = tag_elements.split(",")
        filtered_questions["tag_names"] = tags

        combined_result = {**options, **filtered_questions} # combining options and filtered required questions after removing pre options

        result = [] # list to store combined result
        result.append(combined_result)

        # Creating json file and adding content inside json file
        with open("output.json", "w") as json_file:
            json.dump(result, json_file, indent=2)

        print("Conversion completed. JSON file created.")

    else:  # if required fields not given in the file this will handle the error
        print(result)


