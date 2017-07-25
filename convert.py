import json
import os
import pandas as pd
import nltk
# Initialize global variables
DATASETS_DIR = './'
TEST_FILE = 'test_20170724.json'
END_OF_STRING = ' '
TOKEN_DELIMETR = ' '
ALICE_ID = 'Alice'
BOB_ID = 'Bob'

#debug
import pprint
pp = pprint.PrettyPrinter(indent=4)

context = []
thread = []
thread_alice = []
thread_bob = []
dialogId = []


tknzr = nltk.word_tokenize

with open(os.path.join(DATASETS_DIR, TEST_FILE), encoding='utf-8') as fh:
    data = json.load(fh)
    for row in data:
        context.append(TOKEN_DELIMETR.join(tknzr(row['context'])))
        dialogId.append(row['dialogId'])
        utts = []
        utts_alice = []
        utts_bob = []
        for utt in row["thread"]:
            tokenized_text = TOKEN_DELIMETR.join(tknzr(utt["text"]))
            utts.append(tokenized_text)
            if utt["userId"] == ALICE_ID:
                utts_alice.append(tokenized_text)
            if utt["userId"] == BOB_ID:
                utts_bob.append(tokenized_text)

        thread.append(END_OF_STRING.join(utts))
        thread_alice.append(END_OF_STRING.join(utts_alice))
        thread_bob.append(END_OF_STRING.join(utts_bob))

#debug
#pp.pprint(thread)
#pp.pprint(context)
#pp.pprint(dialogId)

pd.DataFrame.from_dict({'id': dialogId,
                        'context': context,
                        'response': thread,
                        'response_alice': thread_alice,
                        'response_bob': thread_bob
                        }
                       ) \
    .set_index('id') \
    .to_csv('test_2.csv', sep="\t")

