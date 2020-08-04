from datetime import date

from django.contrib.auth.models import User
from django.urls import resolve, reverse
from django.test import TestCase, tag

from ..models import Athlete, Apparatus, Event, TargetResult
from ..views import athlete_detail


class AthleteDetailViewTests(TestCase):
    
    def setUp(self):
        method = getattr(self,self._testMethodName)
        tags = getattr(method,'tags', {})
        self.athlete = Athlete.objects.create(first_name="Bob", last_name="Marley",
            birth_date=date.fromisoformat("1945-02-06"), gender=1)
        if 'skip_setup' in tags:
            return # if skipped, don't do anything
        self.user = User.objects.create_user(username="John", email="john@rambo.com", password="123")
        self.client.login(username="John", password="123")


    @tag('skip_setup')
    def test_not_connected_status_code(self):
        """
        If a user is not authenticated, the page is forbidden
        """
        response = self.client.get(reverse('board:athlete_detail',
            kwargs={'athlete_id': self.athlete.id}))
        self.assertEquals(response.status_code, 302)


    def test_connected_status_code(self):
        """
        If a user is authenticated, the page is available
        """
        response = self.client.get(reverse('board:athlete_detail',
            kwargs={'athlete_id': self.athlete.id}))
        self.assertEquals(response.status_code, 200)



    def test_board_url_resolves_board_view(self):
        """
        Check if the url of the board match with the function representing the view
        """
        view = resolve(f'/board/athlete/{self.athlete.id}/')
        self.assertEquals(view.func, athlete_detail)


    def test_athlete_not_found(self):
        """
        An athlete view not existing gives an error 404
        """
        response = self.client.get(reverse('board:athlete_detail',
            kwargs={'athlete_id': 99}))
        self.assertEquals(response.status_code, 404)


    def test_athlete_details(self):
        """
        An athlete view gives proprer information
        """
        response = self.client.get(reverse('board:athlete_detail',
            kwargs={'athlete_id': self.athlete.id}))
        self.assertContains(response, self.athlete.first_name.capitalize())
        self.assertContains(response, self.athlete.last_name.capitalize())
        self.assertContains(response, self.athlete.gend().capitalize())

    def test_athlete_no_target_result(self):
        """
        An athlete with no target results display nothing
        """
        response = self.client.get(reverse('board:athlete_detail',
            kwargs={'athlete_id': self.athlete.id}))
        self.assertContains(response, "There is no target for this athlete.")


    def test_athlete_with_target_result(self):
        """
        An athlete with a target display a table
        """
        apparatus = Apparatus.objects.create(name="Floor", short_name="FX")
        event = Event.objects.create(name="One Love Peace", place="Kingston", date=date.fromisoformat("1978-04-04"))
        TargetResult.objects.create(athlete=self.athlete, event=event, apparatus=apparatus)
        response = self.client.get(reverse('board:athlete_detail',
            kwargs={'athlete_id': self.athlete.id}))
        self.assertContains(response, "Graph of events")

        self.assertContains(response, f'{event.name} - {event.date:%Y}')
