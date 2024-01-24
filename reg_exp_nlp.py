#get the regular expressions from regex101.com

import re
chat1 = 'codebasic: you ask alot question 12345678912, abc@xyz.com'
chat2 = 'codebasic: yes phone 12345678912, and email abc@xyz.com'

pattern = '\d{10}'
matches = re.findall(pattern, chat1)
print(matches)