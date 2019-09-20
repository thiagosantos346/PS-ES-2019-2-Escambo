# Sumário: MCU-F-001 - Fornecedor Avaliar Transação de Venda;
##  Ator Primário: 
 - Fornecedor;
##  Atores Secundários:
 - Consumidor;
 - Servidor Web;
##  Precondições:
 - MCU-F-002;
## Fluxo Principal: 
1. Selecionar a opção avaliar transação;
2. Atribuir uma pontuação de 1 a 5;
3. Criar um comentário;
4. Enviar avaliação;
5. Receber confirmação da avaliação;
##  Fluxo Exceção (4): Sem conexão ao serviço ,
- a. Mantém em um banco local;
- b. Enquanto o serviço estiver indisponível reenviar;
##  ##  Pós-condições: 
##  ##  Regras de Negócio: