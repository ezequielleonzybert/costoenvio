from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

class RV(RecycleView):
    data = [{'text': 'hello'},{'text':'bye'}]

class RecycleApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    RecycleApp().run()