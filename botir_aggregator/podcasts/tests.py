from django.test import TestCase


class PodcastsTestCase(TestCase):
    def setUp(self):
        self.Episode=Episode.objects.create(
            title="Test Title",
            description="Test Description",
            pub_date="2021-10-10 10:10:10",
            link="https://test.com",
            image="https://test.com/image.jpg",
            podcast_name="Test Podcast",
            guid="1234567890"
        )
    
    def test_ep_content(self):
        self.assertEqual(self.Episode.title, "Test Title")
    