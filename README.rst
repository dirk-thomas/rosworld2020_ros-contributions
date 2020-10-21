Visualize ROS contributions over time
=====================================

Usage
-----

Only tested on Ubuntu Focal with ROS specific packages like ``python3-rosdistro`` being installed.

1. Run the ``get-repos.py`` script to fetch list of considered repositories and branches.
2. Edit ``github.yaml`` providing an OAuth token to use the GraphQL API.
3. Run the ``get-commits.py`` script to fetch commit information from each repository.
   This step will take quite a while but the information is stored locally and the script works incrementally if aborted and reinvoked.
4. Run the ``create-data.py`` script generate the data in ``json`` in the format needed by the web application.
5. Start a local webserver to host the files: ``python3 -m http.server``
6. Open ``http://0.0.0.0:8000/index.html`` in a web browser.

Limitations
-----------

Only a subset of the repositories of the ROS ecosystem are considered:

* The repository must be registered in the `ros/rosdistro <https://github.com/ros/rosdistro.git>`_ for an active / rolling ROS distribution and the branch must exist.

  * Additionally a set of tooling repositories are enumerated manually in the file ``tooling_repos.yaml``.

* Must be hosted on GitHub.
* Only commits since 2012 are used.

Commits in a repository are also being counted if they are from before the point in time the repository was added to the rosdistro.

If repositories were split, commits before the split are being counted multiple times.

Preview
-------

A preview using a snapshot of the collected data can be viewed at `www.dirk-thomas.net/rosworld2020_ros-contributions/ <http://www.dirk-thomas.net/rosworld2020_ros-contributions/index.html>`_.
