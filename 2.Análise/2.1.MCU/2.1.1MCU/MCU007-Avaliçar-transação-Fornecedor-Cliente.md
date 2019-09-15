# MCU007 - Avaliçar transação Cliente Fornecedor; 

## Ator Primário:
-  [ Consumidor ] : Avaliar transação com [ Consumidor ];

## Atores Secundários:
-  [ Fornecedor ] : Receber avaliação;
-  [ Aplicação Servidor ] : Dar suporte transação;

## Pré-condições:
  -  MCU004;
  -  MCU003;

## Fluxo Principal:
  1) [ Consumidor ] : Sinaliza entrega do item;
  2) [ Aplicação Servidor ] : Envia formulario de avaliação;
  3) [ Consumidor ] : Avalia o [ Fornecedor ];
  4) [ Aplicação Servidor ] : Atualiza a reputação do [ Fornecedor ];
  5) [ Aplicação Servidor ] : Publica a nova reputação do [ Fornecedor ];


## Pós-condições:
  1) Que o [ Fornecedor ] tenha sua reputação alterada;
