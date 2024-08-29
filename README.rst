Handy Stats
~~~~~~~~~~~

Small Python library to quickly run statistic aggregations.

.. contents:: Table of Contents
   :depth: 3
   :local:

Get started
===========

Install
-------

Simple as::

  pip install https://github.com/cloudmercato/handystats/archive/refs/heads/main.zip

Usage
-----

Make an average::

   >>> import handystats
   >>> data = range(1, 1001)
   >>> handystats.mean(data)
   500.5

Here's the available operations::

    mean
    stdev
    min
    max
    median
    harmonic_mean
    geo_mean
    perc1
    perc5
    perc95
    perc99
    variance
    pvariance


External links
==============

handystats is used in the following projects:

- `Ollama benchmark Q2 2024 - Exoscale A40 <https://projector.cloud-mercato.com/projects/exoscale-a40-gpus>`_


Contribute
==========

This project is created with ❤️ for free by `Cloud Mercato`_ under BSD License. Feel free to contribute by submitting a pull request or an issue.

.. _`Probes`: https://github.com/cloudmercato/Probes
.. _`Cloud Mercato`: https://www.cloud-mercato.com/
