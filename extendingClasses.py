import SSHLogEntry


INCORR_PASSWD = 'Incorrect password'
CORR_PASSWD = 'Successful login'
ERR = 'Error'

class passwdDenied(SSHLogEntry):

    def __init__(self):
        super().__init__()

    def validate(self):
        return self.info['message-type'] == INCORR_PASSWD


class passwdAccepted(SSHLogEntry):

    def __init__(self):
        super().__init__()

    def validate(self):
        return self.info['message-type'] == CORR_PASSWD


class error(SSHLogEntry):

    def __init__(self):
        super().__init__()

    def validate(self):
        return self.info['message-type'] == ERR


class otherInfo(SSHLogEntry):

    def __init__(self):
        super().__init__()

    def getMsgType(self):
        return True