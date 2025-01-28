from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """Manager for custom user model."""

    def create_user(self, email, first_name, last_name, role, password=None, **extra_fields):
        """Create and return a user with the given email and password."""
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        extra_fields.pop("role", None)  # Remove 'role' from extra_fields if it exists
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,  # Explicitly set the role
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # Call create_user with role explicitly set to 'Manager'
        return self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role="Manager",  # Explicitly set the role
            password=password,
            **extra_fields
        )
