from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Указываем имя проекта Django и устанавливаем переменную окружения DJANGO_SETTINGS_MODULE.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_upload_project.settings')

# Создаем экземпляр Celery и называем его, например, "app".
app = Celery('file_upload_project')

# Загружаем настройки Celery из файла settings.py нашего проекта.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически загружаем задачи из всех файлов tasks.py в приложениях Django.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Задача выполнена: {0!r}'.format(self.request))
