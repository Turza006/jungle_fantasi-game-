from .models import Players
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlayersSerializer,PlayersDetailsSerializer
# Create your views here.

class PlayersListAPI(APIView):
    def get(self,request):
        try:

            _players = Players.objects.all()
            json = PlayersSerializer(data=_players, many=True)
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
        dimond = params.get('dimond',None)
        shield_spell = params.get('shield_spell',None)
        slo_mo_spell= params.get('slo_mo_spell',None)
        productive_spell= params.get('productive_spell',None)
        momentum_spell = params.get('momentum_spell',None)
        healing_spell = params.get('healing_spell',None)

        one_scene_un = params.get('one_scene_un',None)
        two_scene_un = params.get('two_scene_un',None)
        three_scene_un = params.get('three_scene_un',None)
        four_scene_un = params.get('four_scene_un',None)
        five_scene_un = params.get('five_scene_un',None)
        six_scene_un = params.get('six_scene_un',None)
        seven_scene_un = params.get('seven_scene_un',None)
        eight_scene_un = params.get('eight_scene_un',None)
        nine_scene_un = params.get('nine_scene_un',None)
        ten_scene_un = params.get('ten_scene_un',None)
        one_fruits_un = params.get('one_fruits_un',None)
        two_fruits_un = params.get('two_fruits_un',None)
        three_fruits_un = params.get('three_fruits_un',None)
        four_fruits_un = params.get('four_fruits_un',None)
        five_fruits_un = params.get('five_fruits_un',None)
        six_fruits_un = params.get('six_fruits_un',None)
        seven_fruits_un = params.get('seven_fruits_un',None)
        eight_fruits_un = params.get('eight_fruits_un',None)
        nine_fruits_un = params.get('nine_fruits_un',None)
        ten_fruits_un = params.get('ten_fruits_un',None)
        eleven_fruits_un = params.get('eleven_fruits_un',None)
        twelve_fruits_un = params.get('twelve_fruits_un',None)
        thirteen_fruits_un = params.get('thirteen_fruits_un',None)
        fourteen_fruits_un = params.get('fourteen_fruits_un',None)
        fifteen_fruits_un = params.get('fifteen_fruits_un',None)
        sixteen_fruits_un = params.get('sixteen_fruits_un',None)
        seventeen_fruits_un = params.get('seventeen_fruits_un',None)
        eighteen_fruits_un = params.get('eighteen_fruits_un',None)
        nineteen_fruits_un = params.get('nineteen_fruits_un',None)
        twenty_fruits_un = params.get('twenty_fruits_un',None)
        twentyone_fruits_un = params.get('twentyone_fruits_un',None)
        twentytwo_fruits_un = params.get('twentytwo_fruits_un',None)
        twentythree_fruits_un = params.get('twentythree_fruits_un',None)
        twentyfour_fruits_un = params.get('twentyfour_fruits_un',None)
        twentyfive_fruits_un = params.get('twentyfive_fruits_un',None)


        if _id and email and country:
            players = Players()
            players._id = _id
            players.name = name
            players.email = email
            Players.playing = playing
            players.xp = xp
            players.coin= coin
            players.country=country
            players.image=image
            players.dimond = dimond
            players.shield_spell = shield_spell
            players.slo_mo_spell = slo_mo_spell
            players.productive_spell = productive_spell
            players.momentum_spell=momentum_spell
            players.healing_spell = healing_spell
            players.one_scene_un = one_scene_un
            players.two_scene_un = two_scene_un
            players.three_scene_un = three_scene_un
            players.four_scene_un = four_scene_un
            players.five_scene_un = five_scene_un
            players.six_scene_un = six_scene_un
            players.seven_scene_un = seven_scene_un
            players.eight_scene_un = eight_scene_un
            players.nine_scene_un = nine_scene_un
            players.ten_scene_un = ten_scene_un
            players.one_fruits_un = one_fruits_un
            players.two_fruits_un = two_fruits_un
            players.three_fruits_un = three_fruits_un
            players.four_fruits_un = four_fruits_un
            players.five_fruits_un = five_fruits_un
            players.six_fruits_un = six_fruits_un
            players.seven_fruits_un = seven_fruits_un
            players.eight_fruits_un = eight_fruits_un
            players.nine_fruits_un = nine_fruits_un
            players.ten_fruits_un = ten_fruits_un
            players.eleven_fruits_un = eleven_fruits_un
            players.twelve_fruits_un = twelve_fruits_un
            players.thirteen_fruits_un = thirteen_fruits_un
            players.fourteen_fruits_un = fourteen_fruits_un
            players.fifteen_fruits_un = fifteen_fruits_un
            players.sixteen_fruits_un = sixteen_fruits_un
            players.seventeen_fruits_un = seventeen_fruits_un
            players.eighteen_fruits_un = eighteen_fruits_un
            players.nineteen_fruits_un = nineteen_fruits_un
            players.twenty_fruits_un = twenty_fruits_un
            players.twentyone_fruits_un = twentyone_fruits_un
            players.twentytwo_fruits_un = twentytwo_fruits_un
            players.twentythree_fruits_un = twentythree_fruits_un
            players.twentyfour_fruits_un = twentyfour_fruits_un
            players.twentyfive_fruits_un = twentyfive_fruits_un

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
        pass

        _id = request.data.get('id', None)
        _players = Players.objects.filter(_id=_id).all()
        if _players.count() > 0:
            _players = _players[0]

            data = request.data
            for key, value in data.items():
                _players.__setattr__(key, value)
            _players.save()
            res = {"Success": True, "Message": "User Data Updated"}
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {"Success": False, "Reason": "No user found with this id"}
            return Response(res, status=status.HTTP_200_OK)

class PlayersDetailsAPI(APIView):

    def post(self, request):
        try:
            players_id = request.data.get('_id', 1)
            players = Players.objects.filter(_id=players_id).all()
            json = PlayersDetailsSerializer(data=players, many=True)
            json.is_valid()
            return Response(json.data, status=status.HTTP_200_OK)
        except BaseException as e:
            return Response({"exception": str(e)}, status=status.HTTP_400_BAD_REQUEST)
