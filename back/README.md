# Aplicação Back-end

Contexto referente a API da Aplicação MyApp

[Quadro de Atividades do contexto back-end](https://github.com/users/armandossrecife/projects/5/views/1)

# A. Estrutura da aplicação back-end

Esta estrutura separa as funcionalidades de forma clara. Aqui está uma análise dos componentes principais:

* **app**: Este é o diretório base da aplicação.
* **app/init.py**: Este arquivo vazio marca o diretório como um pacote Python.
* **app/processamento**: Diretório dedicado a tarefas de processamento de dados.
* **app/routes**: Este diretório contém endpoints de API agrupados por funcionalidade.
* **app/routes/auth.py**: Define endpoints para autenticação de usuário.
* **app/routes/users.py**: Define endpoints relacionados ao gerenciamento de usuários.
* **app/routes/profile.py**: Contém endpoints para gerenciamento de perfil do usuário.
* **app/routes/tarefas.py**: Define endpoints para interagir com dados das tarefas processados.
* **app/routes/jobs.py**: Define endpoints relacionados a trabalhos (conjunto de tarefas) do usuário.
* **app/entidades.py**: Contém modelos de entidade que representam estruturas de dados base da aplicação.
* **app/modelos.py**: Armazena os modelos de dados principais usados em toda a aplicação.
* **app/dtos.py**: Contém objetos de Transferência de Dados (DTOs) que representam estruturas de dados para interações com a API.
* **app/banco.py**: Contém lógica relacionada à interação com o banco de dados.
* **app/seguranca.py**: Contém funções para medidas de segurança como autorização.
* **app/utilidades.py**: Arquivo de utilitário geral contendo funções auxiliares usadas em toda a aplicação.
* **main.py**: O ponto de entrada principal da aplicação back-end, inicializando o FastAPI e iniciando o servidor.
* **exec.sh**: Este script pode ser usado para executar a aplicação back-end a partir da linha de comando.
* **images**: Este diretório armazena imagens, potencialmente fotos de perfil do usuário em uma subpasta chamada "profile".
* **uploads**: Este diretório pode ser usado para armazenar arquivos enviados pelo usuário.
* **requirements.txt**: Este arquivo deve listar as dependências da aplicação para fácil instalação usando gerenciadores de pacotes como o pip.
* **users.db**: Este pode ser seu arquivo de banco de dados, supondo que você esteja usando um banco de dados leve como o SQLite.
* **utilidades.py (fora da pasta app)**: Este pode ser um arquivo de utilitário que pode ter funcionalidades específicas relacionadas à aplicação como um todo.

**Observações gerais**

- Esta estrutura promove a separação de conceitos, tornando o código mais fácil de entender e manter. 
- DTOs são usados para troca de dados.

# B. Visão Geral da Arquitetura

Esta seção apresenta uma visão geral da arquitetura de software da aplicação "MyApp". Descreve os principais componentes, camadas e fluxo de dados da aplicação, fornecendo uma compreensão geral da estrutura e organização do sistema.

## Abordagem baseada em camadas

A arquitetura da aplicação segue uma abordagem de camadas, separando as responsabilidades e promovendo a modularidade. Ela consiste nos seguintes componentes principais:

### Camada de serviços

Responsável por lidar com a interface do usuário e a interação com o cliente. Composta pelas rotas que fornecem os dados para a aplicação cliente.

### Camada de dados:

Responsável pela manipulações de dados entre a aplicação e o banco de dados. 

## Diagrama de Componentes

TBD

## Fluxo de dados de referência da aplicação back-end

O fluxo de dados na aplicação segue o seguinte padrão:

TBD

# C. Tecnologias e configurações do projeto da aplicação back-end

## Tecnologias

Aqui estão as principais tecnologias e frameworks utilizados na aplicação:

**FastAPI**: É um framework web em Python utilizado para desenvolvimento de aplicações web. Ele fornece recursos para gerenciamento de rotas,  manipulação de requisições e muito mais. É a base da aplicação e permite a criação de uma API web de forma simples e eficiente.

**SQLite**: SQLite é um banco de dados relacional embutido utilizado para armazenar os dados dos usuários cadastrados na aplicação. É uma opção leve e prática para aplicações de pequeno a médio porte.

**HTML**: [HTML](https://en.wikipedia.org/wiki/HTML) (Hypertext Markup Language) é a linguagem de marcação utilizada para estruturar e organizar o conteúdo das páginas web. É a base para a criação dos templates HTML da aplicação.

**CSS**: [CSS](https://en.wikipedia.org/wiki/CSS) (Cascading Style Sheets) é uma linguagem utilizada para estilizar e formatar as páginas web. É utilizada para definir o layout, cores, fontes e outros aspectos visuais da aplicação.

**JWT**: [JWT](https://jwt.io) (JSON Web Token) é um método padrão para transmitir informações de forma segura entre partes como um objeto JSON. É amplamente utilizado para autenticação e autorização em aplicações web.

**PlantUML**: [PlantUML](https://en.wikipedia.org/wiki/PlantUML) é uma ferramenta para criação de diagramas UML de forma textual. Foi utilizado para gerar os diagramas de componentes e camadas da aplicação.

## Configurações do projeto

**Secret Key**: A configuração da chave secreta (SECRET_KEY) é fundamental para a segurança da aplicação. Ela é utilizada para codificar o payload do pacote JWT. Certifique-se de definir uma chave secreta forte e única para cada ambiente de implantação da aplicação.

**Banco de Dados**: A aplicação utiliza o SQLite como banco de dados embutido. Certifique-se de ajustar as configurações do banco de dados de acordo com as necessidades da aplicação, como nome do arquivo de banco de dados e localização.

**Autenticação e Autorização:** A aplicação implementa um sistema de autenticação básico utilizando nome de usuário e senha para gerar um token para cada usuário da aplicação back-end. É importante considerar a segurança nessa área, como o armazenamento seguro das senhas (por exemplo, utilizando hash e [salt](https://en.wikipedia.org/wiki/Salt_(cryptography))) e o uso de medidas adicionais, como limitação de tentativas de login e proteção contra ataques de força bruta.

# D. Execução da aplicação back-end

```bash
./exec.sh
```

Abra o browser: http://localhost:8000/docs para listar a documentação da API


# E. Testes da aplicação back-end

Existem vários tipos de testes de software que podem ser aplicados durante o processo de desenvolvimento para garantir a qualidade do software. Logo abaixo seguem os tipos de testes que deverão ser feitos para garantir a qualidade da nossa aplicação. 

## Tipos de Testes

### Testes Unitários

É realizado para verificar se as unidades individuais de código (geralmente funções, métodos ou classes) funcionam corretamente. O objetivo é testar cada unidade isoladamente para identificar possíveis erros lógicos ou funcionais. Geralmente, é executado pelos desenvolvedores.

[Casos de Testes Unitários](?)
