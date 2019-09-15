@startuml
left to right direction
skinparam packageStyle rectangle
actor Consumidor
actor Fornecedor
actor Servidor

rectangle Aplicação {
  Consumidor -- (Inicio)
  Consumidor --> (Modulo de Contato)
  Servidor <-- (Modulo de Contato)
  Servidor --> (Canal de Comunicação)
  Fornecedor <-- (Canal de Comunicação)
  Consumidor <-- (Canal de Comunicação)
}
@enduml