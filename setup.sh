#!/bin/bash

# Clonar o repositório
git clone https://github.com/ksdev28/Agendamentos-kivy.git
cd Agendamentos-kivy

# Criar o ambiente Conda
conda env create --file environment.yml

# Ativar o ambiente Conda
# Isso garante que o 'conda' funcione mesmo em shells que não carregam o base automaticamente
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate agendamentos-kivy

# Atualiza o pip
pip install --upgrade pip
pip install kivy kivymd

# Mensagem final
echo "Kivy e Kivymd instalados!"
echo "✅ Ambiente 'agendamentos-kivy' configurado e ativado com sucesso!"
echo "🚀 Para iniciar o sistema, execute: python main.py"
