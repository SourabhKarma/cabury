
# Create your views here.
from urllib import response
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail  import send_mail
import random
from django.http import JsonResponse
from requests import request
from rest_framework import exceptions


from .serializer import UserRegistrationSerializer,VerifyUserOtpSerializer,ResendOtpSerializer,UserLoginSerializer,ResetPasswordSerializer,UserDetailSerializer

from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView

from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework import viewsets
from .models import User
from rest_framework.throttling import ScopedRateThrottle
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
# funtion to send otp

def send_mail_otp(email):
        subject = 'User Management System'
        otp =  random.randint(1000 ,9999)

        message = f'Your  OTP is - {otp}' 
        email_from = settings.EMAIL_HOST
        send_mail( subject, message, email_from, [email] )
        user_obj = User.objects.get(email= email)

        user_obj.otp = otp
        user_obj.save()





# user registration 



class UserRegistrationView(APIView):


    def post(self, request):

        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        
        if serializer.is_valid():

            serializer.save()
            send_mail_otp(serializer.data['email'])


            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'verify': 'Check mail and enter otp to verify Account',
                'email': serializer.data["email"]
            }

            return Response(response)

        else:
            return JsonResponse({"message":"email/username already exists"})


# user verify by email otp

class UserVerifyView(APIView):


    def post(self, request):

        data = request.data
        serializer = VerifyUserOtpSerializer(data=data)

        if serializer.is_valid():
            email = serializer.data['email'] 
            otp = serializer.data['otp'] 
            

            user = User.objects.filter(email = email)
            otpcheck =  User.objects.filter(otp = otp)
            if not user.exists():
                response = {
                    'success': True,
                    'statusCode':400,
                    'message': 'something went worng',
                    'data':'invalid email',
                }
                return Response(response)

            if user[0].otp != otp:
                response = {
                    'success': True,
                    'statusCode':400,
                    'message': 'something went worng',
                    'data':'Wrong Otp',
                }
                return Response(response)
            
            user = user.first()
            user.is_active = True
            user.save()



            # return JsonResponse({"message":"Successfully verified"})
            response = {
                'success': True,
                'statusCode':200,
                'message': 'verified',
                'data':'Otp and email matched',
            }
        return Response(response)




class ResendOtpView(APIView):
    throttle_scope = 'resend_opt_scope'
    throttle_classes = [ScopedRateThrottle,]
    def post(self, request):


        data = request.data
        serializer = ResendOtpSerializer(data=data)

        if serializer.is_valid():

            email = serializer.data['email'] 


            user = User.objects.filter(email = email)
            if not user.exists():

                response = {


                    'statusCode':400,

                    'message': 'invalid email',

                }

                return Response(response)

            user = user.first()

            send_mail_otp(email)

        return JsonResponse({"message":"OTP Resend Successfully"})




#login 


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )
    throttle_scope = 'login_scope'
    throttle_classes = [ScopedRateThrottle,]
    def post(self, request):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        valid = serializer.is_valid(raise_exception=True)
        # User = serializer.data['email']
        if valid:
            status_code = status.HTTP_200_OK
            userphoto = serializer.data['user_photo']
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    # 'id':User.pk
                    # 'id': serializer.data['id'],
                    'role': serializer.data['role_id'],
                    'user_photo':userphoto,
                    # 'username':serializer.data['username'],
                    # 'is_active':serializer.data['is_active']
                }
            }
            email = serializer.data['email']
            # user = User.objects.filter(email = email)
            # user =  user.first()
            # user.user_notification_token = request.data['user_notification_token']
            # user.save()
            return Response(response, status=status_code)




# ------------- user noti login  start ---------------------------

class UserNotiLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )
    # throttle_scope = 'login_scope'
    # throttle_classes = [ScopedRateThrottle,]
    def post(self, request):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        print(serializer)
        valid = serializer.is_valid(raise_exception=True)
        # User = serializer.data['email']
        if valid:



            status_code = status.HTTP_200_OK

            userphoto = serializer.data['user_photo']
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    # 'id':User.pk
                    # 'id': serializer.data['id'],
                    'role': serializer.data['role_id'],
                    # 'user_photo':userphoto,
                    # 'username':serializer.data['username'],
                    # 'is_active':serializer.data['is_active']
                }
            }

            email = serializer.data['email']
            user = User.objects.filter(email = email)
            user =  user.first()
            # user.user_notification_token = request.data['user_notification_token']
            # user.save()

            # for same token 
            # if not user.user_notification_token:
            #     return Response(response, status=status_code)
            #     or try pass
            # else:
            #     user.save()

            return Response(response, status=status_code)









# ------------------ user noti login end ---------------------------------------




#----------------------------- Reset Password -------------------------------------------

class ResetPasswordView(APIView):

    throttle_scope = 'reset_password_scope'
    throttle_classes = [ScopedRateThrottle,]
    def post(self, request):
        # throttle_scope = 'reset_password_scope'
        # throttle_classes = [ScopedRateThrottle,]
        data = request.data
        serializer = ResetPasswordSerializer(data=data)
    
        if serializer.is_valid():
            email = serializer.data['email'] 
            otp = serializer.data['otp'] 
            password = serializer.data['password']        

            user = User.objects.filter(email = email)
            otpcheck =  User.objects.filter(otp = otp)
            if not user.exists():
                response = {
                    'success': True,
                    'statusCode':400,
                    'message': 'something went worng',
                    'data':'invalid email',
                }
                return Response(response)

            if user[0].otp != otp:
                response = {
                    'success': True,
                    'statusCode':400,
                    'message': 'something went worng',
                    'data':'Wrong Otp',
                }
                return Response(response)
            
            user = user.first()
            user.set_password(password)
            user.save()
            return JsonResponse({"message":"Successfully Password Changed"},status = status.HTTP_201_CREATED)

#----------------------------- Reset Password End   ---------------------------------------------------









# ----------------------------------- userdetailview ---------------------------------



class UserListView(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        queryset = User.objects.filter(id = self.request.user.id)

        serializer = UserDetailSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # not permitted check
        if instance.id != self.request.user.id:
            print(instance.id)
            print(self.request.user)
            raise exceptions.PermissionDenied()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



# ----------------------------------- userdetailviewend-------------------------------





# --------------------- user active inactive S--------------------------------
from .serializer import UserDetailSerializerForGroup

class UserActiveView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializerForGroup
    permission_classes  = [IsAdminUser,]
    filter_fields = ["role_id"]


# ----------------------user inactive E---------------------------------------




# --------------------- User Logout S ------------------------------------

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token_r = RefreshToken(refresh_token)
            token_r.blacklist()

            return JsonResponse({"message":"logout"},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"invalid token"},status=status.HTTP_400_BAD_REQUEST)


# --------------------- User Logout E ------------------------------------
