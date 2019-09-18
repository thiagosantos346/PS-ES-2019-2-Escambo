# MCU003 - Autenticação na aplicação Cliente

## Ator Primário:
- [ Usuário ]: obter acessoa previlegios no [ Aplicação servidor ];

## Atores Secundários:
- [ Aplicação servidor ] : conceder ou negar acesso a privilegios;

## Pré-requistos:

## Fluxo Principal:
  1) [ Usuário ]: Solicita o formulário de autenticação a [ Aplicação servidor ]; 
  2) [ Aplicação servidor ] : Envia ao [ Usuário ] o formulário de autenticação;
  3) [ Usuário ]: Preenche o campo nome de [ Usuário ];
  4) [ Usuário ]: Preenche o campo chave de acesso;
  5) [ Usuário ]: Envia formulário de autenticação para a [ Aplicação servidor ] ;

## ##  Pós-condições:
  1) Acesso a privilegios de acordo com o perfil do [ Usuário ];
