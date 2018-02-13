#!/bin/bash

set -x #-e

echo "*** PREFIX"
echo ${PREFIX}

echo "*** pwd"
echo `pwd`

echo "*** PYTHON"
echo $PYTHON

cp metos3d ${PREFIX}/bin/.
