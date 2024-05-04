from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400') 
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView

class RV(RecycleView):
    data=[{'text':'1'},{'text':'2'}]

class MainScreen(Widget):
    pass

class MainApp(App):
    title='Shipping cost'
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MainApp().run()