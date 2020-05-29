# -*- coding: utf-8 -*-

"""
***************************************************************************
    OgrGeoProcessingProvider.py
    ---------------------
    Date                 : August 2019
    Copyright            : (C) 2019 by Giovanni Manghi
    Email                : giovanni dot manghi at naturalgis dot pt
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Alexander Bruy and Giovanni Manghi'
__date__ = 'August 2019'
__copyright__ = '(C) 2019, Giovanni Manghi'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os

from qgis.PyQt.QtGui import QIcon

from qgis.core import QgsProcessingProvider
from processing.core.ProcessingConfig import ProcessingConfig, Setting
from processing.tools import system

from export_to_sql_server.OgrToSQLServer import OgrToSQLServer

OGRTOSQLSERVER_ACTIVE = 'OGRTOSQLSERVER_ACTIVE'

pluginPath = os.path.dirname(__file__)


class OgrGeoprocessingProvider(QgsProcessingProvider):

    def __init__(self):
        super().__init__()
        self.algs = []

    def id(self):
        return 'exporttosqlserver'

    def name(self):
        return 'Export to SQL Server'

    def icon(self):
        return QIcon(os.path.join(pluginPath, 'icons', 'mIconMssql_32.png'))

    def load(self):
        ProcessingConfig.settingIcons[self.name()] = self.icon()
        ProcessingConfig.addSetting(Setting(self.name(),
                                            OGRTOSQLSERVER_ACTIVE,
                                            'Activate',
                                            True))
        ProcessingConfig.readSettings()
        self.refreshAlgorithms()
        return True

    def unload(self):
        ProcessingConfig.removeSetting(OGRTOSQLSERVER_ACTIVE)

    def isActive(self):
        return ProcessingConfig.getSetting(OGRTOSQLSERVER_ACTIVE)

    def setActive(self, active):
        ProcessingConfig.setSettingValue(OGRTOSQLSERVER_ACTIVE, active)

    def supportsNonFileBasedOutput(self):
        return True

    def getAlgs(self):
        algs = [
                OgrToSQLServer()
               ]

        return algs

    def loadAlgorithms(self):
        self.algs = self.getAlgs()
        for a in self.algs:
            self.addAlgorithm(a)
