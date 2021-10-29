#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from ansible.module_utils.basic import AnsibleModule

MODULES_URL = "https://docs.ansible.com/ansible/2.8/modules/"




def main():
    # define the parameters the user needs to pass to the module
    args = dict(
        module_type=dict(type='str', required=True))
    module = AnsibleModule(
        argument_spec=args,
        supports_check_mode=True
    )
    module_type = module.params['module_type']
    url = MODULES_URL + 'list_of_{}_modules.html'.format(module_type)
    try:
        return_req = requests.get(url=url)
        soup = BeautifulSoup(return_req.content, 'html.parser')
        counter = 0
        for ultag in soup.find_all('ul', class_='simple'):
            for litag in ultag.find_all('li'):
                counter+=1
        module.exit_json(changed = True, module_counter=counter)
    except Exception as e:
        module.fail_json(msg = e)


if __name__ == '__main__':
    main()