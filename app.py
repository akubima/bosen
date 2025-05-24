import controller
from controller import index_controller

if __name__ == '__main__':
    index_controller.render()
    index_controller.hide()
    index_controller.show()
    controller.app_controller.run()