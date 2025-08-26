class ListController:

    mem_location = ""

    def __init__(self):
        if self.hasLeftedList():
           list = self.load_list()
        else:
            list = self.create_list()
        pass

    def hasLeftedList(self):
        # todo
        pass

    def load_list(mem_location):
        # todo return
        pass

    def create_list(self):
        # todo return
        pass

    def controll_list(self):
        pass

    async def controllRequest(self, request):
        pass