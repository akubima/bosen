import customtkinter as ctk
from view.abc import ViewsComponentsABC

class ViewComponentMessage(ViewsComponentsABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, frame: ctk.CTkFrame, title: str = None, message: str = None):
        super().__init__(frame)
        self.title: str = title or 'Information'
        self.message: str = message or "I'm confused just like you"

    def render(self):
        ctk.CTkLabel(master=self.frame, text=self.title, text_color='#0069ff', font=ctk.CTkFont(size=18, weight='bold')).grid(row=0, column=0, columnspan=3)
        ctk.CTkLabel(master=self.frame, text=self.message, width=350).grid(row=1, column=0, columnspan=3)

    def hide(self):
        for child in self.frame.winfo_children():
            self.grid_config[child] = child.grid_info()
            child.grid_forget()

    def show(self):
        for child, info in self.grid_config.items():
            child.grid(**info)

if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')