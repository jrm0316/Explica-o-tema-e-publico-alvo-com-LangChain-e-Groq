# explica-o-tema-e-publico-alvo-LangChain e Groq

- Este projeto demonstra como utilizar LangChain para criar um sistema simples de explicação de conceitos, onde o tema e o público-alvo são definidos dinamicamente. O objetivo é mostrar, na prática, como estruturar prompts reutilizáveis e profissionais, indo além do uso direto de APIs de IA.
- O foco está em educação, clareza de respostas e boas práticas de Prompt Engineering com Python.


Como a IA responde
A IA recebe um prompt estruturado por meio de um PromptTemplate, que define:
- qual é o tema a ser explicado
- para quem a explicação deve ser direcionada
Com isso, o modelo gera respostas mais adequadas ao nível do público informado, tornando o conteúdo mais acessível e contextualizado.


Tecnologias e conceitos utilizados
- Python
- LangChain
-PromptTemplate
- LLM (Large Language Model)
- Groq API
- Prompt Engineering
- Automação de geração de text
- Variáveis de ambiente (.env)


Estrutura do projeto
projeto/
│
├── main.py                # Código principal
├── .env                   # Contém a GROQ_API_KEY
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação


Como executar o projeto
  1.) Clone o repositório
    git clone https://github.com/seu-usuario/Explica-o-tema-e-publico-alvo-com-LangChain-e-Groq.git

  2.) Crie e ative um ambiente virtual (opcional)
      python -m venv venv
      source venv/bin/activate   # Linux/Mac
      venv\Scripts\activate      # Windows

  3.) Instale as dependências
      pip install langchain langchain-groq python-dotenv

  4.) Configure sua chave da Groq
      Crie um arquivo .env:

        GROQ_API_KEY=sua_chave_aqui

  5.) Execute o script
      python main.py

Alterando o tema analisado
Você pode facilmente mudar o conteúdo gerado alterando os valores do PromptTemplate:

    prompt_final = prompt_template.format(
    tema="Inteligência Artificial",
    publico="estudantes do ensino médio")
Isso permite criar explicações personalizadas para diferentes áreas e públicos.
