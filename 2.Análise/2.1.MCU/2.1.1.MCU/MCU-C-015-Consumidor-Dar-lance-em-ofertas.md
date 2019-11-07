# Sumário: MCU-C-015 - Consumidor Dar lance em ofertas;
## Ator Primário: 
 - Consumidor; 
## Atores Secundários: 
 - Fornecedor;
## Precondições:
 - MCU-F-004;
## Fluxo Principal
1.  Busca oferta;
2.  Abre a oferta;
3.  Enviar lance;
4.  Aguarda resposta;
##  Fluxo Alternativo (4): Lance aceito
 -  a. MCU-C-012;
 -  b. MCU-C-018;
##  Fluxo de Exceção (4): 
- a. Não obter resposta; 
 -  fim;
- b.  Problema na entrega e outros:
 - MCU-C-017;
##  Pós-condições: 
 - Envio de uma oferta em um item qualquer; 
##  Regras de Negócio;