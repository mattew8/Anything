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

// result를 오름차순으로 정렬 -> 그냥 sort()사용하면x!
// why) 숫자 정렬시 문자열 반환 후 정렬한다는 특징 때문에 의도한대로 작동x
// so sort()함수가 인자로 받을 수 있는 비교 함수를 새로 만들어(지금은 익명함수 형태로), result의 모든 요소를 a-b를 통해 비교 후 줄세우기!
result.sort(function(a,b){
    return a-b;
    // a-b가 양수면 sort를 통해 a는 b의 뒤에 위치(반대 마찬가지!) -> 숫자 정렬 가능!
})

// i번째 result를 html에 입력
for (var i=0; i<6; i++) {
    document.write('<span class="ball">' + result[i] + '</span>');
}