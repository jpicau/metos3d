# Custom install

cc, c++, f90

mpicc, mpic++, mpif90

blas, lapack,

yaml,

hdf5,


*macOS:*

```
curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
```

macOS, Linux, Windows:

Optimization / Simulation:

Before usage, Metos3D compiles the transport driver and the bgc model.
We support the C, C++ and the Fortran programming language.
Thus, we need compilers for those languages.

The easy install is based on the gnu compilers, i.e., gcc, g++ and gfortran.
However, there are many other compilers that you may wish to use.

Portland, Intel, IBM, ...

Moreover, Metos3D is a high-performance software that runs in parallel.
distributed computing model, Message Passing Interface (MPI),

the easy install uses ... mpich???, openmpi??? 

Thus, we need the MPI variants of those compiler. 
here as well, we have many possibilities.

openmpi, mpich, intelmpi, ibm / bullxmpi, ...

module concept,
many clusters maintain software using modules, 

environment variables, all three languages are needed,
parallel is preferred, if both are provided, parallel is used, 

sequential, 

```
export M3D_CC=''
export M3D_CXX=''
export M3D_FC=''
```

parallel,

```
export M3D_MPICC=''
export M3D_MPICXX=''
export M3D_MPIFC=''
```

example:

DKRZ, intel compilers, intel mpi, modules,

```
module load intel/18.0.2            # icc, icpc, ifort
module load intelmpi/2018.1.163     # mpiicc, mpiicpc, mpiifort

export M3D_MPICC='mpiicc -cc=icc'
export M3D_MPICXX='mpiicpc -cxx=icpc'
export M3D_MPIFC='mpiifort -fc=ifort'
```


