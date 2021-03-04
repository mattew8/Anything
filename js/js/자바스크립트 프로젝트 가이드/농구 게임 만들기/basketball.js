// text : 성공 실패 표시해주는 부분
var textElem = document.getElementById('text');

// 컴퓨터/유저 점수
var comScore = 0;
var userScore = 0;

// 남은 슛 횟수
var shotsLeft = 5;

// 성공 실패 text 보여주는 함수
function showText(texts){
    textElem.innerHTML = texts;
}

// 컴퓨터 점수 계산 함수
function updateComScore(score){
    comScore += score

    var comScoreElem = document.getElementById('com-score');
    comScoreElem.innerHTML = comScore;
}

// 유저 점수 계산 함수
function updateUserScore(score){
    userScore += score

    var userScoreElem = document.getElementById('user-score');
    userScoreElem.innerHTML = userScore;
}

// 컴퓨터 버튼 활성화/비활성화 함수
function disableComBtn(flag){
    var comBtn = document.getElementsByClassName('btn-com');
    // 컴퓨터가 슛한 후 버튼 비활성화 - getElementsByClassName은 선택된 elem가 `하나라도 리턴값은 복수! -> for문으로 받아줘야 함
    for (var i=0; i < comBtn.length; i++){
        comBtn[i].disabled = flag;
    }    
}

// 유저 버튼 활성화/비활성화 함수
function disableUserBtn(flag){
    var userBtn = document.getElementsByClassName('btn-user');
    for (var i=0; i < userBtn.length; i++){
        userBtn[i].disabled = flag;
    }    
}

function onCumputerShoot(){
    // 컴퓨터 차례가 아니면 -> 함수작동x 바로 return
    // if (isComTurn === false){
    //     return;
    // }

    // 컴퓨터는 2점슛, 3점슛 중 랜덤하게 선택
    var shootType = Math.random() < 0.5 ? 2 : 3;

    if (shootType === 2){
        if (Math.random() < 0.5){
            showText('컴퓨터 2점슛 성공!');
            updateComScore(2);
        } else {
            showText('컴퓨터 2점슛 실패!');
        }
    } else {
        if (Math.random() < 0.333){
            showText('컴퓨터 3점슛 성공!');
            updateComScore(3);
        } else {
            showText('컴퓨터 3점슛 실패!');
        }
    }
    // isComTurn = false;
    
    disableUserBtn(false);
    disableComBtn(true);
}

function onUserShoot(shootType){
    // 컴퓨터 차례면 -> 함수 작동x 바로 return
    // if (isComTurn === true){
    //     return;
    // }

    if (shootType === 2){
        if (Math.random() < 0.5){
            showText('2점슛 성공!');
            updateUserScore(2)
        } else {
            showText('2점슛 실패!');
        }
    } else {
        if (Math.random() < 0.333){
            showText('3점슛 성공!');
            updateUserScore(3);
        } else {
            showText('3점슛 실패!');
        }
    }
    // isComTurn = true;
    
    
    disableUserBtn(true);
    disableComBtn(false);

    // 남은 슛 횟수 차감
    shotsLeft --;

    var shotsLeftElem = document.getElementById('left');
    shotsLeftElem.innerHTML = shotsLeft;

    // 남은 shots가 없을 경우
    if (shotsLeft === 0){
        disableComBtn(true);
        disableUserBtn(true);

        if (comScore < userScore){
            textElem.innerHTML = "승리!";
        } else if (comScore > userScore){
            textElem.innerHTML = "패배...";
        } else {
            textElem.innerHTML = "비김";
        }
    }
}

