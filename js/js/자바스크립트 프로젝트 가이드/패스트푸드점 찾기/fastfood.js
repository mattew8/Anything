var API_URL = 'https://floating-harbor-78336.herokuapp.com/fastfood';

$(function(){
    $('.btn-search').click(function(){

        // $.get() : 제이쿼리의 Ajax 용 API -> XMLHttpRequest 함수를 추상화하여 데이터 요청 및 응답을 도와줌
        // $.get(요청URL, 요청에 포함시킬 인자들, 응답 왔을 때 실행될 함수)
        $.get(API_URL, {}, function(data){
            var total = data.total;
            $('.total').html('총' + total + '개의 패스트푸드점을 찾았습니다');

            var list = data.list;
            var $showlist = $('.list');
            for (var i=0; i < list.length; i++){
                // item이라는 변수에 list속 패스트푸트점 정보 담김
                var item = list[i];

                // item들을 html상에 차례로 보여주고 싶다!
                // 1) html에 만들어둔 템플릿 복제
                // 2) 복제한 템플릿에 데이터 세팅
                // 3) 목록에 복제한 템플릿을 추가


                // 1) html에 만들어둔 템플릿 복제
                // elem란 변수에 복제할 템플릿(DOM element)을 담음
                var $elem = $('#item-template')
                    .clone()
                    // 복제를 마친 elem들은 더 이상 복제할 템플릿이 아니므로 id 삭제
                    .removeAttr('id');

                    // 2) 복제한 템플릿에 데이터 세팅
                    $elem.find('.item-no').html(i+1); // 일련번호
                    // find()를 통해 해당 elem의 자식 요소들 내에서 특정 elem 찾아줌
                    $elem.find('.item-name').html(item.name);
                    $elem.find('.item-addr').html(item.addr);
                
                // 3) 목록에 복제한 템플릿을 추가
                $showlist.append($elem)    
            }
        });
    });
})