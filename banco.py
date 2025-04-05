
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

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

    def cadastrar_profissional(self, nome, servicos):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO profissionais (nome) VALUES (?)', (nome,))
            profissional_id = cursor.lastrowid
            for servico in servicos:
                cursor.execute('INSERT INTO servicos (nome, profissional_id) VALUES (?, ?)', (servico.strip(), profissional_id))

    def cadastrar_horario(self, hora):
        with self.conn:
            self.conn.execute('INSERT INTO horarios (hora) VALUES (?)', (hora,))

    def get_profissionais(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, nome FROM profissionais')
        return cursor.fetchall()

    def get_servicos(self, profissional_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, nome FROM servicos WHERE profissional_id=?', (profissional_id,))
        return cursor.fetchall()

    def get_horarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, hora FROM horarios')
        return cursor.fetchall()

    def is_horario_disponivel(self, data, hora, profissional_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM agendamentos WHERE data=? AND hora=? AND profissional_id=?',
                       (data, hora, profissional_id))
        return cursor.fetchone() is None

    def agendar(self, data, hora, profissional_id, servico_id):
        with self.conn:
            self.conn.execute('INSERT INTO agendamentos (data, hora, profissional_id, servico_id) VALUES (?, ?, ?, ?)',
                              (data, hora, profissional_id, servico_id))

    def get_historico(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT a.data, a.hora, p.nome, s.nome 
                          FROM agendamentos a 
                          JOIN profissionais p ON a.profissional_id = p.id 
                          JOIN servicos s ON a.servico_id = s.id''')
        return cursor.fetchall()
