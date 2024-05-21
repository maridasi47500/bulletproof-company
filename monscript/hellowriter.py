def BulletproofMusicianWord():
    data = 'Hello bulletproof musician Python'

    # ~ Current document
    doc = XSCRIPTCONTEXT.getDocument()

    # ~ Current selection always return a ranges, and get to end
    text = doc.CurrentSelection[0].End
    
    # ~ Write data
    text.String = data
    
    return
