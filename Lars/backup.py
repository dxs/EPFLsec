from config import Config
import subprocess

param = Config()

def BackupSupervisor():
    print("Start Backup Supervisor")
    print("Tar")
    output = subprocess.check_output(['tar', '-cvf', '/tmp/scality-backup/{0}_supervisor.tar'.format(param.date_string), '/var/lib/scality/backup/archives/*{0}*'.format(param.date_string)])

def BackupServers():
    print("backup servers")
    for i in param.server_list:
        output = subprocess.check_output(['scp', 'root@{0}:/var/lib/scality/backup/archives/*{1}*'.format(i,param.date_string), '/tmp/scality-backup/tmp'])


if __name__ == '__main__':
    BackupSupervisor()
    BackupServers()