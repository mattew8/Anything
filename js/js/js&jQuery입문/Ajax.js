window.onload = function(){
    var request = new XMLHttpRequest();
    // XMLHttpRequest? : js가 Ajax를 사용할 때 사용하는 객체
    // 생성자 함수를 사용해 객체 만들기!

    request.open('GET', '/Home/MyFirstStringAction', false);
    // XMLHttpRequest의 open() 메서드를 사용해 전송 방식(GET등) , 전송 위치(URL) , 방식 지정

    request.send()
    // send() 메서드를 사용해 XMLHttpRequest를 보내기!

    alert(request.responseText);
    // 성공적으로 보내지면 XMLHttpRequest 객체의 responseText 속성으로 답장이 옴!

    document.body.innerHTML = request.responseText
};

// 코드 리뷰
function save_ans(){
    var ans = $("input:radio[name=name]:checked").val();
    var url = '/save_ans?ans='+ans
    // XMLHttpRequest를 전송할 위치를 지정해주려고!

    var req = new XMLHttpRequest();
    // XMLHttpRequest 객체 생성

    req.onreadystatechange = function() {
        // XMLHttpRequest의 속성 -> onreadystatechange : 객체에 변화가 발생하면..!

        if (this.readyState == 4 && this.status == 200) {
            // onreadystatechange에 등록된 콜백 함수는 readyState라는 프로퍼티 값이 변경될 때마다 호출!
            
            alert(req.responseText)
            // 성공적으로 보내질 경우 responseText로 답장!
        };
    };
    req.open("GET", url, true);
    // XMLHttpRequest의 전송 방식-GET , 전송 위치-url , 방식은 true로!

    req.send();
    // XMLHttpRequest 요청 보내기
}