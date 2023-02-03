You must first install ansible on a Linux host. The install below was setup on Ubuntu 18.04.
Windows Subsystem Linux can also run the playbook applications.

# set env
# set venv in F5 folder
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# verify ansible is install
ansible --version

# install ansible collection
ansible-galaxy -r install ansible/collections/requirements.yml

# Playbooks dependancies
  1. Use the desired/current hostname for the inventory that is stored in an inventory file call "inv.yml".
  2. Use an use the vault file to encryt your credentials. ENV variable can be used as well. NOTE the vault.yml in repo serve as an exmaple real credential should not be stored in git as a best practice.
  3. Change all test variable value for the values you need. Variable are located in the group_vars and host_vars folder.

# testing
ansible-playbook --syntax-check f5_onboard.yml
ansible-playbook --syntax-check deploy_virtual_server.yml
ansible-playbook --syntax-check ltm_info.yml


# How to run playbooks
ansible-playbook f5onboard.yml
ansible-playbook deploy_virtual_server.yml
ansible-playbook ltm_info.yml

# This project was to create config f5 device using ansible and IAC practices while also showing the value of network automation.


### TODO
    ## Create F5 custom collection
    ## add topology
    ## create readme for each role
    ## add validation check for vip deployment
    ## configure second lb
    ## make f5 HA pair
    ## add scheme validation