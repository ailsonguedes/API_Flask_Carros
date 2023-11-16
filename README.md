<h1 align='center'> API de Catálogo de Livros </h1>

<p align='center'>Esta é uma API de lista de carros desenvolvida com Flask, foi projetada para armazenar informações sobre carros, incluindo marca, modelo e ano.</p>

<div align='center'>
  <a href="https://www.python.org/" target="_blank">
      <img src="./img/Python-logo.png" width="150" height="150" />
  </a>

  <a href="https://flask.palletsprojects.com/en/3.0.x/" target="_blank">
      <img src="./img/Flask-logo.png" width="250" height="150" />
  </a>
</div>

## 🔧 Ferramentas

-   Python: é uma linguagem de programação de alto nível, interpretada, orientada a objetos e de propósito geral.
-   Flask: é um pequeno framework web escrito em Python. É classificado como um microframework porque não requer ferramentas ou bibliotecas particulares, mantendo um núcleo simples, porém, extensível.

## 📍 Endpoints

- `GET /carros/`: Retorna a lista de todos os carros no catálogo.
- `POST /carros/`: Cria um novo carro no catálogo.
- `DELETE /carros/{id}/`: Exclui um carro específico com base no ID.

## 💻 Como Executar o Projeto

Siga estas etapas para configurar e executar a API em seu ambiente:

1. Clone este repositório:

  ```shell
  git clone https://seurepositorio.git
  ```
2. Navegue até o diretório do projeto:

  ```shell
  cd nomedoprojeto/
  ```
3. Crie e ative um ambiente virtual:

  ```shell
  python -m venv venv
  source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
  ```
4. Instale as dependências:

  ```shell
  pip install -r requirements.txt
  ```

  ```
5. Inicie o servidor de desenvolvimento:

  ```shell
  flask run
  ```

A API estará acessível em http://127.0.0.1:5000.

## 🌐 Exemplo de Solicitação

### Criar um Novo Livro

      Método: POST
      URL: http://127.0.0.1:5000/api/carros

### Corpo da Solicitação:

```json
{
  "id":1,
  "marca": "Marca do Carro",
  "modelo": "Modelo do Carro",
  "ano": 2023

}
```
