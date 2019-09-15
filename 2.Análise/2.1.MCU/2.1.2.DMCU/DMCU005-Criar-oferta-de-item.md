@startuml
left to right direction
skinparam packageStyle rectangle
actor Fornecedor
actor Servidor

rectangle Aplicação {
  Fornecedor <-- (Inicio)
  Fornecedor --> (Pede)
  (Pede) --> (Formulario Criar Oferta)
  Servidor --> (Envia)
  (Envia) --> (Formulario Criar Oferta)
  (Formulario Criar Oferta) --> Fornecedor
  Fornecedor --> (Preenche)
  (Preenche) --> (Formulario Criar Oferta)
  Fornecedor --> (Envia)
  (Envia) --> (Formulario Criar Oferta)
  (Formulario Criar Oferta) --> Servidor
  
}
@enduml