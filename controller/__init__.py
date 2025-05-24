from controller.app_controller import AppController
from controller.index_controller import IndexController

if __name__ != 'main':
    app_controller = AppController()
    index_controller = IndexController(app_controller.ft, app_controller.fc, app_controller.fb)
else:
    raise RuntimeError('Should NOT be executed directly!')