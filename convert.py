import json
import os
import pandas as pd
# Initialize global variables
DATASETS_DIR = './'
TEST_FILE = 'example_nolabel.json'
END_OF_STRING = '  '

#debug
import pprint
pp = pprint.PrettyPrinter(indent=4)

context = []
thread = []
dialogId = []

with open(os.path.join(DATASETS_DIR, TEST_FILE), encoding='utf-8') as fh:
    data = json.load(fh)
    for row in data:
        context.append(row['context'])
        dialogId.append(row['dialogId'])
        utts = []
        for utt in row["thread"]:
            utts.append(utt["text"])
        thread.append(END_OF_STRING.join(utts))


#debug
#pp.pprint(thread)
#pp.pprint(context)
#pp.pprint(dialogId)

pd.DataFrame.from_dict({'id': dialogId, 'context': context, 'response': thread}) \
    .set_index('id') \
    .to_csv('test.csv')

