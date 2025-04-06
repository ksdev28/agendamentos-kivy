from kivymd.app import MDApp
from telas import SistemaAgendamento
from kivy.core.window import Window

Window.size = (1100, 800)

class AgendamentoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"  # muda a cor principal
        self.theme_cls.theme_style = "Dark"     # ou "Dark"
        return SistemaAgendamento()


if __name__ == '__main__':
    AgendamentoApp().run()
