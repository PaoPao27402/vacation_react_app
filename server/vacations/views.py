from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .models import Vacation, User
from .serializers import VacationSerializer, UserSerializer
import datetime
from django.db.models import Sum

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_admin:
            login(request, user)
            return Response({"message": "Login successful"})
        return Response({"error": "Invalid credentials"}, status=400)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})

class StatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        past_vacations = Vacation.objects.filter(end_date__lt=datetime.date.today()).count()
        on_going_vacations = Vacation.objects.filter(start_date__lte=datetime.date.today(), end_date__gte=datetime.date.today()).count()
        future_vacations = Vacation.objects.filter(start_date__gt=datetime.date.today()).count()
        total_users = User.objects.count()
        total_likes = Vacation.objects.aggregate(Sum('likes'))['likes__sum'] or 0
        likes_distribution = Vacation.objects.values('destination').annotate(likes=Sum('likes'))

        return Response({
            "past_vacations": past_vacations,
            "on_going_vacations": on_going_vacations,
            "future_vacations": future_vacations,
            "total_users": total_users,
            "total_likes": total_likes,
            "likes_distribution": likes_distribution
        })