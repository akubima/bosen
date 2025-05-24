from controller.app_controller import AppController
from controller.index_controller import IndexController
from controller.search_controller import SearchController

if __name__ != 'main':
    app = AppController()
    index = IndexController(app.ft, app.fc, app.fb)
    search = SearchController(app.ft, app.fc, app.fb)
else:
    raise RuntimeError('Should NOT be executed directly!')