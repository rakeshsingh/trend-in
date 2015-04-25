from trendin import utils


def test_meant_to_pass():
    assert 1 == 1


def test_valid_config_file():
    assert True == utils.get_config()
