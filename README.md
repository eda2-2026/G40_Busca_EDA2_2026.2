# G40_Busca_EDA2_2026.2
Repositório dedicado ao Trabalho 1 de Estruturas de Dados 2 do 2º semestre de 2026.

O projeto tem como objetivo implementar e analisar diferentes **algoritmos de busca**, utilizando como base uma tabela contendo informações sobre jogos.

## Alunos

| Matrícula | Nome |
| --- | --- |
| 202023805 | João Paulo Barros de Cristo |
| 211062787 |LucasOliveiraDiasMarquesFerreira  |

**Disciplina:** Estrutura de Dados 2  
**Professor:** Mauricio Serrano
**Semestre:** 2026.2

---

## 🎯 Objetivo

O objetivo deste projeto é implementar diferentes algoritmos de busca estudados na disciplina de Estruturas de Dados 2, utilizando uma base de dados de jogos como conjunto de dados para os testes.

Os algoritmos serão implementados e posteriormente comparados considerando aspectos como:

- Funcionamento;
- Quantidade de comparações;
- Desempenho em diferentes tamanhos de entrada.

---

## 🎮 Base de Dados

A aplicação utiliza uma tabela contendo informações sobre jogos.

Os dados são utilizados como entrada para os algoritmos de busca, permitindo realizar consultas a partir de determinados atributos dos jogos.

A escolha dessa base possibilita testar os algoritmos com uma quantidade significativa de registros e observar as diferenças de desempenho entre as estruturas e métodos de busca.

---

## 🔎 Algoritmos de Busca

O trabalho contempla os seguintes algoritmos:

| Algoritmo | Status |
| --- | --- |
| Busca Sequencial | ✅ Implementado |
| Busca Binária | ⏳ A implementar |
| Hash Estático | ✅ Implementado |
| Hash Dinâmico | ⏳ A implementar |

## 🗂️ Estrutura do Projeto

A estrutura do projeto será organizada de maneira a separar os diferentes algoritmos e componentes da aplicação.

```text
G40_Busca_EDA2_2026.2/
│
├── README.md
├── dados/
│   └── Planilha de Games.xlsx
│
├── buscas/
│   └── sequencial.py
│
├── buscas/
│   └── hash_estatico.py
│
├── buscas/
│   └── ...
│
└── buscas/
    └── ...
```

## 🚧 Status do Projeto

Atualmente, foram implementados:

- ✅ Busca Sequencial
- ✅ Hash Estático

Ainda serão implementados:

- ⏳ Busca Binária
- ⏳ Hash Dinâmico
