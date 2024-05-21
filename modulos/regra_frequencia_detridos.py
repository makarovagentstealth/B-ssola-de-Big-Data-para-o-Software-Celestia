class RegraFrequenciaDetridos:
    def aplicar(self, dados, equacao):
        frequencias_suspeitas = []
        for item in dados['detridos']:
            frequencia = equacao.calcular(item)
            if frequencia > 0.7:
                frequencias_suspeitas.append(item)
        return frequencias_suspeitas
