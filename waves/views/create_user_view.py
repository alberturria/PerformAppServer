from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from waves.use_cases.create_user_use_case import CreateUserUseCase


class CreateUserView(ObtainAuthToken):

    def post(self, request):
        try:
            username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')
            create_user_use_case = CreateUserUseCase(username, email, password)
            return create_user_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)


    def options(self, request, *args, **kwargs):
        pass
