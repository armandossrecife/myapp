# Minha aplicação web modelo

Aplicação modelo para servir de referência para aplicações web python. Exemplo de Protótipo de Aplicação Web (Prova de Conceito) de CRUD de usuários, anotações, tarefas, trabalhos e arquivos dos usuários.

[Quadro de Atividades do Projeto](?)

## Contextos

A aplicação é dividida em dois contextos principais: 
- [Back-end](https://github.com/armandossrecife/myapp/tree/main/back)
- [Front-end](https://github.com/armandossrecife/myapp/tree/main/front)

A aplicação back-end é feita usando o web framework FastAPI.

A aplicação front-end é feita usando o web framework Flask, além de usar HTML, CSS, Javascript e Bootstrap.

## Features 

A aplicação base terá as seguintes features: 

- F1. Login do usuário
- F2. Logout do usuário
- F3. Registro de novo usuário
- F4. Recuperar senha do usuário
- F5. Dashboard do usuário
- F6. Perfil do usuário
- F7. Anotações do usuário
- F8. Tarefas do usuário
- F9. Trabalhos do usuário
- F10. Arquivos (imagens, áudios e vídeos) do usuário

# A. Esquema de controle de branches

Definir um esquema de controle de versão e criar branches de desenvolvimento é fundamental no desenvolvimento de software colaborativo usando o Git por várias razões:

1. **Separação de funcionalidades:** Ao criar branches de desenvolvimento para implementar as features da aplicação, cada funcionalidade pode ser desenvolvida de forma isolada em seu próprio branch. Isso permite que diferentes desenvolvedores trabalhem em diferentes funcionalidades ao mesmo tempo, sem interferir no código uns dos outros.

2. **Isolamento de alterações:** Cada branch de desenvolvimento contém apenas as alterações relacionadas a uma determinada funcionalidade. Isso facilita a revisão de código, depuração e a identificação de problemas, pois as alterações são limitadas a um escopo específico.

3. **Versionamento independente:** Cada branch de desenvolvimento permite que as alterações sejam versionadas de forma independente. Isso significa que é possível controlar o histórico de commits e realizar rollbacks específicos para cada funcionalidade, sem afetar o restante do código.

4. **Facilidade de colaboração:** Com um esquema de controle de versão bem definido e branches de desenvolvimento, vários desenvolvedores podem trabalhar simultaneamente em diferentes funcionalidades sem conflitos diretos. Eles podem compartilhar suas alterações por meio de pull requests e revisar o código uns dos outros antes de mesclar as alterações no branch principal.

5. **Estabilidade do código principal:** O branch principal, geralmente chamado de "master" ou "main", é mantido em um estado estável, contendo apenas as funcionalidades concluídas e testadas. Isso permite que outras equipes ou partes interessadas tenham acesso a uma versão funcional e estável da aplicação.

[Exemplo de roteiro para implementação das features](https://github.com/my-prototypes/tflk/blob/main/docs/guia_branches.md)

# B. Notas de Release

Notas de release (release notes) é um documento que acompanha o lançamento do produto de software, fornecendo informações detalhadas sobre as alterações, melhorias e correções incluídas na nova versão. Essas notas são destinadas aos usuários, clientes e outros stakeholders para comunicar o que foi adicionado, modificado ou corrigido na nova versão do software. As boas release notes são claras, concisas e fornecem informações relevantes para os usuários, ajudando-os a entender as mudanças e a aproveitar ao máximo a nova versão.

[Recomendações para uma nota de release](https://github.com/my-prototypes/tflk/blob/main/docs/recomendacoes_notas_release.md)

# C. Bug-fix

O processo de bug-fix padrão, também conhecido como processo de correção de bugs ou processo de tratamento de defeitos, é uma parte essencial da engenharia de software e é usado para identificar, relatar, resolver e testar problemas ou defeitos no software após a sua liberação ou durante o processo de desenvolvimento. O objetivo do processo é melhorar a qualidade do software e garantir que os problemas sejam corrigidos de forma eficiente e eficaz.

[Recomendações para o processo de correção de bugs](https://github.com/my-prototypes/tflk/blob/main/docs/recomendacoes_bux_fix.md)
