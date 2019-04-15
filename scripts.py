import subprocess as subp


def doc():
    subp.run([
        'pdoc', '--html', '--overwrite',
        '--html-dir', 'docs', 'lcu_connectorpy'
    ])
