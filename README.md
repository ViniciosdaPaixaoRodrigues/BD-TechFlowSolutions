# Desafio-TechFlowSolutions
O foco deste projeto é ser uma atividade entregável da faculdade, o objetivo é fazer um sistema de Cadastro e Login usando Python.

TechFlow Solutions sendo o nome fictício de uma empresa, especializada em Soluções em Software.

Proposta:
"aplicando os conceitos de Engenharia de Software para planejar, criar, e gerenciar um repositório no GitHub que simule o desenvolvimento do sistema. A atividade envolverá desde a organização do repositório até a implementação de funcionalidades básicas, uso de ferramentas de controle de qualidade e gestão de mudanças.

A TechFlow Solutions, uma empresa fictícia especializada em soluções de software, foi contratada para desenvolver um sistema de gerenciamento de tarefas baseado em metodologias ágeis. O cliente, uma startup de logística, busca um sistema que permita acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe"

## Objetivo do Projeto

Usando Python, com a biblioteca Flask, o usuário poderá realizar Login e Cadastro em um site da empresa, sendo capaz de editar informações e removê-las (deletar cadastro). 

1. Cadastro e Login como tarefa principal
2. Deve ser capaz de redefinir a senha
3. Tela depois de Login para localizar o usuário.

### Escopo do Projeto
O escopo do projeto é simplístico, com foco em aplicar as metodologias e testes de funcionalidade com a maior prioridade, portanto não haverá diversas funções / adições. Ou seja, inicialmente só as funções básicas em Flask.

Para esse projeto, não será usado Banco de Dados, inicialmente guardará os resultados em memória (ou seja, temporários) para efeitos de demonstração.

Além disso, o foco do projeto é testar o sistema de login/cadastro com a validação do GitHub Actions e outras validações.

A segurança não foi o foco principal do projeto, pois o objetivo é validar fluxo de autenticação, estrutura do sistema e integração com ferramentas de CI/CD.

**Durante a produção do projeto**, foi identificado a necessidade de validação forte de senha por motivos de segurança, ou seja, requisitando que os usuários cadastrem senhas fortes. Requisitos: Mínimo de 8 caracteres, pelo menos 1 numero e 1 letra maiúscula.

### Metodologia Aplicada
A metodologia aplicada será a "Metodologia Ágil", com atualizações incrementais e atualizações constantes, diferente de outros métodos como o Cascata.

A organização das tarefas foi feita utilizando Kanban no GitHub Projects.

### Tecnologias
* Python
* Flask
* PyTest
* GitHub Actions

## Controle de Qualidade

O projeto utiliza GitHub Actions para automação de testes com PyTest, garantindo validação contínua do sistema.

## Como Rodar.
No terminal Powershell ou do Visual Studio Code (Recomendado), abra a pasta onde deseja adicionar o repositório, depois siga os passos a seguir:

1. No terminal Powershell / Terminal do Visual Studio Code, clone o repositório com o seguinte comando.

```bash
git clone https://github.com/ViniciosdaPaixaoRodrigues/BD-TechFlowSolutions
```

2. Instale as dependências

```bash
pip install -r requirements.txt
```

3. Execute o projeto

```bash
python -m src.app
```

4. Acesse no navegador pela seguinte URL:

http://127.0.0.1:5000

## Demonstração em Vídeo

https://youtu.be/ROho9B7vvUk
