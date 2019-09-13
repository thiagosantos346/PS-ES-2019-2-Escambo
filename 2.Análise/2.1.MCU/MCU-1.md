
# MCU-1 - Cria Anuncio

 - Eu como **fornecedor** desejo anunciar um item ou Serviço
 - Eu espero que após a criação o sistema publique o meu item/serviço.

```
@startuml

:Fornecedor: as vender << Humano >>
:Sistema: as Escambo << Aplicação >>

rectangle Anunciar-Item {
  (publicar) << executar >>
  (Anuncio)  << Criar >>
  
  
  vender --> (Anuncio)
  Escambo --> (publicar)
  publicar <-- (Anuncio)
  
}

@enduml
```

![Diagrama](https://github.com/thiagosantos346/PS-ES-2019-2--Escambo/blob/master/2.An%C3%A1lise/2.1.MCU/caso-criar-anuncio.png)



