from django.db import models

CHAR_CHOICES = (
    ('test1', 'Test 1'),
    ('test2', 'Test 2'),
    ('test3', 'Test 3'),
    ('test4', 'Test 4'),
    ('test5', 'Test 5'),
    ('test6', 'Test 6'),
    ('test7', 'Test 7'),
)

INTEGER_CHOICES = (
    (1, 'Test 1'),
    (2, 'Test 2'),
    (3, 'Test 3'),
    (4, 'Test 4'),
    (5, 'Test 5'),
    (6, 'Test 6'),
    (7, 'Test 7'),
)


class TestRelatedModel(models.Model):
    class Meta:
        app_label = "tests"


class TestModel(models.Model):
    very_short_char = models.CharField(max_length=2)
    short_char = models.CharField(max_length=10)
    char = models.CharField(max_length=30)
    middle_char = models.CharField(max_length=75)
    long_char = models.CharField(max_length=120)
    longer_char = models.CharField(max_length=250)

    very_short_slug = models.SlugField(max_length=2)
    short_slug = models.SlugField(max_length=10)
    slug = models.SlugField(max_length=30)
    middle_slug = models.SlugField(max_length=75)
    long_slug = models.SlugField(max_length=120)
    longer_slug = models.SlugField(max_length=250)

    email = models.EmailField()
    url = models.URLField()
    text = models.TextField()

    integer = models.IntegerField()
    small_integer = models.SmallIntegerField()
    positive_integer = models.PositiveIntegerField()
    positive_small_integer = models.PositiveSmallIntegerField()
    big_integer = models.BigIntegerField()
    float = models.FloatField()
    boolean = models.BooleanField(default=False)
    null_boolean = models.NullBooleanField()
    comma_separated_integers = models.CommaSeparatedIntegerField(max_length=100)
    decimal = models.DecimalField(decimal_places=10, max_digits=20)

    date = models.DateField()
    datetime = models.DateTimeField()
    time = models.TimeField()

    file = models.FileField(upload_to="tests/tmp")
    file_path = models.FilePathField()
    image = models.ImageField(upload_to="tests/tmp")

    ip = models.GenericIPAddressField()
    generic_ip = models.GenericIPAddressField()

    foreing_key = models.ForeignKey('tests.TestRelatedModel',
                                    related_name="test_related_1",
                                    on_delete=models.CASCADE)
    one_to_one = models.OneToOneField(TestRelatedModel,
                                      related_name="test_related_2",
                                      on_delete=models.CASCADE)
    many_to_many = models.ManyToManyField(TestRelatedModel,
                                          related_name="test_related_3")

    # With choices
    integer_choices = models.IntegerField(choices=INTEGER_CHOICES)
    char_choices = models.CharField(max_length=30, choices=CHAR_CHOICES)
    foreing_key_choices = models.ForeignKey('tests.TestRelatedModel',
                                            related_name="test_related_4",
                                            on_delete=models.CASCADE,
                                            limit_choices_to={'id__gt': 0})
    one_to_one_key_choices = models.OneToOneField('tests.TestRelatedModel',
                                                  related_name="test_related_5",
                                                  on_delete=models.CASCADE,
                                                  limit_choices_to={'id__gt': 0})

    class Meta:
        app_label = "tests"
