// setting variables
var flip_card_question = document.getElementById("flip-card-question");
var flip_card_answer = document.getElementById("flip-card-answer");
var btnNextQuestion = document.getElementById("btn-next-question");
var questionHeading = document.getElementById("question-heading");
var answerHeading = document.getElementById("answer-heading");
// var audio = new Audio('../sounds/reloading.mp3');
var index = 1;


// setting event listeners
btnNextQuestion.onclick = function(){

    if (index <= totalQuestions) {
        nextQuestion(index);
        // audio.play();

    } else {
        alert("You have completed all the flashcards! Thank you for using this application and good luck !!!");
    }
}


function nextQuestion(indexParamater){
    questionHeading.value = formatQuestionText(indexParamater,totalQuestions);
    answerHeading.value   = formatAnswerText(indexParamater,totalQuestions);
    flip_card_question.innerHTML = questions[indexParamater].question;
    nextQuestionChangeAnswer(index);
    console.log(index);
}

function nextQuestionChangeAnswer(indexParamater){ // separate function to change the answer to add a bit of delay
    setTimeout(function() {
        flip_card_answer.innerHTML = questions[indexParamater].answer;
        index++;
    }, 100 * 1);
}

function formatQuestionText(index,totalQuestions){
    let text = `Question  (${index}/${totalQuestions})`
    return text;
}

function formatAnswerText(index,totalQuestions){
    let text = `Answer  (${index}/${totalQuestions})`
    return text;
}


// console.log(questions.length);
// console.log("---------------");
// console.log(questions[indexParamater].answer);

var totalQuestions =questions.length;

nextQuestion(index); // Setting the first question