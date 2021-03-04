// text : 성공 실패 표시해주는 부분
var textElem = document.getElementById('text');

// 컴퓨터 점수
var comScore = 0;
// 컴퓨터 차례
var isComTurn = true;
var comBtn = document.getElementsByClassName('btn-com');

// 유저 점수
var userScore = 0;
var userBtn = document.getElementsByClassName('btn-user');

// 남은 슛 횟수
var shotsLeft = 15;

function onCumputerShoot(){
    // 컴퓨터 차례가 아니면 -> 함수작동x 바로 return
    if (isComTurn === false){
        return;
    }

    // 컴퓨터는 2점슛, 3점슛 중 랜덤하게 선택
    var shootType = Math.random() < 0.5 ? 2 : 3;

    var comScoreElem = document.getElementById('com-score');

    if (shootType === 2){
        if (Math.random() < 0.5){
            textElem.innerHTML = '컴퓨터 2점슛 성공!';
            comScore += 2;
            comScoreElem.innerHTML = comScore;
        } else {
            textElem.innerHTML = '컴퓨터 2점슛 실패!';
        }
    } else {
        if (Math.random() < 0.333){
            textElem.innerHTML = '컴퓨터 3점슛 성공!';
            comScore += 3;
            comScoreElem.innerHTML = comScore;
        } else {
            textElem.innerHTML = '컴퓨터 3점슛 실패!';
        }
    }
    isComTurn = false;
    
    // 컴퓨터가 슛한 후 버튼 비활성화 - getElementsByClassName은 선택된 elem가 하나라도 리턴값은 복수! -> for문으로 받아줘야 함
    for (var i=0; i < comBtn.length; i++){
        comBtn[i].disabled = true;
    }

    // 유저가 슛한 후 버튼 활성화
    for (var i=0; i < userBtn.length; i++){
        userBtn[i].disabled = false
    }
}

function onUserShoot(shootType){
    // 컴퓨터 차례면 -> 함수 작동x 바로 return
    if (isComTurn === true){
        return;
    }

    var userScoreElem = document.getElementById('user-score');

    if (shootType === 2){
        if (Math.random() < 0.5){
            textElem.innerHTML = '2점슛 성공!';
            userScore += 2;
            userScoreElem.innerHTML = userScore;
        } else {
            textElem.innerHTML = '2점슛 실패!';
        }
    } else {
        if (Math.random() < 0.333){
            textElem.innerHTML = '3점슛 성공!';
            userScore += 3;
            userScoreElem.innerHTML = userScore;
        } else {
            textElem.innerHTML = '3점슛 실패!';
        }
    }

    isComTurn = true;
    
    // 컴퓨터가 슛한 후 버튼 활성화
    for (var i=0; i < comBtn.length; i++){
        comBtn[i].disabled = false;
    }

    // 유저가 슛한 후 버튼 비활성화
    for (var i=0; i < userBtn.length; i++){
        userBtn[i].disabled = true;
    }

    // 남은 슛 횟수 차감
    shotsLeft --;

    var shotsLeftElem = document.getElementById('left');
    shotsLeftElem.innerHTML = shotsLeft;

    // 남은 shots가 없을 경우
    if (shotsLeft === 0){
        for (var i=0; i < userBtn.length; i++){
            userBtn[i].disabled = true;
        }
        for (var i=0; i < comBtn.length; i++){
            comBtn[i].disabled = true;
        }

        if (comScore < userScore){
            textElem.innerHTML = "승리!";
        } else if (comScore > userScore){
            textElem.innerHTML = "패배...";
        } else {
            textElem.innerHTML = "비김";
        }
    }
}