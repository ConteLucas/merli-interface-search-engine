-- Struct Repository --

project/

└── src/

    ├── app/                  # Camada responsável pela interface com o usuário e pontos de entrada da aplicação
    │   ├── controller/       # Contém os endpoints da API REST, gerencia as solicitações HTTP e resposta com dados apropriados
    │   ├── dtos/             # Data Transfer Objects (DTOs) definem a estrutura dos dados trocados entre a API e a aplicação
    │   │   └── request/      # DTOs específicos para requisições
    │   └── services/         # Contém a lógica de negócios e serviços auxiliares
    │       ├── impl/         # Implementações concretas de serviços
    │       └── interface/    # Interfaces que definem os contratos dos serviços
    ├── domain/               # Camada central da lógica de negócios e regras de domínio
    │   ├── entities/         # Representa as entidades de domínio e suas características essenciais
    │   ├── usecases/         # Casos de uso da aplicação, encapsula regras de negócios e interage com entidades
    │   │   └── handler/      # Processa as regras específicas de negócios e orquestra a execução dos casos de uso
    │   └── utils/            # Funções utilitárias e constantes que auxiliam na lógica de domínio
    │       ├── enums/        # Enumerações usadas no domínio
    │       └── constants/    # Constantes usadas no domínio
    ├── infrastructure/       # Implementação dos detalhes técnicos e externos da aplicação
    │   ├── config/           # Arquivos de configuração do sistema, como parâmetros e credenciais
    │   ├── dataprovider/     # Interações com fontes de dados externas, como bancos de dados e APIs
    │   ├── database/         # Conexões e modelos do banco de dados
    │   │   └── model/        # Modelos do banco de dados, define esquemas e estruturas persistentes
    │   ├── gateway/          # Gateways para comunicação com sistemas externos
    │   ├── mapper/           # Mapeamento entre DTOs, Entities e Models, converte dados entre diferentes camadas
    │   └── mq/               # Configuração e gerenciamento de filas de mensagens, como Kafka
    │       ├── producer/     # Produção de mensagens para as filas
    │       └── consumer/     # Consumo de mensagens das filas
    └── tests/                # Testes automatizados para garantir o funcionamento correto da aplicação

Sobre a API:
    KeywordController: Expõe a API REST e encaminha para o serviço.
    KeywordService: Processa a lógica de aplicação e chama o use case.
    KeywordUseCase: Implementa a lógica de negócios para lidar com keywords.
    KeywordDataProvider: Interage com o banco de dados para manipular keywords.

Serviço utiliza: BeautifulSoup, Python, Flask, Pandas e PostgreSQL
