
class Cancel(Exception):
    def __init__(self):
        self.value = ''

class Override(Exception):
    def __init__(self):
        self.value = ''

class TooMany(Exception):
    def __init__(self):
        self.value = ''

def comm_cancel(content):
    if content == 'c':
        raise Cancel()

    if content.startswith('!'):
        raise Override()

    return None
