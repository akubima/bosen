import customtkinter as ctk
from abc import ABC, abstractmethod

class ViewsComponentsABC(ABC):
    @abstractmethod
    def __init__(self, frame: ctk.CTkFrame):
        self.frame = frame
        self.grid_config = {}

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def hide(self):
        pass

    @abstractmethod
    def show(self):
        pass