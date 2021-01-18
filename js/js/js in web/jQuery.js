// 모든 웹브라우저에서 정상 작동하는 js..? -> jQuery!
$(document).ready(function(){
    // window.onload와 유사한 기능 -> 웹 페이지를 모두 불러오면~~
    var $headers = $('h1');
    // 왜 $? -> 변수! jQuery문서 객체가 들어 있는 객체는 앞에 $ 관례
    for (var i = 0; i < $headers.length; i++){
        if (i % 2 == 1){
        var domElment = $headers.get(i);
        // get(i) -> i번째 요소를 추출
        $(domElment).css('backgroundColor', 'yellow');
        }
    }
    // alert($('p').text());
    // 모든 p태그 문자 출력
    // alert($('p').html());
    // 첫 번째로 선택된 p태그 문자 출력

    // 내부 문자 변경
    $('h1').text('<h1>바꾼 문자</h1>')
    // text()는 html태그 사용 x
    $('h2').html('<h2>html로 바꾼 문자</h2>')
    // html()은 html태그 사용 O
    $('h2').css({
        color:'red',
    })

    // attr() -> 속성 가져오기
    // $('img').attr('src')
    // $('img').css({
    //     src: 'http://placehold.it/100x100',
    // });
    // 속성 제어 -> attr 통해 내부 속성 조작
    $('img').each(function (index, element){
        $(this).attr('src', 'http://placehold.it/' + (index+1)*100+'x100');
    });

    // 문서 객체 생성 -> $() 함수의 매개 변수에 html문자열 입력
    // -> 글자, 속성, 스타일 조작 o
    $('<h1></h1>')
    .text('안녕하세요')
    .attr('data-test', 'test')
    .css({
        backgroundColor:'red',
        color:'white'
    })
    // 아직은 js코드로만 존재! -> 문서 객체 추가 메소드 사용해야 출력o
    .appendTo('body');
    // $(<A>).prependTo(<B>) : A를 B 안쪽 앞에 추가
    // $(<A>).apendTo(<B>) : A를 B 안쪽 뒤에 추가
    // $(<A>).InsertBefore(<B>) : A를 B 앞에 추가
    // $(<A>).apendTo(<B>) : A를 B 뒤에 추가
}); 

// - jQuery 객체 생성
// $(document) : 일반 문서 객체로 jQuery 객체 생성 -> 기존 문서 객체 선택 o 새로운 문서 객체 생성 o
// $('h1') : CSS 선택자로 jQuery 객체 생성 -> 기존 문서 객체 선택 o
// $('<h1></h1>') : HTML 문자열로 jQuery 객체 생성 -> 새로운 문서 객체 생성 o

// - 문서 객체 선택
// $('h1') : h1 태그 선택
// $('h1.logo') : h1 태그 중 logo라는 class 가진 태그 선택
// $('#head') : id가 head인 태그 선택
// $('input[type=submit]') : input 태그 중 type이 submit인 태그 선택
// $('h1').parent() : h1 태그의 부모 태그 선택
// $('h1').find('i') : h1 태그 내부에 있는 i 태그 선택

