import inspect
from threading import Lock
from clazz.ControlHandler import ControlHandler
from clazz.ListController import ListController


class ControllerService:
    handler: ControlHandler
    controller: ListController
    isBusy = False

    def __init__(self):
        self.lock = Lock()
        pass

    def isHandlerValid(self):
        return self.handler is not None

    def setControlHandler(self, handler):
        import inspect
        if inspect.stack()[1].frame.f_locals['self'] == handler:
            self.handler = handler
        pass

    def emptyHandler(self):
        if inspect.stack()[1].frame.f_locals['self'] == self.handler and isinstance(self.handler, ControlHandler):
            self.handler = None  # FIXME

    def call_handler(self, request):
        with self.lock:
            if self.isHandlerValid():
                self.handler.append(request)
            else:
                ControlHandler(self.controller, request)
