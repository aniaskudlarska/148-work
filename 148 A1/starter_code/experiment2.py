ó
Ã¿åWc           @   s¨   d  Z  d d l m Z m Z d d l m Z m Z d d l m Z d d d     YZ	 d   Z
 d   Z d	   Z d
   Z e d k r¤ d d l Z e j d d  n  d S(   s¬  Assignment 1 - Running experiments (Tasks 5 & 6)

This module contains class SchedulingExperiment.  It can create an experiment
with input data and an algorithm configuration specified in a dictionary, then
run the experiment, generate statistics as the result of the experiment, and
(optionally) report the statistics.

This module is responsible for all the reading of data from the data files.

To test your code, we will construct instances of SchedulingExperiment, call
its methods, and examine the dictionary of statistics that method run
returns.

If you defined any domain classes other than Parcel and Truck, you may import
them here.  You may not import external libraries.
iÿÿÿÿ(   t   RandomSchedulert   GreedyScheduler(   t   Parcelt   Truck(   t   DistanceMapt   SchedulingExperimentc           B   s5   e  Z d  Z d   Z e d  Z d   Z d   Z RS(   sÎ  An experiment in scheduling parcels for delivery.

    To complete an experiment involves four stages:

    1. Read in all data from necessary files, and create corresponding objects.
    2. Run a scheduling algorithm to assign parcels to trucks.
    3. Compute statistics showing how good the assignment of parcels to trucks
       is.
    4. Report the statistics from the experiment.

    TODO: Complete this class docstring with any missing information.
    c         C   s   d S(   s[  Initialize a new experiment from a configuration dictionary.

        Precondition: <config> contains keys and values as specified
        in Assignment 1.

        @type config: dict[str, str]
            The configuration for this experiment, including
            the data files and algorithm configuration to use.
        @rtype: None
        N(    (   t   selft   config(    (    s?   X:\Dropbox\148 ASSIGNEMTN 1 PRIORITy\starter_code\experiment.pyt   __init__#   s    c         C   s   d S(   si  Run the experiment and return statistics on the outcome.

        If <report> is True, print a report on the statistics from this
        experiment.  Either way, return the statistics in a dictionary.

        If <self.verbose> is True, print step-by-step details
        regarding the scheduling algorithm as it runs.

        @type self: SchedulingExperiment
        @type report: bool
            Whether or not to print a report on the statistics.
        @rtype: dict[str, int | float]
            Statistics from this experiment. Keys and values are as specified
            in Step 6 of Assignment 1.
        N(    (   R   t   report(    (    s?   X:\Dropbox\148 ASSIGNEMTN 1 PRIORITy\starter_code\experiment.pyt   run1   s    c         C   s   d S(   s/  Compute the statistics for this experiment.

        Precondition: _run has already been called.

        @type self: SchedulingExperiment
        @rtype: Dict[str, int | float]
            Statistics from this experiment. Keys and values are as specified
            in Step 6 of Assignment 1.
        N(    (   R   (    (    s?   X:\Dropbox\148 ASSIGNEMTN 1 PRIORITy\starter_code\experiment.pyt   _compute_statsD   s    c         C   s   d S(   s  Report on the statistics for this experiment.

        This method is *only* for debugging purposes for your benefit, so
        the content and format of the report is your choice; we
        will not call your run method with <report> set to True.

        Precondition: _compute_stats has already been called.

        @type self: SchedulingExperiment
        @rtype: None
        N(    (   R   (    (    s?   X:\Dropbox\148 ASSIGNEMTN 1 PRIORITy\starter_code\experiment.pyt   _print_reportQ   s    (   t   __name__t
   __module__t   __doc__R   t   FalseR
   R   R   (    (    (    s?   X:\Dropbox\148 ASSIGNEMTN 1 PRIORITy\starter_code\experiment.pyR      s
   		c         C   s   t  |  d  y } xo | D]g } | j   j d  } t | d j    } | d j   } | d j   } t | d j    } q WWd QXd S(   sê   Read parcel data from <parcel_file> and return XXXX

    @type parcel_file: str
        The name of a file containing parcel data in the form specified in
        Assignment 1.
    @rtype: XXXX

    TODO: Complete this docstring.
    t   rt   ,i    i   i   i   N(   t   opent   stript   splitt   int(   t   parcel_filet   filet   linet   tokenst   pidt   sourcet   destinationt   volume(    (    s?   X:\Dropbox\148 ASSIGNEMTN 1 PRIORITy\starter_code\experiment.pyt   read_parcelsd   s    c         C   sx   t  |  d  c } xY | D]Q } | j   j d  } | d j   } | d j   } t | d j    } q WWd QXd S(   sú   Read distance data from <distance_map_file> and return XXXX

    @type distance_map_file: str
        The name of a file containing distance data in the form specified in
        Assignment 1.
    @rtype: XXXX

    TODO: Complete this docstring.
    R   R   i    i   i   N(   R   R   R   R   (   t   distance_map_fileR   R   R   t   c1t   c2t   dist(    (    s?   X:\Dropbox\148 ASSIGNEMTN 1 PRIORITy\starter_code\experiment.pyt   read_distance_map|   s    c         C   sb   t  |  d  M } xC | D]; } | j   j d  } t | d  } t | d  } q WWd QXd S(   se  Read truck data from <truck_file> and return XXXX

    @type truck_file: str
        The name of a file containing truck data in the form specified in
        Assignment 1.
    @type depot_location: str
        The city where all the trucks (and packages) are at the start of the
        experiment.
    @rtype: XXXX

    TODO: Complete this docstring.
    R   R   i    i   N(   R   R   R   R   (   t
   truck_filet   depot_locationR   R   R   t   tidt   capacity(    (    s?   X:\Dropbox\148 ASSIGNEMTN 1 PRIORITy\starter_code\experiment.pyt   read_trucks   s
    c         C   sS   d d l  } t |  d   } | j |  } Wd QXt |  } | j d t  d S(   s  Configure and run a single experiment on the scheduling problem
    defined in <config_file>

    Precondition: <config_file> is a json file with keys and values
    as in the dictionary format defined in Assignment 1.

    @type config_file: str
    @rtype: None
    iÿÿÿÿNR   R	   (   t   jsonR   t   loadR   R
   t   True(   t   config_fileR*   R   t   configurationt
   experiment(    (    s?   X:\Dropbox\148 ASSIGNEMTN 1 PRIORITy\starter_code\experiment.pyt   sanity_check«   s
    t   __main__NR   s	   .pylintrc(    (   R   t	   schedulerR    R   t   domainR   R   t   distance_mapR   R   R   R$   R)   R0   R   t	   python_tat	   check_all(    (    (    s?   X:\Dropbox\148 ASSIGNEMTN 1 PRIORITy\starter_code\experiment.pyt   <module>   s   N				