@QUESTION_ID: 52f4fd04-cb72-4372-89c1-0b69c38fa6f4 ---END

@QUESTION_TYPE: CODE_ANALYSIS_MULTIPLE_CHOICE ---END

@QUESTION:

Considering the given code snippet, which of the following options is correct?<br/><br/>Statement-1: In the <b>read</b> method, <i>this</i> refers to the <i>window</i> object.<br/>Statement-2: In the <b>save</b> method, <i>this</i> refers to the <b>blog1</b> object.<br> ---END

@QUESTION_CONTENT_TYPE: MARKDOWN ---END

@CODE:
function book(author, title) {
return {  
 author: author,
title: title,
read: function() {
console.log(this);
}
};
}

const book1 = book("Stan Lee", "The Fantastic Four");
book1.read();

function blog(author, title) {
return {
author,
title,
save: () => {
console.log(this);
}
};
}

const blog1 = blog("Mark", "Latest Updates in ES6");
blog1.save(); ---END

@OPTION1:2
@OPTION2:3
@OPTION3:4
@OPTION4:5
@CORRECT_OPTIONS: OPTION4 ---END

@TAG_NAMES: markdown, html ---END
@EXPLANATION: Nothing ---END
