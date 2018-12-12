import subprocess

PYTHON_VERSION = (3,6,5)

def editor(arg):
    with TemporaryFile() as tempfile:
        Path(str(tempfile)).write_text(arg)
        subprocess.run('sensible-editor', tempfile)
        return Path(str(tempfile)).read_text()
