# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo.
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.
- [`copilot-instructions.md`](../copilot-instructions.md) Sempre que houver uma atualização na estrutura do projeto ou diretrizes, atualize este arquivo para refletir as mudanças.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

## Padrão de Commits

Sempre utilize o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/) ao realizar commits neste projeto. Isso garante histórico organizado e facilita o entendimento das mudanças.

### Exemplos de Conventional Commits

- **feat:** Adiciona nova funcionalidade ou recurso
	- Exemplo: `feat: adiciona página de detalhes da tarefa`
- **fix:** Corrige um bug
	- Exemplo: `fix: corrige erro de carregamento das tarefas`
- **docs:** Atualiza documentação
	- Exemplo: `docs: atualiza README com instruções de uso`
- **style:** Ajusta formatação, espaços, ponto e vírgula, etc. (sem alteração de código funcional)
	- Exemplo: `style: padroniza indentação do CSS`
- **refactor:** Refatora código sem alterar funcionalidade
	- Exemplo: `refactor: simplifica função de listagem de tarefas`
- **test:** Adiciona ou corrige testes
	- Exemplo: `test: adiciona testes para componente de tarefa`
- **chore:** Atualiza tarefas de build, dependências, configurações, etc.
	- Exemplo: `chore: atualiza dependências do projeto`