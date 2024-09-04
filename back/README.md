# A. Estrutura da aplicação

Esta estrutura separa as funcionalidades de forma clara. Aqui está uma análise dos componentes principais:

* **app**: Este é o diretório principal da aplicação.
* **app/init.py**: Este arquivo vazio marca o diretório como um pacote Python.
* **app/processamento**: Diretório dedicado a tarefas de processamento de dados.
* **app/routes**: Este diretório contém endpoints de API agrupados por funcionalidade.
* **app/routes/auth.py**: Define endpoints para autenticação de usuário.
* **app/routes/users.py**: Define endpoints relacionados ao gerenciamento de usuários.
* **app/routes/profile.py**: Contém endpoints para gerenciamento de perfil do usuário.
* **app/routes/tarefas.py**: Define endpoints para interagir com dados processados.
* **app/routes/jobs.py**: Define endpoints relacionados a tarefas em segundo plano.
* **app/entidades.py**: Contém modelos de entidade que representam estruturas de dados para da aplicação.
* **app/modelos.py**: Armazena os modelos de dados principais usados em toda a aplicação.
* **app/dtos.py**: Contém objetos de Transferência de Dados (DTOs) que representam estruturas de dados para interações com a API.
* **app/banco.py**: Contém lógica relacionada à interação com o banco de dados.
* **app/seguranca.py**: Contém funções para medidas de segurança como autorização.
* **app/utilidades.py**: Arquivo de utilitário geral contendo funções auxiliares usadas em toda a aplicação.
* **main.py**: O ponto de entrada principal da sua aplicação, provavelmente inicializando o FastAPI e iniciando o servidor.
* **exec.sh**: Este script pode ser usado para executar sua aplicação a partir da linha de comando.
* **images**: Este diretório armazena imagens, potencialmente fotos de perfil do usuário em uma subpasta chamada "profile".
* **uploads**: Este diretório pode ser usado para armazenar arquivos enviados pelo usuário.
* **requirements.txt**: Este arquivo deve listar as dependências da sua aplicação para fácil instalação usando gerenciadores de pacotes como o pip.
* **users.db**: Este pode ser seu arquivo de banco de dados, supondo que você esteja usando um banco de dados leve como o SQLite.
* **utilidades.py (fora da pasta app)**: Este pode ser um arquivo de utilitário duplicado ou pode ter funcionalidades específicas não relacionadas à lógica principal da aplicação.

**Observações gerais**

- Esta estrutura promove a separação de preocupações, tornando o código mais fácil de entender e manter. 
- DTOs são usados para troca de dados.

# B. Visão Geral da Arquitetura

Esta seção apresenta uma visão geral da arquitetura de software da aplicação "MyApp". Descreve os principais componentes, camadas e fluxo de dados da aplicação, fornecendo uma compreensão geral da estrutura e organização do sistema.

## Abordagem baseada em camadas

A arquitetura da aplicação segue uma abordagem de camadas, separando as responsabilidades e promovendo a modularidade. Ela consiste nos seguintes componentes principais:

### Camada de serviços

Responsável por lidar com a interface do usuário e a interação com o cliente.
Composta pelas rotas que fornecem os dados para a aplicação cliente.

### Camada de dados:

Responsável pela manipulações de dados entre a aplicação e o banco de dados. 

## Diagrama de Componentes

TBD

## Fluxo de dados de referência

O fluxo de dados na aplicação segue o seguinte padrão:

TBD

# C. Tecnologias e configurações do projeto

## Tecnologias

Aqui estão as principais tecnologias e frameworks utilizados na aplicação:

**FastAPI**: É um framework web em Python utilizado para desenvolvimento de aplicações web. Ele fornece recursos para gerenciamento de rotas,  manipulação de requisições e muito mais. É a base da aplicação e permite a criação de uma API web de forma simples e eficiente.

**SQLite**: SQLite é um banco de dados relacional embutido utilizado para armazenar os dados dos usuários cadastrados na aplicação. É uma opção leve e prática para aplicações de pequeno a médio porte.

