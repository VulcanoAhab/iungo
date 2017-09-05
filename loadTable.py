import csv
from datetime import datetime

class Transform:
    """
    """
    _dateFormat="%Y-%m-%d"
    _frequency="month"

    @staticmethod
    def betweens(start, end):
        """
        """
        startDate=datetime.strpdatetime(start, cls._dateFormat)
        endisDate=datetime.strpdatetime(end, cls._dateFormat)
        deltaDates=endisDate-startDate
        return (start+timedelta(days=d) for d in deltaDates)

    @staticmethod
    def loadCsv(filePath):
        """
        """
        fd=open(filePath, "r")
        table=list(csv.reader(fd))
        fd.close()
        return table

    @classmethod
    def setDateFormat(cls, dateFormat):
        """
        """
        cls._dateFormat=dateFormat

    @classmethod
    def parseRow(cls, row, columnsMapper):
        """
        """
        newRow={}
        for colName,processDict in columnsMapper.items():
            newColName=processDict["name"]
            newColValue=processDict.get("parse", lambda x:x)(row[colName])
            newRow[newColName]=newColValue
        return newRow


    def __init__(self, filePath):
        """
        """
        self._rawIter=Transform.loadCsv(filePath)
        self._processedIter=None


    def parseRows(self, columnsMapper={}):
        """
        mapperFormat ->
            {"column_name":{
                "name":-value-,
                "parse":-value-,
                }
            }
        """
        for row in self._rawIter:
            if not columnsMapper:
                yield row
                continue
            yield self.parseRow(row, columnsMapper)
