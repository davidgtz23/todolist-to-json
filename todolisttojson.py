import click
import csv
import json


def lee_csv(nom_arch):
	with open(nom_arch) as arch_txt:
		arch_reader = csv.reader(arch_txt)
		datos = list(arch_reader)
	return datos

def escribe_json(nom_arch, datos):
	nombres = datos[0]
	datos_obj = []  
	for fila in datos[1:]: 
		objeto = {}
		for i, valor in enumerate(fila):  
			objeto[ nombres[i] ] = valor
		datos_obj.append(objeto)

	with open(nom_arch, "w") as arch_txt:
		json.dump(datos_obj, arch_txt, indent=4) 

@click.command()
@click.argument("nom_arch", type=str)
def main(nom_arch):
	datos = lee_csv(nom_arch)
	nom_arch_json = nom_arch.replace(".csv", ".json")
	escribe_json(nom_arch_json, datos)
	print("La lista de tareas se ha convertido a Json con el nombre", nom_arch_json)

if __name__ == '__main__':
	main()