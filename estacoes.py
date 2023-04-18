dias_do_mes = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]

def converter_data_em_dias(dia: int, mes: int) -> int:
    dias = dia
    for num_mes, quant_dias in enumerate(dias_do_mes):
        if num_mes >= mes-1:
            break
        dias += quant_dias
    return dias

intervalos = [
    range(converter_data_em_dias(22, 9), converter_data_em_dias(21, 12)),
    list(range(converter_data_em_dias(21, 12), converter_data_em_dias(31, 12))) + list(range(0, converter_data_em_dias(22, 3))),
    range(converter_data_em_dias(22, 3), converter_data_em_dias(22, 6)),
    range(converter_data_em_dias(22, 6), converter_data_em_dias(22, 9)),
]

estacoes_hemisferios = {
    "sul": {
    	"primavera": intervalos[0],
    	"verão": intervalos[1],
    	"outono": intervalos[2],
    	"inverno": intervalos[3],
    },
    "norte": {
    	"outono": intervalos[0],
    	"inverno": intervalos[1],
   		"primavera": intervalos[2],
    	"verão": intervalos[3],
    }
}

hemisferio = input("Digite em qual hemisferio você está(Norte/Sul): ").lower()

dia, mes = input("Digite a data(dd/mm): ").split("/")

for estacao in estacoes_hemisferios[hemisferio]:
    if converter_data_em_dias(int(dia), int(mes)) in estacoes_hemisferios[hemisferio][estacao]:
        print(f"A data {dia}/{mes:0>2}, está na estação: {estacao}.")
        break