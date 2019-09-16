#  MCU002 - Entrar em contato com fornecedor

## Ator Primário:
- [ Consumidor ] : Obter informaçõe sobre um item anunciado;

## Atores Secundários:
- [ Aplicação Servidor ] : criar canal de comunicação entre [ Consumidor ] e Fornecedor.
- [ Fonecedor ] : Serder informações ao [ Consumidor ]; 

## Pré-requistos:
  - MCU001;
  - MCU003;

## Fluxo Principal:
  1) [ Consumidor ] : Solicita a [ Aplicação Servidor ] o formulario para entrar em contato;
  2) [ Aplicação Servidor ] : Responde com o formulario para o [ Consumidor ];
  3) [ Consumidor ]: Preenche e envia o formulario para a [ Aplicação Servidor ];
  4) [ Aplicação Servidor ] : envia ao fornecedor o formulario do [ Consumidor ];
  5) Fornecedor: Envia a [ Aplicação Servidor ] a resposta solicitada pelo [ Consumidor ]; 
  4) [ Aplicação Servidor ] : Envia ao fornecedor o formulario para [ Consumidor ];
  

## Pós-condições:
  1) Criação de um canal de comunicação;

