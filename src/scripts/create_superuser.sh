# default superuser
# email: 'admin@admin.com'
# password: 'password'
echo "
from django.contrib.auth import get_user_model;
User = get_user_model();

if not len(User.objects.all()):
    User.objects.create_superuser(username='admin', email='admin@admin.com', password='password')" | python manage.py shell
