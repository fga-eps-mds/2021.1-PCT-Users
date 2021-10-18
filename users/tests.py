from django.test import TestCase
from users.models import User


class UserEdited(TestCase):

    def create_and_edit_user(self):
        user_saved = User.objects.create(
            name='User',
            email='email@test.com',
            password='user123',
            roleId=1
        )

        user_edited = {
            'name':'User Editado',
            'email':'email_editado@test.com',
            'roleId':2
        }

        self.assertNotEqual(user_saved.name, user_edited['name'])
        self.assertNotEqual(user_saved.email, user_edited['email'])
        self.assertNotEqual(user_saved.roleId, user_edited['roleId'])

        user = User.objects.filter(id=user_saved.id).update(
            name=user_edited['name'],
            email=user_edited['email'],
            roleId=user_edited['roleId']
        )

        self.assertEqual(user.name, user_edited['name'])
        self.assertEqual(user.email, user_edited['email'])
        self.assertEqual(user.roleId, user_edited['roleId'])