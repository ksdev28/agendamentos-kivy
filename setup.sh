#!/bin/bash

# Clonar o repositório
git clone https://github.com/ksdev28/Agendamentos-kivy.git
cd agendamentos-kivy

# Criar o ambiente Conda
conda env create --file environment.yml

# Ativar o ambiente
# Isso pode variar dependendo do sistema operacional e do shell usado
# No Linux/MacOS, você pode usar o comando:
source $(conda info --base)/etc/profile.d/conda.sh
conda activate nome_do_seu_ambiente

# Atualiza o pip (última versao)
pip install --upgrade pip
# Instalar dependências adicionais, se necessário
pip install kivy kivymd

echo "Ambiente configurado e ativado. Pronto para uso!"
