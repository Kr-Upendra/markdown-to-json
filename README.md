# Markdown to JSON Conversion

A Python Script that converts given markdown file's content into JSON but there are some condition in markdown which it needs to be follow which giving markdown to this python script.

## Process

- First We need to create an markdown file based on the condition.
- There are some required fields in markdown which needs to be there otherwise it will generate an error.
- After creating markdown we need to pass it's path at here.
  ```code
  
  default_filename = "your markdown file path"
     
  ```
- After this we need to run main script
  ```bash
  
  python main.py
  
  ```
- If there are no missing required fields it will generate an output file called output.json which will be containing well structured json data extracted from markdown file.

## Input Type 

- It requires a markdown file like following structure..
```

@QUESTION_ID: 52f4fd04-cb72-4372-89c1-0b69c38fa6f4 ---END

@QUESTION_TYPE: CODE_ANALYSIS_MULTIPLE_CHOICE ---END

@CODE: function book(author, title) { return {
author: author, title: title, read: function() { console.log(this); } }; }

const book1 = book("Stan Lee", "The Fantastic Four"); book1.read();

function blog(author, title) { return { author, title, save: () => { console.log(this); } }; }

const blog1 = blog("Mark", "Latest Updates in ES6"); blog1.save(); ---END

```

- It requires a '---END' flag at the end of a specific question.
- Some required fields which needs to be in markdown.
```

["@QUESTION_ID", "@QUESTION_TYPE", "@QUESTION", "@OPTION1", "@OPTION2", "@CORRECT_OPTIONS"]

```

## Output 
- The script will generate an output file of type json.
- Structure of output file
```json
[
  {
    "options": [
      {
        "content": "2",
        "content_type": "MARKDOWN",
        "is_correct": false,
        "multimedia": []
      },
      // other options
    ],
    "question_id": "question id",
    "question_type": "question type",
    "question": "question text",
    "question_content_type": "question content type",
    "code": "code if there is",
    "tag_names": [
      "tag 1",
      "tag 2"
    ],
    "explanation": "explanation text"
  }
]

```
## Different Modules And Their Working

### Main.py
- It is responsible for running all module and also to generate generate output.json file.
- It takes markdown file path as input and generate output.js.

### extract_data.py 
- This is main file where all the magic happen.
- It takes filepath then read it and then extract content that are in the markdown and returns a dictionary containing all the fields.

### check_required.py
- It takes extracted data.
- This file check if the required fields are in markdown or not.
- If required fields not found in the markdown this will not generate output.json file and throw error with the fields that are not provided.
- If everything goes well this will pass to next step.

### options_json.py 
- This module takes options_list and correct_option as argument and prepare a list of options dictionary.
- In the last it will return the prepared list of option's dictionary.

### remove_pre_options.py
- It takes extracted data and remove pre-defined options and return the filtered extracted data without options.

## Test in Local Environment
- If you want to test this script in your local environment follow these steps..
1. Clone the repository
```bash
git clone https://github.com/Kr-Upendra/markdown-to-json.git
```

2. Change directory to markdown-to-json
```bash
cd markdown-to-json
```

3. Run python main file
```bash
python main.py
```

## About 
- It was an assignment project given by [hidden](#)


#### Happy Coding

