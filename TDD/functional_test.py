from selenium import webdriver
import unittest
# 브라우저 열고 닫기를 위한 unittest 모듈

class NewVisitorTest(unittest.TestCase):
    # unittest.TestCase를 상속!

    def setUp(self):
        # 테스트 시작 전 실행
        self.brower = webdriver.Chrome()

        self.brower.implicitly_wait(3)
        # 암묵적 대기 기능 -> 안정적으로 페이지 로딩이 이뤄지게끔!

    def tearDown(self):
        # 테스트 시작 후 실행
        self.brower.quit()
        # -> 테스트에 에러 발생해도 실행됨(창이 닫김)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # test라는 명칭으로 시작하는 모든 메소드는 -> 테스트 메소드!
        # 테스트 실행자에 의해 실행 - 클래스당 하나 이상의 테스트 메소드 작성 o
        # 테스트 내용을 알 수 있는 명칭을 사용하는게 좋다!

        self.brower.get('http://localhost:8000')
        # 사용자가 브라우저 접속!

        self.assertIn('To-Do', self.brower.title)
        # unittest가 제공하는 asserIn 함수! assert를 생성할 때 사용됨

        self.fail('Finish the test')
        # fail()함수 -> 강제적으로 테스트 실패 발생! - 에러 메시지 출력
        # (여기서는 테스트가 끝났음을 알리기 위해 사용)

if __name__ == '__main__':
    # 해당 모듈이 import된 경우가 아니라, 커맨드라인을 통해 실행됬을 경우에..!
    unittest.main(warnings='ignore')
    # unittest.main()을 호출해 unittest 테스트 실행자를 가동!

    # warnings='ignore'? -> 테스트 작성 시 발생하는 불필요한 경고 제거