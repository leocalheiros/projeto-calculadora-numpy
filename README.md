# Projeto Calculadoras Python

Este é um projeto Python que implementa três calculadoras diferentes. Cada calculadora tem sua própria lógica de cálculo e retorna um resultado acompanhado por informações detalhadas em formato de dicionário. Abaixo, você encontrará informações sobre como cada calculadora funciona, bem como instruções de uso.

## Requisitos
Para rodar esse projeto é necessário instalar os requisitos através do comando no terminal:
```
pip install -r requirements.txt
```

É necessário ter as bibliotecas Numpy e pytest instaladas.

Para rodá-lo:
```
python run.py
```

## Primeira calculadora:
- Um número real de entrada é dividido em três partes iguais.
- A primeira parte é dividida por 4 e o resultado é somado a 7. Em seguida, é calculada a raiz quadrada desse valor e multiplicada por uma constante de 0.257.
- A segunda parte é elevada à potência de 2.121, dividida por 5 e somada a 1.
- A terceira parte permanece com o mesmo valor.
- A média desses três valores é calculada e o resultado é retornado juntamente com o status de "Sucesso" ou "Falha" e os valores de entrada.

## Segunda calculadora:
- N números são fornecidos como entrada.
- Cada um desses números é multiplicado por 11 e elevado à potência de 0.95.
- Em seguida, é calculado o desvio padrão desses resultados.
- O inverso do desvio padrão é retornado como resultado, juntamente com o status de "Sucesso" ou "Falha", e os valores de entradas.

## Terceira calculadora:
- N números são fornecidos como entrada.
- A variância de todos esses números é calculada.
- O desvio padrão desses números também é calculado.
- Se a variância for maior que o desvio padrão, a calculadora retorna uma mensagem de sucesso; caso contrário, retorna uma mensagem de falha.

## Informações de saída:
Após a utilização de qualquer calculadora, o sistema retorna uma informação ao usuário em formato de dicionário. O dicionário contém as seguintes informações:

- calculator: O nome da calculadora que foi utilizada.
- inputs: Uma lista com as entradas utilizadas.
- status: Indica se o processo foi um sucesso ou falha.
- result: O resultado do cálculo (se aplicável).
