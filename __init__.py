# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
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

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from export_to_sql_server.OgrGeoprocessingProviderPlugin import OgrGeoprocessingProviderPlugin


def classFactory(iface):
    return OgrGeoprocessingProviderPlugin()
