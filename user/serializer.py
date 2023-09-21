from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import User
from django.conf import settings




#--------- userlist---------------------


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'role_id',
            'user_photo',
            'email',
            'pincode',
            'profession',
            'mobile',
        )







class UserDetailSerializerForGroup(serializers.ModelSerializer):

    # user_photo = serializers.SerializerMethodField('get_user_photo')

    # def get_user_photo(self,obj):
    #     return '%s%s'%(settings.MEDIA_URL,obj.user_photo)
    # user_photo = serializers.ImageField(use_url =True,required = False )
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'role_id',
            'user_photo',
            'is_active',
        )

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['user_photo'] = "demo"+str(instance.user_photo)


    #     return response

    
    # def get_serializer_context(self):
    #     return{'request':self.request}

#---------userlistend-------------------









class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'first_name'


        )
    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user





class VerifyUserOtpSerializer(serializers.Serializer):
    email  = serializers.EmailField()
    otp =  serializers.CharField()






class ResendOtpSerializer(serializers.Serializer):
    email  = serializers.EmailField()



class UserLoginSerializer(serializers.Serializer):
    # username = serializers.CharField(max_length=128, write_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role_id = serializers.CharField(read_only=True)
    is_active = serializers.CharField(read_only=True)
    user_photo = serializers.FileField(read_only = True)
    username = serializers.CharField(read_only = True)
    user_notification_token = serializers.CharField(required= False,allow_null= True)


    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        # username = data['username']
        email = data['email']
        password = data['password']
        # print(email)
        # print(password)
        User = authenticate(email= email, password=password)

        if User is None:
            raise serializers.ValidationError("Invalid login")

        try:
            refresh = RefreshToken.for_user(User)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, User)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': User.email,
                # 'id': User.pk
                'role_id':User.role_id,
                'is_active':User.is_active,
                'user_photo':User.user_photo,
                'username':User.username,
                # 'user_notification_token':User.user_notification_token,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")





#------------------------------- Reset Password --------------------------------------------------


class ResetPasswordSerializer(serializers.Serializer):
    email  = serializers.EmailField()
    otp =  serializers.CharField()
    password = serializers.CharField()


#---------------------------  reset password end ------------------------------------------------