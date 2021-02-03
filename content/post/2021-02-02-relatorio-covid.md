+++
title = "Relatório COVID-19"
description = "Estudo das mortes por COVID-19 no Brasil, Estados Unidos e Itália"
date = 2021-02-02T02:13:50Z
author = "Rodrigo Pinheiro"
tags = ["covid19", "R", "estatística"]
categories = ["estatística"]
aliases = ["mortes-covid"]
+++

Este é o relatório diário da situação de óbitos por COVID19 no Brasil e
Estados Unidos, com base em dados obtidos a partir de API, disponível no
endereço

<a href="https://covid19api.com/" class="uri">https://covid19api.com/</a>

Consultando a documentação de origem, nota-se que a URL base a ser
pesquisada possui o seguinte padrão (usando como exemplo os Estados
Unidos):

`https://api.covid19api.com/total/country/united-states/status/deaths?from=2020-03-01T00:00:00Z&to=2020-07-25T00:00:00Z`

Portanto, será necessário construir esta URL combinando o nome do país,
a data de início e a data de fim, nos formatos especificados na URL.

Importação dos Dados
--------------------

Inicialmente é necessário carregar as bibliotecas para acesso à API e a
manipulação dos dados. A biblioteca `openxlsx` é responsável pela
manipulação de arquivos xlsx (escrita e leitura). A biblioteca `httr` é
responsável pela execução de requisições HTTP e a biblioteca `jsonlite`
é responsável pela manipulação de dados JSON.

``` r
#Carregando os pacotes necessários
library("openxlsx")
library("httr")
library("jsonlite")
```

Agora serão definidos os parâmetros utilizados para a construção deste
relatório. Iremos considerar para esse caso os países `Estados Unidos`,
`Brasil` e `Itália`.

O período considerado na pesquisa é entre `01/03/2020` e o dia corrente.

``` r
PAIS <- c("united-states", "brazil", "italy")
CODIGO <- c("US", "BR", "IT")
POPULACAO <- c(328.2, 209.5, 60.36) #em milhoes (google)

datainicio <- "2020-03-01T00:00:00Z"
hoje <- format(Sys.time(), "%Y-%m-%d")
datafim <-paste(hoje,"T00:00:00Z",sep="")
```

Uma idéia interessente nestes casos consistem em fazer a consulta das
informações na API e, então, salvar os resultados em algum tipo de
arquivo. Desta forma, se for necessário rodar novamente o relatório,
pode-se consultar se os respectivos arquivos existem antes de “chamar” a
API, conforme a seguir:

``` r
npaises <- length(PAIS)

#Importando os dados da API e salvando para arquivos excel, caso eles jánão existam.
for(i in 1:npaises){

    nomearquivo <- paste(hoje, "_", CODIGO[i], ".xlsx", sep="")
    
    if(!file.exists(nomearquivo)){
        url<-paste("https://api.covid19api.com/total/country/", PAIS[i], "/status/deaths?from=", datainicio, "&to=", datafim, sep="");
        get_dados <- GET(url)
        get_dados_txt <- content(get_dados, "text")
        get_dados_json <- fromJSON(get_dados_txt, flatten = TRUE)   
        write.xlsx(get_dados_json, nomearquivo)
    }
    
}
```

Para a título de visualização, exibimos a estrutura final do arquivo (
2021-02-02\_IT.xlsx ) para cada um dos países. Para esta pesquisa é
importante observarmos a coluna `Country` (nome do país), `Cases`(número
de casos coletados até a data X), `Date` (data da coleta da informação).

|      | Country                  | CountryCode | Province | City | CityCode | Lat  | Lon  |  Cases | Status | Date                 |
| :--- | :----------------------- | :---------- | :------- | :--- | :------- | :--- | :--- | -----: | :----- | :------------------- |
| 325  | United States of America |             |          |      |          | 0    | 0    | 401807 | deaths | 2021-01-19T00:00:00Z |
| 326  | United States of America |             |          |      |          | 0    | 0    | 406184 | deaths | 2021-01-20T00:00:00Z |
| 327  | United States of America |             |          |      |          | 0    | 0    | 410387 | deaths | 2021-01-21T00:00:00Z |
| 328  | United States of America |             |          |      |          | 0    | 0    | 414147 | deaths | 2021-01-22T00:00:00Z |
| 329  | United States of America |             |          |      |          | 0    | 0    | 417476 | deaths | 2021-01-23T00:00:00Z |
| 330  | United States of America |             |          |      |          | 0    | 0    | 419251 | deaths | 2021-01-24T00:00:00Z |
| 331  | United States of America |             |          |      |          | 0    | 0    | 421168 | deaths | 2021-01-25T00:00:00Z |
| 332  | United States of America |             |          |      |          | 0    | 0    | 425252 | deaths | 2021-01-26T00:00:00Z |
| 333  | United States of America |             |          |      |          | 0    | 0    | 429195 | deaths | 2021-01-27T00:00:00Z |
| 334  | United States of America |             |          |      |          | 0    | 0    | 433196 | deaths | 2021-01-28T00:00:00Z |
| 335  | United States of America |             |          |      |          | 0    | 0    | 436799 | deaths | 2021-01-29T00:00:00Z |
| 336  | United States of America |             |          |      |          | 0    | 0    | 439530 | deaths | 2021-01-30T00:00:00Z |
| 337  | United States of America |             |          |      |          | 0    | 0    | 441324 | deaths | 2021-01-31T00:00:00Z |
| 338  | United States of America |             |          |      |          | 0    | 0    | 443355 | deaths | 2021-02-01T00:00:00Z |

