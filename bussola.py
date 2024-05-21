import json
from modulos.regra_composicao_coordenadas import RegraComposicaoCoordenadas
from modulos.regra_frequencia_detridos import RegraFrequenciaDetridos
from modulos.equacao_frequencia_periodica import EquacaoFrequenciaPeriodica
from modulos.equacao_frequencia_gravitacional import EquacaoFrequenciaGravitacional

class Bussola:
    def __init__(self):
        self.regra_composicao_coordenadas = RegraComposicaoCoordenadas()
        self.regra_frequencia_detridos = RegraFrequenciaDetridos()
        self.equacao_frequencia_periodica = EquacaoFrequenciaPeriodica()
        self.equacao_frequencia_gravitacional = EquacaoFrequenciaGravitacional()

    def analisar_dados(self, dados):
        resultados = {}

        # Aplicar regra de composição de coordenadas
        resultados['composicao_coordenadas'] = self.regra_composicao_coordenadas.aplicar(dados)

        # Aplicar regra de frequência de detridos intergalácticos
        resultados['frequencia_detridos'] = self.regra_frequencia_detridos.aplicar(dados, self.equacao_frequencia_periodica)

        # Calcular frequência gravitacional de composição planetária
        resultados['frequencia_gravitacional'] = self.equacao_frequencia_gravitacional.calcular(dados)

        return resultados
