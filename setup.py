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

import metos3d

from setuptools import setup

setup(name          = __title__,
      version       = __version__,
      description   = __summary__,
      url           = __uri__,
      author        = __author__,
      author_email  = __email__,
      license       = __license__,
      packages      = ["metos3d"],
      entry_points  = {
        "console_scripts": ["metos3d=metos3d.cli:metos3d"],
      },
      install_requires=["click", "pyyaml"],
      zip_safe      = False)


