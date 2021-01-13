// js 이벤트
// 마우스/키보드/HTML프레임/HTML입력양식/사용자인터페이스/구조변화/터치

function buttonClick(){
    alert('클릭');
}

// window.onload = function(){ 
//     var button = document.getElementById('button');
//     button.onclick = function(){
//         this.innerHTML = this.innerHTML + '★';
//         // 이벤트 리스터 내부 this 키워드 -> 이벤트를 발생한 자기 자신!
//         // 즉 this.innerHTML -> 자기 자신의 문자를 변경
//     }
// }


// event 객체
// event가 발생했을 때 -> event 객체 사용하면 누가 언제 어디서 등 관련 정보 알 수 O
// window.onload = function(event){
//     // event = 이벤트 객체!
//     alert(event);
// };

window.onload = function(event){
    var button = document.getElementById('button');
    button.onclick = function(){
        return false;
        // html 태그의 기본 이벤트 제거!
    };
};
