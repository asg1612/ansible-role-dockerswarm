import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('docker_swarm_worker')


def test_docker_swarm_enabled(host):

    assert 'Swarm: active' in host.check_output('docker info')


def test_docker_swarm_status(host):

    assert 'Is Manager: false' in host.check_output('docker info')
