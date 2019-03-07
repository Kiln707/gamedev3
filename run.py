
if __name__ == '__main__':
    import subprocess, os
    cwd = os.path.dirname(os.path.realpath(__file__))
    subprocess.call('python -m pip install -r %s/requirements.txt'%cwd)
