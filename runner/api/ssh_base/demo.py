
import paramiko

# 创建一个ssh的客户端，用来连接服务器
ssh = paramiko.SSHClient()
# 创建一个ssh的白名单
know_host = paramiko.AutoAddPolicy()
# 加载创建的白名单
ssh.set_missing_host_key_policy(know_host)
# 连接服务器
private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
ssh.connect(
    hostname="172.20.1.175",
    port=22,
    username="admin",
    password="1qaz!QAZ"
)

# 执行命令
stdin, stdout, stderr = ssh.exec_command("show running-config ")
# stdin  标准格式的输入，是一个写权限的文件对象
# stdout 标准格式的输出，是一个读权限的文件对象
# stderr 标准格式的错误，是一个写权限的文件对象
private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')

print(stdout.read().decode())
ssh.close()
