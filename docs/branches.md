# A. Esquema de controle de branches

Definir um esquema de controle de versão e criar branches de desenvolvimento é fundamental no desenvolvimento de software colaborativo usando o Git por várias razões:

1. **Separação de funcionalidades:** Ao criar branches de desenvolvimento para implementar as features da aplicação, cada funcionalidade pode ser desenvolvida de forma isolada em seu próprio branch. Isso permite que diferentes desenvolvedores trabalhem em diferentes funcionalidades ao mesmo tempo, sem interferir no código uns dos outros.

2. **Isolamento de alterações:** Cada branch de desenvolvimento contém apenas as alterações relacionadas a uma determinada funcionalidade. Isso facilita a revisão de código, depuração e a identificação de problemas, pois as alterações são limitadas a um escopo específico.

3. **Versionamento independente:** Cada branch de desenvolvimento permite que as alterações sejam versionadas de forma independente. Isso significa que é possível controlar o histórico de commits e realizar rollbacks específicos para cada funcionalidade, sem afetar o restante do código.

4. **Facilidade de colaboração:** Com um esquema de controle de versão bem definido e branches de desenvolvimento, vários desenvolvedores podem trabalhar simultaneamente em diferentes funcionalidades sem conflitos diretos. Eles podem compartilhar suas alterações por meio de pull requests e revisar o código uns dos outros antes de mesclar as alterações no branch principal.

5. **Estabilidade do código principal:** O branch principal, geralmente chamado de "master" ou "main", é mantido em um estado estável, contendo apenas as funcionalidades concluídas e testadas. Isso permite que outras equipes ou partes interessadas tenham acesso a uma versão funcional e estável da aplicação.

[Exemplo de roteiro para implementação das features](https://github.com/my-prototypes/tflk/blob/main/docs/guia_branches.md)