Export to SQL Server - Tool for the QGIS Processing Toolbox
--------------------------------------

Developed by Pedro Venâncio

Exports a vector layer to a new SQL Server database connection. 

It needs a Microsoft SQL Server driver installed: https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server. 

This driver doesn’t support creating new databases, you might want to use the Microsoft SQL Server Client Tools for this purpose, but it does allow creation of new layers within an existing database.

More information about the tool: https://gdal.org/drivers/vector/mssqlspatial.html.

Based in PostGIS Geoprocessing Tools plugin developed by Alexander Bruy and Giovanni Manghi for NaturalGIS (https://github.com/NaturalGIS/naturalgis_postgis_geoprocessing) and in Export to PostgreSQL tool developed by Victor Olaya.
