from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UploadArquivoForm
import uuid


def upload_view(request):
    if request.method == "POST":
        form = UploadArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES["arquivo"]

            # TODO: Aqui vamos salvar o arquivo temporariamente e chamar o Celery
            # Por enquanto, apenas simulamos uma resposta de sucesso
            fake_task_id = uuid.uuid4()

            return JsonResponse(
                {
                    "message": "Upload recebido com sucesso!",
                    "task_id": str(fake_task_id),
                    "file_name": arquivo.name,
                }
            )
    else:
        form = UploadArquivoForm()

    return render(request, "ingestion/upload.html", {"form": form})
