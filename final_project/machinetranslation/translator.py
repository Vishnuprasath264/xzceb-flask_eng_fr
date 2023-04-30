import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version=os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    #write the code here
    translate = language_translator.translate(englishtext
    ,model_id='en-fr').get_result()
    frenchtext = json.dumps(translate['translations'], indent=2, ensure_ascii=False)
    return frenchtext

def french_to_english(frenchtext):
    #write the code here
    translate = language_translator.translate(frenchtext,
    model_id='fr-en').get_result()
    englishtext = json.dumps(translate['translations'], indent=2, ensure_ascii=False)
    return englishtext