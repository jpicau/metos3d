# SimDSL example

```java
class MyClass {
	System.out.println("Hello!");
}
```


```yaml
# # # # # # # # # # # # # # # # # #
# SimDSL application config file  #
# # # # # # # # # # # # # # # # # #
#
#
# How to use:
# 1.  Copy file as sim-dsl.yaml or any other new file name and write your configuration in the file.
# 2.  For use a default value, you have to comment the line out with #.
# 3.  You can write an input string in quotation marks or without. Without quotation marks
#     you have to write the string in one line. If the string is over more lines, you have to write it
#     in quoatation marks.If you write special signs that can't be parse, you have to write the string
#     in quotation marks, too, and write for the special signs unicode. For example the unicode
#     for '\' is \u005c. You can find an unicode table under https://unicode-table.com/de/.
# 4.  If the input type is bool, you can write 'true' or 'false' as value.
# 5.  If behind or under an input type is a list with values it means, that only that values can be
#     used for the parameter. If something is in parentheses, it is explanations of the values, not a value.
# 6.  If the input type is a string, you can put a variable value from the prepare_job_mpiom_hamocc file
#     with ${variable-name} in the sim-dsl parameter. Example: Number of nodes: ${node}
# 7.  If an input type is int and string: ${ncpu} or string: ${node}, it means, that you can input an int or
#     ${ncpu} or rather ${node}, that stands for the value ncpu / node from the prepare_job_mpiom_hamocc file.
# 8.  If the default value is -, it means, that there isn't a default value.
# 9.  Self-explanatory parameters are not explained.
# 10. For generating the prepare-file for the MPIOM model, execute, in the same directory in that the
#     configuration file is, in the console ./sim-dsl-processor. If your file isn't named sim-dsl.yaml,
#     you can choose with the parameter -y another input file. Automatically you get the output file
#     sim-dsl-output. You can choose another output file with the paramater -o.
#     Examples: ./sim-dsl-processor for input file sim-dsl.yaml und -o for output file sim-dsl-output
#               It is	equivalent to ./sim-dsl-processor -y sim-dsl.yaml -o sim-dsl-output
#               ./sim-dsl-processor -y example-input.yl -o example-output.sh for input file
#               example-input.yl and output file example-output.sh
#
#
# SimDSL settings
#
#
# 1. Experiment
# ===============

## Name and description of the experiment.
Experiment:
   # Input type: string
   Name: example1 # default value: toyl10
   # Input type: string
   Description: Testing MPIOM setup. # default value: ""

# 2. Grid
# =========

## Grid of the experiment.
Grid:
    # There are five commonly used combinations for resolution and level. Instead of entering
    # the two individual values of Resolution and Level, the name can be entered to select
    # a combination. If you write an value in Name, there must be no value in Resolution
    # and in Level, otherwise an error message is put out.
    # Input type: string
    # 1. TOYL10 (Resolution: TOY, Level: L10)
    # 2. GR30L40 (Resolution: GR30, Level: L40)
    # 3. GR15L40 (Resolution: GR15, Level: L40)
    # 4. TPO4L40 (Resoltuion: TPO4, Level: L40)
    # 5. TP6ML80 (Resolution: TP6M, Level: L80)
    Name: # default value: ""
    # Input type: string
    Resolution: GR30 # default value: TOY
    # Altitude level.
    # Input type: string
    Level: L40 # default value: L10
    # Horizontal x-dimension.
    # Input type: int
    Horizontal x: # default value: -
    # Horizontal y-dimension.
    # Input type: int
    Horizontal y: # default value: -
    # Vertical z-dimension.
    # Input type: int
    Vertical z: # default value: -
    # Input type: string
    # 1. tripolar: Benefit of tripolar grid.
    # 2. bipolar: Benefits of bipolar grid.
    Boundaries: # default value: -
    # Input type: string
    # 1. intern: Calculate the grid distances and the Coriolis parameters.
    # 2. extern: Read the grid distances and Coriolos parameters from the external file arcgri.nc.
    Distances and corioles parameter: intern # default value: extern
    # Description for the grid.
    Description: This example has a resolution GR30 and a level L40. # default value: ""

# 3. Directories
# ================

## Paths and folders for the experiment.
Directories:
    # Path to the working directory.
    # Input type: string
    Working: /mywork/mylogname # default value: $WORK/$LOGNAME
    # Folder for projects. The folder is created as a subfolder in the working directory.
    # Input type: string
    Projects: example-experiments # default value: experiments
    # Absolute path to the directory where the current experiment is located.
    # Input type: string
    Experiment: /mywork/mylogname/example-experiments/example1 # default value: ${WORKDIR}/${SUBDIR}/${EXPNO}
    # Absolute path to the directory where much free space is available.
    # Input type: string
    Plenty of spaces: /mywork/mylogname/example-experiments/example1 # default value: ${WORKDIR}/${SUBDIR}/${EXPNO}
    # Path to the model binary files.
    # Input type: string
    Binary: /mywork/mpiesm/mpiesm-1.2.00p4/src/mpiom/bin # default value: ""
    # Path to the binaries of module cdo.
    # Input type: string
    Binary cdo: /myhome/mymodules/cdo-1.7.0-magicsxx-gcc48/bin/cdo # default value: ""
    # Path to the directory containing the information output by the model.
    # Input type: string
    Information: /myhome/experiment_info # default value: "${HOME}/experiment_info"
    # Path to the initial data.
    # Input type: string
    Initial data: /myhome/data/MPIOM/input/r0004 # default value: "/pool/data/MPIOM/input/r0004"
    # Path to the forcing data.
    # Input type: string
    Forcing data: /myhome/data/MPIOM/input/r0004/SOURCE/forcing365/original_data # default value: ${INITIAL_DATA}/SOURCE/forcing365/original_data
    # Path to the task geometry.
    # Input type: string
    Task geometry: /mywork/mpiesm/mpiesm-1.2.00p4/src/mpiom/contrib/aix # default value: ""
    # Description of the paths and folders for the experiment.
    # Input type: string
    Description: My examlpe path and folders are on myhome and mywork. # default value: ""

# 4. Files
# ==========

## Files for the experiment.
Files:
    # Give the output file a file name.
    # Input type: string
    Output: example1.out # default value: "${jobname}.out"
    # Give the error file a file name.
    # Input type: string
    Error: example1.err # default value: "${jobname}.err"
    # Name of the binary file of the model.
    # Input type: string
    Binary: mympiom.x # default value: "mpiom.x"
    # Input type: string
    Task geometry: mygeometry.pl # default value: "geometry.pl"
    # Description of the files for the experiment.
    # Input type: string
    Description: My files for the experiment wird output file name and error file name. # default value: ""

# 5. Information
# ================

## Information from the experiment.
Information:
    # Enables outputting information from the model.
    # Input type: bool
    Enable information output: true # default value: false
    # Enter an information text about the model. Since there are no formatting options
    # within the text, it should be kept short.
    # Input type: string
    Short information: not_avaible # default value: ""
    # Input type: string
    # The description of the information from the experiment.
    Description: My informations for example1. # default value: ""

# 6. Hamocc
# ===========

## Details of the submodel HAMOCC.
Hamocc:
    # Activates the HAMOCC submodel.
    # Input type: bool
    Enable hamocc: true # default value: true
    # Adds the cyanobacteria.
    # Input type: bool
    Enable cyano: true # default value: false
    # Activate the martin curve.
    # Input type: bool
    Enable martin: false # default value: false
    # Loads greenhouse gas data from the provided file.
    # Input type: bool
    Enable ghg file: false # default value: false
    # Activates the passive tracer chlorofluorocarbon.
    # Input type: bool
    Enable cfc: false # default value: false
    # Activates the passive tracer age.
    # Input type: bool
    Enable age: false # default value: false
    # Activates the passive tracer decay.
    # Input type: bool
    Enable decay: false # default value: false
    # Activates the passive tracer cesium-137.
    # Input type: bool
    Enable cs137: false # default value: false
    # The description of the details of the submodel HAMOCC.
    # Input type: bool
    Description: With cyanobacteria. # default value: false

# 7. Forcing
# ============

## Details about the forcing.
Forcing:
    # Selection of the forcing data set.
    # Input type: string
    # 1. OMIP
    # 2. NCEP24
    # 3. NCEP6
    # 4. NOAA
    # 5. ERA
    # 6. ERAINT
    Data Set: OMIP
    # Date from which the forcing is started.
    # Input type: string in form YYYY-MM-DD. No date allowed before 0000-01-01.
    Start: 0000-01-01 # default value: for OMIP: 0000-01-01
    #                                      NCEP24: 1948-01-01
    #                                      NCEP6: 1948-01-01
    #                                      NOAA: 1872-01-01
    #                                      ERA: 1958-01-01
    #                                      ERAINT: 1980-01-01
    # Distance between two next times in the forcing.
    # Input type: int. Value is always positive.
    Frequency: 86400 # default value: for OMIP: 86400
    #                                     NCEP24: 86400
    #                                     NCEP6: 21600
    #                                     NOAA: 21600
    #                                     ERA: 21600
    #                                     ERAINT: 21600
    # The available years from the forcing in the data set.
    # Input type: int. Value is always negative.
    Periodicity: -999 # default value: for OMIP: -999
    #                                      NCEP24: -1
    #                                      NCEP6: -1
    #                                      NOAA: -1
    #                                      ERA: -1
    #                                      ERAINT: -1
    # Sets the internal calendar. One calendar year has 365 fixed days,
    # one calendar year has 360 fixed days, or the Gregorian calendar
    # with leap years is used.
    # Input type: string.
    # 1. 360
    # 2. 365
    # 3. gregorian
    Calender: 365 # default value: for OMIP: 365
    #                                  NCEP24: gregorian
    #                                  NCEP6: gregorian
    #                                  NOAA: gregorian
    #                                  ERA: gregorian
    #                                  ERAINT: gregorian
    # Start date of the simulation.
    # Input type: string in form YYYY-MM-DD. No date allowed before 0000-01-01.
    Model start: 0001-01-01 # default value: for OMIP: 0000-01-01
    #                                            NCEP24: 1948-01-01
    #                                            NCEP6: 1948-01-01
    #                                            NOAA: 1872-01-01
    #                                            ERA: 1958-01-01
    #                                            ERAINT: 1980-01-01
    # End date of the simulation.
    # Input type: string in form YYYY-MM-DD. No date allowed before 0000-01-01.
    # The date must be greater than or equal to the date of 'Model start'.
    Model end: 9999-01-01 # default value: for OMIP: 0100-01-01
    #                                          NCEP24: 2010-12-31
    #                                          NCEP6: 2012-12-31
    #                                          NOAA: 2007-12-31
    #                                          ERA: 2000-12-31
    #                                          ERAINT: 2012-12-31
    # Input type: string
    # 1. model: Use of the model timeline to account for leap years.
    # 2. forcing: Use of te forcing time axis.
    Time axis: model # default value: model
    # Input type: bool
    Enable rewind files to initial point at turn of the year: true # default value: false,
    #                                                                for Data Set OMIP: true
    # Input type: bool
    Enable write interpolated forcing fields: false # default value: false
    # Enables bilinear horizontal interpolation of forcing input fields.
    # Input type: bool
    Enable spatial interpolation: true # default value: true
    # Enables linear interpolation of forcing fields.
    # Input type: bool
    Enable linear time interpolation: false # default value: false
    # Activates a different original grid for outflow data, for example,
    # if the outflow of different climatologies is taken.
    # Input type: bool
    Enable OMIP runoff data: false # default value: for Data Set OMIP: false
    #                                                            NCEP24: true
    #                                                            NCEP6: true
    #                                                            NOAA: true
    #                                                            ERA: true
    #                                                            ERAINT: true
    # Enables the debug mode for the forcing.
    # Input type: bool
    Enable debugging: false # default value: false
    # Enable the Climate Data Interface (CDI) library for I / O.
    # Input type: bool
    Enable Climate Data Interface: true # default value: true
    # Activates active tide forcing. It calculates the gravitational potential
    # of the sun and moon.
    # Input type: bool
    Enable active tidal: # default value: -
    # Activate the buoyancy forcing.
    # Input type: bool
    Enable buoyancy: # default value: -
    # Activates the wind pressure forcing.
    # Input type: bool
    Enable windstress: # default value: -
    # The description of the details about the forcing.
    # Input type: string
    Description: Calender is over 365 days. # default value: ""

# 8. Environment settings
# =========================

## The settings for the execution environment.
Environment settings:
    ## The general settings for the execution environment,
    ## regardless of the parallelization method used.
    General:
        # The selection of the shell. For example, 'ksh' (Korn shell) or 'sh' (Bourne shell).
        # Input type: string
        Shell: ksh # default value: ""
        # The path to the folder where the modules are installed.
        # Input type: string
        Modules path: /mymodulehome/init/ksh\ # default value: ""
        # Enables the loading of the listed modules.
        # Input type: Array: string (as list)
        Modules: # default value: []
          - cdo/1.7.0-magicsxx-gcc48
        # The path to the mkdir program to create new folders.
        # Input type: string
        Mkdir path: /mybin/mkdir # default value ""
        # The description of the general settings for the execution environment.
        # Input type: string
        Description: Shell selection is ksh. # default value: ""
    ## The computing settings for the experiment.
    Compute:
        # Maximum calculation time of the model.
        # Input type: string: HH:MM:SS
        Job time limit: 00:45:00 # default value: 01:00:00
        # Using the Supporting Queue System.
        # Input type: string
        # 1. TWS (Tivoli Workloader Scheduler - IBM)
        # 2. SGE (Sun Grid Engine)
        # 3. NQS (Network Queuing System - NEC SX)
        # 4. SLURM (Simple Linux Utility for Resource Management)
        Queuing: SLURM # default value: ""
        # Way of adding the job to the queuing system.
        # Input type: string
        Submit: sbatch # default value: ""
        # Enables simultaneous multithreading in the TWS queuing system.
        # Input type: bool
        Enable SMT for TWS: true # default value: true
        # Class for the LoadLeveler in the queue system TWS.
        # Input type: string
        Class for TWS: cluster # default value: cluster
        # The path to the files from the Message Passing Interface (MPI).
        # Input type: string
        MPI path: /myhome/compilers_and_libraries/linux/mpi # default value: ""
        # The path to the binaries from the Message Passing Interface (MPI).
        # Input type: string
        MPI binary: /myhome/compilers_and_libraries/linux/mpi/bin # default value: ${MPIROOT}/bin
        # Description of the computer settings of the model.
        # Input type: string
        Description: Job time limit is 45 minutes. # default value: ""
    ## The settings for the parallelization.
    Parallelisation:
        # Specifies which tasks run together on a node.
        # Input type: bool
        Enable task geometry: false # default value: false
        # Number of tasks.
        # Input type: int, string: ${ncpu}
        Tasks: ${ncpu} # default value: ${ncpu}
        # Number of processors in x-direction.
        # Input type: int
        Direction x: 3 # default value: 2
        # Number of processors in y-direction.
        # Input type: int
        Direction y: 8 # default value: 2
        # Start the calculation taking into account the job type Intel MPI.
        # Input type: bool
        Enable IntelMPI Options: # default value: false
        # Input type: int, string: ${node}
        Number of nodes: ${node} # default value: for Queuing SLURM: ${node}
        #                                         for Queuing NQS: 2
        # Enable sharing of nodes.
        # Input type: bool
        Enable shared nodes: false # default value: false
        # Input type: float
        # Unit: gb (bigabyte)
        Memory per node: 4.0 # default value: 5.0
        # Input type: int, string: ${ncpu}
        Cpus per node: # default value: ${ncpu}
        # Input type: int, string: ${ncpu}
        Cores per node: # default value: ${ncpu}
        # Number of threads.
        # Input type: int
        Threads: 1 # default value: 1
        # Input type: int
        Threads per core: 2 # default value: 2
        # Input type: int
        Cpus per Task: 2 # default value: 2
        # Enables the writing of error data and output data to a file.
        # Input type: bool
        Enable join error and out: # default value: true
        # Requested batch class.
        # Input type: string
        Batch class: # default value: ""
        # Selection of the partitions.
        # Input type: Array: string (as list)
        Partition: # default value: []
         - compute
         - compute2
        # Selection of the project to be loaded.
        # Input type: string
        Account: $GROUP # default value: ""
        # The description of the settings for the parallelization.
        # Input type: string
        Description: My memory per node is 4.0 gb. # default value: ""

# 9. Basic physical model parameter
# ===================================

## Setting options of the basic physical model parameters.
Basic physical model parameter:
    ## The physical model parameters that relate to time.
    Time:
        # Number of simulated years for a single run.
        # Input type: int
        Years per run: 0 # default value: 0
        # Number of simulated months for a single run.
        # Input type: int
        Months per run: 12 # default value: 12
        # Number of simulated days for a single run.
        # Input type: int
        Days per run: 0 # default value: 0
        # Sets the timestep of the model.
        # Input type: int
        Timestep: # default value: -
        # Enables the model's internal timer.
        # Input type: bool
        Enable timer: true # default value: true
        # The description of the time-related physical model parameters.
        # Input type: string
        Description: 12 months for a single run. # default value: ""
    ## Optimization settings for the Message Passing Interface (MPI).
    Optimisation MPI:
        # Use MPI-derived data types instead of basic data types.
        # Input type: bool
        Enable MPI derivated data types: false # default value: false
        # Using non-blocking MPI communication.
        # Input type: bool
        Enable non blocking MPI communication: true # default value: true
        # The description of the optimization settings for the Message Passing Interface (MPI).
        # Input type: string
        Description: Using non-blocking MPI communication. # default value: ""
    ## The initialization methods.
    Initialisation methods:
        # Input type: string
        # 1. Read topography from file anta: Topography is read from the input file anta. The new topography
        # is written to the file topo.
        # 2. Enable ocean start at rest: Enables setting the initial value of the ocean temperature to 0 and
        # setting the initial value of the ocean salinity to 34.8 PSU. The temperature and salinity values can
        # be changed with 'Ocean start at rest temperature' and 'Ocean start at rest salinity'.
        # The start of the ocean takes place in rest position. Topography is read from the input file topo.
        # 3. Enable ocean start temperature and salinity from 3d climatology: Enables extraction of the initial
        # value of ocean temperature and ocean salinity from 3D Climatology. Topography is read from the input
        # file topo.
        # 4. Enable ocean start from restart file: Enables the launch of the ocean from the restart file.
        # Topography is read from the input file topo.
        Ocean start: # default value: -
        # Sets the initial value of the temperature of the ocean. The start of the ocean takes place
        # in rest position.
        # Input type: float
        Ocean start at rest temperature: # default value: -
        # Sets the initial value of the salinity of the ocean. The start of the ocean takes
        # place in rest position.
        # Input type: float
        Ocean start at rest salinity: # default value: -
        # Input type: bool
        Enable write restart file: # default value: -
        # Input type: bool
        Enable write debug output: false # default value: false
        # The description of the initialization methods.
        # Input type: string
        Description: # default value: ""
    ## The settings for the diffusion and for the viscosity.
    Diffusion and viscosity:
        # Input type: float
        Biharmonic horizontal diffusion: 0. # default value: 0.
        # Input type: float
        Biharmonic horizontal viscosity: # default value: -
        # Input type: float
        Harmonic horizontal diffusion: 1000. # default value: 1000.
        # Input type: float
        Harmonic horizontal viscosity: 0. # default value: 0.
        # Input type: string
        # 1. isopycnal: Using the isopycnal diffusion scheme.
        # 2. horizontal: Use the horizontal diffusion scheme.
        Diffusion scheme: # default value: -
        # The description of diffusion and viscosity.
        # Input type: string
        Description: Harmonic horizontal diffusion is 1000. # default value: ""
    ## The setting options for the advection scheme.
    Advection scheme:
        # Input type: string
        # 1. no: No tracer advection.
        # 2. upwind: Using the upwind scheme.
        # 3. central-difference: Use the central difference scheme.
        # 4. adpo: Using the TVD scheme after Sweby, 1984.
        # 5. adpo and slopecon: Using the TVD scheme after Sweby, 1984,
        #    and the Bottom Boundary Layer Transport Scheme.
        # 6. adfs: Using the Predictor Corrector Advection Scheme.
        # 7. quick FS: Using the Quick Scheme after Farrow and Stevens, 1995
        # 8. quick modified boundary: Using the Quick Scheme with modified boundary treatment.
        # 9. adpo with staggered tracer transport: Using the TVD scheme after Sweby, 1984,
        #    but with displace horizontal / vertical tracer transport.
        # Note: Using 'adpo and slopecon' is outdated. Instead, "adpo" should be used
        #    in cominbination with Bbl velocities 'true'.
        # Input type: string
        Tracer: # default value: -
        # 1. no: No tracer advection.
        # 2. upwind: Using the upwind scheme.
        # 3. central-difference: Use the central difference scheme.
        # 4. adpo: Using the TVD scheme after Sweby, 1984.
        # 5. adpo and slopecon: Using the TVD scheme after Sweby, 1984,
        #    and the Bottom Boundary Layer Transport Scheme.
        # 6. adfs: Using the Predictor Corrector Advection Scheme.
        # 7. quick FS: Using the Quick Scheme after Farrow and Stevens, 1995
        # 8. quick modified boundary: Using the Quick Scheme with modified boundary treatment.
        # 9. adpo with staggered tracer transport: Using the TVD scheme after Sweby, 1984,
        #    but with displace horizontal / vertical tracer transport.
        # Note: Using 'adpo and slopecon' is outdated. Instead, "adpo" should be used
        #    in cominbination with Bbl velocities 'true'.
        Momentum: # default value: -
        # Enables calculation of the speed of the lower boundary layer.
        # Input type: bool
        Enable bbl velocities: true # default value: true
        # The description for the advection scheme.
        # Input type: string
        Description: # default value: ""
    ## The setting options for the Successive Over Relaxation (SOR) scheme.
    Successive Over Relaxation:
        # Standard number of iterations.
        # Input type: int
        Iterations: # default value: -
        # User-specific value for the SOR parameter.
        # Input type: float
        Parameter: # default value: -
        # Standard number of iterations for SOR hack. Useful in higher resolution setup
        # to attenuate 2dx noise.
        # Input type: int
        Iterations hack: # default value: -
        # User-specified value for the SOR parameter in the last "iteration hack" steps of SOR.
        # Input type: float
        Parameter hack: # default value: -
        # The description of the Successive Over Relaxation (SOR) scheme.
        # Input type: string
        Description: # default value: ""
    ## The settings for Gent and McWilliams (GM).
    Gent and McWilliams:
        # Input type: string
        # 1. off: Gent and McWilliams (GM) is off.
        # 2. calculation after Visbek: GM parameters are calculated according to Visbek, 1997.
        # 3. scaling with N: GM parameter N is scaled by dx / 400km, for N: N> 0.
        # 4. scaling with Harmonic horizontal diffusion: Using the value of Harmonic horizontal diffusion,
        #    value is scaled with dx / 400km.
        Parameter: # default value: -
        # The description for Gent and McWilliams (GM).
        # Input type: string
        Description: # default value: ""
    ## The settings for nudging.
    Nudging:
        # Input type: bool
        Enable sea surface salinity: # default value: -
        # Input type: bool
        Enable sea surface temperature: # default value: -
        # Input type: bool
        Enable subsurface default region 1 salinity: # default value: -
        # Input type: bool
        Enable subsurface default region 1 temperature: # default value: -
        # Input type: bool
        Enable subsurface default region 2 salinity: # default value: -
        # Input type: bool
        Enable subsurface default region 2 temperature: # default value: -
        # The description for nudging.
        # Input type: string
        Description: # default value: ""
    ## Settings for shortwave radiation (SWR).
    Shortwave radiation:
        # Input type: bool
        Enable Jerlov SWR: true # default value: true
        # Input type: float
        Parameter for attenuation of photosyntheic active radiation: 0.06 # default value: 0.06
        # Input type: float
        Parameter for blue fraction: 0.41 # default value: 0.41
        # Activate the response to shortwave (sw) absorption without the BGC itself running.
        # Input type: bool
        Enable feedback on sw absorbtion without the bgc running itself: false # default value: false
        # The description for the shortwave radiation (SWR) settings.
        # Input type: string
        Description: # default value: ""
    ## The settings for the sea ice dynamics.
    Sea ice:
        # Input type: bool
        Enable sea ice dynamics: # default value: -
        # Input type: string
        Description: # default value: ""

# 10. Reading and writing options
# =================================

## The reading and writing options for the model.
Reading and writing options:
    ## The settings for the convection scheme.
    Convection scheme:
        # Input type: string
        # 1. enhanced: Improved vertical diffusion.
        # 2. complete mixing: complete mixing of upper and lower box.
        # 3. interchange: exchange of upper and lower box.
        # 4. plume: Plume convection to Paluskiewicz and Romea, 1997.
        Vertical tracer: # default value: -
        # The settings for the convection scheme.
        # Input type: string
        Description: # default value: ""
    ## The settings for the Pacanowski and Philander (PP) schema coefficients.
    ## All parameter have unit m^2/s.
    Pacanowski and Philander scheme coefficients:
        # Input type: float
        Vertical viscosity: 0.2e-2 # default value: 0.2e-2
        # Input type: float
        Vertical diffusivity: 0.2e-2 # default value: 0.2e-2
        # Input type: float
        Background for vertical viscosity: 5.e-5 # default value: 5.0e-5
        # Input type: float
        Background for vertical diffusivity: 1.05e-5 # default value: 1.05e-5
        # Input type: float
        Vertical windmixing for tracers: 0.5e-3 # default value: 0.5e-3
        # Input type: float
        Vertical windmixing for momentum: 0.75e-3 # default value: 0.75e-3
        # Input type: float
        Vertical windmixing for stability: 0.03 # default value: 0.03
        # Input type: float
        Enhanced vertical viscosity: 0.0 # default value: 0.0
        # Input type: float
        Enhanced vertical diffusivity: 0.1 # default value: 0.1
        # The description of the settings for the Pacanowski and Philander schema coefficients.
        # Input type: string
        Description: # default value: ""
    ## The parameters for bottom friction.
    Bottom friction parameter:
        # Unit: m^2/s
        # Input type: float
        Linear: # default value: -
        # Input type: float
        Quadratic: # default value: -
        # The description of the parameters for the bottom friction.
        # Input type: string
        Description: # default value: ""
    ## Two lists of reading and writing information.
    Iolists:
        # A list for the iolists written in prepare_job_mpiom_hamocc within lines 1221-1248.
        # Input type: Array: int, bool, string, bool (as list)
        # 1. Number: Number of iolist.
        # 2. Enable new content: If true, the content under Content is taken as the value for the iolist.
        #    If false, if exists, the content is taken from the prepare_job_mpiom_hamocc file.
        # 3. Content: The new content for the iolist.
        # 4. Enable comment: If true, the iolist is commented out, by an exclamation mark is written
        #    in front of the line. If false, the iolist is not commented out.
        First lists: # default value: []
          - Number: 95
            Enable new content: true
            Content: 3, '\${EXPNO}_mpiom_data_3d_ym.nc', 'nc2', 2, 3, 4, 5, 6, 18, 21, 22, 23, 24, 110, 111, 112, 135, 197, 214 \${AGE} \${DECAY} \${CS137}
            Enable comment: false
          - Number: 81
            Enable new content: false
            Content:
            Enable comment: true
          - Number: 80
            Enable new content: false
            Content:
            Enable comment: true
        # A list for the iolists written in prepare_job_mpiom_hamocc within lines 1372-1400.
        # Input type: Array: int, bool, string, bool (as list)
        # 1. Number: Number of iolist.
        # 2. Enable new content: If true, the content under Content is taken as the value for the iolist.
        #    If false, if exists, the content is taken from the prepare_job_mpiom_hamocc file.
        # 3. Content: The new content for the iolist.
        # 4. Enable comment: If true, the iolist is commented out, by an exclamation mark is written
        #    in front of the line. If false, the iolist is not commented out.
        Second lists: # default value: []
          - Number: 98
            Enable new content: true
            Content: "3, '\u005c\u0024{EXPNO}_hamocc_data_3d_ym.nc', 'nc2', 7, 10, 11, 12, 14,
                   15, 16, 17, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31, 37, 158,
                   288, 401, 402, 403, 404, 405, 406, 407, 408\u005c\u0024{OCYA}"
            Enable comment: false
          - Number: 97
            Enable new content: false
            Content:
            Enable comment: true
        ## Description of lists with read and write information.
        # Input type: string
        Description: In First Lists 80 and 81 are comment out and 95 get a new content.

# 11. Further parameter
# =======================

## Add further basic physical and biogeochemical model parameters.
Further parameter:
    # Further basic physical model parameters.
    # Input type: Array: string (as list) in form:
    # parameter = value
    Basic physical model: # default value: []
    # Further biogeochemical model parameters.
    # Input type: Array: string (as list) in form:
    # parameter = value
    Biogeochemistry: # default value: []
      - sinkspeed_poc = 0.5
      - deltacalc = 1000.
      - deltaorg = 3.
      - deltasil = 210.
    # The description of the further basic physical and biogeochemical model parameters.
    Description: Four further parameter from biogeochemie.
```
