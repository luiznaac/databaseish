class Action:

    def __init__(self, function, params=None):
        self.status = 'running'
        self.function = function
        self.params = params

    def perform(self):
        succeeded = self.function(*self.params) if (self.params is not None) else self.function()
        if succeeded:
            self.status = 'finished'
            return

        self.status = 'failed'
        return
