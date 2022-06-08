import re
import json
import pkg_resources

def clean(text):
    filepath = pkg_resources.resource_filename(__name__, 'regex.json')
    rulesFile = open(filepath, 'r')
    rulesList = json.load(rulesFile)
    for rule in rulesList:
        rules = rulesList.get(rule)
        if rule == 'suffix': 
            for substring in rules:
                pattern = re.compile(re.escape(substring)+'.*')
                text = pattern.sub('', text)
        elif rule == 'prefix':
            for substring in rules:
                pattern = re.compile('.*'+re.escape(substring))
                text = pattern.sub('', text)
    return text