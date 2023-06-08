from django_filters import FilterSet, DateFilter
from .models import Post
from django.forms import DateInput


# создаём фильтр
class PostFilter(FilterSet):
    # В мета классе надо предоставить модель и указать поля,
    # по которым будем фильтровать
    added_after = DateFilter(
        field_name='dateCreated',
        label='Дата публикации начиная с:',
        lookup_expr='gt',
        widget=DateInput(
            format='%d-%m-%Y',
            attrs={'type': 'date'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            # 'dateCreated': ['gt'],
            'title': ['icontains'],
            'authorArticle': ['exact'],
            'postCategory': ['exact'],
        }
        # fields = '__all__'
