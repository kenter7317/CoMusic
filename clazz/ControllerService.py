from clazz.ControlHandler import ControlHandler
from clazz.ListController import ListController


class ControllerService:

    handler : ControlHandler
    controller : ListController

    def __init__(self):

        pass

    def isHandlerValid(self):
        return self.handler is not None
        pass

    def setControlHandler(self, handler):
        import inspect
        if inspect.stack()[1].frame.f_locals['self'] == handler:
            self.handler = handler
        pass

    def call_handler(self, request):
        if self.isHandlerValid():
            self.handler.append(request)
        else:
            ControlHandler(self.controller, request)