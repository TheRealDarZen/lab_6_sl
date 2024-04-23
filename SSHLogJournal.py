from SSHLogEntry import SSHLogEntry
import ipaddress

class SSHLogJournal:
    def __init__(self, lines):
        self.logs = []
        for line in lines:
            self.logs.append(SSHLogEntry(line))

    def __len__(self):
        return len(self.logs)

    def __iter__(self):
        return iter(self.logs)

    def __contains__(self, item):
        return item in self.logs

    def __getitem__(self, item):
        return self.logs[item]

    def append(self, line):
        newEntry = SSHLogEntry(line)
        newEntry.validate()
        self.logs.append(newEntry)

    def getLogsForIpv4(self, ip):
        result = []
        for log in self.logs:
            if log.has_ip():
                if log.getIPv4() == ipaddress.IPv4Address(ip):
                    result.append(log)
        return result