import controller
import customtkinter as ctk
from view import search_view

class SearchController:
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

        self.view = search_view.SearchView(self.ft)

        self.category = None
        self.keyword = None

        self.flag_insearch = False

        self._initialized = True

    def search(self, category: ctk.StringVar, keyword: ctk.StringVar):
        self.category = category
        self.keyword = keyword

        controller.index.view.hide()
        self.view.render()
        self.view.hide()

        self.flag_insearch = True

        self.view.show()

        self.flag_insearch = False


if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')