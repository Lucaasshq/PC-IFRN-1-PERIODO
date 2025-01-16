while True:
  
    H1, M1, H2, M2 = map(int, input().split())
    
   
    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break
    
    
    minutos_atual = H1 * 60 + M1
    minutos_alarme = H2 * 60 + M2
    

    if minutos_alarme >= minutos_atual:
        minutos_para_dormir = minutos_alarme - minutos_atual
    else:
      
        minutos_para_dormir = (1440 - minutos_atual) + minutos_alarme
    
    
    print(minutos_para_dormir)