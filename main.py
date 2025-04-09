from kivymd.app import MDApp
from telas import SistemaAgendamento
from kivy.core.window import Window

Window.size = (582, 855)

class AgendamentoApp(MDApp):
    def build(self):
        self.title = "Sistema de Agendamentos - Kivy"
        self.theme_cls.theme_style = "Dark"   #Tema principal
        self.theme_cls.primary_palette = "DeepPurple" 
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_hue = "400"
        return SistemaAgendamento()
    
    


if __name__ == '__main__':
    AgendamentoApp().run()
