from django.shortcuts import render
from .models import Player
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.

def admin(request):
    return render(request, 'boardgame/admin.html')


def init_game(request):
    return render(request, 'boardgame/init_game.html')


def moneyboard(request):
    return render(request, 'boardgame/moneyboard.html')


def add_player(request):
    return render(request, 'boardgame/add_player.html')


def player_view(request, player_name):
    player = Player.objects.get(name=player_name)
    return render(request, 'boardgame/player_view.html', {'player_name': player_name, 'player_money': player.money, 'player_color_code': player.color_code})


# api views
@csrf_exempt
def api_init_game(request):
    if request.method == 'POST':
        # delete all players
        try:
            Player.objects.all().delete()

            # add players with name '1조', '2조', '3조', '4조', '회계실'
            player1 = Player(name='1조', money=1000, color_code='#F5897A')
            player2 = Player(name='2조', money=1000, color_code='#F5EA7A')
            player3 = Player(name='3조', money=1000, color_code='#65E573')
            player4 = Player(name='4조', money=1000, color_code='#6584E6')
            player5 = Player(name='회계실', color_code='#F5EA7A')

            player1.save()
            player2.save()
            player3.save()
            player4.save()
            player5.save()

            # return JSON response
            return JsonResponse({'result': '게임 초기화에 성공했습니다.', 'success': True }, status=200)
        except:
            return JsonResponse({'result': '게임 초기화에 실패했습니다.', 'success': False }, status=500)

@csrf_exempt
def api_get_my_money(request, player_name):
    if request.method == 'GET':
        # get my money
        player = Player.objects.get(name=player_name)
        return JsonResponse({'money': player.money}, status=200)
    
@csrf_exempt
def api_get_players(request):
    if request.method == 'GET':
        # get players
        players = Player.objects.all().order_by('name')
        player_list = []
        for player in players:
            player_list.append({'name': player.name, 'money': player.money, 'color_code': player.color_code})
        return JsonResponse({'players': player_list}, status=200)

@csrf_exempt
def api_send_money(request):
    if request.method == 'POST':
        # send money
        try:
            data = json.loads(request.body)
            from_player_name = data['from_player_name']
            to_player_name = data['to_player_name']
            money = data['money']
            from_player = Player.objects.get(name=from_player_name)
            to_player = Player.objects.get(name=to_player_name)
            from_player.money -= int(money)
            to_player.money += int(money)
            from_player.save()
            to_player.save()
            
            return JsonResponse({'result': '점수 전송에 성공했습니다.', 'success': True }, status=200)
        except:
            return JsonResponse({'result': '점수 전송에 실패했습니다.', 'success': False }, status=500)
    
@csrf_exempt
def api_add_money(request):
    if request.method == 'POST':
        # plus money
        try:
            data = json.loads(request.body)
            player_name = data['player_name']
            money = data['money']

            player = Player.objects.get(name=player_name)
            player.money += int(money)
            player.save()
            
            return JsonResponse({'result': '해당 조 점수가 추가되었습니다.', 'success': True}, status=200)
        except:
            return JsonResponse({'result': '오류가 발생했습니다.', 'success': False }, status=500)
        

@csrf_exempt
def api_sub_money(request):
    if request.method == 'POST':
        # minus money
        try:
            data = json.loads(request.body)
            player_name = data['player_name']
            money = data['money']

            player = Player.objects.get(name=player_name)
            player.money -= int(money)
            player.save()
            
            return JsonResponse({'result': '해당 조 점수가 감소되었습니다.', 'success': True}, status=200)
        except:
            return JsonResponse({'result': '오류가 발생했습니다.', 'success': False }, status=500)