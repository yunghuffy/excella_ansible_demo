import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_dnsmasq_package(host):
    exc_dnsmasq_package = host.package('dnsmasq')

    assert exc_dnsmasq_package.is_installed
    assert exc_dnsmasq_package.version.startswith("2.76")
