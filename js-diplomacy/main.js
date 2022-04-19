'use strict';

function colorChanger() {
    const colorChange = document.querySelectorAll(".color-change");

    for (const el of colorChange) {
        el.classList.add('red');
    }
}


function validateInput(evt) {
    evt.preventDefault();    

    const numberInput = document.querySelector('#number-input');
    const input = Number(numberInput.value); // typecast to num
    const frmFeedBack = document.querySelector('#formFeedback');    

    if (input >= 10) {
        frmFeedBack.textContent = "Please enter a smaller number";
    } else if (isNaN(input)) {
        frmFeedBack.textContent = "Please enter a valid number";
    } else {
        frmFeedBack.textContent = "You are good to go!";
    }
}


document.querySelector('.color-changer').addEventListener('click', colorChanger);
document.querySelector('.number-form').addEventListener('submit', validateInput);

