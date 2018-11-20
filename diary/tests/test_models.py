from django.test import TestCase
from diary.models import Page, Diary, Tag


class TestingModels(TestCase):

    def setUp(self):
        """
        Set up creating database's objects
        """

        Diary.objects.create(username='tony')
        Diary.objects.create(username='tintin')
        diary = Diary.objects.all()
        Tag.objects.create(name='happy')
        Tag.objects.create(name='sad')
        tag = Tag.objects.all()
        Page.objects.create(
            diary=diary[0], title='title' ,tag=tag[0], story='This was awesome', date='today', picture='pic1.jpg')
        Page.objects.create(
            diary=diary[1], title='title', tag=tag[1], story='This was awesome', date='today', picture='pic1.jpg')

    def test_count_diary(self):
        """
        Test counting the total diarys.
        """

        num_diary = Diary.objects.all().count()
        self.assertEqual(num_diary, 2)

    def test_count_tag(self):
        """
        Test counting the total tags.
        """

        num_tag = Tag.objects.all().count()
        self.assertEqual(num_tag, 2)

    def test_count_page(self):
        """
        Test counting the total pages.
        """

        num_page = Page.objects.all().count()
        self.assertEqual(num_page, 2)

    def test_diary_username(self):
        """
        Test the diary object's username.
        """

        diary = Diary.objects.all()
        self.assertEqual(diary[0].username, 'tony')
        self.assertEqual(diary[1].username, 'tintin')

    def test_tag_name(self):
        """
        Test the tag object' name.
        """

        tag = Tag.objects.all()
        self.assertEqual(tag[0].name, 'happy')
        self.assertEqual(tag[1].name, 'sad')

    def test_diary_string_representation(self):
        """
        Test that the string is correctly represented in diary.
        """

        diary = Diary.objects.all()
        self.assertEqual(str(diary[0]), diary[0].username)
        self.assertEqual(str(diary[1]), diary[1].username)

    def test_tag_string_representation(self):
        """
        Test that the string is correctly represented in diary's tag.
        """

        tag = Tag.objects.all()
        self.assertEqual(str(tag[0]), tag[0].name)
        self.assertEqual(str(tag[1]), tag[1].name)

    def test_diary_max_length(self):
        """
        Test that the max length of the field is equal or not.
        """

        diary = Diary(username='tony')
        max_length = diary._meta.get_field('username').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        page = Page.objects.all()
        self.assertEquals(page[0].get_absolute_url(), '/diary/')
