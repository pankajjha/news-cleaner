import re
import json
import pkg_resources

def clean(text):
    filepath = pkg_resources.resource_filename(__name__, 'regex.json')
    rulesFile = open(filepath, 'r')
    rulesList = json.load(rulesFile)
    for substring in rulesList:
        pattern = re.compile(re.escape(substring)+'.*')
        text = pattern.sub('', text)
    return text