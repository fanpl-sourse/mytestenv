import pytest

## scope: 模块级别
# @pytest.fixture(scope="module")
# def login():
#     print('这是登录')
#     #yield 生成器，激活teardown
#     yield
#     print('最末执行')

## scope: 类级别
# @pytest.fixture(scope="class")
# def login():
#     print('这是登录')
#     #yield 生成器，激活teardown
#     yield
#     print('最末执行')

## autouse：适用于所有测试用例
# @pytest.fixture(autouse=True)
# def login():
#     print('这是登录')
#     #yield 生成器，激活teardown
#     yield
#     print('最末执行')

## param
@pytest.fixture(params=['user1','user2'])
def login(request):
    print("login")
    print(request.param)
    # yield 激活fixture teardown
    yield
    print("down")
