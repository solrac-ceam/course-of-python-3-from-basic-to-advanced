# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

# Criar ambiente virtual:
# python -m venv <nome_do_ambiente>
#
# Antes de ativar o ambiente virtual o path do python é o global:
# which python -> /Users/carlosmorales/.pyenv/shims/python
#
# Ativar:
# . venv/bin/activate
# ou
# source venv/bin/activate
#
# Depois de ativa o path é ate o ambinete virtual:
# which python -> /Users/carlosmorales/Documents/udemy/course of puthon 3 from basic to advanced/venv/bin/python
#
# Desativar:
# deactivate
#
# Instalando pacotes no ambiente virtual. O ambiente tem que estar ativo:
# pip install <pacote>[==<versão>]
# ou
# python -m pip install <pacote>[==<versão>]
# 
# Desintalar pacotes do ambinete virtual. O ambiente tem que estar ativo:
# pip uninstall <pacote>
# ou
# python -m pip uninstall <pacote>
# 
# Listar os pacotes instalados:
# pip freeze
# ou
# python -m pip freeze
# 
# Gerando arquivo de requerimentos:
# pip freeze > requirements.txt
# 
# Instalando dependencias usando o arquivo de requerimentos:
# pip install -r requirements.txt
# 
