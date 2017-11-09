

class JsonError(Exception):
    """Base class for exceptions """
    pass

class JsonKeyError(JsonError):
    """Exception raised in utils.py if the value associated with the input json key does not match the expected format

        Attributes:
            key -- json key 
            value -- json value that doesn't fit structure 
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
