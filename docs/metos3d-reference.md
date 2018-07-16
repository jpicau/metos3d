# Metos3D BGC API

Application programming interface (API) for biogeochemical (BGC) models

Definition, realization in *Fortran*

```
metos3dbgcinit(...)
metos3dbgcbegin(...)
metos3dbgc(...)
metos3dbgcend(...)
metos3dbgcfinal(...)
```

## Description

The interface decouples biogeochemical models and driver routines
(ocean circulation, forcing, geometry) programmatically.

It gives the modeler the possibility to provide a free number of tracers,
parameters, boundary and domain conditions. It suits well an
optimization as well as an Automatic Differentiation (AD) context.

The interface changed (more or less) since it was introduced for the first time.
The initial version can be found at \citep[][]{PiwSla16}.

#### C model template

#### Fortran model template

#### Example 1

in the simplest case, assuming you have a model written in Fortran,

File: `simple_bgc_model.f90`

```
subroutine metos3dbgc(ny, nx, nu, nb, nd, ndg, dt, q, t, y, u, b, d, dg, ctx)

    integer :: ny           ! tracer count
    integer :: nx           ! layer count
    integer :: nu           ! parameter count
    integer :: nb           ! boundary condition count
    integer :: nd           ! domain condition count
    integer :: ndg          ! diagnostic variable count
    real(8) :: dt           ! ocean time step
    real(8) :: q(nx, ny)    ! bgc model output
    real(8) :: t            ! point in time
    real(8) :: y(nx, ny)    ! bgc model input
    real(8) :: u(nu)        ! parameters
    real(8) :: b(nb)        ! boundary conditions
    real(8) :: d(nx, nd)    ! domain conditions
    real(8) :: dg(nx, ndg)  ! diagnostic variables
    integer :: ctx          ! unsed variable, place holder for bgc context
    
    ! your code here ...
    
end subroutine
```

#### Example 2

File: `bgctype.h90`

```
type bgcctx
    sequence
    real(8) :: a
    real(8) :: b
    logical(4) :: yesOrNo
    real(8), pointer :: ptr(:)
end type
```

File: `more_sophisticated_bgc_model.f90`

```
subroutine metos3dbgc(ny, nx, nu, nb, nd, ndg, dt, q, t, y, u, b, d, dg, ctx)

#include "bgctype.h90"

    integer         :: ny           ! tracer count
    integer         :: nx           ! layer count
    integer         :: nu           ! parameter count
    integer         :: nb           ! boundary condition count
    integer         :: nd           ! domain condition count
    integer         :: ndg          ! diagnostic variable count
    real(8)         :: dt           ! ocean time step
    real(8)         :: q(nx, ny)    ! bgc model output
    real(8)         :: t            ! point in time
    real(8)         :: y(nx, ny)    ! bgc model input
    real(8)         :: u(nu)        ! parameters
    real(8)         :: b(nb)        ! boundary conditions
    real(8)         :: d(nx, nd)    ! domain conditions
    real(8)         :: dg(nx, ndg)  ! diagnostic variables
    type(bgcctx)    :: ctx          ! own bgc context

    ! your code here ...

end subroutine

```

--------------
#### Example 3

Good practice,

- store constants in a *module*,
- store pointers for own memory allocation, (usually not needed at all), in data type
    - use `metos3dbgcinit` to allocate memory
    - use `metos3dbgcfinal` to free memory

was        what
wie        how
warum    why
wofuer    what for

