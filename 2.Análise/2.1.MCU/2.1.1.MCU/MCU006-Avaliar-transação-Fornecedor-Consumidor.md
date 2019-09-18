# MCU006 - Avaliçar transação Fornecedor Cliente; 

##Ator Primário:
-  [ Fornecedor ] : Avaliar transação com [ Consumidor ] ;

## Atores Secundários:
-  [ Consumidor ] : Receber avaliação;
-  [ Aplicação Servidor ] : Dar suporte transação;

## Pré-requistos:
  -  MCU004;
  -  MCU003;

## Fluxo Principal:
  1) [ Forncedor ] : Sinaliza entrega do item;
  2) [ Aplicação Servidor ] : Envia formulario de avaliação;
  3) [ Fornecedor ] : Avalia o [ Consumidor ];
  4) [ Aplicação Servidor ] : Atualiza a reputação do [ Consumidor ];
  5) [ Aplicação Servidor ] : Publica a nova reputação do [ Consumidor ];


## ##  Pós-condições:
  1) Que o [ Consumidor ] tenha sua reputação alterada;

