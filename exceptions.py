class EmptyStringException(Exception):
    def __init__(self, message="The data is empty, please check the string again."):
        self.message = message
        super().__init__(self.message)

class InvalidStringException(Exception):
    def __init__(self, message="The data is invalid, please check the string again."):
        self.message = message
        super().__init__(self.message)