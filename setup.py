from distutils.core import setup

with open('version.txt', 'r') as f:
  version = f.read()
  version = str(float(version) + 0.01)
with open('version.txt', 'w') as f:
  f.write(version)

setup(
  name = 'ssh2',
  scripts = ['ssh2'],
  version = version,
  description = 'Simplifying EC2 ssh\'ing',
  long_description = open('README.rst', 'rt').read(),
  url = 'https://github.com/alex-kaufman/ssh2',
  keywords = ['ssh', 'ec2', 'aws'],
  classifiers = [],
)
