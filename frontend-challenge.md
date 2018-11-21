# Desafio Frontend

Nesse desafio você deve montar um protótipo de uma interface para organizar os produtos em categorias e vinculá-los em uma árvore.

### Desafio

- Você deve construir a árvore de categorias, menuitems, composições e componentes consultando os seguintes endpoints da nossa API: http://api.staging.onyo.com/v1/mobile/company/1/products e http://api.staging.onyo.com/v1/mobile/company/1.
- Você deve propor e implementar uma forma de vincular/desvincular graficamente (drag and drop ou qualquer outra idéia melhor que tenha) quaisquer dois itens nesta árvore. Exemplos: Um menuitem a uma categoria, uma composição a um menuitem e um componente a uma composição.
- Não é necessário enviar o retorno da reorganização para nossa API, apenas persistir o resultado no browser enquanto não houver um comando de refresh.

### Requisitos Obrigatórios

- A tela a seguir ilustra o que esperamos em termos de layout, mas se atenha apenas à árvore de produtos, e não aos menus todos que aparecem em volta: http://invis.io/RD2SGJE6P
- O código deverá seguir os design patterns e melhores práticas relevantes.
- O código deverá ter uma boa cobertura de testes unitários.
- Todos os testes devem passar.
- Documentação de como instalar e executar o projeto.

### Requisitos Opcionais

- Design responsivo.
- Usar algum framework de SPA.
- Publicar as páginas em algum serviço de hospedagem.

### Entrega

Esperamos um link para um repositório público contendo o código e a documentação.

### Prazo

O prazo para entrega é de uma semana a partir da data que você recebeu o convite para o desafio.

## Estrutura de Dados

Para facilitar seu entendimento, segue um breve descritivo da nossa estrutura de dados:

- Menu: é um agregador de categorias
- Categoria: é um agregador de menuitems.

Os produtos se dividem em tipos:

- MenuItem: é um produto que aparece no cardápio dentro de alguma categoria
- Composição (Choosable): é um produto que agrega subprodutos (ex.: opções). Ele está ligado a um MenuItem (seu pai) e a produtos componentes (seus filhos)
- Componente (Simple): produtos que compõe uma composição
- Produto PDV (material): é o item cadastrado no software que roda no restaurante e não aparece para o app mobile. Pode ignorar este tipo por hora. 
