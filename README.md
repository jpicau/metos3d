# Metos3D

 Marine Ecosystem Toolkit for Optimization and Simulation in 3-D

## About

Metos3D is a software package ...

## Quick start

- What I need: curl, git
- What I get: python, metos3d, fun

### Install conda

More about: Anaconda, Miniconda and Conda

Miniconda installer page: https://conda.io/miniconda.html

[miniconda](https://conda.io/miniconda.html)

https://conda.io/miniconda.html

Download script and run script:

- **Linux:**

```
curl -O ... # download script
bash ...    # run script
```

- **Mac:**

```
curl -O ... # download script
bash ...    # run script
```

- **Windows:**

```
???
```

### install metos3d

```
conda install -c jpicau metos3d
```

### first run

```
$>
python metos3d.py sim init N -v
# initilize simulation with model N
mkdir N ...
cd N ...
ls -s
tree N
...
```

## doc

[Metos3D docs](https://jpicau.github.io/metos3d/)

or

https://metos3d.readthedocs.io/en/latest/

## misc

some advices, good pratices that we try to follow,
- branching model, http://nvie.com/posts/a-successful-git-branching-model/
- semantic versioning, https://semver.org/

what to do to create a new version?
- assuming, the last commit is done, (repository pushed)

```
git tag -a ... -m ...
git push --follow-tags

edit: cli.py
    @click.version_option("0.0.1")
edit: setup.py
    version       = "0.0.1",

python setup.py sdist
twine upload dist/metos3d-...-0.0.1...

```

## Thanks

### scientific

tmm, samar khatiwala
bgc, iris kriest

hamocc, malte heinemann, jochen segschneider

### programming

joscha reimer, python, conda, etc...

copied from others work,
mkdocs, twine,

sphinx,

click, yaml,





