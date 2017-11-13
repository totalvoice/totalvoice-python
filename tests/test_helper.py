import pytest
from totalvoice.cliente.api.helper import utils


class TestHelper(object):

    def test_header(self):
        header = utils.build_header("token")
        assert header is not None
        assert header['Content-Type'] == 'application/json'
        assert header['Accept'] == 'application/json'
        assert header['Access-Token'] == 'token' 
    
    def test_host(self):
        host = utils.build_host("host")
        assert host is not None
        assert host == 'https://host'
