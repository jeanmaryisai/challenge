//circle start
let progressBar = document.querySelector('.e-c-progress');
let indicator = document.getElementById('e-indicator');
let pointer = document.getElementById('e-pointer');
let length = Math.PI * 2 * 100;
progressBar.style.strokeDasharray = length;

function update(value, timePercent) {
    var offset = -length - length * value / (timePercent);
    progressBar.style.strokeDashoffset = offset;
    pointer.style.transform = `rotate(${360 * value / (timePercent)}deg)`;
};
//circle ends
const displayOutput = document.querySelector('.display-remain-time')
const pauseBtn = document.getElementById('pause');
const setterBtns = document.querySelectorAll('button[data-setter]');
let intervalTimer;
let timeLeft;
let wholeTime = 0.5 * 60; // manage this to set the whole time 
let isPaused = false;
let isStarted = false;

update(wholeTime, wholeTime); //refreshes progress bar
displayTimeLeft(wholeTime);

function changeWholeTime(seconds) {
    if ((wholeTime + seconds) > 0) {
        wholeTime += seconds;
        update(wholeTime, wholeTime);
    }
}
for (var i = 0; i < setterBtns.length; i++) {
    setterBtns[i].addEventListener("click", function(event) {
        var param = this.dataset.setter;
        switch (param) {
            case 'minutes-plus':
                changeWholeTime(1 * 60);
                break;
            case 'minutes-minus':
                changeWholeTime(-1 * 60);
                break;
            case 'seconds-plus':
                changeWholeTime(1);
                break;
            case 'seconds-minus':
                changeWholeTime(-1);
                break;
        }
        displayTimeLeft(wholeTime);
    });
}

function timer(seconds) { //counts time, takes seconds
    let remainTime = Date.now() + (seconds * 1000);
    displayTimeLeft(seconds);

    intervalTimer = setInterval(function() {
        timeLeft = Math.round((remainTime - Date.now()) / 1000);
        if (timeLeft < 0) {
            clearInterval(intervalTimer);
            isStarted = false;
            setterBtns.forEach(function(btn) {
                btn.disabled = false;
                btn.style.opacity = 1;
            });
            displayTimeLeft(wholeTime);
            pauseBtn.classList.remove('pause');
            pauseBtn.classList.add('play');
            return;
        }
        displayTimeLeft(timeLeft);
    }, 1000);
}

function pauseTimer(event) {
    if (isStarted === false) {
        timer(wholeTime);
        isStarted = true;
        this.classList.remove('play');
        this.classList.add('pause');

        setterBtns.forEach(function(btn) {
            btn.disabled = true;
            btn.style.opacity = 0.5;
        });
    } else if (isPaused) {
        this.classList.remove('play');
        this.classList.add('pause');
        timer(timeLeft);
        isPaused = isPaused ? false : true
    } else {
        this.classList.remove('pause');
        this.classList.add('play');
        clearInterval(intervalTimer);
        isPaused = isPaused ? false : true;
    }
}

function displayTimeLeft(timeLeft) { //displays time on the input
    let minutes = Math.floor(timeLeft / 60);
    let seconds = timeLeft % 60;
    let displayString = `${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    displayOutput.textContent = displayString;
    update(timeLeft, wholeTime);
}
pauseBtn.addEventListener('click', pauseTimer);


function getToken(name) {
    var cookiePair = null;
    if (document.cookie && document.cookie !== '') {
        var cookieArr = document.cookie.split(";");
        for (var i = 0; i, cookieArr.length; i++) {
            cookiePair = cookieArr[i].trim();
            if (cookiePair.substring(0, name.length + 1) === (name + '=')) {
                return decodeURIComponent(cookiePair.substring(name.length + 1));
            }
        }
    }
    return cookiePair;
}

var csrftoken = getToken('csrftoken');
var numero_global = 0

function research(url) {
    let numero = document.getElementById('input-format').value
    let urll = url.slice(0, 14) + numero
    fetch(urll, {
            method: 'POST',
            headers: {
                'CONTENT-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'name': 'add' })
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            if (data == 404) {
                location.reload()
            } else {
                const obj = JSON.parse(data)
                document.getElementById('info').style.display = 'none'
                document.getElementById('qst_number').innerHTML = 'Question #' + obj.number
                document.getElementById('qst_body').innerHTML = obj.enoncee
                document.getElementById('rpnse_body').innerHTML = obj.reponse
                if (obj.is_unique == true)
                    {
                        document.getElementById('accordion-two').classList.add('accordion-danger-solid')
                    }
                document.getElementById('question').style.display = 'block'
                numero_global = obj.number
            }
        })

}