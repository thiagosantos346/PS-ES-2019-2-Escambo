@startuml
left to right direction
skinparam packageStyle rectangle
actor Consumidor
actor Fornecedor

rectangle Sistema {
  (Catálogo)<--(Ver)
  (Manter)-->(Catálogo)
  (Criar)-->(Oferta)
  (Oferta)<--(Ver)
  (Responder)-->(Oferta)
  (Oferta)<--(Lance)
  (Transação)<-- (Avaliar)
  (Transação)<-- (Concluir)
  (Transação)<-- (Bate-papo)
  (Perfil)<--(Reportar)
  (Perfil)<--(Seguir)
  (Perfil)<--(Bate-papo)
  (Ver)       <-- Consumidor
  (Concluir)  <-- Consumidor
  (Bate-papo) <-- Consumidor
  (Lance)    <-- Consumidor
  (Avaliar)   <-- Consumidor
  (Seguir)    <-- Consumidor
  (Reportar)  <-- Consumidor
   Fornecedor --> (Avaliar)
   Fornecedor --> (Concluir)
   Fornecedor --> (Manter)
   Fornecedor --> (Criar)
   Fornecedor --> (Bate-papo)
   Fornecedor --> (Responder)
   Fornecedor --> (Seguir)
   Fornecedor --> (Reportar)
  }
@enduml
