class ExternalResourceError(Exception):
    pass


class InternalServerError(Exception):
    def __init__(self, error: str):
        super(InternalServerError, self).__init__()
        self.error_msg = error


class SymbolNotFoundError(Exception):
    pass
