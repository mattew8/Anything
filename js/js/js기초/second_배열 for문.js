let array = [52, 244, '아침', '점심', true, false]
array[0] = 0
console.log(array.length)

let i = 0;
while (i<array.length) {
    console.log(i+"번째"+array[i]);
    i++;
    // ++ -> 변수에 1더함
}

let output = 0;
for (let i = 0; i <= 100; i++){
    output += i;
}
console.log(output);

for (let i in array){
    console.log(`${array[i]}번째`);
}

let output2 = ''
for (let i = 0; i<10; i++){
    for (let j = 0; j<i+1; j++){
        output2 += '*';
    }
    output2 += '\n';
}
console.log(output2)
// for문이나 블록({})안 변수는? 외부에서 사용x 당연

let a = 1;
{
    console.log(a);
    // let a = 2;
    // -> 요놈을 쓰면? 곧 a를 쓸 것이기 때문에 위에 지정한 a는 정의X !!
}

var a = 10;
// let과의 차이? var로 생성한 변수는 모든 곳에서 사용 o
// 절대! 사용하지! 않는 것이! 좋다고! 함!
