import os
import customtkinter as ctk
import model.data as modeldata
from view.abc import ViewsComponentsABC

class IndexView(ViewsComponentsABC):
    def __init__(self, frame: ctk.CTkFrame):
        super().__init__(frame)
        self.keyword_category_val = ctk.StringVar(value=modeldata.available_search_keyword['intitle'])

    def render(self):
        # HERO SECTION
        ctk.CTkLabel(master=self.frame, text=os.getenv('APP_NAME'), text_color='#0069ff', font=ctk.CTkFont(size=44,
                                                                                                weight='bold')).grid(row=0, column=0, columnspan=3)
        ctk.CTkLabel(master=self.frame, text='"'+os.getenv('APP_DESCRIPTION')+'"', font=ctk.CTkFont(size=18)).grid(
            row=1, column=0, columnspan=3)

        # SEARCH SECTION
        ctk.CTkComboBox(self.frame, values=list(modeldata.available_search_keyword.values()), height=40, width=120,
                        font=ctk.CTkFont(weight='bold'), variable=self.keyword_category_val).grid(row=3, column=0, padx=5, pady=40)
        ctk.CTkEntry(self.frame, placeholder_text='Search keyword...', height=40, width=300).grid(row=3, column=1,
                                                                                                  padx=5,pady=40)
        ctk.CTkButton(self.frame, text='Search', height=40, width=100).grid(row=3, column=2, padx=5, pady=40)

    def hide(self):
        for child in self.frame.winfo_children():
            self.grid_config[child] = child.grid_info()
            child.grid_forget()

    def show(self):
        for child, info in self.grid_config.items():
            child.grid(**info)