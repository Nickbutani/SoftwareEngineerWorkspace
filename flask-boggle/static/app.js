console.log("Boggle game initialized");

let score = 0;
let gameTimer;

document.addEventListener("DOMContentLoaded", function() {
    startTimer();
    
    // Add event listener for the word form submission
    const form = document.getElementById('word-form');
    form.addEventListener('submit', checkWord);
});

function startTimer() {
    gameTimer = setTimeout(function() {
        document.getElementById("word").disabled = true;
        clearTimeout(gameTimer);
    }, 60000);
}

function checkWord(event) {
    event.preventDefault();
    
    let word = document.getElementById('word-input').value.toLowerCase();
    axios.get('/check-word', { params: { word: word } })
         .then(response => {
            let result = response.data.result;
            let message = '';
            if (result === 'ok') {
                score += word.length;
                message = 'Great! +' + word.length + ' points!';
            } else if (result === 'not-on-board') {
                message = 'Word not on board!';
            } else {
                message = 'Not a valid word!';
            }

            document.getElementById('score').innerText = score;
            document.getElementById('message').innerText = message;
            document.getElementById('word-input').value = "";
         })
         .catch(error => console.error('Error:', error));
}


window.onbeforeunload = function() {
    clearTimeout(gameTimer);
};
