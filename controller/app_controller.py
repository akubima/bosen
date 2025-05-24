import os
import customtkinter as ctk
from dotenv import load_dotenv
from view.components.footer import ViewComponentFooter

class AppController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized: return

        load_dotenv(override=True)
        ctk.set_default_color_theme('etc/theme_default.json')
        ctk.set_appearance_mode(os.getenv('APP_DEFAULT_APPEARANCE') or 'system')

        self.window = ctk.CTk()
        self.window.after(0, lambda:self.window.state('zoomed'))
        self.window.minsize(800, 600)
        self.window.title(os.getenv('APP_NAME') + ' - ' + os.getenv('APP_FULL_NAME'))

        self.ft = ctk.CTkFrame(master=self.window, fg_color='transparent')
        self.ft.place(relx=0.5, rely=0.02, anchor='n')

        self.fc = ctk.CTkFrame(master=self.window, fg_color='transparent')
        self.fc.place(relx=0.5, rely=0.5, anchor='center')

        self.fb = ctk.CTkFrame(master=self.window, fg_color='transparent')
        self.fb.place(relx=0.5, rely=0.98, anchor='s')

        ViewComponentFooter(self.fb).render()

        self._initialized = True

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')