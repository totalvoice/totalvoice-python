class Totalvoice(object):

    cliente = None

    def __init__(self, cliente):
        self.cliente = cliente
    
    def enviar(self, *args):
        raise NotImplementedError
    
    def getById(self, id):
        raise NotImplementedError
    
    def editar(self, *args):
        raise NotImplementedError
    
    def getRelatorio(self, *args):
        raise NotImplementedError
        
    def deletar(self, id):
        raise NotImplementedError

    def getRequest(self, host, params = None):
        if params != None:
            response = requests.get(host, headers=utils.buildHeader(self.cliente.access_token, params=params))
        else:
            response = requests.get(host, headers=utils.buildHeader(self.cliente.access_token))
        return response.content

    def buildHost(self, host, route, values=None):
        host += route
        if values is not None:
            for val in values:
                host +=  "/" + val
        return host
        