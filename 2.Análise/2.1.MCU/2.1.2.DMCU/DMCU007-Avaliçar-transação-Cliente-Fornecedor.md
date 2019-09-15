@startuml
left to right direction
skinparam packageStyle rectangle
actor Consumidor
actor Fornecedor
actor Servidor

rectangle Aplicação {
  Consumidor <-- (Inicio)
  Consumidor --> (Envia)
  (Envia) --> (Sinalização recebimento do Item)
  (Sinalização recebimento do Item) --> Servidor
  (Servidor) --> (Envia)
  (Envia) --> (Formulário de Avaliação)
  (Formulário de Avaliação)  --> (Servidor) 
  (Formulário de Avaliação) --> Consumidor
  Servidor --> (Atualiza)
  (Atualiza) --> (Reputação)
  Servidor --> (Publica)
  (Publica) --> (Reputação)
  (Reputação) --> Fornecedor 
  
}
@enduml