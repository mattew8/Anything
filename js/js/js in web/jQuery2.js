// 모든 웹브라우저에서 정상 작동하는 js..? -> jQuery!
$(document).ready(function(){
    // 이벤트 : on() -> 이벤트 연결 / off() -> 이벤트 제거

    // 직접 연결 : 특정 태그에 이벤트 연결, 특정 태그 눌렀을 때 해당 이벤트 발생
    // $(<선택자>).on(<이벤트 이름>, <콜백 함수>) 형태!
    // 이벤트 연결 시 콜백 함수의 매개 변수로 이벤트 객체가 전달!
    // $("h1").on('click', function(event){
    //     var text = $(this).text();
    //     alert(text);
    //     $('<h1></h1>').text($(this).text()).appendTo('body');
            // 현재 직접 연결로 h1태그에 이벤트 걸어준 것
            // but 이러면? 지금 존재하는 h1태그만 이벤트. 새로 생긴 녀석은 x 
    // });

    // 이를 막기 위한 기능? -> 간접 연결
    $('body').on('click', 'h1', function(event){
        // h1 태그에 이벤트 연결x 부모인 body 태그에 이벤트 연결!
        // -> body 태그 내부에서 h1 태그 클릭했을때 --- 를 구현 o
        $('<h1></h1>').text($(this).text()).appendTo('body');
    })

    // 이벤트 제거
    var handler = function(event){
        $('<h2></h2>')
        // h2 태그 생성해서 body 태그에 추가!
            .text($(this).text())
            .click(handler)
            // 추가된 녀석은? 다시 click하면 handler 함수를 작동시킴!
            .appendTo('body');
        $(this).off();
        // 이벤트가 발생한 자기 자신은 이벤트 제거 
        // .off() : 모든 이벤트 제거
        // .off('click') : click 이벤트만 모두 제거
        // .off('click', 'handler) : click 이벤트로 연결한 콜백 함수 중 특정 함수만 제거
    };
    $('h2').on('click', handler);
    // h2 태그를 클릭 하면? -> handler 함수 작동
});


