# Metos3D

 Marine Ecosystem Toolkit for Optimization and Simulation in 3-D

## About Metos3D

### What is Metos3D?

Metos3D is a collection of

- [simulation](https://github.com/metos3d/simpack/) and [optimization](https://github.com/metos3d/optpack/) software
- chemical / biogeochemical / marine ecosystem [models](https://github.com/metos3d/model/)
- transport and forcing [data](https://github.com/metos3d/data/)

that is based on the [transport matrix approach](https://github.com/samarkhatiwala/tmm).

### What is Metos3D for?

Metos3D can be used for

- simulation of
- computation of annual periodic steady-states of
- parameter estimates for

chemical / biogeochemical / marine ecosystem models coupled to global 3-D ocean circulation.

See: [[Piwonski and Slawig, 2016]](https://www.geosci-model-dev.net/9/3729/2016/)

### Why was Metos3D developed?

In the field of climate research and ocean simulation, marine ecosystem models still entail the most uncertainties.
Therefore

- an application programming interface for biogeochemical models [BGC API](https://github.com/jpicau/metos3d/blob/master/docs/metos3d-reference.html) was designed and
- a comprehensive, state-of-the-art, high-performance software based on [PETSc](https://www.mcs.anl.gov/petsc/index.html) was built around it.

See: [[Piwonski and Slawig, 2016]](https://www.geosci-model-dev.net/9/3729/2016/)

### How do I use Metos3D?

Have a look into the

- [Metos3D cheat sheet](https://github.com/jpicau/metos3d/blob/master/docs/metos3d-cheat-sheet.md).
- [Metos3D BGC API reference](https://github.com/jpicau/metos3d/blob/master/docs/metos3d-bgc-api-reference.md).
- [Metos3D tutorial](https://github.com/jpicau/metos3d/blob/master/docs/metos3d-tutorial.md).

## Reference

[Piwonski and Slawig, 2016]  
[Metos3D: the Marine Ecosystem Toolkit for Optimization and Simulation in 3-D – Part 1: Simulation Package v0.3.2](https://www.geosci-model-dev.net/9/3729/2016/)

## Install Metos3D

Install the [Miniconda/Python3](https://conda.io/miniconda.html) distribution:

```
# Assume a 64-bit Linux operating system ...
curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Install Python bindings for HDF5 ([h5py](https://www.h5py.org/)) and YAML ([pyyaml](https://pyyaml.org/)):

```
conda install h5py
conda install pyyaml
```

Install Metos3D from the `jpicau` Anaconda channel:

```
conda install -c jpicau metos3d
```

Initialize Metos3D:

```
metos3d init
```


