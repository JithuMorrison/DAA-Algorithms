def galeshapley(schpref,advpref):
  match={}
  unmatched = list(schpref.keys())
  while unmatched:
    scholar = unmatched.pop(0)
    advpreflist = schpref[scholar]
    for adv in advpreflist:
      advtest = False
      for matchsch,matchadv in match.items():
        if(adv == matchadv):
          advtest = True
          current_match = matchsch
          break
        if not advtest:
          match[scholar] = adv
          break
        else:
          if advpref[adv].index(scholar) < advpref[adv].index(current_match):
            match[scholar] = adv
            unmatched.append(current_match)
            del match[current_match]
            break
  return match

scholar_preferences = {
    'Stu1': ['Ad1', 'Ad2', 'Ad3'],
    'Stu2': ['Ad2', 'Ad1', 'Ad3'],
    'Stu3': ['Ad3', 'Ad1', 'Ad2']
}

advisor_preferences = {
    'Ad1': ['Stu2', 'Stu3', 'Stu1'],
    'Ad2': ['Stu3', 'Stu1', 'Stu2'],
    'Ad3': ['Stu1', 'Stu2', 'Stu3']
}

matching = galeshapley(scholar_preferences, advisor_preferences)
print("Matching:")
for scholar, advisor in matching.items():
    print(f"{scholar} is matched with {advisor}")
