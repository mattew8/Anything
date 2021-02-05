// 브라우저 객체 모델? : 웹 브라우저와 관련된 객체의 집합
// window객체 / location객체 / navigator객체 / history객체 / screen객체 / document객체

// 1. window 객체
// 모든 브라우저 기반 js의 최상위 객체!
// alert(), prompt() 등이 해당

// open(URL, name, features, replace) : 새로운 window 객체 생성(팝업창 형태로!)
var child = window.open('https://naver.com', 'child', 'width=600', 'height=300', true);
// 윈도우 객체를 return! -> 새로운 윈도우 객체에 접근 o
child.document.write('<h1>Hi</h1>');

// // setTimeOut()/clearTimeOut()) , setInterval()/clearInterval() 역시 window 객체 메서드!

// // window 객체 기본 메서드 - 자신의 형태와 위치를 변경할 수 있게끔!
child.moveTo(0,0)
    // moveTo : 절대적인 기준으로 속성 변화
setInterval(function(){
    child.moveBy(10,10);
    // moveBy : 상대적인 기준으로 속성 변화
}, 1000);

// 2. screen 객체
// 웹 브라우저의 화면이 아닌, 운영체제 화면의 속성! -> 대표적으로 width , height
var output = ''
for (var key in screen) {
    output += '/' + key + ':' + screen[key];
}
alert(output)

// 3. location 객체
// 브라우저의 주소 표시줄과 관련된 객체 - 프로토콜 종류 , 호스트 이름 , 문서 위치 등의 정보 가짐
var output2 = ''
for (var key in location) {
    output2 += '/' + key + ':' + location[key];
}
alert(output2)

// -> 페이지 이동시 가장 많이 쓰임!
location = 'https://23life.tistory.com/'
location.href = 'https://23life.tistory.com/'
    // href : 문서의 URL 주소
location.assign('https://23life.tistory.com/')
    // 현재 위치 이동(뒤로 가기 o)
location.replace('https://23life.tistory.com/')
    // 현재 위치 이동(뒤로 가기 x)
location.reload()
    // 새로 고침

// 4. navigator 객체
// 웹 페이지를 실행하고 있는 브라우저에 대한 정보를 가진 객체
var output4 = ''
for (var key in navigator) {
    output4 += '/' + key + ':' + navigator[key];
}
alert(output4)