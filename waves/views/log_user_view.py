from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.log_user_use_case import LogUserUseCase


class LogUserView(ObtainAuthToken):

    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            log_user_use_case = LogUserUseCase(email, password)
            return log_user_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=403)
