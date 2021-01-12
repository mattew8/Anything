console.log('hello');
// ;를 안붙여도 작동은 하지만 꼭 붙이는 게 약속!

console.log('안녕\n하세요');
// \n 줄바꿈 이스케이프 문자

console.log(!(52 > 1221));
// 비교연산자 : True False 반환. 여러 개 있을 경우 왼쪽부터 차례로 연산
// ! : 논리 부정 연산자 / || : 논리합 연산자(or) / && : 논리곱 연산자(and)

let pi = 3.142;
let radius = 10;
// let : 변수 선언
console.log(`hi:${2*pi*radius}`)

const constant = "변경할 수 없어요";
// const = ""; -> error!
// so... 일단 constant를 사용하고, 요류가 발생하면 let 사용
console.log(constant);

let input = 32;
// if문
if (input % 2 == 0){
    console.log("짝수")
}
else {
    console.log("홀수")
}
// switch문
switch (input % 2){
    // 괄호 안에 비교할 값 입력
    case 0:
        // 입력한 값과 case 옆에 있는 표현식이 같다면->다음 문장 차례로 실행
        console.log("짝수요");
        break;
        // break 만나면 탈출
    case 1:
        console.log("홀수요");
        break;
}
// 삼항 연산자
// -> <불 표현식> ? <참> : <거짓>
console.log(input%2 == 0 ? true:false);
let test ;
test = test ? test : "초기화1";
// test가 초기화된 상태라면 undefined
test = test ? test : "초기화2";
console.log(test);

// || 연산자 -> A||B 에서 A가 참이면 A, A가 거짓이라면 B
test = test || "초기화합니다1"
console.log(test);
test = test || "초기화2"
console.log(test);