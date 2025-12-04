<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Who Wants to Be a MET Expert?</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('/api/placeholder/800/600');
            background-color: #003f7f;
            background-size: cover;
            background-position: center;
            color: #fff;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: rgba(0, 63, 127, 0.85);
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }
        .question {
            font-size: 24px;
            margin-bottom: 20px;
            padding: 15px;
            background-color: rgba(0, 91, 187, 0.6);
            border-radius: 5px;
        }
        .answers {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        .answer {
            padding: 15px;
            border: 2px solid #fff;
            border-radius: 5px;
            cursor: pointer;
            background-color: rgba(0, 91, 187, 0.4);
            transition: background-color 0.3s;
        }
        .answer:hover {
            background-color: rgba(0, 91, 187, 0.6);
        }
        .answer.correct {
            background-color: rgba(0, 255, 0, 0.6);
        }
        .answer.wrong {
            background-color: rgba(255, 0, 0, 0.6);
        }
        .lifeline {
            margin-top: 20px;
            margin-right: 10px;
            padding: 10px 20px;
            background-color: #00a8cc;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .lifeline:disabled {
            background-color: #666;
            cursor: not-allowed;
        }
        .next-button, .reset-button {
            margin-top: 20px;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .next-button {
            display: none;
            background-color: #00a8cc;
            color: white;
        }
        .reset-button {
            background-color: #dc3545;
            color: white;
            margin-left: 10px;
        }
        .score {
            font-size: 20px;
            margin: 15px 0;
            color: #ffd700;
        }
        .signature {
            margin-top: 30px;
            font-size: 14px;
            color: #ccc;
        }
        .signature a {
            color: #00a8cc;
            text-decoration: none;
        }
        .signature a:hover {
            text-decoration: underline;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }
        h1 {
            color: #ffd700;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Who Wants to Be a MET Expert?</h1>
        <div class="score" id="score">Current Prize: $0</div>
        <div class="question" id="question"></div>
        <div class="answers">
            <div class="answer" id="answer1" onclick="checkAnswer(0)"></div>
            <div class="answer" id="answer2" onclick="checkAnswer(1)"></div>
            <div class="answer" id="answer3" onclick="checkAnswer(2)"></div>
            <div class="answer" id="answer4" onclick="checkAnswer(3)"></div>
        </div>
        <div>
            <button class="lifeline" id="lifeline5050" onclick="useLifeline('5050')">50:50</button>
            <button class="lifeline" id="lifelineAudience" onclick="useLifeline('audience')">Ask the Audience</button>
            <button class="lifeline" id="lifelinePhone" onclick="useLifeline('phone')">Phone a Friend</button>
        </div>
        <div class="button-container">
            <button class="next-button" id="nextButton" onclick="nextQuestion()">Next Question</button>
            <button class="reset-button" id="resetButton" onclick="resetGame()">Reset Game</button>
        </div>
        
        <div class="signature">
                    &copy; 2025 Daniel Rojas :: TΣʃ :: &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
                </div>
    </div>

    <script>
        const questions = [
            {
                question: "What is the primary purpose of the Michigan English Test (MET)?",
                answers: [
                    "For university admissions worldwide",
                    "For placement in English programs and institutional requirements",
                    "For immigration purposes",
                    "For business employment only"
                ],
                correct: 1,
                money: 100
            },
            {
                question: "Which skills does the MET assess?",
                answers: [
                    "Listening, Reading, and Writing only",
                    "Listening and Reading only",
                    "Listening, Reading, Writing, and sometimes Speaking",
                    "Speaking and Writing only"
                ],
                correct: 2,
                money: 200
            },
            {
                question: "How is the MET formatted?",
                answers: [
                    "Consistently standardized across all institutions",
                    "Varies depending on the institution",
                    "Only computer-based",
                    "Only paper-based"
                ],
                correct: 1,
                money: 300
            },
            {
                question: "How is the MET scored?",
                answers: [
                    "As pass/fail only",
                    "On a scale of 1-9",
                    "With percentages only",
                    "With scaled scores, often aligned with CEFR"
                ],
                correct: 3,
                money: 500
            },
            {
                question: "What does the Listening section of the MET assess?",
                answers: [
                    "Comprehension of spoken English",
                    "Ability to take dictation",
                    "Pronunciation skills",
                    "Oral fluency"
                ],
                correct: 0,
                money: 1000
            },
            {
                question: "What does the Reading section of the MET assess?",
                answers: [
                    "Spelling ability",
                    "Grammar knowledge only",
                    "Comprehension of written English",
                    "Vocabulary memorization"
                ],
                correct: 2,
                money: 2000
            },
            {
                question: "What does the Writing section of the MET assess?",
                answers: [
                    "Handwriting quality",
                    "Writing ability",
                    "Memorization of essay templates",
                    "Typing speed"
                ],
                correct: 1,
                money: 4000
            },
            {
                question: "What CEFR levels are MET scores typically aligned with?",
                answers: [
                    "A1-B2 levels",
                    "B1-C2 levels",
                    "A2-C1 levels",
                    "C1-C2 levels only"
                ],
                correct: 2,
                money: 8000
            },
            {
                question: "How does the MET's recognition compare to tests like IELTS/TOEFL?",
                answers: [
                    "More widely recognized",
                    "Equally recognized",
                    "Not as widespread",
                    "Recognized only in Michigan"
                ],
                correct: 2,
                money: 16000
            },
            {
                question: "What is the primary focus of the MET?",
                answers: [
                    "Academic English proficiency",
                    "Business English proficiency",
                    "General English proficiency",
                    "Technical English proficiency"
                ],
                correct: 2,
                money: 32000
            },
            {
                question: "How is the MET typically administered?",
                answers: [
                    "Only by testing centers",
                    "Often by the institutions themselves",
                    "Only online",
                    "Only by certified proctors"
                ],
                correct: 1,
                money: 64000
            },
            {
                question: "How standardized is the MET compared to IELTS/TOEFL?",
                answers: [
                    "More standardized",
                    "Equally standardized",
                    "Less standardized",
                    "Not standardized at all"
                ],
                correct: 2,
                money: 100000
            },
            {
                question: "What is the primary use of the MET?",
                answers: [
                    "For university admissions",
                    "As a course placement tool",
                    "For employment screening",
                    "All of the above"
                ],
                correct: 3,
                money: 150000
            },
            {
                question: "How flexible is the MET format?",
                answers: [
                    "Not flexible - completely standardized",
                    "Format and content can vary",
                    "Only the timing is flexible",
                    "Only the speaking section is flexible"
                ],
                correct: 1,
                money: 200000
            },
            {
                question: "Who typically provides preparation materials for the MET?",
                answers: [
                    "Only third-party publishers",
                    "Only online resources",
                    "Materials may be provided by the institution",
                    "No preparation materials are available"
                ],
                correct: 2,
                money: 500000
            },
            {
                question: "What is unique about the MET's cost structure?",
                answers: [
                    "Always free",
                    "Fixed global price",
                    "Cost varies",
                    "Subscription-based only"
                ],
                correct: 2,
                money: 750000
            },
            {
                question: "Which organization developed the Michigan English Test?",
                answers: [
                    "University of Michigan",
                    "Cambridge Assessment English",
                    "Educational Testing Service (ETS)",
                    "British Council"
                ],
                correct: 0,
                money: 1000000
            },
            {
                question: "What type of English does the MET primarily test?",
                answers: [
                    "British English only",
                    "American English only",
                    "Academic English only",
                    "Various English dialects"
                ],
                correct: 3,
                money: 1500000
            },
            {
                question: "How does the MET differ from the TOEFL?",
                answers: [
                    "The MET tests lower proficiency levels",
                    "The MET is for business professionals only",
                    "The MET is paper-based only",
                    "The MET is only for university entrance"
                ],
                correct: 0,
                money: 2000000
            },
            {
                question: "What makes the MET suitable for institutional use?",
                answers: [
                    "Its high cost",
                    "Its flexibility and focus on placement",
                    "Its focus on business English",
                    "Its strict standardization"
                ],
                correct: 1,
                money: 5000000
            }
        ];

        let currentQuestion = 0;
        let lifelinesUsed = { '5050': false, 'audience': false, 'phone': false };
        let currentMoney = 0;

        function loadQuestion() {
            const question = questions[currentQuestion];
            document.getElementById('question').textContent = question.question;
            
            const answers = document.querySelectorAll('.answer');
            answers.forEach((answer, index) => {
                answer.textContent = question.answers[index];
                answer.classList.remove('correct', 'wrong');
                answer.style.visibility = 'visible';
            });
            
            document.getElementById('nextButton').style.display = 'none';
            document.getElementById('score').textContent = `Current Prize: $${currentMoney}`;
        }

        function checkAnswer(selected) {
            const correct = questions[currentQuestion].correct;
            const answers = document.querySelectorAll('.answer');
            
            answers[selected].classList.add(selected === correct ? 'correct' : 'wrong');
            if (selected === correct) {
                currentMoney = questions[currentQuestion].money;
                document.getElementById('score').textContent = `Current Prize: $${currentMoney}`;
            } else {
                currentMoney = 0;
                document.getElementById('score').textContent = `Game Over! Final Prize: $0`;
                endGame();
            }
            
            document.getElementById('nextButton').style.display = 'block';
        }

        function useLifeline(lifeline) {
            const question = questions[currentQuestion];
            const correct = question.correct;
            const answers = document.querySelectorAll('.answer');

            if (lifeline === '5050' && !lifelinesUsed['5050']) {
                lifelinesUsed['5050'] = true;
                const incorrectAnswers = [0, 1, 2, 3].filter(i => i !== correct);
                // Randomly choose two incorrect answers to hide
                incorrectAnswers.sort(() => Math.random() - 0.5);
                incorrectAnswers.slice(0, 2).forEach(index => {
                    answers[index].style.visibility = 'hidden';
                });
                document.getElementById('lifeline5050').disabled = true;
            } else if (lifeline === 'audience' && !lifelinesUsed['audience']) {
                lifelinesUsed['audience'] = true;
                alert(`The audience suggests answer ${String.fromCharCode(65 + correct)}!`);
                document.getElementById('lifelineAudience').disabled = true;
            } else if (lifeline === 'phone' && !lifelinesUsed['phone']) {
                lifelinesUsed['phone'] = true;
                alert(`Your MET expert friend suggests answer ${String.fromCharCode(65 + correct)}!`);
                document.getElementById('lifelinePhone').disabled = true;
            }
        }

        function nextQuestion() {
            currentQuestion++;
            if (currentQuestion < questions.length) {
                loadQuestion();
            } else {
                endGame(true);
            }
        }

        function resetGame() {
            currentQuestion = 0;
            currentMoney = 0;
            lifelinesUsed = { '5050': false, 'audience': false, 'phone': false };
            
            const container = document.querySelector('.container');
            container.innerHTML = `
                <h1>Who Wants to Be a MET Expert?</h1>
                <div class="score" id="score">Current Prize: $0</div>
                <div class="question" id="question"></div>
                <div class="answers">
                    <div class="answer" id="answer1" onclick="checkAnswer(0)"></div>
                    <div class="answer" id="answer2" onclick="checkAnswer(1)"></div>
                    <div class="answer" id="answer3" onclick="checkAnswer(2)"></div>
                    <div class="answer" id="answer4" onclick="checkAnswer(3)"></div>
                </div>
                <div>
                    <button class="lifeline" id="lifeline5050" onclick="useLifeline('5050')">50:50</button>
                    <button class="lifeline" id="lifelineAudience" onclick="useLifeline('audience')">Ask the Audience</button>
                    <button class="lifeline" id="lifelinePhone" onclick="useLifeline('phone')">Phone a Friend</button>
                </div>
                <div class="button-container">
                    <button class="next-button" id="nextButton" onclick="nextQuestion()">Next Question</button>
                    <button class="reset-button" id="resetButton" onclick="resetGame()">Reset Game</button>
                </div>
                
                <div class="signature">
                    &copy; 2025 Daniel Rojas :: TΣʃ :: &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
                </div>
            `;
            
            
            document.getElementById('lifeline5050').disabled = false;
            document.getElementById('lifelineAudience').disabled = false;
            document.getElementById('lifelinePhone').disabled = false;
            
            loadQuestion();
        }

      function endGame(completed = false) {
    const container = document.querySelector('.container');
    
    if (completed) {
        container.innerHTML = `
            <h1>Congratulations!</h1>
            <div class="score">You've won $${currentMoney}!</div>
            <p>You've conquered the MET Challenge and won 5 million dollars!</p>
            <p>You've proven yourself to be a true Michigan English Test expert!</p>
            <button class="reset-button" id="resetButton" onclick="resetGame()">Play Again</button>
            <div class="signature">
                &copy; 2025 Daniel Rojas :: TΣʃ :: &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
            </div>
        `;
    } else {
        container.innerHTML = `
            <h1>Game Over!</h1>
            <div class="score">Final Prize: $${currentMoney}</div>
            <p>Better luck next time!</p>
            <p>You've shown your knowledge of the Michigan English Test!</p>
            <button class="reset-button" id="resetButton" onclick="resetGame()">Play Again</button>
            <div class="signature">
                &copy; 2025 Daniel Rojas :: TΣʃ :: &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
            </div>
        `;
    }
}

        window.onload = loadQuestion;
    </script>
</body>
</html>
