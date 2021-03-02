// 가위바위보 상수 선언
var SCISSORS = '가위';
var ROCK = '바위';
var PAPER = '보';

function onButtonClick(userInput){
    // com가 낼 가위바위보
    var comInput;

    // com은 random하게 가위/바위/보 중 하나 냄
    var rnd = Math.random();
    if (rnd<0.33){
    comInput = SCISSORS;
    } else if (rnd<0.66){
        comInput = ROCK;
    } else {
        comInput = PAPER;
    }

//     switch (userInput) {
//         case SCISSORS:
//             switch (comInput){
//                 case SCISSORS:
//                     alert('컴퓨터:' + comInput + '- 비김!');
//                     break; // -> swich문 : 충족하는 case 나타날 경우, 그 아래 모든 코드(case충족 안하는 녀석들도)작동 -> break 통한 탈출
//                 case ROCK:
//                     alert('컴퓨터:' + comInput + '- 짐!');
//                     break
//                 case PAPER:
//                     alert('컴퓨터:' + comInput + '- 이김!');
//                     break
//             }
//             break;
//         case ROCK:
//             switch (comInput){
//                 case SCISSORS:
//                     alert('컴퓨터:' + comInput + '- 이김!');
//                     break; 
//                 case ROCK:
//                     alert('컴퓨터:' + comInput + '- 비짐!');
//                     break
//                 case PAPER:
//                     alert('컴퓨터:' + comInput + '- 짐!');
//                     break
//             }
//             break;
//         // swich문 모든 조건 해당x 일 때 실행
//         default:
//             switch (comInput){
//                 case SCISSORS:
//                     alert('컴퓨터:' + comInput + '- 짐!');
//                     break; 
//                 case ROCK:
//                     alert('컴퓨터:' + comInput + '- 이김!');
//                     break
//                 default:
//                     alert('컴퓨터:' + comInput + '- 비김!');
//                     break
//             }
//             break;
//     }

}



// ---- prompt 가위바위보 ----
// 이용자 가위바위보 입력
// var userInput = prompt('가위, 바위, 보');

//     // 입력 유효성 검사
// if (userInput !== SCISSORS && userInput !== ROCK && userInput !== PAPER){
//     alert('잘못된 입력입니다');
// } else {
//     // 컴퓨터 가위바위보 선택
//     var comInput;

//     // Math.random -> 0부터 1 사이의 임의의 값 return
//     var rnd = Math.random();

//     if (rnd<0.33){
//         comInput = SCISSORS;
//     } else if (rnd<0.66){
//         comInput = ROCK;
//     } else {
//         comInput = PAPER;
//     }

//         // if문 코드작성 - 반복 지나치게 많음
//     // if (userInput === SCISSORS){
//     //     if(comInput === SCISSORS){
//     //         alert('컴퓨터:' + comInput + '- 비김!');
//     //     }
//     //     if(comInput === ROCK){
//     //         alert('컴퓨터:' + comInput + '- 짐!');
//     //     }
//     //     if(comInput === PAPER){
//     //         alert('컴퓨터:' + comInput + '- 이김!')
//     //     }
//     // }

//         // swich문 통한 결과 비교
//     switch (userInput) {
//         case SCISSORS:
//             switch (comInput){
//                 case SCISSORS:
//                     alert('컴퓨터:' + comInput + '- 비김!');
//                     break; // -> swich문 : 충족하는 case 나타날 경우, 그 아래 모든 코드(case충족 안하는 녀석들도)작동 -> break 통한 탈출
//                 case ROCK:
//                     alert('컴퓨터:' + comInput + '- 짐!');
//                     break
//                 case PAPER:
//                     alert('컴퓨터:' + comInput + '- 이김!');
//                     break
//             }
//             break;
//         case ROCK:
//             switch (comInput){
//                 case SCISSORS:
//                     alert('컴퓨터:' + comInput + '- 이김!');
//                     break; 
//                 case ROCK:
//                     alert('컴퓨터:' + comInput + '- 비짐!');
//                     break
//                 case PAPER:
//                     alert('컴퓨터:' + comInput + '- 짐!');
//                     break
//             }
//             break;
//         // swich문 모든 조건 해당x 일 때 실행
//         default:
//             switch (comInput){
//                 case SCISSORS:
//                     alert('컴퓨터:' + comInput + '- 짐!');
//                     break; 
//                 case ROCK:
//                     alert('컴퓨터:' + comInput + '- 이김!');
//                     break
//                 default:
//                     alert('컴퓨터:' + comInput + '- 비김!');
//                     break
//             }
//             break;
//     }
// }

