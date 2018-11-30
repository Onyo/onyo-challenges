# Desafio de Backend 

O objetivo desse desafio é exercitar alguns conceitos de APIs REST, microsserviços e integrações.

Nele, você deve criar duas APIs usando Django Rest Framework ou algum outro framework similar.
Uma das APIs deve ser uma aplicação que usa a outra como um microsserviço para abstrair parte de sua lógica.

Os modelos de dados e regras de negócio de cada uma ficam a seu critério, pois estamos mais interessados em observar os conceitos REST, a arquitetura e a organização do código do que nas aplicações em si. Você pode implementar as ideias abaixo ou inventar sua própria ideia de aplicação:

  - Um microsserviço de consulta de CEPs, e um serviço de cadastro de funcionários que usa o microsserviço de CEP para consultar endereços no cadastro de novos funcionários.
  - Um microsserviço de sorteios e um serviço de rifas que permite cadastrar e sortear rifas.


## Requisitos **obrigatórios**:

  - Cada microsserviço deve possuir o próprio banco de dados e se comunicar com o outro apenas através de APIs REST.
  - A comunicação deve ser feita através de HTTP com `Content-type: application/json`.
  - Ambos devem suportar chamadas CRUD simples: `GET`, `POST`, `PATCH`, `DELETE`.
  - O microsserviço deve ter sempre a mesma resposta para uma mesma consulta.
  - O serviço de aplicação deve cachear as chamadas para o microsserviço para evitar refazer a mesma consulta diversas vezes.
  - O código deve ser bem coberto com testes unitários.
  - Os serviços devem ser bem desacoplados e cada um deve ter sua própria pasta ou estrutura de módulos.
  - O código deve estar deployado (e.g. Heroku, OpenShift, Digital Ocean, ou qualquer outra plataforma de sua preferência).
  - O código deve possuir documentação explicando como instalar e rodar as duas APIs.

## Bônus:

  - Documentação dos endpoints das APIs
  - Docker
  - Interface para exploração da API
  - Django Rest Framework


## Processo de submissão:
  - Nos envie um link para um ou mais repositórios públicos que contenham o seu código.

