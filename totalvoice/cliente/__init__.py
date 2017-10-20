class Cliente(object):
      
    access_token = None
    host = None

    def __init__(self, access_token, host):
        self.access_token = access_token
        self.host = host