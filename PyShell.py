import argparse

parser = argparse.ArgumentParser(
                    prog='PyShell - Interactive python runner',
                    description='runs a python script an then allows you to interact with the code in a python shell')
parser.add_argument('filename')
args = parser.parse_args()

filename = args.filename

script = ""

with open(filename, 'r') as file:
    script = file.read()

exec(script)

# Interact with the local variables
import code
vars = globals().copy()
vars.update(locals())
code.interact(local=vars)
