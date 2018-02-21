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

from setuptools import setup

setup(name          = "metos3d",
      version       = "0.0.1-3",
      description   = "A Marine Ecosystem Toolkit for Optimization and Simulation in 3-D",
      url           = "https://metos3d.github.io/",
      author        = "Jaroslaw Piwonski (CAU)",
      author_email  = "jpi@informatik.uni-kiel.de",
      license       = "GPL 3.0",
      packages      = ["metos3d"],
      entry_points  = {
        "console_scripts": ["metos3d=metos3d.cli:metos3d"],
      },
      install_requires=["click", "pyyaml"],
      zip_safe      = False)


