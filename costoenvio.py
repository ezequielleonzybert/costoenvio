from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '600') 
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
from geopy.adapters import AioHTTPAdapter
from geopy.geocoders import Nominatim
import asyncio

class RV(RecycleView):
    def set_data(self,locations):
        self.data = []
        if locations:
            for location in locations:
                self.data.append({'text': str(location)})
                # print(location.raw)
                print(location.point)

class MainWidget(Widget): 

    async def query(self):
        query = self.ids.searchbar.text 
        async with Nominatim(
            user_agent="costoenvio",
            adapter_factory=AioHTTPAdapter,
            timeout=3
        ) as geolocator:
            locations = await geolocator.geocode(query, exactly_one=False, country_codes='AR')
            self.ids.rv.set_data(locations)
            
    def awaitquery(self):
        asyncio.create_task(self.query())

class CostoEnvioApp(App):
    title='Shipping cost'
    def build(self):
        return MainWidget()

# CostoEnvioApp().run()
asyncio.run(CostoEnvioApp().async_run('asyncio'))