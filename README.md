## Lenguaje

python 3.9.7

## Ejecución
python ./src/main.py

## Test
python ./src/test.py

Dentro de la carpeta utils tengo funciones que me ayudan a hacer
tareas especificas:
Calcular.
Limpiar el Archivo.

file_utils.py lo que hace es realizar los splits, de cada linea
y devolverme un string "Limpio y Ordenado".

calculator.py lo que hace es detectar si esta dentro de los
dias entresemana o los fin de semana, tambien revisa en que horario
de trabajo esta y con base en esa informacion, realiza el calculo
de los valores a pagar.

El main.py simplemente llama las funciones creadas y nos deveulve
cuanto hay que pagar a cada usuario.
