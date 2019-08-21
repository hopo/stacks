from fabric.api import env, local, run, cd, prefix, hide, execute

# Fabric Settings
env.user = 'ubuntu'
env.key_filename = '~/.ssh/bongbong.pem'

# Fabric Settings for overriding via env
HOSTS_MAP = {
    'dev': ['dev.bongbong.com'],
    'prod': ['bongbong.com']
}

# 원격지에 있는 프로젝트 디렉토리
project_dir = '/var/www/service/bongbong'


def _get_latest_source(branch, commit):
    run('git fetch')
    run('git checkout %s' % (branch, ))
    run('git reset --hard %s' % (commit, ))

def _install_packages():
    run('pip3 install -r requirements.txt', warn_only=True)

def _update_static_files():
    run('python3 manage.py collectstatic --noinput', warn_only=True)

def _update_database():
    run('python3 manage.py migrate --noinput', warn_only=True)

def _restart_server(uwsgi_filename):
    run('sudo pkill -f uwsgi -9', warn_only=True)
    run('uwsgi --ini %s' % (uwsgi_filename, ), warn_only=True)


def _deploy(environment):
    branch = local("git rev-parse --abbrev-ref HEAD", capture=True)
    commit = local("git log -n 1 --format=%H", capture=True)
    uwsgi = 'uwsgi_dev.ini' if environment == 'dev' else 'uwsgi.ini'
    if environment == 'prod' and branch == 'master':
        print('Production only support master.')
        exit(-1)

    print('Deploy: ', branch, commit)
    with cd(project_dir):
        with prefix('workon bongbong'), hide('stdout'):
            _get_latest_source(branch, commit)
            _install_packages()
            _update_static_files()
            _update_database()
            _restart_server(uwsgi)


def dev():
    env.hosts = HOSTS_MAP['dev']
    execute(_deploy, 'dev')


def prod():
    env.hosts = HOSTS_MAP['prod']
    execute(_deploy, 'prod')
