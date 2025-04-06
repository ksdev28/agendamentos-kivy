# 📅 Projeto Agendamentos Kivy

Aplicativo desenvolvido com **Kivy** e **KivyMD** para gerenciamento de agendamentos.

---

## ✅ Pré-requisitos

Certifique-se de ter os seguintes programas instalados:

- [Anaconda ou Miniconda](https://www.anaconda.com/)
- [Git](https://git-scm.com/)

---

## ⚙️ Configuração do Ambiente

O projeto já vem com um arquivo `environment.yml` e um script automático (`setup.sh`) que facilita a configuração do ambiente Conda.

### 🔵 Para Windows (Anaconda Prompt)

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/ksdev28/Agendamentos-kivy.git
   cd Agendamentos-kivy
   ```

2. **Crie e ative o ambiente Conda:**

   ```bash
   conda env create --file environment.yml
   conda activate agendamentos-kivy
   ```

3. **Atualize o pip:**

   ```bash
   pip install --upgrade pip
   ```

4. **(Opcional) Instale as dependências principais manualmente se necessário:**

   ```bash
   pip install kivy kivymd
   ```

---

### 🟢 Para Linux / macOS

1. **Clone o repositório (se ainda não tiver clonado):**

   ```bash
   git clone https://github.com/ksdev28/Agendamentos-kivy.git
   cd Agendamentos-kivy
   ```

2. **Torne o script executável:**

   ```bash
   chmod +x setup.sh
   ```

3. **Execute o script:**

   ```bash
   ./setup.sh
   ```

---

## ▶️ Executar o Projeto

Após a configuração do ambiente, ative-o (caso ainda não esteja ativo):

```bash
conda activate agendamentos-kivy
```

E então, execute:

```bash
python main.py
```

---

## 🔄 Atualizar o Ambiente

Se o `environment.yml` for atualizado e você quiser aplicar as mudanças:

```bash
conda env update --file environment.yml --prune
```
