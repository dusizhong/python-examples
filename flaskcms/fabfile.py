from fabric.api import *

hostweb1 = 'root@112.126.69.157:22'
hostweb2 = 'root@112.126.69.157:22'
hostweb3 = 'root@112.126.69.157:22'
hostdb = 'root@112.126.69.157:22'

env.hosts = [hostweb1,hostweb2,hostweb3,hostdb]

env.password = 'admin123'

env.roledefs = {
    'web' : [hostweb1,hostweb2,hostweb3],
    'db' : [hostdb]
}

@hosts(hostweb1)
def demo():
    run('ifconfig')

    with settings(warn_only=True):
        cd('/ddd/fff')

    run('ls -l')

@roles('web')
def demo2():
    run('ifconfig')

    with settings(warn_only=True):
        cd('/ddd/fff')

    run('ls -l')

