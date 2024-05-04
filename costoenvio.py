from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400') 
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
from geopy.geocoders import Nominatim

class RV(RecycleView):
        pass

class MainScreen(Widget):
    def query(self):
        query = self.ids.searchbar.text
        print(query)

class CostoEnvioApp(App):
    title='Shipping cost'    
    def build(self):
        return MainScreen()

CostoEnvioApp().run()