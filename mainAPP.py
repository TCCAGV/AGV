from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass


class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class addAMB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
       
class mainAPP(App):
    def build(self):      
        return Gerenciador()
    
    
mainAPP().run()