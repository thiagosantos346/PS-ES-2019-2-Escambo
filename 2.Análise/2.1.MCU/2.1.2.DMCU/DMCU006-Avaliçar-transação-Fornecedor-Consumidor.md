@startuml
left to right direction
skinparam packageStyle rectangle
actor Fornecedor
actor Consumidor
actor Servidor

rectangle Aplicação {
  Fornecedor <-- (Inicio)
  Fornecedor --> (Envia)
  (Envia) --> (Sinalização entrega do Item)
  (Sinalização entrega do Item) --> Servidor
  (Servidor) --> (Envia)
  (Envia) --> (Formulário de Avaliação)
  (Formulário de Avaliação)  --> (Servidor) 
  (Formulário de Avaliação) --> Fornecedor
  Servidor --> (Atualiza)
  (Atualiza) --> (Reputação)
  Servidor --> (Publica)
  (Publica) --> (Reputação)
  (Reputação) --> Consumidor 
  
}
@enduml