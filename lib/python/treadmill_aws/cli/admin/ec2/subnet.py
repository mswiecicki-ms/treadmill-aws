"""Implementation of treadmill admin EC2 subnet.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import click

from treadmill import cli

import treadmill_aws
from treadmill_aws import awscontext
from treadmill_aws import ec2client


def init():

    """EC2 subnet CLI group"""
    formatter = cli.make_formatter('ec2_subnet')

    @click.group()
    def subnet():
        """Manage subnet configuration"""
        pass

    @subnet.command(name='list')
    @cli.admin.ON_EXCEPTIONS
    def _list():
        """List subnets"""
        ec2_conn = awscontext.GLOBAL.ec2
        subnets = ec2client.list_subnets(ec2_conn)
        cli.out(formatter(subnets))

    @subnet.command()
    @click.argument('subnet_id')
    @cli.admin.ON_EXCEPTIONS
    @treadmill_aws.cli.admin.ec2.ON_EC2_EXCEPTIONS
    def configure(subnet_id):
        """Configure subnet"""
        ec2_conn = awscontext.GLOBAL.ec2
        subnet = ec2client.get_subnet_by_id(ec2_conn, subnet_id)
        cli.out(formatter(subnet))

    del _list
    del configure

    return subnet
