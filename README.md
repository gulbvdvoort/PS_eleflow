# PS_eleflow
Repositorio feito por @gulbvdvoort para o desafio do processo de seleção da Eleflow

## Instruções
Para executar o projeto, utilize os comandos abaixo:

```
python -m venv env
python -m pip install -r requirements.txt
python solution.ipynb
```

## Explicações do projeto
O projeto foi desenvolvido majoritariamente utilziando `Jupyter Notebook` com códigos `Python` devido sua versatilidade, modularização de códigos permitindo rodar separadamente cada parte do código e também permitir a combinação de blocos em `Markdown` de modo a melhorar a legibilidade e explicação do projeto.

A escolha do `SQLite` foi feita devido à sua fácil portabilidade, permitindo que o projeto seja facilmente transferido. Além disso, o `SQLite` é uma opção gratuita, o que contribui para a economia de recursos no projeto. Embora tenha considerado a possibilidade de criar uma conta "trial" no `Google Cloud Platform` (GCP) para utilizar o `BigQuery`, optei por usar o `SQLite` para garantir uma correção e visualização mais simples dos dados pela equipe da Eleflow, ao mesmo tempo em que reduzimos custos.

### Primeira Questão
- Extração:
    - Utilizei um laço for para iterar por cada um dos arquivos jsons extraindos os dados e guardando-os temporariamente em um dataframe.
- Transformação:
    - Renomeei as colunas para `snake case`.
    - Transformei os tipos das colunas para o tipo correto a ser guardado no banco `SQLite`
- Carga:
    - Utilizei o `SQLite` para inserir os dados no banco na tabela `VRA`.

### Segunda Questão
- Extração:
    - Utilizei um laço for para iterar por cada um dos arquivos csv extraindos os dados e guardando-os temporariamente em um dataframe.
    - A nomeação das colunas no padrão `Snake Case` já foi realizada durante a própria etapa de extração.
- Transformação:
    - Separei as colunas `ICAO IATA` em duas colunas, `ICAO` e `IATA`.
    - Transformei os tipos das colunas para o tipo correto a ser guardado no banco `SQLite`
- Carga:
    - Utilizei o `SQLite` para inserir os dados no banco na tabela `air_cia`.

### Terceira Questão
- Extração:
    - Extraí todos os códigos icao de aeroportos do dataframe utilizado na primeira questão (VRA).
    - Através da API [https://rapidapi.com/Active-api/api/airport-info/] trouxe os dados do aeroporto para cada `ICAO` presente nos dados de `VRA`.
- Transformação:
    - Substituí os valores nulos por `None`.
- Carga:
    - Utilizei o `SQLite` para inserir os dados no banco na tabela `airport`.

### Quarta Questão
***Primeira view:***
- Eu criei a visualização para selecionar várias colunas da seguinte maneira::
  - `cia.razao_social AS razao_social`: A razão social da empresa aérea.
  - `rotas.frequencia AS qtd`: A frequência de voos na rota.
  - `rotas.icao_aerodromo_origem AS icao_origem`: O código ICAO do aeródromo de origem.
  - `origem.name AS origem_name`: O nome do aeródromo de origem.
  - `origem.state AS origem_state`: O estado do aeródromo de origem.
  - `rotas.icao_aerodromo_destino AS icao_destino`: O código ICAO do aeródromo de destino.
  - `destino.name AS destino_name`: O nome do aeródromo de destino.
  - `destino.state AS destino_state`: O estado do aeródromo de destino.
- Eu utilizei uma subconsulta para calcular a frequência de voos em cada rota, classificando-as com base na frequência (do maior para o menor) e atribuindo uma classificação (rank) a cada rota para cada empresa aérea.
- Realizei duas junções `LEFT JOIN` para combinar as informações das rotas com as informações dos aeródromos de origem e destino, bem como com as informações da empresa aérea através de um `INNER JOIN`:
- Apliquei um filtro `WHERE rank = 1` para selecionar apenas as rotas com a classificação mais alta, ou seja, as principais rotas de cada empresa aérea.
- Para organizar os resultados, eu utilizei a cláusula GROUP BY com as colunas `razao_social`, `rotas.icao_empresa_aerea`, `origem_name`, `origem_state`, `destino_name`, `destino_state`. Isso permitiu agrupar os resultados para cada empresa aérea e suas principais rotas.
***Segunda view:***
- Eu criei uma visualização chamada `top_company_per_airport` usando a cláusula `CREATE VIEW`.
- Dividi a subconsulta `totais` em duas partes, uma para chegadas e outra para partidas. Elas calculam a quantidade de voos (qtd) para cada combinação de ano, empresa aérea e aeroporto de destino ou origem, com base na situação do voo 'REALIZADO'.
- Na minha seleção principal, combinei os resultados da subconsulta `totais` com informações adicionais das tabelas `airport` (aeroportos) e `air_cia` (empresas aéreas) para obter informações detalhadas.
- Usei a função `RANK()` para calcular a classificação das estatísticas com base na quantidade total de voos (`qtd_total`) por ano e aeroporto.
- Realizei duas junções `LEFT JOIN` para combinar as informações dos aeroportos (`airport`) e empresas aéreas (`air_cia`) com os resultados da classificação.
- Apliquei um filtro `WHERE rank = 1` para selecionar apenas as estatísticas com a classificação mais alta, ou seja, as principais estatísticas de voos para cada ano e aeroporto.
- Utilizei a cláusula `ORDER BY` para classificar os resultados com base na quantidade total de voos (`qtd_total`) em ordem decrescente.

## Extras:
### Ingestão Incremental
- Para a ingestão incremental, caso os dados continuassem a ser disponibilizados da mesma forma e com volumetria similar, eu colocaria os códigos de ETL Python em `Cloud Functions` do GCP. 
- Para o envio dos dados pelo cliente, eu criaria formulários através do `Pipefy` em que o cliente enviaria os arquivos e automaticamente, através de um gatilho `Webhook`, as functions processariam os dados e os guardariam em suas respectivas tabelas no `BigQuery`.
### Escalabilidade
- Apesar das vantagens do `SQLite`, ele não proporciona muita escalabilidade ao projeto em comparação as tecnologias de `Cloud Computing`, visto que ele é um banco de dados local e dependeria de um servidor `One Premisse` para operar.
- Dessa forma, eu migraria todo o projeto para algum serviço de Cloud de modo que o projeto seja automaticamente escalável.
- Entretanto, como o processo de ETL foi feito através da linguagem Python, ele é facilmente escalável visto que sua manutenção é simples, fácil e totalmente baseada em uma linguagem `Open Source`
### Camadas utilizada
- As camadas utilizadas estão detalhadamentes descritas na seção [Explicações do projeto](#Explicações-do-projeto)

