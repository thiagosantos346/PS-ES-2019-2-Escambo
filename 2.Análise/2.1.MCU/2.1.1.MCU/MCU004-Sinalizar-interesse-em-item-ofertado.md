# MCU004 - Sinalizar interesse em item ofertado;

## Ator Primário:
- [ Consumidor ] : Sinalizar interesse pelo item informado e negociar o item;

## Atores Secundários:
- [ Fornecedor ] : Responder a interação no item publicado;
- [ Aplicação Servidor ] : Notificar ambos usuários, sobre as intereções no item ofertado; 

## Pré-requistos:
  - MCU001;
  - MCU003;
  - MCU005;

## Fluxo Principal:
  1) [ Consumidor ] : Sinaliza interesse em um item;
  2) [ Aplicação Servidor ] : Notifica ao [ Fornecedor ] com as referências ao [ Consumidor ];
  3) [ Aplicação Servidor ] : Criar um canal de comunicão entre [ Consumidor ] e [ Forncedor ] ;
  
  
## ##  Pós-condições:
  1) Notificação do [ Fornecedor ] pela [ Aplicação Servidor ];
  2) Criação de canal de comunicação entre [ Fornecedor ] e [ Consumidor ];

