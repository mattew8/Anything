// 현재 파일 경로 출력
// console.log(__filename);

// 이벤트 연결 매소드 on
// -> on(이벤트 이름, 이벤트 핸들러)

process.on('exit', (code) => {
    // exit -> 프로세스 종료시 발생
    console.log('프로세스 종료');
    console.log(`exit 이벤트 매개 변수:${code}`);
});

process.on('uncaughtException', (error)=> {
    // uncaughtException -> 예외 일어날 시 발생
    console.log('예외 발생');
    console.log(`uncaughtException 이벤트 매개 변수 ${error}`)
});

// error.error.error();
// 강제로 예외 발생

// os 모듈 사용
const os = require('os');

// url 모듈 사용
const url = require('url');
const parsedObject = url.parse('https://naver.com')
console.log(parsedObject);

// File System 모듈
// -> 파일 이름 수정, 이동, 제거 등의 메소드 O
const fs = require('fs');

// request 모듈
// 우선 npm request로 설치
const request = require('request');

const url = 'https://opentutorials.org/course/1375/6620.html';
request(url, (error, response, body) => {
    console.log(body);
})