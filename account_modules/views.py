from django.shortcuts import render, redirect
from django.views import View
from .form import RegistrationForm, LoginForm, ForgetPasswordForm, ResetPasswordForm, VerifyCodeForm
from .models import User
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpRequest
from django.contrib.auth import login, logout
# from django.core.mail import send_mail
# from django.conf import settings
# from utils.email_service import send_email


# Create your views here.
class RegistrationView(View):
    def get(self, request):
        register_form = RegistrationForm()
        context = {'register_form': register_form}

        return render(request, 'account_modules/Register_page.html', context)

    def post(self, request):
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری میباشد')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email,
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('product_list'))

                # send_email('فعال سازی حساب کاربری', new_user.email, {'user': new_user},
                #            'emails/Active_account.html')

        context = {'register_form': register_form}
        return render(request, 'account_modules/Register_page.html', context)


class ActiveAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)  # تا کد قبلی غیر قابل استفاده باشه
                user.save()

                return redirect(reverse('login_page'))
            else:
                pass
        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {'login_form': login_form}
        return render(request, 'account_modules/login_page.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()

            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نیست')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('product_list'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')

            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
        context = {'login_form': login_form}
        return render(request, 'account_modules/login_page.html', context)


class ForgotPasswordView(View):
    def get(self, request: HttpRequest):
        forget_form = ForgetPasswordForm()
        context = {'forget_form': forget_form}
        return render(request, 'account_modules/Forget_password.html', context)

    def post(self, request: HttpRequest):
        forget_form = ForgetPasswordForm(request.POST)
        if forget_form.is_valid():
            user_email = forget_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                user.verification_code = get_random_string(20)
                user.save()
                # try:
                #     send_email('بازیابی کلمه عبور', user.email, {'user': user},
                #                'account_modules/Verify_code.html')
                # except NameError:
                #     pass
                return redirect(reverse('verify_code_page'))
            else:
                forget_form.add_error('email', 'کاربری با این ایمیل یافت نشد')
        context = {'forget_form': forget_form}
        return render(request, 'account_modules/Forget_password.html', context)


class VerifyCodeView(View):
    def get(self, request: HttpRequest):
        verify_form = VerifyCodeForm()
        context = {'verify_form': verify_form}
        return render(request, 'account_modules/Verify_code.html', context)

    def post(self, request: HttpRequest):
        verify_form = VerifyCodeForm(request.POST)
        if verify_form.is_valid():
            verification_code = verify_form.cleaned_data.get('verification_code')
            user = User.objects.filter(verification_code__iexact=verification_code).first()
            if user is not None:
                request.session['verification_code'] = verification_code
                return redirect(reverse('reset_password_page'))
            else:
                verify_form.add_error('verification_code', 'کد تایید نادرست است')
        context = {'verify_form': verify_form}
        return render(request, 'account_modules/Verify_code.html', context)


class ResetPasswordView(View):
    def get(self, request: HttpRequest):
        verification_code = request.session.get('verification_code')
        if not verification_code:
            return redirect(reverse('forgot_page'))

        reset_form = ResetPasswordForm()
        context = {'reset_form': reset_form}
        return render(request, 'account_modules/Reset_password.html', context)

    def post(self, request: HttpRequest):
        verification_code = request.session.get('verification_code')
        if not verification_code:
            return redirect(reverse('forgot_page'))

        reset_form = ResetPasswordForm(request.POST)
        if reset_form.is_valid():
            user = User.objects.filter(verification_code__iexact=verification_code).first()
            if user is not None:
                new_password = reset_form.cleaned_data.get('new_password')
                user.set_password(new_password)
                user.verification_code = ''
                user.save()
                del request.session['verification_code']
                return redirect(reverse('login_page'))
            else:
                reset_form.add_error(None, 'خرابی در سیستم، لطفا دوباره تلاش کنید')
        context = {'reset_form': reset_form}
        return render(request, 'account_modules/Reset_password.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))
