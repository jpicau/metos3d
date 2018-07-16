# Metos3D cheat sheet


`metos3d info`
`~/.metos3drc`

`version`
`data`
`model`
`petsc`



```
4.
$> metos3d
usage: metos3d [command] ...
metos3d
    --help, -h
    --verbose, -v
    info            # print version, config file, docs, etc ...
    simulate        # compile sources, perform a simulation, ...

    update          # not needed, handled externally, pip, conda
    optimize        # save for later

$>
metos3d info
metos3d update
metos3d simulate HAMMOC-mitgcm-128x64x15-3h.yaml

metos3d simulate N-DOP-mitgcm-360x160x23-
metos3d simulate HAMMOC-mpiom-default-mitgcm-128x64x15-3h.yaml
metos3d simulate HAMMOC-ballasting-0.3-mitgcm-128x64x15-3h.yaml
mpirun -n 128 metos3d simulate HAMMOC-mitgcm-128x64x15-3h.yaml

3.
metos3d
    init
    data
    model
    simulation      (sim)
    optimization    (opt)
    info
    update

2.
metos3d                (m3d)
    init
    data
    model
    experiment    (exp)

1.
metos3d
    info
    update
    
    data
    petsc

    run
    model
    compile
    bgc
    tmm
    matrix
```


## update


## info


## usage

```
$> python metos3d.py
```

will print the short usage description

## help

print help texts for each argument

```
$> python metos3d.py -h
```
