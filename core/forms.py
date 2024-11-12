from django import forms
from .models import BookCategory,Book

class BookForm(forms.Form):
    title = forms.CharField(max_length=140,label='Название книги',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Введите название книги'}))
    author = forms.CharField(max_length=140,label='Автор',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Введите автора книги'}))
    category = forms.ModelChoiceField(queryset=BookCategory.objects.all(),required=False,label='Категория',empty_label='Выберите категорию')
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Введите описание книги'}),label='Описание книги')    
    review = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Введите текст обзора'}),label='Текст обзора')
    rate = forms.IntegerField(min_value=1,max_value=10,label='Оценка',widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Введите оценку от 1 до 10'}))
    status = forms.ChoiceField(choices=Book.STATUSES,required=False,label='Статус',initial='Draft')
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if Book.objects.filter(title=title).exists():
            raise forms.ValidationError('Обзор на книгу с таким названием уже есть.')
        return title

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'