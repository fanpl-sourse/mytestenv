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
import yaml


@pytest.fixture(params=['user1','user2'])
def login(request):
    print("login")
    print(request.param)
    # yield 激活fixture teardown
    yield
    print("down")

## 改写hook函数
def pytest_collection_modifyitems(session, config, items):
    """
    :param session:
    :param config:
    :param items:   收集用例列表
    :return:
    """
    print(items)
    print(len(items))
    #测试用例逆序执行
    items.reverse()

    #解决中文乱码问题
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        #item.nodeid: 用例名称
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.adding)
        if 'div' in item.nodeid:
            item.add_marker(pytest.mark.diving)


def pytest_addoption(parser):
    """
    pytest 命令行添加自定义参数
    :param parser: 解析器
    :return:
    """
    # 设置一个group节点
    mygroup = parser.getgroup("fanpl")
    mygroup.addoption("--env",  #注册一个命令行选项
                      default='selenium_ui_jenkins',
                      dest='env',
                      help = 'set your run env'
                      )

# 处理命令行传来大参数，设置为fixrure，从而获取到传入参数环境的数据
@pytest.fixture(scope='session')
def cmdoption(request):
    """
    解析参数
    :param request:
    :return:
    """
    myenv =  request.config.getoption('--env',default='selenium_ui_jenkins')

    if myenv == 'selenium_ui_jenkins':
        datapath = '../data/selenium_ui_jenkins/selenium_ui_jenkins.yaml'
    elif myenv == 'dev':
        datapath = '../data/dev/dev.yaml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv,datas


#通过方法动态生成测试用例
def pytest_generate_tests(metafunc: "Metafunc"):
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.mydatas,
                             ids=metafunc.module.myids,
                             scope='function')














