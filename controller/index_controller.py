import customtkinter as ctk
import view.index_view as index_view

class IndexController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, ft: ctk.CTkFrame, fc: ctk.CTkFrame, fb: ctk.CTkFrame):
        if self._initialized: return

        self.ft = ft
        self.fc = fc
        self.fb = fb

        self.view = index_view.IndexView(fc)

        self._initialized = True


if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')