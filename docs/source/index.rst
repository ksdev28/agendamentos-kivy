
.. raw:: html

    <div class="container">

Sistema de Agendamento com Kivy e KivyMD
=======================================

Este sistema de agendamento foi desenvolvido utilizando as bibliotecas **Kivy** e **KivyMD**, com o objetivo de permitir a criação de uma interface gráfica moderna e interativa para agendar serviços de profissionais. O sistema é ideal para salões de beleza, consultórios médicos, e outros tipos de serviços que exigem o agendamento de horários.

O Kivy é uma biblioteca de Python para o desenvolvimento de interfaces gráficas, com foco em facilitar a criação de aplicativos multi-touch, enquanto o KivyMD traz componentes visuais baseados no Material Design do Google, garantindo uma interface bonita e fácil de usar.

### Funcionalidades do Sistema
-------------------------------

O sistema possui as seguintes funcionalidades:

1. **Cadastro de Profissionais**: Permite que o usuário cadastre profissionais que oferecem serviços.
2. **Cadastro de Serviços**: Cada profissional pode ter uma lista de serviços que ele oferece, como "Corte de Cabelo", "Massagem", etc.
3. **Cadastro de Horários**: O sistema permite que os profissionais cadastrem os horários disponíveis para agendamento.
4. **Agendamento de Serviços**: O usuário pode agendar um serviço escolhendo o profissional, o serviço, a data e a hora.
5. **Histórico de Agendamentos**: O sistema mantém um histórico de todos os agendamentos realizados, facilitando a consulta posterior.

Sumário
--------
.. toctree::
   :maxdepth: 2
   :caption: Índice

   cadastro
   horarios
   agendamento
   historico

Cadastro de Profissionais e Serviços
------------------------------------

Nesta seção, o sistema permite o cadastro de profissionais e os serviços oferecidos por eles. Para isso, o usuário preenche os campos **Nome** e **Serviços**. A seguir, o sistema adiciona as informações no banco de dados, permitindo que o usuário visualize os profissionais e seus serviços cadastrados.

O formulário de cadastro consiste em:

1. **Campo de Nome**: Para o nome do profissional.
2. **Campo de Serviços**: Para a lista de serviços oferecidos, separados por vírgulas.

O código para o cadastro de profissionais é o seguinte:

```python
cadastro_card.add_widget(MDLabel(text='Nome do Profissional', halign='center'))
self.nome_input = MDTextField(hint_text='Nome', size_hint_x=1, pos_hint={'center_x': 0.5})
```

Cadastro de Horários
----------------------

Os horários disponíveis para agendamento são cadastrados nesta aba. O sistema permite que o usuário insira horários, que são então salvos no banco de dados. Esse processo é fundamental para que o agendamento de serviços possa ser feito dentro de horários disponíveis.

O formulário de horário inclui:

1. **Campo de Horário**: Para a hora disponível no formato **HH:MM**.

Exemplo de código para a criação do campo de horário:

```python
horario_card.add_widget(MDLabel(text='Cadastrar Horário (HH:MM)', halign='center'))
self.horario_input = MDTextField(hint_text='Horário', size_hint_x=1, pos_hint={'center_x': 0.5})
```

Agendamento de Serviço
------------------------

Na aba **Agendamento**, o usuário pode selecionar o **profissional**, o **serviço**, a **data** e o **horário** para o agendamento. O processo inclui a validação dos dados e a confirmação do agendamento no banco de dados, garantindo que os dados inseridos são válidos antes de serem salvos.

O agendamento inclui:

1. **Botões de Seleção**: Para selecionar o profissional, serviço, data e hora.
2. **Validação**: Verificação se o horário já está ocupado, para evitar conflitos de agendamento.

O código para o agendamento é o seguinte:

```python
self.profissional_button = MDRaisedButton(text="Selecione o Profissional")
self.profissional_button.bind(on_release=self.open_menu_profissionais)
```

Histórico de Agendamentos
---------------------------

A aba **Histórico** exibe todos os agendamentos realizados, incluindo a data, hora, profissional e serviço. Essa funcionalidade permite que o usuário consulte os agendamentos passados e tenha um controle dos serviços prestados.

Exemplo de código para carregar o histórico:

```python
self.historico_view = MDScrollView(size_hint=(1, 1))
self.historico_content = GridLayout(cols=1, size_hint_y=None)
self.historico_content.bind(minimum_height=self.historico_content.setter('height'))
self.historico_view.add_widget(self.historico_content)
```

Banco de Dados
--------------

O sistema utiliza um banco de dados SQLite para armazenar os profissionais, serviços, horários e agendamentos. A interação com o banco de dados é feita através da classe `Database`, que oferece métodos como:

- **Cadastrar Profissional**: `cadastrar_profissional(nome, servicos)`
- **Cadastrar Horário**: `cadastrar_horario(hora)`
- **Agendar Serviço**: `agendar(data, hora, profissional_id, servico_id)`
- **Consultar Histórico**: `get_historico()`

Funções Utilitárias
--------------------

O sistema inclui funções utilitárias para exibir caixas de diálogo de erro ou sucesso. A função `show_dialog` é utilizada para exibir mensagens ao usuário.

Exemplo de código:

```python
show_dialog("Erro", "Selecione um profissional.")
```

Conclusão
---------

Este sistema foi desenvolvido com o objetivo de facilitar o agendamento de serviços, utilizando uma interface amigável e moderna com o KivyMD. Ele é flexível o suficiente para ser facilmente adaptado para diferentes tipos de serviços e profissionais.

.. raw:: html

    </div>
