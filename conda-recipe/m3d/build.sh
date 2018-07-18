#!/bin/bash

set -eu

echo '*** m3d, shell, begin ********************************************************************'

echo $CC
echo $FC

echo '*** m3d, shell, compile, CC'
$CC $CFLAGS -c m3d_c.c

echo '*** m3d, shell, compile, FC'
$FC $FFLAGS -c m3d_f.f90

echo '*** m3d, shell, link, LD'
#$LD $LDFLAGS_LD -o m3d.exe m3d_c.o m3d_f.o
$FC $LDFLAGS -o m3d.exe m3d_c.o m3d_f.o

./m3d.exe

ls $PYTHON
ls m3d.py

echo '*** m3d, shell, python'
$PYTHON m3d.py

echo '*** m3d, shell, copy'
cp m3d.exe $PREFIX/bin/.

echo '*** m3d, shell, end ********************************************************************'


