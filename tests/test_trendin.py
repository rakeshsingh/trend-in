from trendin import utils
from trendin.exceptions import NotSupportedDayError
from nose.tools import raises


def test_meant_to_pass():
    assert 1 == 1

def test_valid_config_file():
    assert True == utils.get_config()

def test_get_twitter_auth():
    auth = utils.get_twitter_auth()
    assert auth == True
    
@raises(NotSupportedDayError)
def test_get_data_file():
    utils.get_data_file('someday')