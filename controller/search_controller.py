import model.data
import controller
import customtkinter as ctk
from model.search_model import SearchModel
from view import search_view
from view.components.books import ViewComponentBooks
from view.components.error import ViewComponentError
from CTkMessagebox import CTkMessagebox

from view.components.message import ViewComponentMessage


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
        self.flag_insearch = False
        self.category = None
        self.category_key = None
        self.keyword = None
        self._initialized = True

    def search(self, category: str, keyword: str):

        # If there is any ongoing search request abort
        if self.flag_insearch: return False

        print('search')

        self.category = category
        self.keyword = keyword

        # INPUT VALIDATION
        if self.category is None or self.category not in model.data.available_search_categories.values():
            CTkMessagebox(title='Invalid Input', message=f'Search category "{self.category}" is invalid!', icon='warning')
            return False
        if self.keyword is None or len(self.keyword) == 0:
            CTkMessagebox(title='Invalid Input', message='Search keyword must not be empty!', icon='warning')
            return False

        self.flag_insearch = True

        # Get key based on value
        for key, value in model.data.available_search_categories.items():
            if value == self.category: self.category_key = key

        # FETCH DATA
        try:
            print(self.category_key, self.keyword)
            response = SearchModel.api_search(self.category_key, self.keyword)
            response_data: dict = dict(response.json())
        except Exception as e:
            CTkMessagebox(title='An error occurred!', message=f'{type(e).__name__}. Please try again in a moment.',
                          icon='warning')
            self.flag_insearch = False
            return False
        # FETCH DATA END

        controller.index.view.hide()

        if response.status_code == 200:
            self.view.render()
            if response_data['totalItems'] == 0:
                ViewComponentMessage(self.fc, 'No Results Found', f'There are no books with {self.category}: {self.keyword}. Try a different search term!').render()
            else:
                ViewComponentBooks(self.fc, response_data['items'][:10]).render()
                print(response_data['items'][0]['volumeInfo']['title'])
        else:
            ViewComponentError(frame=self.fc, message=getattr(getattr(response_data, 'error', None), 'message',None)).render()

        self.flag_insearch = False

        return True


if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')