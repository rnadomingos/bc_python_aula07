
from etl import calcular_desvio_padrao, filtrar_acima_de, contar_valores_unicos

listagem = [3,5,10,45,60,58,27,30]

resultado = calcular_desvio_padrao(listagem)

filtrar = filtrar_acima_de(listagem, 10)

unique = contar_valores_unicos(listagem)

print('Resultado 1:',resultado)

print('Resultado 2:',filtrar)

print('Resultado 3:', unique)
