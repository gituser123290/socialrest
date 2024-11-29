from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from api.abstract.models import AbstractModel, AbstractManager
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class UserManager(BaseUserManager,AbstractManager):  # Correctly inherit from BaseUserManager
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            raise Http404("User not found")  # Corrected to raise Http404

    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('Users must have a password.')  # Corrected password check
        user = self.model(username=username,
                          email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        if username is None:
            raise TypeError('Superusers must have a username.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractModel,AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    posts_liked = models.ManyToManyField("api_post.Post",related_name="liked_by")
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    # This links your User model to the custom UserManager
    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


    # def like(self, post):
    #     """Like `post` if it hasn't been done yet"""
    #     return self.posts_liked.add(post)
    # def remove_like(self, post):
    #     """Remove a like from a `post`"""
    #     return self.posts_liked.remove(post)
    # def has_liked(self, post):
    #     """Return True if the user has liked a `post`; else False"""
    #     return self.posts_liked.filter(pk=post.pk).exists()