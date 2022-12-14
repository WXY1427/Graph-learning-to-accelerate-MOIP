
Changelog
=========

0.0.0 (2020-05-13)
------------------

* First release on PyPI.


0.0.1 (2020-05-19)
------------------

* First working version, using the (Ozlen et al., 2014) algorithm, for minimisation problems.


0.0.2 (2020-05-19)
------------------

* Implemented maximisation problem solving.
* Improved documentation.
* Improved testing suite.


0.0.3 (2021-11-24)
------------------

* New state of the art algorithm - two stage approach from (Tamby & Vanderpooten, 2020) - implemented and set as the default for the command line executable.


0.0.4 (2021-11-24)
------------------

* Documentation and changelog changes that were missed in previous release.


0.0.5 (2021-11-24)
------------------

* Specify python version to prevent failing documentation build on https://readthedocs.org/


0.0.6 (2021-12-05)
------------------

* Specify which algorithm to use from the command line.
* Keep track of the number of solver calls and report in output.
* Bug fixes to (Tamby & Vanderpooten, 2020) implementation.


0.0.7 (2021-12-05)
------------------

* Provide feasible solutions to solver for (Tamby & Vanderpooten, 2020) implementation.
* Lower required python version number from 3.9 to 3.7 to get online docs compiling.


0.0.8 (2021-12-06)
------------------

* Finally got `the documentation <https://python-moiptimiser.readthedocs.io/en/latest/>`_ compiling on https://readthedocs.org/
* Implemented direct strategy from (Tamby & Vanderpooten, 2020).


0.0.9 (2021-12-07)
------------------

* Track and report the number of infeasible problems attempted.
* Converted examples from `William Pettersson on figshare <https://figshare.com/authors/_/3770188>`_ to be used for testing algorithms and benchmarking.


0.0.10 (2021-12-08)
-------------------

* Fixed rounding bug in (Ozlen et al., 2014).
* Minor code clean up and documentation updates.


0.0.11 (2021-12-08)
-------------------

* Documentation bug fix.


0.0.12 (2021-12-14)
-------------------

* Refactored (Ozlen et al., 2014) to fix bugs, simplify the code and tweak the performance.
* Changed CPU Time format in command line output
