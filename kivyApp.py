from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar
class ConverterApp(MDApp):
    def build(self):
        scr = MDApp()
        self.toolbar = MDToolbar(title='Simple App')
        self.toolbar.pos_hint = {"top":1}
        scr.add_widget(self.toolbar)
        return scr

if __name__ == '__main__':
    ConverterApp().run()