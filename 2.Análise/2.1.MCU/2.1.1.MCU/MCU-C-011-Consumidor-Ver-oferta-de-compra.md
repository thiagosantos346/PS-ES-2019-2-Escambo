# Sumário: MCU-C-011 Listagem de itens do Catalógo.
## Ator Primário: 
    - Consumidor;
## Atores Secundários: 
    - Serviço de dados da aplicação;
## Precondições:
    - MCU-F-004;
## Fluxo Principal
1.  Abrir o catalogo pelo menu principal do Cliente Moblie;
2.  Executar rolagem dos itens, até que se deseje ver os detalhes de um dos item;

##  Fluxo Alternativo (2): Acabou o numero de itens disponiveis.
 -  a. A o serviço de dados da aplicação, para de responder até, o usuáro tenha novos dados, dispiniveis;
##  Fluxo Alternativo (2): Aplicar um Filtro nos itens do catalogo.
 -  a. Escolher a combinação de filtros, preço, distrancia, tipo de operação(Troca, Emprestimo), pontuação do usuário;
 -  b. Aplicar o filtro.
##  Fluxo Alternativo (2): Efetuar busca sobre o catalogo.
 -  a. Informar a chave de busca
 -  c. Buscar Item

##  Fluxo de Exceção (1): Conexão indisponivel. 
 -  O Cliente Moblie, aguranda uma nova conexão;
##  Pós-condições: 
    - Listagem do catalógo, para inicio de uma operação de vendas.
##  Regras de Negócio:
    - RN1 : Itens são dispoivei pela região do usuário, isto é ambos estejam no mesmo raio.
    - RN2 : O raio, é uma intersecção entre o raio de Fornecedor e Consumidor(Ex: { "Fornecedor":3, "Consumidor":2 } = 1, como o resultado é >= a 0, ambos pertencem ao mesmo raio, e o itens podem ser visualidados pelo Consumidor ).
    - RN3 : O raio é até onde uma entidade, se dispoe a ir fazer a transação, sendo assim essa é definida pelo usário da aplicação.