

def dia(dia, mes, ano):
   meses = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
   diasPorMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   
   if(mes < 1 or mes > 12):
      return "Data Invalida"
   
   if dia < 1 or dia > diasPorMes[mes-1]:
      return "Data Invalida"
   
   diaFormatado = f"{dia:02}"
   
   return f"{diaFormatado} de {meses[mes -1]} de {ano}"


resultado = dia(22,1,1500)

print(resultado)