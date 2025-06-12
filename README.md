# Regras do Projeto

## Índice
1. [Regras Gerais](#regras-gerais)
2. [Regras de Código](#regras-de-código)
3. [Regras de Git](#regras-de-git)
4. [Regras de Documentação](#regras-de-documentação)

## Estrutura do Projeto

```mermaid
sequenceDiagram
    participant Main as main.ts
    participant App as app.module.ts
    participant Config as config.module.ts
    participant Core as core/
    participant Modules as modules/
    participant Infra as infrastructure/
    participant Prisma as prisma/
    participant Test as test/

    Main->>App: Bootstrap Application
    App->>Config: Load Configuration
    Config-->>App: Return Config
    App->>Core: Initialize Core Services
    Core-->>App: Core Ready
    App->>Modules: Load Feature Modules
    Modules->>Infra: Initialize Infrastructure
    Infra->>Prisma: Setup Database Connection
    Prisma-->>Infra: Connection Ready
    Infra-->>Modules: Infrastructure Ready
    Modules-->>App: Modules Loaded
    App-->>Main: Application Ready
    Main->>Test: Run Tests (if in test mode)
    Test-->>Main: Test Results
```

## Regras Gerais

## Regras de Código
1. Não utilizar comentários no código. O código deve ser autoexplicativo através de nomes de variáveis, funções e classes bem definidos.

## Regras de Git

## Regras de Documentação 
