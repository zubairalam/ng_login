# serializers for .model
from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200, blank=False)
    last_name = serializers.CharField(max_length=200, blank=False)
    email = serializers.EmailField(blank=False)
    password = serializers.CharField(max_length=25, blank=False)
    password2 = serializers.CharField(max_length=25, blank=False)

    def restore_object(self, attrs, instance=None):
        print attrs,' aya kuch'
        if instance is not None:
            return None
        if attrs['password'] != attrs['password2']:
            return None
        attrs.pop('password2')
        user = User(first_name=attrs['first_name'],
                    last_name=attrs['last_name'],
                    email=attrs['email'])
        user.set_password(attrs['password'])
        user.save()
        return user


# UserRegistrationForm
#class UserRegistrationSerializer(serializers.ModelSerializer):
#    password2 = serializers.CharField(max_length=25, blank=False)
#
#    class Meta:
#        model = User
#        fields = ('email', 'first_name', 'last_name',
#                  'password', 'password2')
#        # Note: Password field is write-only
#        write_only_fields = ('password',)
#
#    def validate(self, attrs):
#        print attrs, 'validat fun'
#        if attrs['password'] != attrs['password2']:
#            raise serializers.ValidationError('passwords do not match')
#        attrs.pop('password2')
#        return attrs
#
#    def restore_object(self, attrs, instance=None):
#        """
#        Instantiate a new User instance.
#        """
#        print attrs,' aya kuch'
#        if instance is not None:
#            return None
#        attrs.pop('password2')
#        user = User(email=attrs['email'],
#                                first_name=attrs['first_name'],
#                                last_name=attrs['last_name'],
#                                password=attrs['password']
#                                )
#
#        user.save()
#
#        return user
# UserRegistrationForm

# UserRegistrationForm
#class UserRegistrationSerializer(serializers.ModelSerializer):
#    password1 = serializers.CharField(max_length=25, blank=False)
#    password2 = serializers.CharField(max_length=25, blank=False)
#
#    class Meta:
#        model = get_user_model()
#        fields = ('email', 'first_name', 'last_name',
#                  'password1', 'password2', 'password')
#        # Note: Password field is write-only
#        write_only_fields = ('password',)
#
#    def restore_object(self, attrs, instance=None):
#        """
#        Instantiate a new User instance.
#        """
#        print "aya kya"
#        assert instance is None, 'Cannot update registered user'
#
#        assert attrs['password1'] == attrs['password2'], "password doesn't matches"
#
#        user = get_user_model()(email=attrs['email'],
#                                first_name=attrs['first_name'],
#                                last_name=attrs['last_name'],
#                                password=attrs['password1']
#                                )
#
#        user.save()
#        assert False, "you are here"
#
#        return user
# UserRegistrationForm
