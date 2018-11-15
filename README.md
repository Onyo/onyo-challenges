# Tutorial de Deploy e Instalação

## Requerimentos

- Ubuntu 16.04
- Git

### Logue no seu servidor (ssh) e instale os pacotes (ubuntu)

### Instalando o Docker

```sh
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
sudo apt-get update
sudo apt-get install -y docker-engine
```

Dando um check no status do Docker

```sh
sudo systemctl status docker
```

### Instalando o Docker Compose

```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Instalando o repositório

```sh
mkdir /apps
cd /apps
git clone https://github.com/VIMGAS/onyo-challenges.git
cd onyo-challenges
```

### Configurando o IP da API de Sorteios

No arquivo `onyo-challenge-main-service/api/views.py` altere a linha `12` para o endereço de IP onde o código estará deployado

```python
API_URL = 'http://0.0.0.0:7000/api/v1' # Substituir o 0.0.0.0 pelo ip ou domínio do host
```

### Iniciando os servidores

```sh
cd /apps/onyo-challenges
sudo docker-compose up -d
```

### Como explorar a API

Na pasta raíz do repositório existem dois arquivos com a API discriminada e pronta para ser testada pelo POSTMAN:

- `Main API.postman_collection.json`
- `Sorteios API.postman_collection.json`

### Código Deployado

A API online pode ser acessada pelo IP `68.183.172.30` nas portas `7000` para o microserviço e `8000` para a aplicação principal
