
from kivy.app import App
from kivy.uix.actionbar import ActionBar
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window



class ActionBar(ActionBar):
    def btnNuev(self):
        show_nuevo()
    def btnMod(self):
        show_Mod()
    def btnVer(self):
        show_exp()

class Nuevo(FloatLayout):
    pass
def show_nuevo():
    show = Nuevo()

    popupWindow = Popup(title="Nuevo Formato", content=show, size_hint=(None,None),size=(800,600))

    popupWindow.open()
class Modificar(FloatLayout):
    pass
def show_Mod():
    show = Modificar()

    popupWindow = Popup(title="Modificar", content=show, size_hint=(None,None),size=(800,600))

    popupWindow.open()

class Ver(FloatLayout):
    pass
def show_exp():
    show = Ver()

    popupWindow = Popup(title="Modificar", content=show, size_hint=(None,None),size=(800,600))

    popupWindow.open()






class MainWindowApp(App):
    def build(self):
        return ActionBar()
if __name__ == "__main__":
    Window.maximize()
    MainWindowApp().run()
