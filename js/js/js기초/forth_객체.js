let snack = {
    제품명: "홈런볼",
    유형 : "과자",
    성분: "망고, 설탕, 색소",
};
// 객체? -> 배열과 유사한 개념! 요소에 접근할 때 index대신 key를 사용
// console.log(snack['성분'])
// console.log(snack.성분)

for (let key in snack){
    console.log(`${key}: ${snack[key]}`);
}

// 속성과 메소드
// 요소 : 배열 내부에 있는 값 하나하나
// 속성 : 객체 내부에 있는 값 하나하나
// 객체 속성에도 -- 다양한 자료형 입력 O

let object = {
    name : '바나나',
    price : 1200,
    print : function(){
        console.log(`${this.name}의 가격은 ${this.price}원입니다`)
        // this? -> 객체 속성을 메소드에서 사용하고 싶을 때! 자신이 가진 속성임을 분명히 표시
    }
};
object.print()

// 생성자 함수 : 객체를 만드는 함수!(대문자를 사용)
function Products(name, price){
    this.name = name;
    this.price = price;
}
// 객체 하나 생성
let product = new Products("바나나", 1200);
// new 키워드를 통해 생성자 함수를 이용한 객체 생성

console.log(product)
// 결과 : Products { name: '바나나', price: 1200 }

// 프로토타입
Products.prototype.print = function(){
    console.log(`${products.name}의 가격은 ${product.price}원입니다`);
}
let products = [
    new Products('바나나', 1200),
    new Products('사과', 2000),
    new Products('고구마', 3000),
]
for (let p of products){
    p.print();
}