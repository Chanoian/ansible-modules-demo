#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from ansible.module_utils.basic import AnsibleModule

MODULES_URL = "https://docs.ansible.com/ansible/2.8/modules/"

DOCUMENTATION = '''
---
module: ansible_modules_countere
short_description: This module will return the number of available modules for specific module type
author:
  - Ara Chanoian
'''

EXAMPLES = '''
- name: Count the number of modules available for cloud
  ansible_modules_counter:
    modules_type: cloud
'''

def main():
    # define the parameters the user needs to pass to the module
    args = dict(
        modules_type=dict(type='str', required=True))
    module = AnsibleModule(argument_spec=args)
    modules_type = module.params['modules_type']
    url = MODULES_URL + 'list_of_{}_modules.html'.format(modules_type)
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        counter = 0
        for ultag in soup.find_all('ul', class_='simple'):
            for litag in ultag.find_all('li'):
                counter+=1
        # remove the note from the count
        counter = counter - 1
        module.exit_json(changed = False, module_counter=counter)
    except Exception as e:
        module.fail_json(msg = "Make Sure The Modules Type {} is Correct !".format(modules_type))


if __name__ == '__main__':
    main()


#  args=dict(
#             name=dict(type='str', required=True),
#             sleep=dict(type='int', required=False),
#             enabled=dict(type='bool', default=True),
#             api_token=dict(type='str', no_log=True),
#             state=dict(type='str', choices=['started', 'stopped', 'reloaded', 'restarted']))