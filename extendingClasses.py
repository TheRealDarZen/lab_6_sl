import SSHLogEntry

class passwdDenied(SSHLogEntry):

    def __init__(self):
        super().__init__()

    def validate(self):
        return self.info['message-type'] == 'Incorrect password'


class passwdAccepted(SSHLogEntry):

    def __init__(self):
        super().__init__()

    def validate(self):
        return self.info['message-type'] == 'Successful login'


class error(SSHLogEntry):

    def __init__(self):
        super().__init__()

    def validate(self):
        return self.info['message-type'] == 'Error'


class otherInfo(SSHLogEntry):

    def __init__(self):
        super().__init__()

    def getMsgType(self):
        return True