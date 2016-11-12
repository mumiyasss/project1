import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Post


class PostMethodTests(TestCase):

    def test_post_without_category(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)