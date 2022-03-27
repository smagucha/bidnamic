from django.urls import reverse
from django.test import TestCase
from userdata.models import UserInfo
from django.contrib.auth.models import User


class UserInfoModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserInfo.objects.create(
            title="Mr.",
            firstname="Peter",
            surname="John",
            date_of_birth="1997-09-01",
            company_name="NIL",
            address="chokaa",
            telephone="+254707181264",
            bidding_setting="LOW",
            google_ads_account_id="smagucha"
        )

    def test_string_method(self):
        usertest = UserInfo.objects.get(id=1)
        expected_string = f"Name: {usertest.firstname} {usertest.surname}"
        self.assertEqual(str(usertest), expected_string)


class UserInfoCreateViewTestcase(TestCase):
    def setUp(self):
        UserInfo.objects.create(
            title="Mr.",
            firstname="peter",
            surname="John",
            date_of_birth="1997-09-01",
            company_name="NIL",
            address="chokaa",
            telephone="+254707181264",
            bidding_setting="LOW",
            google_ads_account_id="smagucha"
        )

    def test_UserInfoCreateView(self):
        response = self.client.post(reverse('insert'),
                                    {
                                        ' title': "Mr.",
                                        'firstname': "peter",
                                        'surname': "John",
                                        'date_of_birth': "1997-09-01",
                                        'company_name': "NIL",
                                        'address': "chokaa",
                                        'telephone': "+254707181264",
                                        'bidding_setting': "LOW",
                                        'google_ads_account_id': "smagucha"
                                    })
        self.assertEqual(response.status_code, 302)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('insert'))
        self.assertEqual(response.status_code, 302)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('insert'))
        self.assertRedirects(response, '/accounts/login/?next=/UserInsertForm')


class HomeTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        user1.save()
        user2.save()

        userinfodata = UserInfo.objects.create(
            title="Mr.",
            firstname="Peter",
            surname="John",
            date_of_birth="1997-09-01",
            company_name="NIL",
            address="chokaa",
            telephone="+254707181264",
            bidding_setting="LOW",
            google_ads_account_id="smagucha"
        )
        userinfodata.save()

    def test_url_exists(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 302)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('home'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

    #     self.assertTemplateUsed(response, 'userdata/home.html')

    def test_get_context_data(self):
        response = self.client.get(reverse('home'))
        response.context = dict()
        response.context['page_title'] = 'home page'
        self.assertEqual(response.context['page_title'], 'home page')


class UpdateUserInfoTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        user1.save()
        userinfodata = UserInfo.objects.create(
            title="Mr.",
            firstname="peter",
            surname="John",
            date_of_birth="1997-09-01",
            company_name="NIL",
            address="chokaa",
            telephone="+254707181264",
            bidding_setting="LOW",
            google_ads_account_id="smagucha"
        )
        userinfodata.save()

    def test_update_book(self):
        updateuserinfo = UserInfo.objects.get(id=1)

        response = self.client.post(
            reverse('update-userinfo', kwargs={'pk': updateuserinfo.id}),
            {
                ' title': "Mr.",
                'firstname': "peter",
                'surname': "John",
                'date_of_birth': "1997-09-01",
                'company_name': "NIL",
                'address': "chokaa",
                'telephone': "+254707181264",
                'bidding_setting': "LOW",
                'google_ads_account_id': "smagucha"
            }
        )
        self.assertEqual(response.status_code, 302)
        updateuserinfo.refresh_from_db()
        self.assertEqual(updateuserinfo.firstname, 'peter')

    def test_redirect_if_not_logged_in(self):
        updateuserinfo = UserInfo.objects.get(id=1)
        response = self.client.get(reverse('update-userinfo', args=[updateuserinfo.id]))
        self.assertRedirects(response, f'/accounts/login/?next=/UpdateUserInfo/{updateuserinfo.id}')

    def test_url_accessible_by_name(self):
        updateuserinfo = UserInfo.objects.get(id=1)
        response = self.client.get(reverse('update-userinfo', args=[updateuserinfo.id]))
        self.assertEqual(response.status_code, 302)

    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertEqual(response.status_code, 302)
    #     print(response)
    #     self.assertTemplateUsed(response, 'userdata/form.html')


class DeleteUserInfoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserInfo.objects.create(
            title="Mr.",
            firstname="Peter",
            surname="John",
            date_of_birth="1997-09-01",
            company_name="NIL",
            address="chokaa",
            telephone="+254707181264",
            bidding_setting="LOW",
            google_ads_account_id="smagucha"
        )

    def test_userinfo_delete(self):
        deleteuserinfo = UserInfo.objects.get(id=1)
        response = self.client.delete(reverse('delete-userinfo', kwargs={'pk': deleteuserinfo.id}),
                                      {
                                          ' title': "Mr.",
                                          'firstname': "peter",
                                          'surname': "John",
                                          'date_of_birth': "1997-09-01",
                                          'company_name': "NIL",
                                          'address': "chokaa",
                                          'telephone': "+254707181264",
                                          'bidding_setting': "LOW",
                                          'google_ads_account_id': "smagucha"
                                      }
                                      )
        self.assertEqual(response.status_code, 302)

    def test_url_accessible_by_name(self):
        deleteuserinfo = UserInfo.objects.get(id=1)
        response = self.client.get(reverse('delete-userinfo', args=[deleteuserinfo.id]))
        self.assertEqual(response.status_code, 302)

    def test_redirect_if_not_logged_in(self):
        deleteuserinfo = UserInfo.objects.get(id=1)
        response = self.client.get(reverse('delete-userinfo', args=[deleteuserinfo.id]))
        self.assertRedirects(response, f'/accounts/login/?next=/DeleteUserInfo/{deleteuserinfo.id}')
