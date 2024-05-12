from kivy.app import App
from kivy.uix.label import Label
import asyncio

class ExampleApp(App):
    
    def build(self):
        return Label(text = 'Greetings Earthlings')

    def on_start(self):
        print("Kivy app started")
        asyncio.create_task(self.my_async_function())
    
    async def my_async_function(self):
        print("woohooo running async function on kivy app")
        await self.another_async_function()

    async def another_async_function(self):
        print("another async function")
        
# Start kivy app as an asynchronous task
asyncio.run(ExampleApp().async_run('asyncio'))