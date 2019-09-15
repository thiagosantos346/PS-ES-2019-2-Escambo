# MCU001 - Busca de Item no feed.

## Ator Primário:
-  [  Consumidor ] : busca por algum item para compra ou troca;

## Atores Secundários:
-  [  Aplicação Servidor ] : Fornece servições de busca e visualização.

## Pré-requistos:

## Fluxo Principal:
    
    1) [ Consumidor ] : soliciata a [  Aplicação Servidor ] formulario de busca ;
    2) [ Aplicação Servidor ] : Envia o formulário de busca;
    3) [ Consumidor ] : Evia filtros e Sentença de busca para a [ Aplicação Servidor ];
    4) [ Aplicação Servidor ] : Envia o resultado de busca ao [ Consumidor ];
    5) [ Consumidor ] : Solicita detalhes de um item para [ Aplicação Servidor ];
    6) [  Aplicação Servidor ] : Envia os detalhes do item para o [ Consumidor ];
    
## Pós-condições:
  1) Visualisar detalhes sobre a oferta;

