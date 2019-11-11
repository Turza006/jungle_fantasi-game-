# Create your views here.
from .models import Score
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ScoreSerializer,ScoreDetailsSerializer
# Create your views here.

class ScoreListAPI(APIView):
    def get(self,request):
        try:

            _score = Score.objects.all()
            json = ScoreSerializer(data=_score, many=True)
            json.is_valid()
            return Response(json.data, status=status.HTTP_200_OK)
        except BaseException as e:
            return Response({"exception": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ScoreCreateAPI(APIView):

    def post(self, request):


        params = request.data

        _id = params.get('_id', None)
        expair = params.get('expair', None)
        shield_spell_u = params.get('shield_spell_u', None)
        slo_mo_spell_u = params.get('slo_mo_spell_u', None)
        productive_spell_u = params.get('productive_spell_u', None)
        momentum_spell_u = params.get('momentum_spell_u', None)
        healing_spell_u = params.get('healing_spell_u', None)

        one_scene_u = params.get('one_scene_u', None)
        two_scene_u = params.get('two_scene_u', None)
        three_scene_u = params.get('three_scene_un', None)
        four_scene_u = params.get('four_scene_u', None)
        five_scene_u = params.get('five_scene_u', None)
        six_scene_u = params.get('six_scene_u', None)
        seven_scene_u = params.get('seven_scene_u', None)
        eight_scene_u = params.get('eight_scene_u', None)
        nine_scene_u = params.get('nine_scene_u', None)
        ten_scene_u = params.get('ten_scene_u', None)
        one_fruits_u = params.get('one_fruits_u', None)
        two_fruits_u = params.get('two_fruits_u', None)
        three_fruits_u = params.get('three_fruits_u', None)
        four_fruits_u = params.get('four_fruits_u', None)
        five_fruits_u = params.get('five_fruits_u', None)
        six_fruits_u = params.get('six_fruits_u', None)
        seven_fruits_u = params.get('seven_fruits_u', None)
        eight_fruits_u = params.get('eight_fruits_u', None)
        nine_fruits_u = params.get('nine_fruits_u', None)
        ten_fruits_u = params.get('ten_fruits_u', None)
        eleven_fruits_u = params.get('eleven_fruits_u', None)
        twelve_fruits_u = params.get('twelve_fruits_u', None)
        thirteen_fruits_u = params.get('thirteen_fruits_u', None)
        fourteen_fruits_u = params.get('fourteen_fruits_u', None)
        fifteen_fruits_u = params.get('fifteen_fruits_u', None)
        sixteen_fruits_u = params.get('sixteen_fruits_u', None)
        seventeen_fruits_u = params.get('seventeen_fruits_u', None)
        eighteen_fruits_u = params.get('eighteen_fruits_u', None)
        nineteen_fruits_u = params.get('nineteen_fruits_u', None)
        twenty_fruits_u = params.get('twenty_fruits_u', None)
        twentyone_fruits_u = params.get('twentyone_fruits_u', None)
        twentytwo_fruits_u = params.get('twentytwo_fruits_u', None)
        twentythree_fruits_u = params.get('twentythree_fruits_u', None)
        twentyfour_fruits_u = params.get('twentyfour_fruits_u', None)
        twentyfive_fruits_u = params.get('twentyfive_fruits_u', None)
        dead = params.get('dead',None)
        total_fruits = params.get('total_fruits',None)
        fblogin = params.get('fblogin',None)


        if _id:
            score = Score()
            score._id = _id
            score.expair = expair
            score.shield_spell_u = shield_spell_u
            score.slo_mo_spell_u = slo_mo_spell_u
            score.productive_spell_u = productive_spell_u
            score.momentum_spell_u = momentum_spell_u
            score.healing_spell_u = healing_spell_u
            score.one_scene_u = one_scene_u
            score.two_scene_u = two_scene_u
            score.three_scene_u = three_scene_u
            score.four_scene_u = four_scene_u
            score.five_scene_u = five_scene_u
            score.six_scene_u = six_scene_u
            score.seven_scene_u = seven_scene_u
            score.eight_scene_u = eight_scene_u
            score.nine_scene_u = nine_scene_u
            score.ten_scene_u = ten_scene_u
            score.one_fruits_u = one_fruits_u
            score.two_fruits_u = two_fruits_u
            score.three_fruits_u = three_fruits_u
            score.four_fruits_un = four_fruits_u
            score.five_fruits_u = five_fruits_u
            score.six_fruits_u = six_fruits_u
            score.seven_fruits_u = seven_fruits_u
            score.eight_fruits_u = eight_fruits_u
            score.nine_fruits_u = nine_fruits_u
            score.ten_fruits_u = ten_fruits_u
            score.eleven_fruits_u = eleven_fruits_u
            score.twelve_fruits_u = twelve_fruits_u
            score.thirteen_fruits_u = thirteen_fruits_u
            score.fourteen_fruits_u = fourteen_fruits_u
            score.fifteen_fruits_u = fifteen_fruits_u
            score.sixteen_fruits_u = sixteen_fruits_u
            score.seventeen_fruits_u = seventeen_fruits_u
            score.eighteen_fruits_u = eighteen_fruits_u
            score.nineteen_fruits_u = nineteen_fruits_u
            score.twenty_fruits_u = twenty_fruits_u
            score.twentyone_fruits_u = twentyone_fruits_u
            score.twentytwo_fruits_u = twentytwo_fruits_u
            score.twentythree_fruits_u = twentythree_fruits_u
            score.twentyfour_fruits_u = twentyfour_fruits_u
            score.twentyfive_fruits_u = twentyfive_fruits_u
            score.dead = dead
            score.total_fruits = total_fruits
            score.fblogin = fblogin

            score.save()

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

class DeleteScoreAPI(APIView):

    def post(self, request):

        _id = request.data.get('_id', None)
        if _id is None:
            res = {"Success": False, "Reason": "Id not found, you didn't give any id"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        _score = Score.objects.filter(_id=_id).all()
        if _score.count() > 0:
            _score = _score[0]
            _score.delete()

        res = {"Success": True}

        return Response(res, status=status.HTTP_200_OK)


class UpdateScoreAPI(APIView):

    def post(self, request):
        _id = request.data.get('_id', None)
        _score = Score.objects.filter(_id=_id).all()
        if _score.count() > 0:
            _score = _score[0]

            data = request.data
            for key, value in data.items():
                _score.__setattr__(key, value)
            _score.save()
            res = {"Success": True, "Message": "User Data Updated"}
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {"Success": False, "Reason": "No user found with this id"}
            return Response(res, status=status.HTTP_200_OK)
        #

class ScoreDetailsAPI(APIView):

    def post(self, request):
        try:
            score_id = request.data.get('_id', 1)
            score = Score.objects.filter(id=score_id).all()
            json = ScoreDetailsSerializer(data=score, many=True)
            json.is_valid()
            return Response(json.data, status=status.HTTP_200_OK)
        except BaseException as e:
            return Response({"exception": str(e)}, status=status.HTTP_400_BAD_REQUEST)