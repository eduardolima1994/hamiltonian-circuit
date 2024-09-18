# Projeto e Análise de Algoritmos - Circuito Hamiltoniano

## Introdução

A técnica do Circuito Hamiltoniano é usada para encontrar um caminho em um grafo que visita cada vértice exatamente uma vez e retorna ao vértice inicial. É uma questão clássica de teoria dos grafos e tem aplicações em logística, planejamento de circuitos e problemas de rota.

## Apresentação do Problema

O problema do Circuito Hamiltoniano pergunta se existe um caminho em um grafo que passa por todos os vértices exatamente uma vez e retorna ao ponto de partida. É um problema NP-completo, o que significa que não há solução eficiente conhecida para todos os casos.

## Exemplo de Aplicação

Um circuito hamiltoniano pode ser aplicado ao transporte coletivo municipal como uma forma de otimizar rotas de ônibus ou transporte público em uma cidade. A ideia central é identificar um circuito que passe por todas as paradas de ônibus sem repetir nenhuma, minimizando o tempo e o custo de deslocamento.

O circuito hamiltoniano procura uma rota que visite cada vértice uma única vez e retorne ao ponto inicial. Neste caso, queremos determinar a melhor rota de ônibus que cubra todas as paradas sem repetição e, idealmente, minimize o tempo de viagem.

## Modelagem com Grafos

Para modelar este problema, cada parada de ônibus será representada como um vértice em um grafo, e as estradas entre as paradas serão as arestas. As arestas não tem um peso associado.

Exemplo:
Vértices: 0, 1, 2, ..., n (paradas de ônibus).
Arestas: a, b, c, ..., n (conexões entre as paradas).

## Como a Técnica Resolve o Problema

A técnica envolve uma busca exaustiva que testa todas as mudanças possíveis de vértices para encontrar um caminho que satisfaça as condições do Circuito Hamiltoniano. Algoritmos como backtracking são usados para explorar todas as possibilidades de forma sistemática.

### Benefícios:

- Otimização de Rota: Usando um circuito hamiltoniano, a rota do ônibus será mais eficiente, evitando passagens repetidas por paradas e garantindo que o percurso cubra todas as áreas da cidade sem sobreposição.

- Redução de Custos: A otimização da rota pode reduzir o consumo de combustível e o desgaste dos veículos, além de economizar o tempo dos passageiros.

- Melhoria do Serviço: Com uma rota otimizada, os ônibus podem atender a todas as paradas de forma mais rápida e previsível, melhorando o atendimento ao usuário.

### Executando o Código

O arquivo *stopping_points.py* é um exemplo funcional em Python usando backtracking para encontrar um Circuito Hamiltoniano em um grafo representado por uma matriz de adjacência, matrizes de exemplo:

Exemplos que satisfaz um circuito hamiltoniano:

```
adjacency_matrix = [
    [0, 0, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0]
]
```
ou
```
adjacency_matrix = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0]
]
```
ou
```
adjacency_matrix = [
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
]
```

Exemplo que não satisfaz um circuito hamiltoniano:

```
adjacency_matrix = [
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
```

### Instalação de Pacotes

Para seu uso é necessário instalar os pacotes:

```
pip install networkx matplotlib
```