|      | Country | CountryCode | Province | City | CityCode | Lat  | Lon  |  Cases | Status | Date                 |
| :--- | :------ | :---------- | :------- | :--- | :------- | :--- | :--- | -----: | :----- | :------------------- |
| 325  | Brazil  |             |          |      |          | 0    | 0    | 211491 | deaths | 2021-01-19T00:00:00Z |
| 326  | Brazil  |             |          |      |          | 0    | 0    | 212831 | deaths | 2021-01-20T00:00:00Z |
| 327  | Brazil  |             |          |      |          | 0    | 0    | 214147 | deaths | 2021-01-21T00:00:00Z |
| 328  | Brazil  |             |          |      |          | 0    | 0    | 215243 | deaths | 2021-01-22T00:00:00Z |
| 329  | Brazil  |             |          |      |          | 0    | 0    | 216445 | deaths | 2021-01-23T00:00:00Z |
| 330  | Brazil  |             |          |      |          | 0    | 0    | 217037 | deaths | 2021-01-24T00:00:00Z |
| 331  | Brazil  |             |          |      |          | 0    | 0    | 217664 | deaths | 2021-01-25T00:00:00Z |
| 332  | Brazil  |             |          |      |          | 0    | 0    | 218878 | deaths | 2021-01-26T00:00:00Z |
| 333  | Brazil  |             |          |      |          | 0    | 0    | 220161 | deaths | 2021-01-27T00:00:00Z |
| 334  | Brazil  |             |          |      |          | 0    | 0    | 221547 | deaths | 2021-01-28T00:00:00Z |
| 335  | Brazil  |             |          |      |          | 0    | 0    | 222666 | deaths | 2021-01-29T00:00:00Z |
| 336  | Brazil  |             |          |      |          | 0    | 0    | 223945 | deaths | 2021-01-30T00:00:00Z |
| 337  | Brazil  |             |          |      |          | 0    | 0    | 224504 | deaths | 2021-01-31T00:00:00Z |
| 338  | Brazil  |             |          |      |          | 0    | 0    | 225099 | deaths | 2021-02-01T00:00:00Z |

|      | Country | CountryCode | Province | City | CityCode | Lat  | Lon  | Cases | Status | Date                 |
| :--- | :------ | :---------- | :------- | :--- | :------- | :--- | :--- | ----: | :----- | :------------------- |
| 325  | Italy   |             |          |      |          | 0    | 0    | 83157 | deaths | 2021-01-19T00:00:00Z |
| 326  | Italy   |             |          |      |          | 0    | 0    | 83681 | deaths | 2021-01-20T00:00:00Z |
| 327  | Italy   |             |          |      |          | 0    | 0    | 84202 | deaths | 2021-01-21T00:00:00Z |
| 328  | Italy   |             |          |      |          | 0    | 0    | 84674 | deaths | 2021-01-22T00:00:00Z |
| 329  | Italy   |             |          |      |          | 0    | 0    | 85162 | deaths | 2021-01-23T00:00:00Z |
| 330  | Italy   |             |          |      |          | 0    | 0    | 85461 | deaths | 2021-01-24T00:00:00Z |
| 331  | Italy   |             |          |      |          | 0    | 0    | 85881 | deaths | 2021-01-25T00:00:00Z |
| 332  | Italy   |             |          |      |          | 0    | 0    | 86422 | deaths | 2021-01-26T00:00:00Z |
| 333  | Italy   |             |          |      |          | 0    | 0    | 86889 | deaths | 2021-01-27T00:00:00Z |
| 334  | Italy   |             |          |      |          | 0    | 0    | 87381 | deaths | 2021-01-28T00:00:00Z |
| 335  | Italy   |             |          |      |          | 0    | 0    | 87858 | deaths | 2021-01-29T00:00:00Z |
| 336  | Italy   |             |          |      |          | 0    | 0    | 88279 | deaths | 2021-01-30T00:00:00Z |
| 337  | Italy   |             |          |      |          | 0    | 0    | 88516 | deaths | 2021-01-31T00:00:00Z |
| 338  | Italy   |             |          |      |          | 0    | 0    | 88845 | deaths | 2021-02-01T00:00:00Z |

Análise Gráfica
---------------

A Análise Gráfica se dará sobre a evolução da quantidade de dias pelo
número de mortes em 3 países, que no caso são **UNITED-STATES, BRAZIL,
ITALY**.

As análises a seguir (**Casos Por Milhão** e **Mortes Diárias por
Milhão**) são feitas considerando a taxa por 1 milhões de habitantes. A
fórmula desse cálculo é:

