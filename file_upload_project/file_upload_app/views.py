from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer
from .tasks import process_file


@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            # Создаем объект модели File
            file_instance = serializer.save()

            # Сохраняем файл на сервере
            uploaded_file = request.data['file']
            file_instance.file.save(uploaded_file.name, uploaded_file)

            # Запускаем асинхронную задачу для обработки файла с использованием Celery
            process_file.delay(file_instance.id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def file_list(request):
    if request.method == 'GET':
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
