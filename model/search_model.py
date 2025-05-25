import requests, os

class SearchModel:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized: return
        self._initialized = True

    @classmethod
    def api_search(cls, category: str, keyword: str):
        return requests.get(url=os.getenv('GOOGLE_BOOKS_API_URL'), params={
            'q': str(category) + ':' + keyword
        })

if __name__ == '__main__':
    raise RuntimeError('Should NOT be executed directly!')