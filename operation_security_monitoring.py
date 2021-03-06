#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Operation Security Monitoring Console Script.

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

import sys

import click


__author__ = "Sandro Fasser"
__email__ = "sfasser@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


@click.command()
def main(*args, **kwargs):
    """operation_security_monitoring Console Script."""
    click.echo("Replace this message by putting your code into "
               "operation_security_monitoring.py")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())


print("This line will be printed.")