#
# Metos3D: A Marine Ecosystem Toolkit for Optimization and Simulation in 3-D
# Copyright (C) 2017  Jaroslaw Piwonski, CAU, jpi@informatik.uni-kiel.de
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

"""
    Metos3D
    =======
    
    Marine Ecosystem Toolkit for Optimization and Simulation in 3-D
    
    [Piwonski and Slawig, 2016]
    https://www.geosci-model-dev.net/9/3729/2016/
    
    """

#import sys
import argparse
import metos3d as m3d

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    
    choices = ["info", "update"]
    parser.add_argument("command", choices=choices, help="metos3d ")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable output")
    
#    parser.add_argument("command", metavar="command", choices=["info", "update"])
#    parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                        help='an integer for the accumulator')
#    parser.add_argument('--sum', dest='accumulate', action='store_const',
#                        const=sum, default=max,
#                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args)
    print(args.command)
#    print(args.accumulate(args.integers))

    # dispatch
    m3d.dispatch_command(args)




