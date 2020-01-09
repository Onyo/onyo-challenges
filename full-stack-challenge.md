# Desafio Full Stack

O objetivo desse desafio é exercitar alguns conceitos de APIs, integrações e desenvolvimento de interfaces web.

Nele, você deve criar uma API usando Django Rest Framework ou algum outro framework similar e um web app que a utiliza.

Os modelos de dados e regras de negócio de cada uma ficam a seu critério, pois estamos mais interessados em observar os conceitos, a arquitetura e a organização do código do que nas aplicações em si. Você pode implementar as ideias abaixo ou inventar sua própria ideia de aplicação:

- Uma aplicação de cadastro de funcionários que permite a consulta, edição ou adição de novos funcionários. Ele pode conter dados como nome, CEP, RG, CPF, etc.
- Uma aplicação de rifas que realiza o seu cadastro e o seu sorteio.

## Requisitos obrigatórios

### Geral

- O código deve ser bem coberto com testes unitários.
- Todos os testes devem passar.
- O código deve possuir documentação explicando como instalar e rodar a API e o frontend.
- Tanto o backend como o frontend devem estar publicados em uma plataforma à sua escolha, como Heroku, Firebase, Digital Ocean, AWS, etc.

### Backend

- A API deverá possuir um banco de dados para realizar a persitência dos seus dados.
- Se você utilizar um banco relacional recomendamos o uso do Postgres. Evite o SQlite.
- A comunicação deve ser feita através de HTTP com `Content-type: application/json`.
- Ambos devem suportar chamadas CRUD simples: `GET`, `POST`, `PATCH`, `DELETE`.
- A API deve ter sempre a mesma resposta para uma mesma consulta.
- A API deve cachear as chamadas para o microsserviço para evitar refazer a mesma consulta diversas vezes.

### Frontend

- O design da aplicação deve ser responsivo.
- Utilize algum framework de SPA como Angular ou React.
- O estado do frontend deverá ser gerenciado por um framework à sua escolha, como Redux, Mobix, Apollo, etc.

## Requisitos Bônus

- Documentação dos endpoints das APIs.
- Docker / Kubernetes.
- Interface para exploração da API.
- Django Rest Framework.
- Typescript.
- Graphql.
- PWA.

## Processo de submissão

- Preencha o formulário do [Google Forms](https://forms.gle/QSQqdpSG5tr51C8fA).
- Envie um e-mail confirmando sua submissão.

