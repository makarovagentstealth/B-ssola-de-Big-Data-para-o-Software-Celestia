class EquacaoFrequenciaGravitacional:
    def calcular(self, dados):
        gravidade = dados['massa'] / (dados['raio'] ** 2)
        frequencia_gravitacional = gravidade * dados['constante_gravitacional']
        return frequencia_gravitacional
