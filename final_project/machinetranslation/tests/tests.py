import json
import translator

testfr = ["Merci","Oui"]
testeng = ["Thank You","Yes"]
print("Output for Null:", translator.english_to_french(" "))
print("Output for Null:", translator.french_to_english(" "))
print("Output for Hello:", translator.english_to_french("Hello"))
print("Output for Bonjour", translator.french_to_english("Bonjour"))
for i in testfr:
    print("Output for", i, translator.french_to_english(i))
for i in testeng:
    print("Output for", i, translator.english_to_french(i))