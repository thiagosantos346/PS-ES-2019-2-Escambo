@startuml
left to right direction
skinparam packageStyle rectangle
actor Consumidor
actor Fornecedor
actor Servidor

rectangle Aplicação {

  Consumidor <-- ( Inicio )
  Consumidor --> ( Sinaliza interesse ) 
  ( Sinaliza interesse ) --> ( item )
  ( item ) --> Servidor 
  Servidor --> (Notifica)
  (Notifica) --> Fornecedor
  Servidor -- (Conecta)
  (Conecta) --> Fornecedor
  (Conecta) --> Consumidor

}
@enduml