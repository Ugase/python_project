const maxNumInput = document.getElementById('maxNumInput');
const startGameButton = document.getElementById('startGame');
const maxNumElement = document.getElementById('maxNum');
const guessOutput = document.querySelector('.guessOutput');

let maxNum;
let guess;

function evaluateGuess() {
  const result = prompt(
    `Is your guess higher or lower than ${guess}? (h/l/c)`
  ).toLowerCase();

  if (result === 'h') {
    return 'higher';
  } else if (result === 'l') {
    return 'lower';
  } else if (result === 'c') {
    return 'correct';
  } else {
    alert('Invalid input. Please enter "h" for higher, "l" for lower, or "c" for correct.');
    return null;
  }
}

function binarySearchGuess(maxNum) {
  let low = 0;
  let high = maxNum;

  while (true) {
    guess = Math.floor((low + high) / 2);
    guessOutput.textContent = `My guess is: ${guess}`;

    const result = evaluateGuess();

    if (result === null) {
      continue;
    } else if (result === 'correct') {
      alert(`Yay! I won! The number was ${guess}.`);
      break;
    } else if (result === 'higher') {
      low = guess + 1;
    } else if (result === 'lower') {
      high = guess - 1;
    }
  }
}

startGameButton.addEventListener('click', () => {
  maxNum = parseInt(maxNumInput.value, 10);

  if (isNaN(maxNum) || maxNum < 1) { alert('Please enter a valid maximum number greater than 0.'); return; }

  maxNumElement.textContent = maxNum; binarySearchGuess(maxNum); });