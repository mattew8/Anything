// 기본 내장 객체
// 1. 기본 자료형
// : js 여섯 자료형 중 숫자, 문자, 불리언 세 가지!
// 객체와의 차이? 크게 구별은x! 속성과 메서드 추가할 수 있느냐 없느냐 차이
var primitiveNumber = 233;
var objectNumber = new Number(233);

// 2. Object 객체
// : js 가장 기본적인 내장 객체 -> 모든 객체는 Object 객체의 메서드를 공통으로 가짐
var object = {};
var object = new Object(); // 7가지 메서드 가짐

// 3. Number 객체

// 4. String 객체
var stringFromLiteral = 'Hi'
var stringFromConstructor = new String('Hi!')
stringFromConstructor.length  // 문자열 길이 -> length 속성

// string 객체의 메서드 -> 자기 자신을 변화시키지 않고 return!
stringFromLiteral.toUpperCase()
console(stringFromLiteral) // 변화x
stringFromLiteral = stringFromLiteral.toUpperCase() // 변화 o

// HTML 메서드 o
// ex) bold() , small() ...

// 5. Array 객체
var array1 = [52, 323, 34];
var array2 = new Array();
var array3 = new Array(10, 46);
array1.length() // 배열 길이 -> length 속성

// Array 객체의 메서드 -> 자기 자신 변화하는 경우도 o (ex push , pop , sort )
array2.sort(function(left, right){
    // sort 정렬방법 변화? -> 매개 변수로 함수 넣어주기
    return left - right;
});

// 배열 요소 삭제하기 -> 삭제하는 메서드 제공 x (pop : 맨 마지막 요소 제거하고 리턴)
// 프로토타입에 remove 메서드 추가하는 식으로 사용
Array.prototype.remove = function(index){
    this.splice(index, 1);
    // splice(a,b) -> 지정 부분 삭제, 삭제한 요소 리턴
}
// for문 사용한 삭제 - 요소 삭제와 인덱스 주의! -> 역 for문 사용해야
var array4 = [52, 499, 204, 43, 122];
for (var i = array.length; i >= 0; i--){
    // 뒤에서부터 삭제하도록 -> index 밀리지 않게
    if (array[i]>100){
        array4.remove(i);
    }
}

// 5-1. ECMAScript5 -> Array 객체의 추가 메서드
// indexof() / lastIndexOf() : 특정 요소를 앞쪽 / 뒤쪽부터 검색, 있으면 해당 요소를 없으면 -1을 리턴
var output1 = array4.indexOf(4);
var output2 = array4.lastIndexOf(4);

// forEach() : 매개 변수로 입력 함수에 배열의 요소와 관련된 정보를 넣어 반복(for in 과 유사하게!)
array4.forEach(function(element, index, array4){
    // function(배열 요소, 배열 요소의 인덱스 , 반복을 수행하는 배열 자체)
    sum += element;
    output2 += index + ':' + element;
})

// filter() : 매개 변수는 불리언을 리턴!
array4.filter(function(element, index, array4){
    // True인 배열 요소만을 골라, 새로운 배열 만들어 리턴
    return element <= 5;
});

// map() : 배열의 각 요소를 변경해 새로운 배열 리턴(간단한 형태의 함수를 매개 변수로)
var output3 = array4.map(function(element){
    return element * element;
});

// JSON 객체
JSON.parse() // JSON 형식 문자열을 js 객체로 만듬
JSON.stringify() // js 객체를 JSON 형식 문자열로 만듬

// 6. Date 객체

// 7. Math 객체