import paramiko


class base_SSH(object):
    def __init__(self, remote_ip, username, password):
        # self.try_time = time
        self.username = username
        self.password = password
        self.remote_ip = remote_ip
        self.ssh = paramiko.SSHClient()
        # private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')

    # connect server
    def connect(self):
        # 创建一个ssh的白名单
        know_host = paramiko.AutoAddPolicy()
        # 加载创建的白名单
        self.ssh.set_missing_host_key_policy(know_host)
        # 连接服务器
        self.ssh.connect(
            hostname=self.remote_ip,
            port=22,
            username=self.username,
            password=self.password,
            timeout=30
        )

        return True

    def send_command(self, cmd):
        # stdin  标准格式的输入，是一个写权限的文件对象
        # stdout 标准格式的输出，是一个读权限的文件对象
        # stderr 标准格式的错误，是一个写权限的文件对象
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        print(stdout.read().decode())
        return stdout.read()

    def send_command_from_context(self,file_path):
        with open(file_path, 'r', encoding='utf-8', newline='\r\n') as f:
            for cmd in f:
                cmd = cmd.replace('\r', '').replace('\n','')
                self.send_command(cmd)

    def cmd_echo_log(self):
        return True


    def close(self):
        self.ssh.close
        return True





def test():
    hostname = "172.20.78.1"
    username = "root"
    password = "ICnt@258!"
    cmd = "show run"
    host = base_SSH(hostname, username, password)
    host.connect()
    host.send_command_from_context('test.txt')
    host.close()

if __name__ == '__main__':
    test()













