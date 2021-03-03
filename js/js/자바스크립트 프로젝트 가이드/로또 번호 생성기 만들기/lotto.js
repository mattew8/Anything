// 1부터 45까지 숫자가 담긴 list
var lottoList = []
for (var i = 1; i <= 45; i++) {
    lottoList.push(i);
}

// 결과(뽑은 공) list
var result = [];

// 랜덤 로또 번호 선정
for (var i = 1; i<=6; i++){
    // 랜덤으로 index 선택
    var index = Math.floor(Math.random()*lottoList.length)

    // 랜덤으로 선택된 1부터 45까지의 숫자
    var num = lottoList[index]

    // 선택된 index자리의 숫자를 lottoList에서 제거(뽑았으니까)
    // slice(제거할 index , 해당 index기준 몇개 제거할 것인지)
    lottoList.slice(index, 1);

    result.push(num);
}