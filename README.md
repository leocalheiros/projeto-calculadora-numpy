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

## Utilização da API
Você também pode utilizar as calculadoras através de uma API HTTP (a qual se encontra na branch http desse repositório). Aqui estão os endpoints disponíveis:

### Primeira Calculadora

- **Endpoint**: `/calculate/first`
- **Método**: POST
- **Entrada**: JSON com o valor desejado `{"values": 10}`
- **Saída**: JSON com o resultado do cálculo.

### Segunda Calculadora

- **Endpoint**: `/calculate/second`
- **Método**: POST
- **Entrada**: JSON com os valores desejados, ex.: `{"values": [10, 20, 30]}`
- **Saída**: JSON com o resultado do cálculo.

### Terceira Calculadora

- **Endpoint**: `/calculate/third`
- **Método**: POST
- **Entrada**: JSON com os valores desejados, ex.: `{"values": [10, 20, 30]}`
- **Saída**: JSON com o resultado do cálculo.

## Estrutura do Projeto API

O projeto é dividido em várias partes que se comunicam para realizar cálculos e fornecer respostas aos usuários. Aqui está uma breve explicação de cada parte:

1. **Controllers**: Esta é a camada que lida com as solicitações HTTP e a lógica de negócios associada. Cada calculadora possui seu próprio controlador, responsável por receber as entradas, processá-las e retornar os resultados. Os controladores implementam a interface `ICalculator`.

2. **Drivers**: A pasta de drivers contém uma classe chamada `CalculationManager`, que atua como um Facade para realizar cálculos matemáticos complexos. O design pattern de Facade permite que os controladores acessem essas funcionalidades sem precisar conhecer todos os detalhes de implementação subjacentes. Neste caso, o `CalculationManager` usa a biblioteca NumPy para realizar cálculos estatísticos.

3. **Adapter**: O Adapter é um padrão de design que permite a comunicação entre partes do sistema que, de outra forma, seriam incompatíveis. Neste projeto, temos um adaptador para lidar com requisições HTTP. O `request_adapter` é responsável por transformar objetos `HttpRequest` em solicitações HTTP reais e, em seguida, converter as respostas HTTP em objetos `HttpResponse` para que possam ser processados pelos controladores.

4. **http_types**: Esta pasta contém as definições dos tipos de objetos HTTP, incluindo `HttpRequest` e `HttpResponse`. Esses objetos são usados para facilitar a troca de dados entre os controladores e o adaptador HTTP.

## Design Patterns

### Padrão de Facade

O padrão de Facade é aplicado com a classe `CalculationManager`. Ele fornece uma interface simples e unificada para realizar cálculos estatísticos complexos, como cálculo de variância e desvio padrão. Os controladores podem chamar métodos do `CalculationManager` sem se preocupar com a implementação interna dos cálculos. Isso ajuda a manter os controladores mais simples e coesos, além de facilitar a manutenção e a troca da implementação subjacente, se necessário.

### Padrão de Adapter

O padrão de Adapter é aplicado com o `request_adapter` e as classes `HttpRequest` e `HttpResponse`. O `request_adapter` age como um adaptador entre o formato de dados usado pelos controladores (objetos `HttpRequest` e `HttpResponse`) e o formato necessário para fazer solicitações e receber respostas HTTP. Isso permite que o aplicativo Flask lide facilmente com solicitações HTTP, usando objetos de entrada e saída personalizados, tornando a comunicação mais flexível e desacoplada.

