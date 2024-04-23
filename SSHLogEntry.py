import ipaddress
from process import line_to_dict
from abc import ABC, abstractmethod

class SSHLogEntry(ABC):

    def __init__(self, line):
        self._log = line
        self.info = line_to_dict(line)

    def getLog(self):
        return self._log

    def getIPv4(self):
        if self.info['ip']:
            return ipaddress.IPv4Address(self.info['ip'])
        return None

    def validate(self):
        pass

    @property
    def has_ip(self):
        return True if self.info['ip'] else False

    def __repr__(self):
        return f"SSHLogEntry({repr(self._log)})"

    def __eq__(self, other):
        if not isinstance(other, SSHLogEntry):
            return False
        return self._log == other._log

    def __lt__(self, other):
        if not isinstance(other, SSHLogEntry):
            raise TypeError("Unmatched type of compared objects")
        return self._log < other._log

    def __gt__(self, other):
        if not isinstance(other, SSHLogEntry):
            raise TypeError("Unmatched type of compared objects")
        return self._log > other._log