#
# Metos3D: A Marine Ecosystem Toolkit for Optimization and Simulation in 3-D
# Copyright (C) 2018  Jaroslaw Piwonski, CAU, jpi@informatik.uni-kiel.de
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import click
import yaml

# metos3d context object
class Metos3D():
    pass

# metos3d
@click.group()
@click.option("-v", "--verbose", is_flag=True, help="Show invoked shell commands and their output.")
@click.version_option("0.0.1")
@click.pass_context
def metos3d(ctx, verbose):
    '''
        Metos3D: A Marine Ecosystem Toolkit for Optimization and Simulation in 3-D
        
        \b
        Sources:
            https://github.com/metos3d
            
        Documentation:
            https://metos3d.github.io
        
        \b
        Scientific article:
            [Piwonski and Slawig, 2016]
            https://www.geosci-model-dev.net/9/3729/2016
        '''

    ctx.obj = Metos3D()
    ctx.obj.verbose = verbose
#    print(ctx.obj)

# info
@metos3d.command()
@click.pass_context
def info(ctx):
    '''
        Show Metos3D configuration.
        
        \b
        petsc, PETSc installation, version, list, active, default: 3.7.7
            compilers,
        data, input file path, list, active, default: data/
        model, bgc file path, list, active, default: model/

        Metos3D stores its configuration ?user-wide.

        '''
#        \b
#        Metos3D stores configuration information in ...
#        ``.~/metos3drc``
#        It is a YAML file located in the users home directory.
#        '''
#
#    filepath = os.path.expanduser("~/.metos3drc")
#    if os.path.exists(filepath):
#        if ctx.obj.verbose:
#            click.echo("Reading configuration from file: " + filepath)
#    else:
#        if ctx.obj.verbose:
#            click.echo("Could not find an existing configuration file.")
#            click.echo("Creating one now ...")
#
#    print(filepath)
#    print(os.path.exists(filepath + ".metos3drc"))
#    print(ctx.obj)
    pass

## petsc
#@metos3d.command()
#@click.pass_context
#def petsc(ctx):
#    '''
#        Show PETSc configuration.
#        '''
#    print(ctx.obj)
#    pass
#
## data
#@metos3d.command()
#@click.pass_context
#def data(ctx):
#    '''
#        Show data configuration.
#        '''
#    print(ctx.obj)
#    pass
#
## model
#@metos3d.command()
#@click.pass_context
#def model(ctx):
#    '''
#        Show model configuration.
#        '''
#    print(ctx.obj)
#    pass



