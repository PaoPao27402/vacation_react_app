# vacations/views.py
from django.http import HttpResponse
from rest_framework import status, generics  # type: ignore
from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.permissions import IsAuthenticated, IsAdminUser # type: ignore
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.utils import timezone
import datetime

from .models import Vacation, User
from .serializers import VacationSerializer, UserSerializer

# Welcome view
class HomeView(APIView):
    def get(self, request):
        return HttpResponse("Welcome to the Vacation Management System")

# Login view for admin users
class LoginView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        # Check if user is admin
        if user is not None and user.is_staff:  
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials or unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

# Logout view for admin users
class LogoutView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

# Comprehensive statistics view
class StatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        past_vacations = Vacation.objects.filter(end_date__lt=timezone.now()).count()
        on_going_vacations = Vacation.objects.filter(
            start_date__lte=timezone.now(), end_date__gte=timezone.now()).count()
        future_vacations = Vacation.objects.filter(start_date__gt=timezone.now()).count()
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

# Count of users
class UserCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_users = User.objects.count()
        return Response({"total_users": total_users})

# Total likes count
class LikesCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_likes = Vacation.objects.aggregate(Sum('likes'))['likes__sum'] or 0
        return Response({"total_likes": total_likes})

# Distribution of likes by destination
class LikesDistributionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        likes_distribution = Vacation.objects.values('destination').annotate(likes=Sum('likes'))
        return Response(likes_distribution)

# Vacation list and creation view
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, delete vacation details
class VacationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
