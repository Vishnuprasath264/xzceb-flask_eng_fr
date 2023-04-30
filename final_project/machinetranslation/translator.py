import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    #write the code here
    if englishtext is None:
        return ''
    translate = language_translator.translate(englishtext
    ,model_id='en-fr').get_result()
    frenchtext = translate['translations'][0]['translation']
    return frenchtext

def french_to_english(frenchtext):
    #write the code here
    if frenchtext is None:
        return ''
    translate = language_translator.translate(frenchtext,
    model_id='fr-en').get_result()
    englishtext = translate['translations'][0]['translation']
    return englishtext