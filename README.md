# NLW Expert - Trilha Python    

## Sobre o repositório  
Este repositório é destinado ao armazenamento de uma aplicação Back-End construída em Python durante o evento nlw expert da RocketSeat.  
O projeto consiste em uma aplicação capaz de gerar código de barras com o python-barcode.  
Este evento foi muito importante para conhecer mais das possibilidades com a linguagem python e sua sintaxe, bem como o Flask (framework), preparação de ambiente 
e boas práticas de projeto com Virtualenv, Pylint e versionamento de código usando o pre-commit e também testes unitários utilizando o Pytest.  

# Como executar/visualizar o projeto      
Pré-requisitos: Possuir o Python 3 em sua máquina e de preferência utilizar ambientes virtuais (venv), utilizar Postman ou Insomnia para criar as tags.  
O principal arquivo a ser executado é o run.py, você pode criar sua requisição para gerar o código de barras entrando na rota usando algum API Client (Postman/Insomnia...)  
Todas as dependências utilizadas e suas versões estão especificadas no arquivo Requirements.txt  

```bash
# clonar repositório:
git clone https://github.com/guuisouza/nlw_python_logistic.git

# entrar na pasta no vscode:
cd nlw_python_logistic

# instalar a biblioteca virtualenv (20.25)
pip3 install virtualenv

# criar o ambiente virtual
py -m venv .venv

# ativar o ambiente virtual - obs: No Linux o caminho é diferente
.venv\Scripts\activate

# instalar o flask
pip3 install Flask

# instalar o barcode e pillow (para imagens)
pip3 install python-barcode
pip3 install pillow

# instalar o cerberus para validação de entrada
pip3 install Cerberus
```

## Pacotes opcionais
```bash
# OPCIONAL - instalar o pylint - (após a instalação baixe também a extensão pylint do vscode reinicie o editor)
pip3 install pylint

# OPCIONAL - instalar o pre-commit
pip3 install pre-commit

# OPCIONAL - instalar o pytest para testes
pip3 install pytest
```




# Contato  

Guilherme Dilio de Souza  

https://www.linkedin.com/in/guilherme-souza-579267250/  
