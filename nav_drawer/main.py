from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.app import App
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineAvatarListItem
from kivy.properties import StringProperty
from kivymd.toast import toast

class ContentNavigationDrawer(BoxLayout):
    """Base Widget for Navigation Drawer"""
    pass

class FirstNavItem(OneLineAvatarListItem):
    """Item in Nav Drawer callback to First screen"""
    icon = StringProperty()
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def callback(self):
        toast(f"First")
        ###################################################
        #functions for populating and going to your screen go here
        ###################################################
        self.app.root.ids.nav_drawer.set_state('toggle')
        


class SecondNavItem(OneLineAvatarListItem):
    """Item in Nav Drawer callback to Second screen"""
    icon = StringProperty()
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def callback(self):
        toast(f"Second")
        ###################################################
        #functions for populating and going to your screen go here
        ###################################################
        self.app.root.ids.nav_drawer.set_state('toggle')
    



    
def build_nav_drawer(running_app):
    running_app.root.ids.content_drawer.ids.box_item.clear_widgets()
    running_app.root.ids.content_drawer.ids.box_item.add_widget(FirstNavItem(icon="home-circle-outline", text="First"))
    running_app.root.ids.content_drawer.ids.box_item.add_widget(SecondNavItem(icon="exit-to-app", text="Second"))





class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.name_selected = None
        self.title = "My Material Application"
        super().__init__(**kwargs)

    def on_start(self):
        build_nav_drawer(self)
    

if __name__ == "__main__":
    my_app = MainApp()
    my_app.run()