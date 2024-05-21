# This file is part of the DebugPoint.com tutorial series for Python Macros in LibreOffice
#
#
import uno

def BulletproofMusicianExcel():

    oDoc = XSCRIPTCONTEXT.getDocument()
    
    oSheet =oDoc.getSheets().getByIndex(0)
    oCell = oSheet.getCellByPosition(0,0)
    
    return None
