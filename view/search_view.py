import os
import customtkinter as ctk
import controller
import model.data as modeldata
from view.abc import ViewsComponentsABC

class SearchView(ViewsComponentsABC):
    def __init__(self, frame: ctk.CTkFrame):
        super().__init__(frame)
        self.widget_keyword_category: ctk.CTkComboBox|None = None
        self.widget_keyword: ctk.CTkEntry|None = None

    def render(self):
        ctk.CTkLabel(master=self.frame, text=os.getenv('APP_NAME'), text_color='#0069ff', font=ctk.CTkFont(size=38,weight='bold')).grid(row=0, column=0, columnspan=3)

        # SEARCH SECTION
        self.widget_keyword_category = ctk.CTkComboBox(self.frame, values=list(modeldata.available_search_categories.values()), height=40, width=120, font=ctk.CTkFont(weight='bold'))
        self.widget_keyword_category.grid(row=1, column=0, padx=5, pady=15)
        self.widget_keyword_category.set(controller.search.category)

        self.widget_keyword = ctk.CTkEntry(self.frame, placeholder_text='Search keyword...', height=40, width=300)
        self.widget_keyword.grid(row=1, column=1,padx=5,pady=15)
        self.widget_keyword.insert(0, controller.search.keyword)

        ctk.CTkButton(self.frame, text='Search', height=40, width=100, command=lambda:controller.search.search(
            self.widget_keyword_category.get(), self.widget_keyword.get())).grid(row=1, column=2, padx=5, pady=15)

    def hide(self):
        for child in self.frame.winfo_children():
            self.grid_config[child] = child.grid_info()
            child.grid_forget()

    def show(self):
        for child, info in self.grid_config.items():
            child.grid(**info)

if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')