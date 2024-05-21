class EquacaoFrequenciaPeriodica:
    def calcular(self, item):
        frequencia = item['amplitude'] * item['frequencia_base'] / item['periodo']
        return frequencia
