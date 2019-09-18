# Sumário: MCU-C-017 - Consumidor Reportar um outro perfil;
## Ator Primário: 
 - Consumidor;
## Atores Secundários:
 - Servidor;
 - Fornecedor;
 - Mediador; 
## Precondições:
 - MCU-C-012;
## Fluxo Principal
1.  Escolher o motivo;
2.  Escrever comentario;
3.  Enviar;
4.  Aguardar resposta Mediador;
##  Fluxo Alternativo (1): Sem motivo compativel
 -  a. Selecionar outros;
##  Fluxo de Exceção (4): Sem retorno do Mediador
 - a. Entrar em contato com Chat; 
##  Pós-condições: O cosnumidor resolveu o seu problema com o Forncedor;
##  Regras de Negócio: