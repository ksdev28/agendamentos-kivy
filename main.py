
import sqlite3
import os
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.tab import MDTabs
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.dialog import MDDialog
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp

class Tab(MDBoxLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(10)
        self.spacing = dp(10)
        self.size_hint_x = None
        self.width = dp(300)  # Define a largura fixa para centralização
        self.pos_hint = {'center_x': 0.5}  # Centraliza o layout

class SistemaAgendamento(MDBoxLayout):
    def __init__(self, **kwargs):
        super(SistemaAgendamento, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(10)
        self.spacing = dp(10)
        self.conn = sqlite3.connect('agendamentos.db')
        self.create_tables()
        
        self.tabs = MDTabs()
        self.add_widget(self.tabs)

        # Cadastro de Profissionais e Serviços Tab
        self.cadastro_tab = Tab(title='Cadastro')
        self.cadastro_tab.add_widget(MDLabel(text='Nome do Profissional', halign='center'))
        self.nome_input = MDTextField(hint_text='Nome', size_hint_x=1, pos_hint={'center_x': 0.5})
        self.cadastro_tab.add_widget(self.nome_input)
        
        self.cadastro_tab.add_widget(MDLabel(text='Serviços (separados por vírgula)', halign='center'))
        self.servico_input = MDTextField(hint_text='Serviços', size_hint_x=1, pos_hint={'center_x': 0.5})
        self.cadastro_tab.add_widget(self.servico_input)
        
        self.cadastrar_button = MDRaisedButton(text='Cadastrar', pos_hint={'center_x': 0.5})
        self.cadastrar_button.bind(on_press=self.cadastrar)
        self.cadastro_tab.add_widget(self.cadastrar_button)
        
        self.tabs.add_widget(self.cadastro_tab)

        # Cadastro de Horários Tab
        self.horarios_tab = Tab(title='Horários')
        self.horarios_tab.add_widget(MDLabel(text='Cadastrar Horário (HH:MM)', halign='center'))
        self.horario_input = MDTextField(hint_text='Horário', size_hint_x=1, pos_hint={'center_x': 0.5})
        self.horarios_tab.add_widget(self.horario_input)
        
        self.cadastrar_horario_button = MDRaisedButton(text='Cadastrar Horário', pos_hint={'center_x': 0.5})
        self.cadastrar_horario_button.bind(on_press=self.cadastrar_horario)
        self.horarios_tab.add_widget(self.cadastrar_horario_button)
        
        self.tabs.add_widget(self.horarios_tab)

        # Agendamento Tab
        self.agendamento_tab = Tab(title='Agendamento')
        self.agendamento_tab.add_widget(MDLabel(text='Profissional', halign='center'))
        
        self.profissional_button = MDRaisedButton(text="Selecione o Profissional", pos_hint={'center_x': 0.5})
        self.profissional_button.bind(on_release=self.open_menu_profissionais)
        self.agendamento_tab.add_widget(self.profissional_button)
        
        self.agendamento_tab.add_widget(MDLabel(text='Serviço', halign='center'))
        self.servico_button = MDRaisedButton(text="Selecione o Serviço", pos_hint={'center_x': 0.5})
        self.servico_button.bind(on_release=self.open_menu_servicos)
        self.agendamento_tab.add_widget(self.servico_button)
        
        self.agendamento_tab.add_widget(MDLabel(text='Data', halign='center'))
        self.data_button = MDRaisedButton(text="Selecione a Data", pos_hint={'center_x': 0.5})
        self.data_button.bind(on_release=self.show_date_picker)
        self.agendamento_tab.add_widget(self.data_button)
        
        self.agendamento_tab.add_widget(MDLabel(text='Hora', halign='center'))
        self.hora_button = MDRaisedButton(text="Selecione a Hora", pos_hint={'center_x': 0.5})
        self.hora_button.bind(on_release=self.open_menu_horarios)
        self.agendamento_tab.add_widget(self.hora_button)
        
        self.agendar_button = MDRaisedButton(text='Agendar', pos_hint={'center_x': 0.5})
        self.agendar_button.bind(on_press=self.agendar)
        self.agendamento_tab.add_widget(self.agendar_button)
        
        self.tabs.add_widget(self.agendamento_tab)
        self.profissionais_menu = None
        self.servicos_menu = None
        self.horarios_menu = None
        self.profissional_ids = {}
        self.servico_ids = {}
        self.horario_ids = {}
        self.load_profissionais()
        self.load_horarios()

        # Histórico Tab
        self.historico_tab = Tab(title='Histórico')
        self.historico_tab.add_widget(MDLabel(text='Histórico de Atendimentos', halign='center'))
        
        self.historico_view = MDScrollView(size_hint=(1, None), size=(400, 200))
        self.historico_content = GridLayout(cols=1, size_hint_y=None)
        self.historico_content.bind(minimum_height=self.historico_content.setter('height'))
        self.historico_view.add_widget(self.historico_content)
        self.historico_tab.add_widget(self.historico_view)
        
        self.tabs.add_widget(self.historico_tab)
        self.load_historico()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS profissionais
                                 (id INTEGER PRIMARY KEY, nome TEXT)''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS servicos
                                 (id INTEGER PRIMARY KEY, nome TEXT, profissional_id INTEGER)''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS horarios
                                 (id INTEGER PRIMARY KEY, hora TEXT)''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS agendamentos
                                 (id INTEGER PRIMARY KEY, data TEXT, hora TEXT, profissional_id INTEGER, servico_id INTEGER)''')

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ],
        )
        dialog.open()

    def cadastrar(self, instance):
        nome = self.nome_input.text
        servicos = self.servico_input.text.split(',')
        if nome and servicos:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute('INSERT INTO profissionais (nome) VALUES (?)', (nome,))
                profissional_id = cursor.lastrowid
                for servico in servicos:
                    cursor.execute('INSERT INTO servicos (nome, profissional_id) VALUES (?, ?)', (servico.strip(), profissional_id))
            self.show_dialog("Cadastro Realizado", f"Cadastrado: {nome} com serviços {', '.join(servicos)}")
            self.load_profissionais()
        else:
            self.show_dialog("Erro", "Nome e serviços não podem estar vazios.")

    def cadastrar_horario(self, instance):
        hora = self.horario_input.text
        if hora:
            with self.conn:
                self.conn.execute('INSERT INTO horarios (hora) VALUES (?)', (hora,))
            self.show_dialog("Horário Cadastrado", f"Horário {hora} cadastrado com sucesso.")
            self.load_horarios()
        else:
            self.show_dialog("Erro", "Horário não pode estar vazio.")

    def load_profissionais(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, nome FROM profissionais')
        profissionais = cursor.fetchall()
        
        menu_items = []
        self.profissional_ids = {}
        
        for p in profissionais:
            menu_items.append({
                "viewclass": "OneLineListItem",
                "text": p[1],
                "on_release": lambda x=p[1]: self.set_profissional(x),
            })
            self.profissional_ids[p[1]] = p[0]
        
        self.profissionais_menu = MDDropdownMenu(
            caller=self.profissional_button,
            items=menu_items,
            width_mult=4
        )

    def open_menu_profissionais(self, instance):
        if self.profissionais_menu:
            self.profissionais_menu.open()

    def set_profissional(self, text_item):
        self.profissional_button.text = text_item
        self.profissionais_menu.dismiss()
        profissional_id = self.profissional_ids[text_item]
        self.load_servicos(profissional_id)

    def load_servicos(self, profissional_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, nome FROM servicos WHERE profissional_id=?', (profissional_id,))
        servicos = cursor.fetchall()
        
        menu_items = []
        self.servico_ids = {}
        
        for s in servicos:
            menu_items.append({
                "viewclass": "OneLineListItem",
                "text": s[1],
                "on_release": lambda x=s[1]: self.set_servico(x),
            })
            self.servico_ids[s[1]] = s[0]
        
        self.servicos_menu = MDDropdownMenu(
            caller=self.servico_button,
            items=menu_items,
            width_mult=4
        )

    def open_menu_servicos(self, instance):
        if self.servicos_menu:
            self.servicos_menu.open()

    def set_servico(self, text_item):
        self.servico_button.text = text_item
        self.servicos_menu.dismiss()

    def load_horarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, hora FROM horarios')
        horarios = cursor.fetchall()
        
        menu_items = []
        self.horario_ids = {}
        
        for h in horarios:
            menu_items.append({
                "viewclass": "OneLineListItem",
                "text": h[1],
                "on_release": lambda x=h[1]: self.set_horario(x),
            })
            self.horario_ids[h[1]] = h[0]
        
        self.horarios_menu = MDDropdownMenu(
            caller=self.hora_button,
            items=menu_items,
            width_mult=4
        )

    def open_menu_horarios(self, instance):
        if self.horarios_menu:
            self.horarios_menu.open()

    def set_horario(self, text_item):
        self.hora_button.text = text_item
        self.horarios_menu.dismiss()

    def show_date_picker(self, instance):
        date_picker = MDDatePicker()
        date_picker.bind(on_save=self.on_date_selected)
        date_picker.open()

    def on_date_selected(self, instance, value, date_range):
        self.data_button.text = str(value)

    def agendar(self, instance):
        data = self.data_button.text
        hora_info = self.hora_button.text
        profissional_info = self.profissional_button.text
        servico_info = self.servico_button.text

        if not profissional_info or "Selecione" in profissional_info:
            self.show_dialog("Erro", "Selecione um profissional.")
            return

        if not servico_info or "Selecione" in servico_info:
            self.show_dialog("Erro", "Selecione um serviço.")
            return

        if not hora_info or "Selecione" in hora_info:
            self.show_dialog("Erro", "Selecione um horário.")
            return

        profissional_id = self.profissional_ids[profissional_info]
        servico_id = self.servico_ids[servico_info]
        hora = hora_info
        
        if self.is_horario_disponivel(data, hora, profissional_id):
            with self.conn:
                self.conn.execute('INSERT INTO agendamentos (data, hora, profissional_id, servico_id) VALUES (?, ?, ?, ?)',
                                  (data, hora, profissional_id, servico_id))
            self.show_dialog("Agendamento Concluído", f"Agendado para {data} às {hora}, Serviço: {servico_info}")
            self.load_historico()
        else:
            self.show_dialog("Erro", "Horário já ocupado.")

    def is_horario_disponivel(self, data, hora, profissional_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM agendamentos WHERE data=? AND hora=? AND profissional_id=?',
                       (data, hora, profissional_id))
        return cursor.fetchone() is None

    def load_historico(self):
        self.historico_content.clear_widgets()
        cursor = self.conn.cursor()
        cursor.execute('''SELECT a.data, a.hora, p.nome, s.nome 
                          FROM agendamentos a 
                          JOIN profissionais p ON a.profissional_id = p.id 
                          JOIN servicos s ON a.servico_id = s.id''')
        for row in cursor.fetchall():
            self.historico_content.add_widget(MDLabel(text=f"Data: {row[0]}, Hora: {row[1]}, Profissional: {row[2]}, Serviço: {row[3]}"))

class AgendamentoApp(MDApp):
    def build(self):
        return SistemaAgendamento()

if __name__ == '__main__':
    # Remova o banco de dados existente para recriar as tabelas com o novo esquema
    if os.path.exists('agendamentos.db'):
        os.remove('agendamentos.db')
    AgendamentoApp().run()
