
class Cancel(Exception):
    def __init__(self):
        self.value = ''

class Override(Exception):
    def __init__(self):
        self.value = ''
