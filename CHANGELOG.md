```
metos3d, version

1. __init__
__version__     = "1.0.0"

2. tag
git tag -a -m '1.0.0' 1.0.0

3. commit
git ci -am '1.0.0' 

4. push
git push --follow-tags

5. sdist
python setup.py sdist

6. twine
twine upload dist/*
```


- [cheat sheet](https://jpicau.github.io/metos3d/metos3d-cheat-sheet.html).
- [BGC API reference](https://jpicau.github.io/metos3d/metos3d-reference.html).
- [tutorial](https://jpicau.github.io/metos3d/metos3d-tutorial.html).

The toolkit suits the biochemocal modelling and fits into an optimization, optimal control as well as automatic differentiation context.

The aim was to develop a 
comprehensive, state-of-the-art, high-performance software,
with a specific focus on parameter estimates for marine ecosystem models.

fits into an optimization, optimal control and automatic differentiation context, respectively.

The [Metos3D BGC API](https://jpicau.github.io/metos3d/metos3d-reference.html) is a convention how biogeochemical models can be coupled to ocean circulation.

the rest is built around the API


with regard to the number of components and parameterization.


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



