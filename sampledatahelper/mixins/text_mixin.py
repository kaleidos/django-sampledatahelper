import sys
import random
try:
    from django.contrib.webdesign import lorem_ipsum
except ImportError:
    sys.exit()


class TextMixin(object):
    def word(self):
        """Random text with 1 word."""
        return lorem_ipsum.words(1, common=False)

    def words(self, min_words=1, max_words=5):
        """Random text with 1 word."""
        words = random.randint(min_words, max_words)
        return lorem_ipsum.words(words, common=False)

    def char(self):
        """Random character."""
        return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

    def chars(self, min_chars=1, max_chars=5):
        """Random text with 1 word."""
        chars = random.randint(min_chars, max_chars)
        result = ''
        for _ in range(chars):
            result += self.char()
        return result

    def email(self):
        """Random mail address."""
        return lorem_ipsum.words(1, common=False) + u'@' + lorem_ipsum.words(1, common=False) + \
               random.choice([u'.es', u'.com', u'.org', u'.net', u'.gov', u'.tk'])

    def url(self):
        """Random url."""
        protocol = random.choice(["http", "https"])
        domain = self.word() + random.choice([u'.es', u'.com', u'.org', u'.net', u'.gov', u'.tk'])
        path = self.word()
        return "%s://%s/%s" % (protocol, domain, path)

    def sentence(self):
        """Random sentence with text shorter than 255 characters."""
        sentence = lorem_ipsum.sentence()
        while len(sentence) >= 255:
            sentence = lorem_ipsum.sentence()
        return sentence

    def short_sentence(self):
        """Random sentence with text shorter than 100 characters."""
        sentence = lorem_ipsum.sentence()
        while len(sentence) >= 100:
            sentence = lorem_ipsum.sentence()
        return sentence

    def long_sentence(self):
        """Random sentence with text longer than 150 characters."""
        sentence = lorem_ipsum.sentence()
        while len(sentence) <= 150:
            sentence = lorem_ipsum.sentence()
        return sentence

    def paragraph(self):
        """Random text with variable number of words, several sentences."""
        return lorem_ipsum.paragraph()

    def slug(self, min_words=5, max_words=5):
        """Random slug"""
        return "-".join([self.word() for x in range(self.int(max_value=max_words, min_value=min_words))])

    def tags(self, max_tags=5, tags_list=None):
        tags = []
        for i in range(random.randrange(0, max_tags)):
            if tags_list:
                tags.append(tags_list[random.randrange(0, len(tags_list))])
            else:
                tags.append(self.word())
        return ','.join(tags)
