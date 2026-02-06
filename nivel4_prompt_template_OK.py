# -*- coding: utf-8 -*-

import sys
sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate    # Isso é o coração do LC, é o que diferencia de "usar API" de arquitetar prompts.

# Criar o modelo
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# Criar o Prompt Template
template = """
Explique o tema abaixo de forma clara e simples.

Tema: {tema}               
Público-alvo: {publico}     
"""

prompt_template = PromptTemplate(           # Aqui você diz, esse prompt espera duas entradas
    input_variables=["tema", "publico"],    # Aqui você diz, esse prompt espera duas entradas
    template=template                       # Aqui você diz, esse prompt espera duas entradas
)

# Preencher o template
prompt_final = prompt_template.format(      # O LC substitui automaticamente
    tema="Banco de Dados",                          # O LC substitui automaticamente
    publico="quem nunca programou"                    # O LC substitui automaticamente
)

# Chamar a IA                               # Chamando o modelo, com prompt profissional
resposta = llm.invoke(prompt_final)         # Chamando o modelo, com prompt profissional

# Mostrar resultado
print("Resposta da IA:\n")
print(resposta.content)
