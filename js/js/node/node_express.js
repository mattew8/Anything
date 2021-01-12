// express 모듈 설치 -> npm install express
// express 모듈 추출
const { response } = require('express');
const express = require('express');
const request = require('request');

// 서버 생성
const app = express();

// request 이벤트 리스너 설정
app.use((request, response)=>{
    // app.use() -> 요청이 왔을 때 실행할 함수
    response.send(`<h1>hello world</h1>`);
});

app.get('/page/:id', (request, response) => {
    const id = request.params.id;
    response.send(`<h1>${id} Page</h1>`);
    // response.send()->문자열 클라이언트에게 제공 O
});


// 서버 실행
app.listen(8000,() => {
    console.log('Server running at http://127.0.0.1:8000');
});