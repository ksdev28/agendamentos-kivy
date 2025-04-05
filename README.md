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

### Passos para configurar:

1. **Clone o repositório (se ainda não tiver clonado):**

   ```bash
   git clone https://github.com/ksdev28/Agendamentos-kivy.git
   cd Agendamentos-kivy
   ```

2. **Torne o script executável (Linux/Mac):**

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

---

## 👨‍💻 Autor

Desenvolvido por **Kelven Sousa**  
[github.com/ksdev28](https://github.com/ksdev28)
