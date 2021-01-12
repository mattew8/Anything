//  익명함수
let 익명함수 = function(){
    console.log("첫줄");
    console.log("둘째줄");
};
익명함수();
// 함수를 호출
console.log(익명함수);
// 함수 자체를 출력

// 화살표함수
let 화살표함수 = () => {
    console.log("첫줄");
    console.log("둘째줄");    
}
화살표함수();
console.log(화살표함수);

// 선언함수
function 선언함수(){
    console.log("첫줄");
    console.log("둘째줄");    
};
// 선언함수 -> 코드 실행되기 전에 생성..!
// 즉 익명 함수는 선언 함수를 무조건! 덮어씀..!!
선언함수();
console.log(선언함수);

function power(x){
    return x * x;
}
console.log(power(10));
console.log(power(20));

// * this? -> 자바스크립트 최상위 객체 또는 외부에서 강제로 연결한 객체
(function(){
    console.log(this)
})();
// (); -> 익명 함수 생성 후 곧바로 호출
(() => {
    console.log(this)
})();
// but 화살표 함수 내에서 this는 자기 자신과 관련된 것만을 나타냄



// 함수 기본 형태
function sum(min, max) {
    let output = 0;
    for (let i = min; i <= max; i++){
        output += i;
    }
    return output;
}
console.log(sum(1,100));

// 매개 변수 초기화
function apple(name, count) {
    count = count || 1;
    console.log(`${name}이/가 ${count}개 있습니다`)
}
apple("사과")

// 콜백 함수 -> 함수를 변수에 저쟝해 다른 함수의 매개 변수로 사용한 것!

// Number() : 문자열을 숫자로 반환
// parseInt() : 문자열을 정수로 반환
// parseFloat() : 문자열을 실수로 반환

setTimeout(function(){
    // setTimeout(함수, 시간) : 특정 시간 후에 함수를 실행!
    console.log("1초가 지났습니다");
}, 1000)
// setInterval(function(){
//     // setInterval(함수, 시간) : 특정 시간마다 함수를 실행!
//     console.log("1초마다 실행됩니다");
// }, 1000)