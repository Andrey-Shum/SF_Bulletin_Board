from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    """
    Кастомная форма регистрации для allauth
    
    Настройки:
    - Email обязателен и уникален
    - Username не обязателен
    - Аутентификация по email
    - Обязательная верификация email
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Настройка поля email
        self.fields['email'].required = True
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите ваш email',
            'type': 'email'
        })
        
        # Настройка поля username (необязательное)
        if 'username' in self.fields:
            self.fields['username'].required = False
            self.fields['username'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Имя пользователя (необязательно)'
            })
        
        # Настройка поля password1
        if 'password1' in self.fields:
            self.fields['password1'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            })
        
        # Настройка поля password2
        if 'password2' in self.fields:
            self.fields['password2'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Подтвердите пароль'
            })
    
    def save(self, request):
        """
        Сохранение пользователя с дополнительной логикой
        """
        user = super().save(request)
        
        # Дополнительная логика при создании пользователя
        # Например, можно добавить пользователя в определенную группу
        # или отправить дополнительные уведомления
        
        return user
    
    def clean_email(self):
        """
        Дополнительная валидация email
        """
        email = self.cleaned_data.get('email')
        
        # Здесь можно добавить дополнительную логику валидации
        # Например, проверка домена, фильтрация и т.д.
        
        return email 