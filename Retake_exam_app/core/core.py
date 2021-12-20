from Retake_exam_app.profiles.models import Profile


def get_user_name():
    user = Profile.objects.first()
    return user.first_name
