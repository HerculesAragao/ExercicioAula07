lista = ['eu','tu','ele','nos','vos','eles','eu','tu','ele']
dict_aux = dict.fromkeys(lista)
resultado = list(dict_aux)
print('Com os nomes duplicados: ',lista)
print('Sem os nomes duplicados',resultado)