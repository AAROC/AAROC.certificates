[![Build Status](https://travis-ci.org/AAROC/AAROC.certificates.svg?branch=master)](https://travis-ci.org/AAROC/AAROC.certificates)

AAROC.certificates
=========

A role to contextualise the security and trust anchors for hosts in AAROC inventories. This is an evolution of the previous `certificates` role in @AAROC/DevOps/Ansible/roles , but created with Ansible Galaxy so as to promote re-use.


Requirements
------------

Requires escalation priveliges on the managed hosts, since it will install packages.

Role Variables
--------------

None yet.

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role:AAROC.certificates, become: true }

License
-------

Apache-2.0

Author Information
------------------

Bruce Becker CSIR Meraka Institute @brucellino
