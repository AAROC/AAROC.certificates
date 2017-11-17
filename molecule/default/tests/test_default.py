import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    """Basic sanity test on the host."""
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_hosts_package(host):
    """Check that the package is installed."""
    package = host.package('ca-policy-egi-core')
    assert package.is_installed


def test_hosts_grid_security(host):
    """Run tests on installed files."""
    f = host.file('/etc/grid-security')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0755'
