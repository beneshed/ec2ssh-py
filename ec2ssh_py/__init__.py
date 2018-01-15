import os
import configparser

DEFAULTCONFIG = configparser.ConfigParser()
DEFAULTCONFIG['DEFAULT'] = {
    'profile': ['default'],
    'regions': ['us-east-1'],
    'filters': [],
    'anti_filters': []
}

DEFAULTCONFIG['SSH'] = {
    'template': """
    Host {{ tags.Name }}.{{availablity_zone}}
        HostName {{dns_name || private_ip_address }}
    """
}

class Ec2Ssh(object):
    def __init__():
        pass

    def init(self):
        with open(os.path.expanduser('~/.ec2ssh'), 'w') as sshfile:
            DEFAULTCONFIG.write(sshfile)