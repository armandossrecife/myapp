# Aplicação Front-end 

Contexto referente a interação (UI) com o usuário final da Aplicação MyApp.

[Quadro de Atividades do contexto front-end](?)

# A. Estrutura da aplicação front-end

A seguinte estrutura representa o aplicativo front-end Flask:

* **app:** Este é o diretório base do aplicativo front-end.
* **routes:** Este diretório abriga todas as rotas do aplicativo front-end definidas em arquivos Python separados para melhor organização.
* **auth.py, dashboard.py, jobs.py, tarefas.py:** Esses arquivos contêm definições de rota para lidar com autenticação de usuário, painel, tarefas e funcionalidades de tarefas, respectivamente.
* **dto.py:** (Opcional) Este arquivo pode conter objetos de transferência de dados usados para troca de dados entre o front-end e o back-end.
* **utilidades.py:** Este define funções utilitárias usadas em todo o aplicativo para tarefas como manipulação de extensões de arquivo ou URLs de API.
* **exec.sh:** (Opcional) Este pode ser um script shell para implantar ou executar o aplicativo em um ambiente específico.
* **main.py:** Este é o ponto de entrada principal para o seu aplicativo Flask. Ele configura o aplicativo, registra blueprints (rotas) e inicia o servidor de desenvolvimento.
* **static:** Este diretório armazena arquivos estáticos como imagens, folhas de estilo CSS e arquivos Javascript usados pelos seus templates.
* **favicon.ico, my_login.png, script.js, style.css:**  Esses representam o favicon do aplicativo, uma imagem de login, um arquivo Javascript para interatividade e uma folha de estilo CSS para estilizar suas páginas web, respectivamente.
* **templates:** Este diretório contém todos os seus templates HTML usados para renderizar a interface do usuário.
    * Subdiretórios aqui representam diferentes seções do seu aplicativo.
* **auth, base, base_dashboard, dashboard, error, index, jobs, list_files, tarefas, users, view_ (vários):**
    * Subdiretórios temáticos como `auth` contêm templates para funcionalidades de login, registro e esquecimento de senha.
    * `base.html` e `base_dashboard.html` contêm layouts básicos para diferentes seções das telas do aplicativo.
    * Outros subdiretórios como `dashboard`, `jobs`, `tarefas` contêm templates específicos para essas funcionalidades (por exemplo, `starter.html` para uma página inicial do painel principal do dashboard do usuário).
    * Templates iniciando com `view_` (por exemplo, `view_image.html`) são usados para exibir diferentes tipos de mídia (imagens, vídeos, áudio) baixados do back-end.

Considerações gerais:

Esta estrutura promove boas práticas para o desenvolvimento front-end:

* **Separação de conceitos:** Rotas, lógica, templates e arquivos estáticos são separados para melhor manutenção.
* **Modularidade:** As rotas são organizadas por funcionalidade em módulos dedicados.
* **Reusabilidade:** Layouts base permitem uma estrutura de IU consistente em diferentes seções.
* **Nomeação clara:** Nomes descritivos de arquivos e diretórios melhoram a legibilidade.

# B. Para executar a aplicação principal

```bash
./exec.sh
```

Abra o browser: http://localhost:5000

# C. Visão Geral da Arquitetura

Esta seção apresenta uma visão geral da arquitetura de software da aplicação front-end "MyAPP". Descreve os principais componentes, camadas e fluxo de dados da aplicação, fornecendo uma compreensão geral da estrutura e organização do sistema.

## Abordagem baseada em camadas

A arquitetura da aplicação segue uma abordagem de camadas, separando as responsabilidades e promovendo a modularidade. Ela consiste nos seguintes componentes principais:

### Camada de Apresentação (Presentation Layer):

Responsável por lidar com a interface do usuário e a interação com o cliente.
Composta pelos templates HTML localizados na pasta app/templates, que definem a estrutura e o layout das páginas. Os arquivos de template são renderizados pelo Flask para exibir as informações dinâmicas do sistema.

### Camada de Controle (Controller Layer):

Gerencia as requisições HTTP, processa a lógica de negócios e direciona as ações apropriadas. Implementada nos módulos auth.py, usuarios.py e imagens.py localizados na pasta app/controllers. Os controladores recebem as requisições do cliente, extraem os parâmetros necessários e invocam os serviços correspondentes da API da aplicação back-end.

## Diagrama de Componentes

