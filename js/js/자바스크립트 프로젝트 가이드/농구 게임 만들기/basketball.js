// text : 성공 실패 표시해주는 부분
var textElem = document.getElementById('text');

// 컴퓨터 점수
var comScore = 0;

// 유저 점수
var userScore = 0;

function onCumputerShoot(){
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
}

function onUserShoot(shootType){
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
}