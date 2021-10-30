Ansible Custom Module Demo

# Ansible Modules Counter
- This Module will return the number of Predefined modules for specific module type
- currently there are few module types [List Of Modules](https://docs.ansible.com/ansible/2.8/modules/modules_by_category.html)
- You need to pass the module type to this module let's say **cloud**
- Then this module will scrape the html page and count the number of the modules
- You will get an integer number which shows how many module exists there


```yaml
name: Ansible All Modules Counter
        ansible_modules_counter: 
          modules_type: cloud
        register: monitoring_module_return
```