// 객체{}? -> 배열[]과 굉장히 유사한 개념!
// 차이점 : 배열은 index, 객체는 key를 통해 접근

var product = {
    제품명 : '망고',
    유형 : '달달함',
    성분 : '망고, 설탕, 색소',
    원산지 : '부산',
    // 접근시? -> product['제품명'] or product.제품명 == '망고' (후자를 더 많이 사용)
    // 제품명 : ... , 유형 : ... , 성분 : ...  에 해당 하는 녀석들 -> "속성"

    eat : function(food){
        // eat - 함수 자료형 -> "메서드"
        alert(this.제품명 + food + '를 먹자');
        // 메서드 내에서 자기 자신이 가지고 있는 속성 출력
        // -> 자신이 가지고 있는 속성임을 명확하게 표시!! -> this
    }
};

// 배열 : for / for in 반복문 사용해 요소 접근 o
// 객체 : for 사용 X , for in 반복문 사용해야 객체 속성 접근 o
var output = '';
for (var key in product){
    // 객체 키에 접근

    output += key + product.key;
    // 객체 키 + 객체 속성 접근
}

// 객체 관련 키워드
var student1 = {
    이름 : 'lee',
    국어 : '100', 수학 : '0',
    영서 : '50',
};
// in 키워드 : 해당 키가 객체 안에 있는지를 확인
'이름' in student1 // -> True
'성별' in student1 // -> False

// with 키워드 : 객체 명시하지 않고도 속성을 쉽게 사용
with (student1) {
    var output = ('이름:' + 이름);
    output += ('국어:' + 국어);
};

var student2 = {};
// 객체 속성 동적 추가 및 제거
// 추가
student2.이름 = 'lee2'
// 메서드 역시 속성이므로 동적 추가 가능
student2.Hello = function(){
    alert('Hello');
};

// 제거
delete(student2.이름)

// 생성자 함수
// -> new 키워드를 사용해 객체를 생성할 수 있는 함수
function Student3(name, Korean, math, english){
    // 생성자 함수 내에서 this 키워드를 사용해 생성자 함수를 통해 생성될 객체의 속성 지정
    // 각각 이름 , 국어 , 수학 , 영어 라는 속성 생성
    this.이름 = name;
    this.국어 = Korean;
    this.수학 = math;
    this.영어 = english;
    // 이후 Student3 함수를 통해 생성된 객체는 이름 , 국어 ... 속성을 가짐!

    this.getSum = function(){
        return this.국어 + this.수학 + this.영어;
    };
    this.getAverage = function(){
        return this.getSum()/4;
    }
    // 당연히 메서드 생성도 o
};

// 생성자 함수 사용한 객체 생성
var student = new Student3('lee3', 100, 50, 0)

// 프로토타입
// 만일 지금과 같이 객체 생성 -> getSum()/getAverage() 메서드 계속 생성
// 똑같은 내용의 메소드가 계속해서 만들어짐!! -> 비효율..!

// js의 프로토타입 공간 사용 -> 생성자 함수를 통해 생성된 객체가 공통으로 가지는 공간
// so 생성자 함수 사용 시 내부에는 속성만! 메서드는 모두 프로토타입 내에!

Student3.prototype.getSum = function(){return this.국어 + this.수학 + this.영어};
Student3.prototype.getAverage = function(){return this.getSum/4};