import NAME

def setup_module(module):
    print("setup_module        module:%s" % module.__name__)

def teardown_module(module):
    print("teardown_module     module:%s" % module.__name__)

def test_basic():
    print("I ran!")
