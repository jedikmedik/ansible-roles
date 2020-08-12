import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_check_host_name(host):
    assert host.ansible.get_variables()["inventory_hostname"] == \
           host.run('hostname').stdout.rstrip()


@pytest.mark.parametrize("name", [
    ("nginx"),
    ("goaccess"),
    ("certbot"),
])
def test_pkg_instaleed(host, name):
    pkg = host.package(name)

    assert pkg.is_installed


# @pytest.mark.parametrize("name", "version", [
#    ("python2-pyOpenSSL", "16.2.0-4.el7"),
# ])
# def test_check_pkg_custom_version(host, name, version):
#    pkg = host.package(name)
#
#    assert pkg.is_installed
#    assert pkg.version == version


@pytest.mark.parametrize("name", [
    ("nginx"),
])
def test_service_started(host, name):
    svc = host.service(name)

    assert svc.is_running
    assert svc.is_enabled
