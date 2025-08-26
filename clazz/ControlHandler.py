from inspect import stack
from typing import final
from urllib.request import Request

from clazz.ControllerService import ControllerService
from clazz.ListController import ListController


@final
class ControlHandler:
    def __init__(self, controller : ListController, request):
        self.isProcessing = False
        self.controller = controller
        self.que = []
        self.que.append(request)
        if stack()[1].frame.f_locals['self'] == ControllerService:
          service = stack()[1].frame.f_locals['self']
          service.setControlHandler(self)
        while self.que:
            self.handle(self.que.pop(0))


    def handle(self, request):
        if not self.isProcessing:
            self.isProcessing = True
            self.controller.controllRequest(request)
            self.isProcessing = False

    def append(self, request):
        self.que.append(request)
