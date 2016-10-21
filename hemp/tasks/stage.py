from fabric.api import task, env

from hemp.internal.utils import print_err, print_info


@task(name='on')
def on(env_name=None):
    print_info('Loading settings for {0}'.format(env_name))
    if env_name is None:
        print_err('Please, provide environment name, like, on:staging')
    if not env.hemp:
        print_err('No hemp entry in environment')
    if not env.hemp['environments']:
        print_err('No hemp environments defined')
    if env_name not in env.hemp['environments']:
        print_err('Environment not defined: {0}'.format(env_name))
    environment = env.hemp['environments'][env_name]
    if 'roles' not in environment:
        print_err('Roles are not defined for this environment')

    env.environment = env_name

    if 'env' in environment:
        for key, value in environment['env'].items():
            print_info('[ENV] {0}: {1}'.format(key, value))
            setattr(env, key, value)

    all_hosts = []

    for role, hosts in environment['roles'].items():
        all_hosts += hosts
        if role not in env.roledefs:
            env.roledefs[role] = hosts
        else:
            env.roledefs[role] = list(set(env.roledefs[role] + hosts))

    all_hosts = list(set(all_hosts))
    env.hosts = list(set(all_hosts + env.hosts))

    print_info('[ENV] hosts: {0}'.format(env.hosts))
    print_info('[ENV] roles: {0}'.format(env.roledefs))
    print_info('Loaded env, hosts and roles for {0}'.format(env_name))


@task
def staging():
    on('staging')


@task
def production():
    on('production')


@task
def development():
    on('development')
