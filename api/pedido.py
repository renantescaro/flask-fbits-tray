from api.tray import Tray

class Pedido(Tray):
    def pedidos(self, data_inicio, data_final):
        parametros = {
            'dataInicial' : data_inicio,
            'dataFinal'   : data_final
        }
        return self._consulta.get(endpoint='/pedidos', headers=self._headers, parametros=parametros).json()


    def pedido_por_id(self, id):
        return self._consulta.get(endpoint='/pedidos/'+str(id), headers=self._headers).json()