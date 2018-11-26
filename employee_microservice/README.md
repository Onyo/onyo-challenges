# Entendimento do projeto

## Overview

Mostar conhecimento em APIs REST, Microserviços e Integração de serviços, através da comunicação entre dois microserviços.

## Pontos mais importantes

REST conceitos, arquitetura, organização do código.

## Comportamento

### *funcionario_servico:*


GET /cep/<numero_cep> - retorna o endereço para um cep selecionado
POST / - salva um funcionario  
PATCH /<id> atualiza um funcionario  
DELETE /<id> remove um funcionario  

### *cep_servico:*

GET /<numero_cep> - retorna o endereço relacionado ao cep passado
POST / - salva um endereço
PATCH /<id> atualiza um endereço
DELETE /<id> remove um endereço

### *sorteio_servico:*

GET /rifa/<numero_rifa>/sortear - retorna um número sorteado em uma rifa
POST / - salva um sorteio
PATCH /<id> atualiza um sorteio
DELETE /<id> remove um sorteio

### *rifa_servico:*

GET /<numero_rifa> - retorna uma rifa por número
POST / - salva uma rifa
PATCH /<numero_rifa> atualiza uma rifa
DELETE /<numero_rifa> remove uma rifa

## Objetos

### employee
{"id": number, "name": string, "zip_code": string, "address": number, "created_at": datetime, "updated_at": datetime}

### zip_code
{"id": number, "zip_code": number, "address": string}

### sorteio
{"id": number, "numero_rifa":"", "data":""}

### rifa
{"id": number, "numeros":""}

## Tecnologias
  * [Django Rest Framework] - Api
  * [Mongodb] - escalabilidade, relacionamento fraco
  * [memcached] - Django nativo
  * [UnitTest] - Qualidade
  * [Heroku] - Núvem
  * [Make] - Automation
  * [Docker/docker-compose] - infra

## Tarefas

  - [x] Criar ambiente Django
  - [x] TDD funcionário serviço
  - [x] Comunicação assíncrona
  - [x] Documentação Api
  - [x] Adicionar cache
  - [] TDD cep serviço
  - [] TDD sorteio serviço
  - [] TDD rifa serviço
  - [] Criar ambiente banco
  - [] Integrar banco
  - [] Criar ambiente docker e docker-compose
  - [] Criar make file
  - [] Deploy no Heroku


## Instalação

```sh
$ cd employee_microservice
$ make install
$ make run
```