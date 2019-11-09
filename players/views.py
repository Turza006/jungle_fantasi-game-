from .models import Players
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlayersSerializer
# Create your views here.

class PlayersListAPI(APIView):
    def get(self):
        try:
            players = Players.objects.all()
            json = PlayersSerializer(data=players, many=True)
            json.is_valid()
            return Response(json.data, status=status.HTTP_200_OK)
        except BaseException as e:
            return Response({"exception": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PlayersCreateAPI(APIView):

    def post(self, request):

        params = request.data

        _id = params.get('_id', None)
        email = params.get('email', None)
        xp = params.get('xp', None)
        coin = params.get('coin', None)
        image = params.get('image', None)
        name = params.get('name',None)
        playing = params.get('playing',None)
        country = params.get('country',None)

        if _id and email and xp and coin and playing and country:
            players = Players()
            players.id = _id
            players.name = name
            players.email = email
            players.xp = xp
            players.coin= coin
            players.country=country
            players.image=image
            players.save()

            res = {
                'Success': True,
                'UserId': _id
            }
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {
                'Success': False,
                'Reason': 'you are missing some required fields'
            }

            return Response(res, status=status.HTTP_400_BAD_REQUEST)

class DeletePlayersAPI(APIView):

    def post(self, request):
        _id = request.data.get('_id', None)
        if _id is None:
            res = {"Success": False, "Reason": "Id not found, you didn't give any id"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        players = Players.objects.filter(_id=_id).all()
        if players.count() > 0:
            players = players[0]
            players.delete()

        res = {"Success": True}

        return Response(res, status=status.HTTP_200_OK)


class UpdatePlayersAPI(APIView):

    def post(self, request):
        _id = request.data.get('id', None)
        players = Players.objects.filter(id=_id).all()
        if players.count() > 0:
            players = players[0]

            data = request.data
            for key, value in data.items():
                players.__setattr__(key, value)
            players.save()
            res = {"Success": True, "Message": "User Data Updated"}
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {"Success": False, "Reason": "No user found with this id"}
            return Response(res, status=status.HTTP_200_OK)


