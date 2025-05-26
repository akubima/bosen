import customtkinter as ctk
from view.abc import ViewsComponentsABC

class ViewComponentError(ViewsComponentsABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, frame: ctk.CTkFrame, message: str = None, callback = lambda: None):
        super().__init__(frame)
        self.message: str = message or 'An unknown error occurred!'
        self.callback = callback

    def render(self):
        ctk.CTkLabel(master=self.frame, text="Something is not right...", text_color='#DC2626', font=ctk.CTkFont(
            size=18,
                                                                                            weight='bold')).grid(
            row=0, column=0, columnspan=3)
        ctk.CTkLabel(master=self.frame, text=self.message).grid(row=1, column=0, columnspan=3)
        ctk.CTkButton(master=self.frame, text='Retry', command=lambda: self.callback, height=40, width=100).grid(
            row=2, column=0, columnspan=3,pady=20)

    def hide(self):
        for child in self.frame.winfo_children():
            self.grid_config[child] = child.grid_info()
            child.grid_forget()

    def show(self):
        for child, info in self.grid_config.items():
            child.grid(**info)

if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')