from django.test import TestCase

from contacts.models import Contact, Address, Group

# Create your tests here.

class ContactsTest(TestCase):
    a0 = Address.objects.create(address='76 Mhlanga Street', city='Ekurhuleni', state='Gauteng', zip='2041')
    a1 = Address.objects.create(address='4 Gwigwi Mrwebi Street', city='Johannesburg', state='Gauteng', zip='2000')
    a2 = Address.objects.create(address='81 Vlok Street', city='Pretoria', state='Gauteng', zip='1990')
    a3 = Address.objects.create(address='81 Wisani Street', city='Makhado', state='Limpopo', zip='0957')

    g0 = Group.objects.create(group_name='family', about='my fam')
    g1 = Group.objects.create(group_name='friends', about='my buddz')
    g2 = Group.objects.create(group_name='blacklisted', about='those I hate!')
    # g3 = Group.objects.create(group_name='whitelisted', about='they can call!')

    c0 = Contact.objects.create(first_name='Wis', last_name='Sal', birthdate='1990-12-06', email='wis@gmail.com', address=a0, group=g0)
    c1 = Contact.objects.create(first_name='Lon', last_name='Rah', birthdate='1990-12-06', email='lon@yahoo.com', address=a0, group=g1)
    c2 = Contact.objects.create(first_name='Londani', last_name='Sala', birthdate='1991-10-09', email='londani@yahoo.com', address=a0, group=g2)
    c3 = Contact.objects.create(first_name='Londa', last_name='Peters', birthdate='1989-1-05', email='londa@yahoo.net', address=a0, group=g2)


    def test_with_email(self):
        # make a couple Contacts
        Contact.objects.create(first_name='Nathan')
        Contact.objects.create(email='nathan@eventbrite.com')

        self.assertEqual(
            Contact.objects.get(first_name='wis').first_name, 'Wis'
        )

    def test_db_contact_list_size(self):

        self.assertEqual(
            Contact.objects.all().count(), 4
        )

    def test_db_group_list_size(self):

        self.assertEqual(
            Group.objects.all(), 3
        )

    def test_group_list(self):

        self.assertEqual(
            Contact.objects.all().filter(group__exact='blacklisted').count(), 1
        )

    def test_exclude_list(self):

        self.assertEqual(
            Contact.objects.exclude(group__exact='blacklisted').count(), 2
        )
