# -*- coding: utf-8 -*-
from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from wsgiref.simple_server import make_server

class TimeOneTheRoad(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def calcul_heures(ctx, number01, number02):
        result = int(number01) / int(number02)
        float_result = int(round(((result % 1)*60), 0))
        result = int(result)
        yield u'%s heures %s minutes' % (result,float_result)

application = Application([TimeOneTheRoad], 'spyne.examples.hello.soap',
                         in_protocol=Soap11(validator='lxml'),
                         out_protocol=Soap11())
wsgi_application = WsgiApplication(application)


server = make_server('172.18.2.1', 8000, wsgi_application)
server.serve_forever()
