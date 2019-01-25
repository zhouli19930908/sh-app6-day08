import allure
class Test_01:
    @allure.step(title="我是test_001测试步骤名称")
    def test_001(self):
        print('----01----')
        assert True

    @allure.step(title="我是test_002测试步骤名称")
    def test_002(self):
        print('----02----')
        assert False