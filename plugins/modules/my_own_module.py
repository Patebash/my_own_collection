#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file on remote host

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This module creates a file on a remote host wich given content.

options:
    path:
        description: Path to file on remote host.
        required: true
        type: str
    content:
        description:
            - Content to write into the file.
        required: true
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Alexander Patylitsin (@Patebash)
'''

EXAMPLES = r'''
- name: Create file
  patebash.my_own_collection.my_own_module:
    path: /tmp/hello.txt
    content: "Hello world"
'''

RETURN = r'''
changed:
    description: Whether file was changed
    type: bool
    returned: always
path:
    description: File path
    type: str
    returned: always
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        path='',
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path

    # читаем существующий файл (если есть)
    existing_content = None

    if os.path.exists(path):
        with open(path, 'r') as f:
            existing_content = f.read()

    # идемпотентность: если содержимое одинаковое — ничего не делаем
    if existing_content == content:
        module.exit_json(**result)

    result['changed'] = True

    # check_mode: не пишем файл
    if module.check_mode:
        module.exit_json(**result)

    # создаём/перезаписываем файл
    try:
        with open(path, 'w') as f:
            f.write(content)

    except Exception as e:
        module.fail_json(msg=str(e), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
