
test_text = '''The beef was fine—tough, but with body in it. They said it was
bull-beef; others, that it was dromedary beef; but I do not know, for
certain, how that was. They had dumplings too; small, but substantial,
symmetrically globular, and indestructible dumplings. I fancied that
you could feel them, and roll them about in you after they were
swallowed. If you stooped over too far forward, you risked their
pitching out of you like billiard-balls. The bread—but that couldn’t be
helped; besides, it was an anti-scorbutic; in short, the bread
contained the only fresh fare they had. But the forecastle was not very
light, and it was very easy to step over into a dark corner when you
ate it. But all in all, taking her from truck to helm, considering the
dimensions of the cook’s boilers, including his own live parchment
boilers; fore and aft, I say, the Samuel Enderby was a jolly ship; of
good fare and plenty; fine flip and strong; crack fellows all, and
capital from boot heels to hat-band.

But why was it, think ye, that the Samuel Enderby, and some other
English whalers I know of—not all though—were such famous, hospitable
ships; that passed round the beef, and the bread, and the can, and the
joke; and were not soon weary of eating, and drinking, and laughing? I
will tell you. The abounding good cheer of these English whalers is
matter for historical research. Nor have I been at all sparing of
historical whale research, when it has seemed needed.

The English were preceded in the whale fishery by the Hollanders,
Zealanders, and Danes; from whom they derived many terms still extant
in the fishery; and what is yet more, their fat old fashions, touching
plenty to eat and drink. For, as a general thing, the English
merchant-ship scrimps her crew; but not so the English whaler. Hence,
in the English, this thing of whaling good cheer is not normal and
natural, but incidental and particular; and, therefore, must have some
special origin, which is here pointed out, and will be still further
elucidated.
'''
import re
from collections import Counter
from scraper import Scrape
scrape = Scrape()

class TextStat():
    def __init__(self, text: str):
        self.text = text
        self.counted_words = {}
        self.word_stat()


    def word_stat(self):
        '''counting words from self.text'''
        content = self.text
        content = content.lower()
        words = re.findall(r'\w+', content)

        # # second way to split words without whitespaces and punctuations
        # content = content.strip('')
        # for char in (r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""+'\t\n\r\v\f'+'â€œ'+'â€˜'+''+''):
        #     content = content.replace(char, ' ')
        # content = content.lower()
        # words = content.split(" ")

        for word in words:
            if word in self.counted_words:
                self.counted_words[word] = self.counted_words[word] + 1
            else:
                self.counted_words[word] = 1
        return self.counted_words

    def find_word(self, word: str):
        word = word.lower()
        return {word: self.counted_words[word]}

    def most_common(self, how_much=5):
        most_occur = dict(Counter(self.counted_words).most_common(how_much))
        return most_occur

    def least_common(self, how_much=10):
        least_occur = Counter(self.counted_words).most_common()[-how_much:]
        least_occur = dict(least_occur)
        return least_occur

    def sentences(self):
        content = self.text
        content = content.lower()
        words = len(re.findall(r'\w+', content))
        punctuates = len(re.findall(r'\w+\.|\!|\?', content))
        average = words/punctuates

        return {'words': words,
                'sentences': punctuates,
                'average amount words in sentence': average
                }


if __name__ == '__main__':
    text_stat = TextStat(test_text)
    # print(text_stat.counted_words)
    # print(f'words most repeated: {text_stat.most_common()}')
    # word = 'whale'
    # print(f'find word : {text_stat.find_word(word)}')
    print(text_stat.least_common())









