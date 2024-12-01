def dia_da_semana(h, d):
    dias = ["Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    
    
    indice_atual = dias.index(h)
    
    
    indice_evento = (indice_atual + d) % 7
    
    
    return dias[indice_evento]