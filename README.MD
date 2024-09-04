# Projeto e Análise de Algoritmos - Circuito Hamiltoniano

## Introdução

A técnica do Circuito Hamiltoniano é usada para encontrar um caminho em um grafo que visita cada vértice exatamente uma vez e retorna ao vértice inicial. É uma questão clássica de teoria dos grafos e tem aplicações em logística, planejamento de circuitos e problemas de rota.

## Apresentação do Problema

O problema do Circuito Hamiltoniano pergunta se existe um caminho em um grafo que passa por todos os vértices exatamente uma vez e retorna ao ponto de partida. É um problema NP-completo, o que significa que não há solução eficiente conhecida para todos os casos.

## Exemplo de Aplicação

Um exemplo de aplicação é na otimização de rotas de entrega (caixeiro-viajante), onde é necessário visitar cada ponto de entrega uma vez antes de retornar ao ponto inicial.

## Como a Técnica Resolve o Problema

A técnica envolve uma busca exaustiva que testa todas as permutações possíveis de vértices para encontrar um caminho que satisfaça as condições do Circuito Hamiltoniano. Algoritmos como backtracking são usados para explorar todas as possibilidades de forma sistemática.

### Executando o Código

O arquivo *delivery_routes.py* é um exemplo funcional em Python usando backtracking para encontrar um Circuito Hamiltoniano em um grafo representado por uma matriz de adjacência, matrizes de exemplo:

Exemplos que satisfaz um circuito hamiltoniano:

```
adjacency_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
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

### visualizando o Grafo

O arquivo *view_routes.py* é um exemplo funcional em Python usando backtracking para visualizar o grafo usando os exemplos de matriz de adjacência usado anteriomente. Para seu uso é necessário instalar os pacotes:

```
pip install networkx matplotlib
```