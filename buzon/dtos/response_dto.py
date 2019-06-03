class ResponseDto(object):

    def __init__(self, data=None, status=True, message="Correcto"):
        self.Status = status
        self.Message = message
        self.Data = data
