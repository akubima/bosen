from io import BytesIO
from PIL import Image
import customtkinter as ctk, requests
from etc.tools import limit_text
from view.abc import ViewsComponentsABC
from CTkMessagebox import CTkMessagebox
import webbrowser

class ViewComponentBooks(ViewsComponentsABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, frame: ctk.CTkFrame, books: list[dict]):
        super().__init__(frame)
        self.books: list[dict] = books

    def render(self):
        try:
            print(self.books)
            for index, book in enumerate(self.books):

                if book['kind'] != 'books#volume' or book['volumeInfo'] is None:
                    continue

                row = index // 2
                col_base = (index % 2) * 3  # 0 untuk kiri, 3 untuk kanan

                image_url = book['volumeInfo'].get('imageLinks', {}).get(
                    'thumbnail',
                    'https://dummyimage.com/128x200/cccccc/000000&text=No+Image'
                )

                response = requests.get(image_url)
                response.raise_for_status()

                image = ctk.CTkImage(
                    light_image=Image.open(BytesIO(response.content)),
                    dark_image=Image.open(BytesIO(response.content)),
                    size=(50, 63)
                )

                ctk.CTkLabel(master=self.frame, text='', image=image).grid(
                    row=row,
                    column=col_base,
                    padx=5,
                    pady=5,
                    sticky="n"
                )

                ctk.CTkLabel(master=self.frame,
                             text=limit_text(book['volumeInfo'].get('title', '')),
                             font=ctk.CTkFont(weight='bold')).grid(
                    row=row,
                    column=col_base + 1,
                    padx=5,
                    pady=0,
                    sticky="nw"
                )

                ctk.CTkLabel(master=self.frame,
                             text=limit_text('By: ' + ", ".join(book['volumeInfo'].get('authors', ['Unknown']))),
                             font=ctk.CTkFont(size=11)).grid(
                    row=row,
                    column=col_base + 1,
                    padx=5,
                    pady=5,
                    sticky="w"
                )

                ctk.CTkLabel(master=self.frame,
                             text=limit_text(book['volumeInfo'].get('publisher', 'Unknown')),
                             font=ctk.CTkFont(size=11)).grid(
                    row=row,
                    column=col_base + 1,
                    padx=5,
                    pady=0,
                    sticky="sw"
                )

                ctk.CTkButton(self.frame,
                              text='Detail',
                              height=40,
                              width=100,
                              command=lambda b=book: webbrowser.open(b['volumeInfo'].get('infoLink',
                                                                                      'https://books.google.com/'))
                ).grid(
                    row=row,
                    column=col_base + 2,
                    padx=5,
                    pady=5
                )
        except Exception as e:
            CTkMessagebox(title='An error occurred!', message=f'{type(e).__name__}. Please try again in a moment.',
                          icon='warning')
            print(str(e))

    def hide(self):
        for child in self.frame.winfo_children():
            self.grid_config[child] = child.grid_info()
            child.grid_forget()

    def show(self):
        for child, info in self.grid_config.items():
            child.grid(**info)

if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')