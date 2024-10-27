# vacations/views.py
from django.http import HttpResponse
from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from django.contrib.auth import authenticate, login, logout
from .models import Vacation, User
from .serializers import VacationSerializer, UserSerializer
import datetime
from django.db.models import Sum
from rest_framework import generics   # type: ignore

print("Importing serializers...")
from .serializers import VacationSerializer, UserSerializer
print("Serializers imported successfully.")

class HomeView(APIView):
    def get(self, request):
        return HttpResponse("Welcome to the Vacation Management System")

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

class UserCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_users = User.objects.count()
        return Response({"total_users": total_users})

class LikesCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_likes = Vacation.objects.aggregate(Sum('likes'))['likes__sum'] or 0
        return Response({"total_likes": total_likes})

class LikesDistributionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        likes_distribution = Vacation.objects.values('destination').annotate(likes=Sum('likes'))
        return Response(likes_distribution)

class VacationListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        vacations = Vacation.objects.all()
        serializer = VacationSerializer(vacations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Add VacationDetailView here
class VacationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
