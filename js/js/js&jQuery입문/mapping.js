// 배열.map((요소, 인덱스, 배열) => { return 요소 });

// map? : 반복문을 돌며 배열 안의 요소들을 1:1로 짝지어줌(매핑!)
// 어떻게 짝지어줄 것인가 -> 를 정의한 함수를 메서드의 인자로!

const oneTwoThree = [1, 2, 3];
let result = oneTwoThree.map((v) => {
    // 반복문으로 요소를 순회(1,2,3 순서!)하여 각 요소를 어떻게 짝지을지 알려줌
    console.log(v);
    return v;
    // 지금은 그냥 v를 return(똑같음)
});
oneTwoThree; // [1, 2, 3]
result; // [1, 2, 3]
oneTwoThree === result; // false -> 기존 배열 수열이 아닌, 새로운 배열 만듬!

result2 = oneTwoThree2.map((v) => {
    return v + 1;
// v+1을 return
});
console(result2); // [2, 3, 4]


// 배열.reduce((누적값, 현잿값, 인덱스, 요소) => { return 결과 }, 초깃값);

result3 = oneTwoThree3.reduce((acc, cur, i) => {
console.log(acc, cur, i);
// 덧셈 예시
    return acc + cur;
}, 0);
// 0 1 0
// 1 2 1
// 3 3 2
result3; // 6

result4 = oneTwoThree4.reduce((acc, cur) => {
acc.push(cur % 2 ? '홀수' : '짝수');
// 홀수만 배열에 넣도록
    return acc;
}, []);
// 초깃값을 배열로 설정

// 배열 도는 도중 빠져나가고 싶다? -> every나 some 사용하기

result4; // ['홀수', '짝수', '홀수']



