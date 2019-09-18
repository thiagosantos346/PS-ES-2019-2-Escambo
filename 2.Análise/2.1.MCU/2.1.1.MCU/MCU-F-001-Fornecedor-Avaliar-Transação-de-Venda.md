# Sumário: MCU-F-001 - Fornecedor Avaliar Transação de Venda;
##  Ator Primário: 
 - Forcedor;
##  Atores Secundários:
 - Consumidor;
 - Servidor Web;
##  Precondições:
 - MCU-F-002;
## Fluxo Principal: 
1. Selecionar a opção avaliar transação;
2. Atribuir uma pontuação de 1 a 5;
3. Criar um comentario;
4. Enviar avaliação;
5. Receber confirmação da avaliação;
##  Fluxo Execeção (4): Sem conexão ao serviço ,
- a. Mantem em um banco local;
- b. Enquanto o serviço estiver indiponivel reenviar;
##  ##  Pós-condições: 
##  ##  Regras de Negócio: 