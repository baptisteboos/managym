from datetime import date

from django.contrib.auth.models import User
from django.urls import resolve, reverse
from django.test import TestCase, tag

from ..views import AthleteListView
from ..models import Athlete


class AthletesViewTests(TestCase):
    def setUp(self):
        method = getattr(self,self._testMethodName)
        tags = getattr(method,'tags', {})
        if 'skip_setup' in tags:
            return # if skipped, don't do anything
        self.user = User.objects.create_user(username="John", email="john@rambo.com", password="123")
        self.client.login(username="John", password="123")


    @tag('skip_setup')
    def test_not_connected_status_code(self):
        """
        If a user is not authenticated, the page is forbidden
        """
        response = self.client.get(reverse('board:athlete-list'))
        self.assertEquals(response.status_code, 302)


    def test_connected_status_code(self):
        """
        If a user is authenticated, the page is available
        """
        response = self.client.get(reverse('board:athlete-list'))
        self.assertEquals(response.status_code, 200)


    def test_board_url_resolves_board_view(self):
        """
        Check if the url of the board match with the function representing the view
        """
        view = resolve('/board/athletes/')
        self.assertEquals(view.func.view_class, AthleteListView)

    def test_no_athlete(self):
        """
        If no athlete, display nothing
        """
        response = self.client.get(reverse('board:athlete-list'))
        self.assertContains(response, "No athlete.")
        self.assertQuerysetEqual(response.context['athletes'], [])


    def test_athletes_in_list(self):
        """
        If athletes, display list of athletes valid link of profile
        """
        athlete = Athlete.objects.create(first_name="Bob", last_name="Marley",
            birth_date=date.fromisoformat("1945-02-06"), gender=1)
        athlete = Athlete.objects.create(first_name="Fred", last_name="Doe",
            birth_date=date.fromisoformat("1993-09-01"), gender=1)
        response = self.client.get(reverse('board:athlete-list'))
        self.assertQuerysetEqual(response.context['athletes'],
            ['<Athlete: Bob Marley>', '<Athlete: Fred Doe>'])
        athlete_url = reverse('board:athlete-detail', kwargs={'athlete_id': athlete.id})
        self.assertContains(response, f'<a href="{athlete_url}">')