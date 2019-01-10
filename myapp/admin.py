from django.contrib import admin
from myapp.snippets import models as snippet


admin.register(snippet.Snippet)