Arquitetura ([C4](https://c4model.com/)) de Alto Nível 

TBD

Componentes da Aplicação (Web Application)

```
@startuml
package "App" <<Cloud>> {
  [Controllers]
  [Templates]
  [Models]
}
[Controllers] ..> [Templates]
[Controllers] ..> [Models]
@enduml
```

Neste diagrama, temos os seguintes componentes mais importantes:

**Controllers**: Estes componentes são responsáveis por receber as requisições do cliente, manipular os dados necessários e chamar os serviços apropriados. Eles interagem com os componentes Templates e Models. No contexto do padrão [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller), os Controllers atuam como os controladores da aplicação, lidando com a lógica de controle e coordenação das interações entre as outras camadas.

**Templates**: Estes componentes contém os arquivos de templates ou views que são usados para renderizar a interface do usuário. Os templates são populados com os dados fornecidos pelos Controllers e exibidos ao usuário final.

**Models**: Estes componentes contém as classes que representam os objetos de domínio ou entidades da aplicação. Os Models também podem encapsular a lógica de negócio e o estado dos dados. Eles são utilizados pelos Controllers para obter os dados das entidades base.

Essa arquitetura pode ser divida em camadas, seguindo os conceitos do MVC, o que ajuda a separar as responsabilidades da aplicação, tornando o código mais modular, reutilizável e facilitando a manutenção. Os Controllers lidam com a lógica de controle, os Templates cuidam da apresentação e os Models encapsulam as entidades base da aplicação.

## Fluxo de dados de referência

O fluxo de dados na aplicação segue o seguinte padrão:

O cliente (navegador) faz uma requisição HTTP para uma determinada URL, como /login, /cadastrar, /listar, etc.

O Flask, como framework, recebe a requisição e identifica o controlador correspondente com base na rota definida nas rotas registradas.

O controlador processa a requisição, extrai os dados necessários dos parâmetros da requisição ou do formulário enviado pelo cliente.

O controlador invoca o serviço apropriado, passando os dados relevantes.

O serviço realiza as operações necessárias, como cadastro de usuário, autenticação ou consulta a API da aplicação back-end.

O serviço retorna os resultados para o controlador.

O controlador renderiza o template HTML apropriado, passando os dados resultantes para serem exibidos ao cliente.

O Flask envia a resposta HTTP contendo o HTML renderizado de volta para o cliente, que exibe a página ao usuário.

# D. Tecnologias e configurações do projeto

## Tecnologias

Aqui estão as principais tecnologias e frameworks utilizados na aplicação:

**Flask**: Flask é um framework web em Python utilizado para desenvolvimento de aplicações web. Ele fornece recursos para gerenciamento de rotas, renderização de templates, manipulação de requisições e muito mais. É a base da aplicação e permite a criação de uma aplicação web de forma simples e eficiente.

**HTML**: [HTML](https://en.wikipedia.org/wiki/HTML) (Hypertext Markup Language) é a linguagem de marcação utilizada para estruturar e organizar o conteúdo das páginas web. É a base para a criação dos templates HTML da aplicação.

**CSS**: [CSS](https://en.wikipedia.org/wiki/CSS) (Cascading Style Sheets) é uma linguagem utilizada para estilizar e formatar as páginas web. É utilizada para definir o layout, cores, fontes e outros aspectos visuais da aplicação.

**Bootstrap:** é um framework front-end gratuito e de código aberto que proporciona uma maneira rápida e fácil de criar interfaces de usuário responsivas para sites e aplicativos web. Ele oferece um conjunto abrangente de componentes pré-construídos, como botões, formulários, grids, navegação e muito mais, que você pode personalizar e combinar para criar designs modernos e profissionais.

**PlantUML**: [PlantUML](https://en.wikipedia.org/wiki/PlantUML) é uma ferramenta para criação de diagramas UML de forma textual. Foi utilizado para gerar os diagramas de componentes e camadas da aplicação.

Essas são as principais tecnologias e frameworks utilizados na aplicação. Cada uma desempenha um papel importante na construção e funcionamento da aplicação web Flask, desde o framework Flask em si até as linguagens de marcação utilizadas para criar as páginas web.

## Configurações do projeto

**Secret Key**: A configuração da chave secreta (app.secret_key) é fundamental para a segurança da aplicação. Ela é utilizada para assinar as sessões e proteger os dados sensíveis armazenados nelas. Certifique-se de definir uma chave secreta forte e única para cada ambiente de implantação da aplicação.

**Proteção CSRF**: É importante adicionar proteção [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) (Cross-Site Request Forgery) nas rotas que modificam dados sensíveis ou realizam operações destrutivas. O Flask possui recursos embutidos para lidar com CSRF, como o uso do token CSRF na geração de formulários.

**Configurações de Ambiente**: Considere utilizar configurações de ambiente para separar as configurações específicas de cada ambiente, como desenvolvimento, produção e teste. Isso permite que a aplicação seja facilmente configurada em diferentes ambientes sem a necessidade de modificar o código fonte.

**Controle de Acesso**: Além da [autenticação](https://en.wikipedia.org/wiki/Authentication), é importante considerar o [controle de acesso](https://en.wikipedia.org/wiki/Authorization) em nível de permissões de usuário. Isso pode envolver a definição de papéis de usuário (por exemplo, administrador, usuário comum) e a restrição de acesso a determinadas funcionalidades ou recursos com base nas permissões associadas a cada papel.

# E. Testes da Aplicação

Existem vários tipos de testes de software que podem ser aplicados durante o processo de desenvolvimento para garantir a qualidade do software. Logo abaixo seguem os tipos de testes que deverão ser feitos para garantir a qualidade da nossa aplicação. 

### Testes Unitários

É realizado para verificar se as unidades individuais de código (geralmente funções, métodos ou classes) funcionam corretamente. O objetivo é testar cada unidade isoladamente para identificar possíveis erros lógicos ou funcionais. Geralmente, é executado pelos desenvolvedores.

[Casos de Testes Unitários](?)

### Testes de Integração

Tem como objetivo verificar se as diferentes unidades do software se integram corretamente e funcionam em conjunto. Verifica se a comunicação entre as unidades é eficiente e se os dados são transferidos corretamente. Pode ser realizado em diferentes níveis de integração, como integração de módulos, integração de subsistemas ou integração do sistema como um todo.

[Casos de Testes de Integração](?)

### Testes de Sistema

É realizado para avaliar o sistema como um todo e verificar se ele atende aos requisitos especificados. Verifica se todas as funcionalidades estão implementadas corretamente, se a interação entre os componentes é adequada e se o sistema funciona conforme o esperado em diferentes cenários e condições.

[Casos de Testes de Sistema](?)

[Testes Automáticos de Sistema](https://github.com/my-prototypes/tflk/blob/desenvolvimento/docs/roteiro_selenium_web_driver.md)

### Testes de Aceitação

É conduzido para verificar se o software atende aos critérios de aceitação definidos pelo cliente ou usuário final. Geralmente, é realizado em um ambiente próximo ao ambiente de produção. O objetivo é validar se o software está pronto para ser entregue e utilizado pelos usuários finais.

[Roteiro para criar os testes de aceitação](https://github.com/my-prototypes/tflk/blob/main/docs/roteiro_testes_aceitacao.md)

### Testes de Regressão

É realizado após modificações no software para garantir que as alterações não tenham introduzido novos defeitos ou afetado o funcionamento das funcionalidades existentes. Visa garantir que as partes do software que estavam funcionando corretamente antes das alterações ainda funcionem conforme o esperado.

[Roteiro para criar os testes de Regressão](https://github.com/my-prototypes/tflk/blob/main/docs/roteiro_testes_regressao.md)

### Testes de Desempenho

Tem como objetivo avaliar o desempenho do software em termos de tempo de resposta, capacidade de processamento, escalabilidade e estabilidade sob diferentes cargas de trabalho. Ajuda a identificar gargalos, otimizar o desempenho e garantir que o software possa lidar com a demanda esperada.

[Roteiro para criar os testes de Desempenho](https://github.com/my-prototypes/tflk/blob/main/docs/roteiro_testes_desempenho.md)

### Testes de Segurança

É realizado para identificar vulnerabilidades de segurança no software. Visa garantir que o software seja resistente a ataques e que as informações sejam protegidas adequadamente. Envolve testes de penetração, testes de autenticação, testes de autorização e outros métodos de avaliação de segurança.

[Roteiro para criar os testes de segurança](https://github.com/my-prototypes/tflk/blob/main/docs/roteiro_testes_seguranca.md)

## Plano de Testes

[Plano de Testes](?)

## Execução dos Testes 

### Testes Unitários 

No diretório principal da aplicação execute o comando abaixo:

```bash
python3 -m unittest app.tests.test_run
```

### Testes de Sistema automáticos

No diretório principal da aplicação execute o comando abaixo:

```bash
python3 test_ts_run.py
```

Obs: É preciso ter o Firefox instalado.

## Resultados dos Testes

[Protótipo 1 - resultados](?)