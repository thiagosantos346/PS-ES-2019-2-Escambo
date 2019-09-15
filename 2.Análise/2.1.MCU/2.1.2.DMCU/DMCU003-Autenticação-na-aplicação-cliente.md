@startuml
left to right direction
skinparam packageStyle rectangle
actor Usuario
actor Servidor

rectangle Aplicação {
  Usuario <-- ( Inicio )
  Usuario --> ( Pede ) 
  ( Pede ) --> (Formulário de autenticação)
  
  (Formulário de autenticação) --> ( Envia )
  ( Envia ) --> Servidor

   Servidor --> ( Envia )
  ( Envia ) --> (Formulário de autenticação)
  (Formulário de autenticação) --> Usuario
  (Formulário de autenticação) --> Servidor
   Usuario --> ( Envia )
   Servidor --> ( Credência )
   ( Credência ) --> Usuario
 
}
@enduml