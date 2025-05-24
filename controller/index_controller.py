from customtkinter import CTkFrame
import view.index_view as index_view

class IndexController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, ft: CTkFrame, fc: CTkFrame, fb: CTkFrame):
        if self._initialized: return

        self.ft = ft
        self.fc = fc
        self.fb = fb

        self.view = index_view.IndexView(fc)

        self._initialized = True

    def render(self):
        self.view.render()

    def hide(self):
        self.view.hide()

    def show(self):
        self.view.show()


if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')