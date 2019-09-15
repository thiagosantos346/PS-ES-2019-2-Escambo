@startuml
left to right direction
skinparam packageStyle rectangle
actor Consumidor
actor Servidor

rectangle Aplicação {
  Consumidor -- (Inicio)
  Consumidor --> (Modulo de Busca)
  (Modulo de Busca) <-- (Resultados)
  Servidor --> (Resultados)
}
@enduml
