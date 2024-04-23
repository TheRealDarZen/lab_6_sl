from SSHLogEntry import SSHLogEntry
from SSHLogJournal import SSHLogJournal
import re

class SSHUser:
    def __init__(self, name, lastLogin):
        self.name = name
        self.lastLogin = lastLogin

    def setName(self, name):
        self.name = name

    def setLastLogin(self, lastLogin):
        self.lastLogin = lastLogin

    def validate(self):
        pattern = r'^[a-z_][a-z0-9_-]{0,31}$'
        return True if re.match(pattern, self.name) else False
