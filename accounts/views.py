from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Partner
from .serializers import PartnerSerializer
from .license import IsOwnerProfileOrReadOnly

import logging

class ApiPartner(APIView):
	permission_classes=[IsAuthenticated]

	def post(self, request):
		method = request.data.get('method')

		if method == 'get_me':
			return self.get_me(request)

	def get_me(self, request):
		user = request.user
		logging.error(user)
		if user:
			partner = Partner.objects.filter(id=user.id)
			serializer = PartnerSerializer(partner)
			return Response({"partner": serializer.data})
		return Response({"403"})