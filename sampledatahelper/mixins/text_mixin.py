import random
import string
from ..exceptions import ParameterError

from django.contrib.webdesign import lorem_ipsum


class TextMixin(object):
    def word(self):
        """Random text with 1 word."""
        return lorem_ipsum.words(1, common=False)

    def words(self, min_words=1, max_words=5):
        """Random text with 1 word."""

        if min_words > max_words:
            raise ParameterError('min_words greater than max_words')

        words = random.randint(min_words, max_words)
        return lorem_ipsum.words(words, common=False)

    def char(self):
        """Random character."""
        return random.choice(string.ascii_letters)

    def chars(self, min_chars=1, max_chars=5):
        """Random text with 1 word."""

        if min_chars > max_chars:
            raise ParameterError('min_chars greater than max_chars')

        chars = random.randint(min_chars, max_chars)
        result = ''
        for _ in range(chars):
            result += self.char()
        return result

    def email(self):
        """Random mail address."""
        username = lorem_ipsum.words(1, common=False)
        domain = lorem_ipsum.words(1, common=False)
        termination = random.choice([u'.com', u'.org', u'.net'])

        return "{0}@{1}{2}".format(username, domain, termination)

    def url(self):
        """Random url."""
        protocol = random.choice(["http", "https"])
        domain = self.word()
        termination = random.choice([u'.com', u'.org', u'.net'])
        path = self.word()

        return "{0}://{1}{2}/{3}".format(protocol, domain, termination, path)

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

    def paragraphs(self, min_paragraphs=1, max_paragraphs=5):
        """Random text with variable number of words, several sentences."""

        if min_paragraphs > max_paragraphs:
            raise ParameterError('min_paragraphs greater than max_paragraphs')

        return "\n\n".join(lorem_ipsum.paragraphs(random.randrange(min_paragraphs, max_paragraphs+1)))

    def slug(self, min_words=5, max_words=5):
        """Random slug"""

        if min_words > max_words:
            raise ParameterError('min_words greater than max_words')

        return "-".join([self.word() for x in range(self.int(max_value=max_words, min_value=min_words))])

    def tags(self, min_tags=1, max_tags=5, tags_list=None):
        if min_tags > max_tags:
            raise ParameterError('min_tags greater than max_tags')

        tags = []
        for i in range(random.randrange(min_tags, max_tags+1)):
            if tags_list:
                tags.append(tags_list[random.randrange(0, len(tags_list))])
            else:
                tags.append(self.word())
        return ','.join(tags)
