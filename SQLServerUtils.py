# -*- coding: utf-8 -*-

"""
***************************************************************************
    SQLServerUtils.py
    ---------------------
    Date                 : December 2019
    Copyright            : (C) 2019 by Pedro Venancio
    Email                : pedrongvenancio at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Pedro Venancio'
__date__ = 'December 2019'
__copyright__ = '(C) 2019, Pedro Venancio'

import os
import subprocess
import platform
import re
import warnings

import psycopg2

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    from osgeo import ogr

from qgis.core import (Qgis,
                       QgsApplication,
                       QgsVectorFileWriter,
                       QgsProcessingFeedback,
                       QgsProcessingUtils,
                       QgsMessageLog,
                       QgsSettings,
                       QgsCredentials,
                       QgsDataSourceUri)
from processing.core.ProcessingConfig import ProcessingConfig
from processing.tools.system import isWindows, isMac

try:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        from osgeo import gdal  # NOQA

    gdalAvailable = True
except:
    gdalAvailable = False

class SQLServerUtils:

    @staticmethod
    def escapeAndJoinSQLServer(strList):
        joined = ''
        for s in strList:
            if not isinstance(s, str):
                s = str(s)
            if s and s[0] != '-' and ' ' in s:
                escaped = '"' + s.replace('"', '\\"').replace('\\"', '') \
                          + '"'
            else:
                escaped = s
            if escaped is not None:
                joined += escaped + ' '
        return joined.strip()

    @staticmethod
    def gdal_crs_string(crs):
            """
            Converts a QgsCoordinateReferenceSystem to a string understandable
            by GDAL
            :param crs: crs to convert
            :return: gdal friendly string
            """
            if crs.authid().upper().startswith('EPSG:'):
                return crs.authid()

            # fallback to proj4 string, stripping out newline characters
            return crs.toProj4().replace('\n', ' ').replace('\r', ' ')
