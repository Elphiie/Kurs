"use strict";

const startBtn = document.getElementById('start-btn')
const nextBtn = document.getElementById('next-btn')
const qContElmt = document.getElementById('question-container')
const questionElmt = document.getElementById('question')
const ansBtnElmt = document.getElementById('answer-btns')


let shuffledQuestions, currentQuestionIndex

startBtn.addEventListener('click', startGame)
nextBtn.addEventListener('click', () => {
    currentQuestionIndex++
    setNextQuestion()
})

function startGame() {
    startBtn.classList.add('hide')
    shuffledQuestions = questions.sort(() => Math.random() - .5)
    currentQuestionIndex = 0
    qContElmt.classList.remove('hide')
    setNextQuestion()
}

function setNextQuestion () {
    resetState()
    showQuestion(shuffledQuestions[currentQuestionIndex])
}

function showQuestion(question) {
    questionElmt.innerText = question.question
    question.answers.forEach(answer => {
        const button = document.createElement('button')
        button.innerText = answer.text
        button.classList.add('btn')
        if (answer.correct) {
            button.dataset.correct = answer.correct
        }
        button.addEventListener('click', selectAnswer)
        ansBtnElmt.appendChild(button)
    })
}

function resetState() {
    clearStatusClass(document.body)
    nextBtn.classList.add('hide')
    while (ansBtnElmt.firstChild) {
        ansBtnElmt.removeChild(ansBtnElmt.firstChild)
    }
}

function selectAnswer(e) {
    const selectedBtn = e.target
    const correct = selectedBtn.dataset.correct
    setStatusClass(document.body, correct)
    Array.from(ansBtnElmt.children).forEach(button => {
        setStatusClass(button, button.dataset.correct)
    })
    if (shuffledQuestions.length > currentQuestionIndex + 1) {
        nextBtn.classList.remove('hide')
    } else {
        startBtn.innerText = 'Restart'
        startBtn.classList.remove('hide')
    }
}

function setStatusClass(element, correct) {
    clearStatusClass(element)
    if (correct) {
        element.classList.add('correct')
    } else {
        element.classList.add('wrong')
    }
}

function clearStatusClass(element) {
    element.classList.remove('correct')
    element.classList.remove('wrong')
}

const questions  =  [
    {
        question: 'What is 2 + 2?',
        answers: [
            { text: '4', correct: true },
            { text: '22', correct: false },
            { text: '8', correct: false },
            {text: '1', correct: false }
        ]
    },
    {
        question: 'Is javascript fun?',
        answers: [
            { text: 'Yes', correct: false },
            { text: 'No', correct: false },
            { text: 'Maybe', correct: false},
            { text: 'It´s shit', correct: true }
        ]
    },
    {
        question: 'This is a lie',
        answers: [
            {text: 'True', correct: false},
            {text: 'False', correct: false}
        ]
    },
    {
        question: '',     
        answers: [
            {text: 'These are not the droids you are looking foor', correct: true},
            {text: 'These are the droids you are looking foor', correct: false}
        ]
},
    {
        question: 'What is the answer to life?',
        answers: [
            {text: '42', correct: true},
            {text: 'It is yet to be found', correct: false},
            {text: '3.14', correct: false},
            {text: 'Love', correct: false}
        ]
    },
    {
        question: 'What is the funny number?',
        answers: [
            {text: '42069', correct: true},
            {text: '1337', correct: false},
            {text: '3.14', correct: false},
            {text: '1349', correct: false}
        ]
    } 
]