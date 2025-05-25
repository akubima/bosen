import os
import customtkinter as ctk
from view.abc import ViewsComponentsABC

class ViewComponentFooter(ViewsComponentsABC):
    def __init__(self, frame: ctk.CTkFrame):
        super().__init__(frame)

    def render(self):
        ctk.CTkLabel(master=self.frame, text=os.getenv('APP_DESCRIPTION') + ' \u00B7 \u00A9 2025 Bima Mukhlisin Bil Sajjad, Revaldi Rifwianda, Dafa Dzaki Putra Husada under MIT License \u00B7 Version ' + os.getenv('APP_VERSION'), font=ctk.CTkFont(size=12)).grid(padx=10)

    def hide(self):
        for child in self.frame.winfo_children():
            self.grid_config[child] = child.grid_info()
            child.grid_forget()

    def show(self):
        for child, info in self.grid_config.items():
            child.grid(**info)

if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')