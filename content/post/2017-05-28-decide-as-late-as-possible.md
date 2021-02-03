+++
title = "Decida o mais tarde possível"
description = "Um entendimento do princípio Lean: Decida o mais tarde possível"
date = 2017-05-28T14:25:50Z
author = "Rodrigo Pinheiro"
tags = ["Lean Software",]
categories = ["metodologias-ágeis"]
aliases = ["decida-mais-tarde-possível"]
+++

![bfs-dfs](/images/DFSBFS.png "DFS BFS")

Na computação de grafos há dois algoritmos de busca bem conhecidos: Busca em amplitude
(**BFS  - Breadth First Search**) e Busca em profundidade (**DFS - Depht First
Search**).

A idéia por trás do BFS é processar os vértices por níveis, começar por aqueles
vértices mais próximos do vértice inicial **S** e deixando os vértices mais
distante para depois, conforme a Figura 1.

Já a idéia do **DFS** é buscar verticalmente, sempre que possível. Sempre que um novo
vértice **V** é descoberto ele deve ser explorado por completo, conforme Figura 1.

Certo! Mas qual a relação com a forma que eu tomo as minhas decisões e até mesmo
desenvolvo o meu software?

Para responder a essa pergunta, vamos primeiramente analisar como aplicamos os
conceitos de **DFS** e **BFS** ao mundo do desenvolvimento de software.

DSF se assemelha a uma forma de desenvolvimento sequencial ou em cascata, na qual
estabelece que todos os requisitos estejam completos antes do desenvolvimento
iniciar, como uma forma de se proteger contra erros. Contudo, o problema com
**Depht First** é que ele força a tomar decisões de baixo nível antes de realizar
experimentações com as decisões de alto nível.

Já **BFS** se assemelha ao desenvolvimento concorrente de software que se utiliza
de iterações. É a técnica preferida quando o domínio é complexo e difícil de
entender ou quando mudanças são inevitáveis. Mover do modo **Depht First** para o
**Breadth First** significa que se inicia o desenvolvimento dos requisitos de
mais alto nível, enquanto se pesquisa ou se descobre os requisitos de forma mais
detalhada. Pode soar estranho, mas pense que é uma técnica exploratória que
permite aprender tentando uma variedade de opções antes de tomar alguma decisão
mais concreta.

Com isso, explicamos que dependendo do contexto em que se encontra, do domínio
no qual se trabalha pode-se aplicar um desenvolvimento **Depht First** ou
**Breadth First**.

Mas em relação ao custo? Como aplicar uma técnica ou outra vai aumentar ou diminuir os
meus custos?

Software é diferente da maioria dos produtos no sentido de que é sempre esperado
que um sistema de software sofra atualizações periódicas. Em média, mais da
metade do trabalho de desenvolvimento que ocorre em um software é realizado depois
que o sistema está em produção. Um pergunta que pode comprovar isso é: quantos
projetos você já trabalhou que eram para dar manutenção e quantos você iniciou
do zero?

É um comportamento esperado que a maioria dos softwares sofram
mudança no decorrer da sua vida útil. O que nos leva a uma nova categoria de
custo: gastos causados por um software que é difícil de manter.

Mas nem toda mudança é igual. No início de qualquer software há sempre decisões
que você terá que tomar no início do desenvolvimento, porque elas são
pré-requisitos para o sistema começa a ganhar vida, tais como qual linguagem
utilizar, qual arquitetura ou como e se irá acessar uma base de dados
compartilhada. Essas são decisões cruciais e de alto risco com um alto impacto.
Portanto, adotar uma técnica **Breadth First** e fazer experimentações com as
opções para diminuir o risco dessas decisões já impacta no custo.

Outro fator que impacta é quando elas são tomadas. No **Depht First** as decisões
são tomadas o mais cedo possível, portanto todas as mudanças atuais ou futuras
possuem o mesmo custo - muito alto. Já numa técnica **Breadth First** as decisões
são tomadas o mais tarde possível, causando os seguintes efeitos:

* Reduz o número de decisões de alto risco. Não é que as decisões de alto risco deixarão de existir, mas é pelo fato que elas sejam as escolhas naturais depois de um certo tempo de aprendizado do domínio;
* Fazendo experimentações em decisões de alto risco, dá uma certeza maior da
corretude da decisão;
* Adia a maior parte das decisões, reduzindo significativamente a necessidade
de mudanças.

Uma das razões que o desenvolvimento **Lean** de software atrasa as decisões é
pelo fato que é mais fácil de mudar uma decisão que não foi tomada ainda. O que, implicitamente, leva a um desenvolvimento robusto, uma vez que se cria designs tolerantes a mudanças.

Já que é inevitável que um software mude, porque não criar flexibilidade para acomodar mudanças arbitrárias de forma barata? A ideia é observar as mudanças que ocorreram durantes as iterações, pois elas são uma boa indicação de onde o sistema precisa ser mais flexível. Se certos tipos de mudanças são frequentes durante o desenvolvimento é de se esperar que essas mudanças continuam acontecendo mesmo o produto estando "pronto".

Logo, se um sistema é desenvolvido permitindo que o design emerja através das iterações,
o design será mais robusto, mais adaptativo aos tipos de mudanças que ocorrem
durante o desenvolvimento. E mais importante, a habilidade de se adaptar será
uma propriedade inerente do sistema mesmo após o software estiver em produção.
Por outro lado, se um sistema é construído com foco em ter tudo correto no
início com o objetivo de reduzir custo de mudanças no futuro, seu design não
aceitará mudanças facilmente. Ou pior, as mudanças irão fazer surgir erros maiores
na estrutura do sistema.
