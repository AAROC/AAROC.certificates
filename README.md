[![Build Status](https://travis-ci.org/AAROC/AAROC.certificates.svg?branch=master)](https://travis-ci.org/AAROC/AAROC.certificates) [![DOI](https://zenodo.org/badge/70912062.svg)](https://zenodo.org/badge/latestdoi/70912062)


# AAROC.certificates


A role to contextualise the security and trust anchors for hosts in AAROC inventories. This is an evolution of the previous `certificates` role in @AAROC/DevOps/Ansible/roles , but created with Ansible Galaxy so as to promote re-use.

This role is to be used on AAROC sites wishing to ensure that the certificate roll is up to date. 


## CRLs 

CRLs are _not_ tested in this role, but in [AAROC.UMD-role](https://github.com/AAROC/UMD-role).
The reasoning is described in #1.




## IGTF and EGI Trust Anchor

This role will install the necessary files for the host to trust others in the EGI and IGTF circle. 
Files installed are the public keys of the certificate authorities which make up these PMA's. 
For more information, see [IGTF](http://igtf.net) and [EGI](http://repository.egi.eu/sw/production/cas/1/current/) websites.


## Releases

We follow the IGTF release cycle - versions follow the form `v <major>.<patch>.<IGTF-release>`
When new tickets are opened for the IGTF release, we create a branch for the version and check it.

The only file which should change across versions, in a stable state, is `defaults/main.yml`, where `igtf_release_version` is set.

Requirements
------------

Requires escalation priveliges on the managed hosts, since it will install packages.

Role Variables
--------------

  - `needs_cert` : does this host need a host certificate ? (truthy)
  - `igtf_release_version`: the IGTF release version


Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role:AAROC.certificates, become: true, needs_cert: false }

License
-------

Apache-2.0

Author Information
------------------

Bruce Becker CSIR Meraka Institute @brucellino

## Citing

Cite as : 

Bruce Becker. (2017, November 17). AAROC/AAROC.certificates: IGTF and EGI release 1.87-1 (Version v1.0.87-1). Zenodo. http://doi.org/10.5281/zenodo.1052867