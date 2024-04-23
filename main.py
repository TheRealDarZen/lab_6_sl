from SSHLogEntry import SSHLogEntry
from SSHLogJournal import SSHLogJournal
from SSHUser import SSHUser
import sys

if __name__ == "__main__":
    input = sys.stdin.readlines()
    journal = SSHLogJournal(input)

    list = []

    for i in range(5):
        list.append(journal[i+50])
        list.append(SSHUser("Name", i))

    for item in list:
        print(item.validate())