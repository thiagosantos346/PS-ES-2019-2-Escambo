# Sumário: MCU-F-001 - Fornecedor Avaliar Transação de Venda;
##  Ator Primário: 
 - Fornecedor;
##  Atores Secundários:
 - Consumidor;
 - Servidor Web;
##  Precondições:
 - [MCU-F-002;](https://github.com/thiagosantos346/PS-ES-2019-2-Escambo/blob/master/2.An%C3%A1lise/2.1.MCU/2.1.1.MCU/MCU-F-002-Fornecedor-Concluir-Transa%C3%A7%C3%A3o-de-Venda.md)
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