*T* = (*N*/*P*) \* 1.000.000
Em que *N* é o número de casos de morte. *P* é o tamanho da população e
*T* é a taxa por 1 milhão de habitantes.

O motivo de utilizar a taxa por 1 Milhão de habitantes é porque são
proporcionais ao tamanho da população em questão, logo nos permite
comparar populações de países com tamanhos diferentes.

### Gráfico de Casos Por Milhão

Alguns pontos interessantes sobre a análise gráfica.

-   Comparando a taxa de mortes por milhão de habitantes no início da
    pandemia é evidente a superioridade da Itália, destacando-se dos
    demais países (Estados Unidos e Brasil). Havendo uma diferença de
    quase 200 mortes por 1 Milhão de habitantes nos últimos dias.
    Contudo, a Itália entra em uma fase de estabilização.
-   Apesar de Estados Unidos e Brasil iniciarem a curva de maneira
    distinta, a curva inicial dos Estados Unidos é mais linear do que a
    curva do Brasil.
-   A curva de mortes no Brasil e Estados Unidos são quase verticais.
-   O número de casos na Itália cresceu rapidamente no começo nos
    primeiros 50 dias (primeira fase) alcançado uma estabilização após
    os 100 dias e após o dia 250 (segunda fase), quase que de forma
    exponencial, alcançando uma estabilização após 100 dias.
-   É visível o início da segunda fase na Itaália, começando após os 250
    dias.
-   A segunda fase no Brasil se dá aproximadamente no dia 300 da
    pandemia.

Explicamdo o algoritmo de geração do gráfico de mortes por 1 Milhão de
Habitantes:

    Para os países considerados na análise (Estados Unidos, Brasil e Itália), recupera-se o total de mortes por milhão de habitantes. Para o primeiro país, constrói-se a base inicial do gráfico e para os demais adiciona-se uma linha referente ao país. Por fim, adiciona uma legenda no topo da esquerda e um título do gráfico.

``` r
#Definindo os Parâmetros dos Gráficos
COR <- c("red","blue", "gray")
PCH <- c(16, 17, 18)

ndias <- nrow(base);
X<-1:ndias

#Gráfico de mortes por Milhão
for(i in 1:npaises){
  nomey = paste(CODIGO[i],"_casos_total_milhao",sep="")
  Y = base[,nomey]
  
  if(i==1){
    plot(X, Y, type="o", xlab="Dias (Ref: 1 = 01/03/2020)", ylim = c(0, 2000), ylab="Mortes p Milhao", lty=1, lwd=1.5, col=COR[i], pch=PCH[i], cex=1)  
  }else{
    lines(X, Y, type="o", lty=1, lwd=1.5, col=COR[i], pch=PCH[i], cex=1)      
  }

}
grid()
legend("topleft", inset = 0.05, cex=1, lty=1, col=COR, pch=PCH, title="Legenda", legend = CODIGO)
title("Mortes por Milhao")
```

![mortespormilhao](/images/relatorio_covid_files/figure-markdown_github/unnamed-chunk-5-1.png)

### Gráfico de mortes diárias por Milhão

Alguns pontos sobre a análise de mortes diárias por Milhão de
habitantes:

-   Nos primeiros dias observa-se um crescimento muito rápido das mortes
    diárias por Milhão de habitantes na Itália, comparado aos Estados
    Unidos e Brasil, que demoraram para ter um crescimento mais
    ascendente.
-   Durante todo o histórico do COVID-19, a Itália apresenta o maior
    cume de mortes diárias por Milhão, chegando a quase 3 vezes mais.
-   O número de mortes diárias por Milhão nos Estados Unidos foi mais
    ascendente e veloz do que no Brasil.
-   Estados Unidos e Brasil tem apresentado um número de mortes diárias
    por Milhão mais elevados e constantes do que Itália entre os dias
    100 e 250.
-   A Itália apresenta um crescimento muito rápido do caso de mortes
    diárias por milhão, assim como também uma queda muito ascentuada.
-   Nos últimos dias o número de mortes diárias por Milhão no Brasil tem
    mostrado um número elevado e constante, comparado aos Estados
    Unidos.
-   É visívil o início da segunda fase da pandemia em cada um dos
    países.

``` r
for(i in 1:npaises){
  nomey = paste(CODIGO[i],"_casos_diario_milhao",sep="")
  Y = base[,nomey]
  
  if(i==1){
    plot(X, Y, type="o", xlab="Dias (Ref: 1 = 01/03/2020)", ylim = c(0, 20), ylab="Mortes Diarias por Milhao", lty=1, lwd=1.5, col=COR[i], pch=PCH[i], cex=1)  
  }else{
    lines(X, Y, type="o", lty=1, lwd=1.5, col=COR[i], pch=PCH[i], cex=1)      
  }
  
}

grid()
legend("topleft", inset = 0.05, cex=1, lty=1, col=COR, pch=PCH, title="Legenda", legend = CODIGO)
title("Mortes Diarias por Milhao")
```

![mortesdiarias](/images/relatorio_covid_files/figure-markdown_github/unnamed-chunk-6-1.png)