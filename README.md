Ansible Custom Module Demo

# Ansible Modules Counter
- this Module will return the number of Predefined modules in Ansible Core for specific module type.
- currently there are few module types [List Of Modules](https://docs.ansible.com/ansible/2.8/modules/modules_by_category.html)
- pass the module type to this module for example **cloud**.
- this module will scrape the html page and count the number of the modules.
- the return will be an integer number which shows how many module exists there for the specific type.
- pass **all** then you will get all the modules return.


```yaml
name: Ansible All Modules Counter
        ansible_modules_counter: 
          modules_type: cloud
        register: monitoring_module_return

      - name: Print Out Module Return
        debug:
          msg: "{{monitoring_module_return}}"
```