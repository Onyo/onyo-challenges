# Desafio de Backend

O objetivo desse desafio é exercitar alguns conceitos de desenvolvimento de APIs. Nele você deverá desenvolver uma API usando algum framework web de Python como Django ou Flask.

Os modelos de dados e regras de negócio ficam a seu critério, pois estamos mais interessados em observar os conceitos, a arquitetura e a organização do seu código do que na aplicação em si. Você pode implementar a sugestão abaixo ou inventar sua própria ideia:

- Um serviço de cadastro de cardápio com suporte para uma três níveis de produtos e que faça o processamento de um pedido de forma assíncrona:
  1. Menu items: itens principais que podem ser escolhidos em um pedido, como "frango à milanesa" ou "refrigerante".
  2. Choosables: itens que permitem que o usuário faça uma escolha, como "escolha o seu acompanhamento".
  3. Simples: itens secundários que são escolhidos dentro de um choosable pelo usuário, como "batata sautê" ou "legumes no vapor".

## Requisitos **obrigatórios**

- Se você utilizar um banco relacional recomendamos o uso do Postgres. Evite o SQlite.
- A API deve suportar chamadas REST e/ou Graphql.
- O código deve ser bem coberto com testes unitários.
- A API deverá ser modularizada e deverá seguir os princípios SOLID.
- O código deve possuir documentação explicando como deve ser feita a sua instalação e execução.

## Requisitos Bônus

- Utilizar uma interface Graphql.
- Utilizar processamento assíncrono com Celery.
- Usar docker.
- Interface para exploração da API.
- Publicar a API em algum PaaS como Heroku, Google App Engine, etc.

## Processo de submissão

- Preencha o formulário do [Google Forms](https://forms.gle/4imQhNZKtahag1hH8).
- Envie um e-mail confirmando sua submissão.
