class RegraComposicaoCoordenadas:
    def aplicar(self, dados):
        coordenadas_suspeitas = []
        for coord in dados['coordenadas']:
            if 'frequencia_potassio' in coord and coord['frequencia_potassio'] > 0.5:
                coordenadas_suspeitas.append(coord)
        return coordenadas_suspeitas
