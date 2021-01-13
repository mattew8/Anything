// - window / location 객체
// var input = prompt('글자를 입력해주세요', '여기 입력해주세요')
// // prompt(메시지, 임시 글자) : 입력 받을 수 있는 프롬프트 출력

// alert(input)
// // alert(메시지) : 경고창 출력

// setInterval(function(){
//     // 3초 후에 함수 작동
//     location.assign('https://naver.com');
// }, 3000);
// location.href = '링크'
// location.assign('링크')
// location.replace('링크') -> 뒤로 가기 버튼 x

// - 문서 객체 선택
// document.getElementById(아이디) -> 아이디를 이용해 문서 객체 선택
// document.querySelector(선택자) -> 선택자를 사용해 문서 객체 선택

window.onload = function(){
    // widow.onload -> 화면 구성이 완료되면!
    var header = document.getElementById('header');
    var origianlText = header.innerHTML;
    header.innerHTML = "<i>js로 변경했습니다<i>";
    header.innerHTML += "원래는" + origianlText + "였습니다";
    // html상에서 지정한 id값!
    header.style.color = 'red';
    header.style.border = '1px solid black';

    // - 여러 개의 문서 객체 선택
    // document.getElementsByName(이름) -> name 속성으로 여러 개의 문서 객체 선택
    // document.getElementsByClassName(클래스) -> class 속성으로 여러 개의 문서 객체 선택
    // document.querySelectorAll(선택자) -> 선택자로 여러 개의 문서 객체를 선택
    var headers = document.querySelectorAll('h2');
    for (var i =0; i < headers.length; i++){
        var head2 = headers[i];
        head2.style.color = 'orange';
        head2.innerHTML = 'From JS';
    }

    var image = document.getElementById('image');
    image.src = 'Charlie_Brown.png';
    image.width = 300;
    image.height = 200;
};