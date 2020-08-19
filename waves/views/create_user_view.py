from rest_framework.views import APIView
from waves.use_cases.create_user_use_case import CreateUserUseCase


class CreateUserView(APIView):

    def post(self, request):
        try:
            username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')
            create_user_use_case = CreateUserUseCase(username, email, password)
            return create_user_use_case.run()

        except Exception as exception:
            print(exception)


    def options(self, request, *args, **kwargs):
        pass
