// 문서 객체 모델(Document Object Model)
// 넓은 의미 : 웹 브라우저가 HTML 페이지를 인식하는 방식
// 좁은 의미 : document 객체와 관련된 객체의 집합


// 노드?
// DOM 트리의 각 요소들! -> 요소 노드(=HTML 태그)와 텍스트 노드(요소 노드 안에 있는 글자)로 구분

// 2. 문서 객체 만들기
// 텍스트 노드를 갖는 문서 객체 생성?
// -> 요소 노드 , 텍스트 노드 생성 후 텍스트 노드를 요소 노드에 붙여주면 됨
window.onload = function(){
    var header = document.createElement('h1');
    // 요소 노드 생성
    var textnode = document.createTextNode('hello DOM');
    // 텍스트 노드 생성

    // header.appendChild(textnode);
    // // 요소 노드와 텍스트 노드 연결!
    // document.body.appendChild(header)
    // body 문서 객체에 header 문서 객체 추가!


// 텍스트 노드를 갖지 않는 노드를 생성?
// 대표적으로 img 태그! -> 속성 역시 하나의 노드이므로, 속성 노드를 생성해 요소 노드에 붙여야 함
    var img = document.createElement('img');
    // img라는 노드 생성!
    img.src = 'js&jQuery입문\Charlie_Brown.png';
    // img 태그는 src 지정해줘야!
    img.width = 500;
    img.height = 500;

    // document.body.appendChild(img);

    var output = '';
    output += '<ul>';
    output += '<li>JS</li>'
    output += '</ul>'
    // document.body.innerHTML = output;
    // document.body.innerHTML += '<h1>Hello</h1>';

// 문서 객체 제거   
    var willRemove = document.getElementById('will_remove');
    document.body.removeChild(willRemove)
    // body 문서 객체 바로 아래에 제거하고자 하는 문서 객체가 있으므로 -> removeChild 사용

    willRemove.parentNode.removeChild(willRemove);
    // 일반적으로는 다음과 같이 부모 노드로 이동한 후, 부모 노드에서 자식 노드 삭제
}   