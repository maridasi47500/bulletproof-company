from langdetect import DetectorFactory
from langdetect import detect
from deep_translator import GoogleTranslator
class Translate():
    def __init__(self,content):
        self.content=content
    def detect_and_translate(self,target_lang):
        result_lang = detect(self.content)
        print("langue détectée:"+result_lang)
        if result_lang == target_lang:
             return self.content
        else:
             translator = GoogleTranslator(source=result_lang, target=target_lang)
             translate_text = translator.translate(self.content)
             return translate_text 