**HTML**: [HTML](https://en.wikipedia.org/wiki/HTML) (Hypertext Markup Language) é a linguagem de marcação utilizada para estruturar e organizar o conteúdo das páginas web. É a base para a criação dos templates HTML da aplicação.

**CSS**: [CSS](https://en.wikipedia.org/wiki/CSS) (Cascading Style Sheets) é uma linguagem utilizada para estilizar e formatar as páginas web. É utilizada para definir o layout, cores, fontes e outros aspectos visuais da aplicação.

**JWT**: TBD

**PlantUML**: [PlantUML](https://en.wikipedia.org/wiki/PlantUML) é uma ferramenta para criação de diagramas UML de forma textual. Foi utilizado para gerar os diagramas de componentes e camadas da aplicação.

## Configurações do projeto

**Secret Key**: A configuração da chave secreta (app.secret_key) é fundamental para a segurança da aplicação. Ela é utilizada para assinar as sessões e proteger os dados sensíveis armazenados nelas. Certifique-se de definir uma chave secreta forte e única para cada ambiente de implantação da aplicação.

**Banco de Dados**: A aplicação utiliza o SQLite como banco de dados embutido. Certifique-se de ajustar as configurações do banco de dados de acordo com as necessidades da aplicação, como nome do arquivo de banco de dados e localização.
Autenticação e Autorização: A aplicação implementa um sistema de autenticação básico utilizando nome de usuário e senha. É importante considerar a segurança nessa área, como o armazenamento seguro das senhas (por exemplo, utilizando hash e [salt](https://en.wikipedia.org/wiki/Salt_(cryptography))) e o uso de medidas adicionais, como limitação de tentativas de login e proteção contra ataques de força bruta.

**JWT**: TBD

# D. Execução da aplicação back-end

```bash
./exec.sh
```

Abra o browser: http://localhost:8000/docs para listar a documentação da API


# E. Testes da Aplicação

Existem vários tipos de testes de software que podem ser aplicados durante o processo de desenvolvimento para garantir a qualidade do software. Logo abaixo seguem os tipos de testes que deverão ser feitos para garantir a qualidade da nossa aplicação. 

## Tipos de Testes

### Testes Unitários

É realizado para verificar se as unidades individuais de código (geralmente funções, métodos ou classes) funcionam corretamente. O objetivo é testar cada unidade isoladamente para identificar possíveis erros lógicos ou funcionais. Geralmente, é executado pelos desenvolvedores.

[Casos de Testes Unitários](?)

# F. Esquema de controle de branches

Definir um esquema de controle de versão e criar branches de desenvolvimento é fundamental no desenvolvimento de software colaborativo usando o Git por várias razões:

1. Separação de funcionalidades: Ao criar branches de desenvolvimento para implementar as features da aplicação, cada funcionalidade pode ser desenvolvida de forma isolada em seu próprio branch. Isso permite que diferentes desenvolvedores trabalhem em diferentes funcionalidades ao mesmo tempo, sem interferir no código uns dos outros.

2. Isolamento de alterações: Cada branch de desenvolvimento contém apenas as alterações relacionadas a uma determinada funcionalidade. Isso facilita a revisão de código, depuração e a identificação de problemas, pois as alterações são limitadas a um escopo específico.

3. Versionamento independente: Cada branch de desenvolvimento permite que as alterações sejam versionadas de forma independente. Isso significa que é possível controlar o histórico de commits e realizar rollbacks específicos para cada funcionalidade, sem afetar o restante do código.

4. Facilidade de colaboração: Com um esquema de controle de versão bem definido e branches de desenvolvimento, vários desenvolvedores podem trabalhar simultaneamente em diferentes funcionalidades sem conflitos diretos. Eles podem compartilhar suas alterações por meio de pull requests e revisar o código uns dos outros antes de mesclar as alterações no branch principal.

5. Estabilidade do código principal: O branch principal, geralmente chamado de "master" ou "main", é mantido em um estado estável, contendo apenas as funcionalidades concluídas e testadas. Isso permite que outras equipes ou partes interessadas tenham acesso a uma versão funcional e estável da aplicação.

[Exemplo de roteiro para implementação das features](https://github.com/my-prototypes/tflk/blob/main/docs/guia_branches.md)

# G. Notas de Release

Notas de release (release notes) é um documento que acompanha o lançamento do produto de software, fornecendo informações detalhadas sobre as alterações, melhorias e correções incluídas na nova versão. Essas notas são destinadas aos usuários, clientes e outros stakeholders para comunicar o que foi adicionado, modificado ou corrigido na nova versão do software. As boas release notes são claras, concisas e fornecem informações relevantes para os usuários, ajudando-os a entender as mudanças e a aproveitar ao máximo a nova versão.

[Recomendações para uma nota de release](https://github.com/my-prototypes/tflk/blob/main/docs/recomendacoes_notas_release.md)

# H. Bug-fix

O processo de bug-fix padrão, também conhecido como processo de correção de bugs ou processo de tratamento de defeitos, é uma parte essencial da engenharia de software e é usado para identificar, relatar, resolver e testar problemas ou defeitos no software após a sua liberação ou durante o processo de desenvolvimento. O objetivo do processo é melhorar a qualidade do software e garantir que os problemas sejam corrigidos de forma eficiente e eficaz.

[Recomendações para o processo de correção de bugs](https://github.com/my-prototypes/tflk/blob/main/docs/recomendacoes_bux_fix.md)