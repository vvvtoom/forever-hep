from django.shortcuts import render
from .models import Player
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

def admin(request):
    return render(request, 'boardgame/admin.html')


def init_game(request):
    return render(request, 'boardgame/init_game.html')


def edit_player_money(request):
    return render(request, 'boardgame/edit_player_money.html')


def moneyboard(request):
    return render(request, 'boardgame/moneyboard.html')


def add_player(request):
    return render(request, 'boardgame/add_player.html')


def player_view(request, player_name):
    return render(request, 'boardgame/player_view.html', {'player_name': player_name})


# api views
@csrf_exempt
def api_init_game(request):
    if request.method == 'POST':
        # delete all players
        try:
            Player.objects.all().delete()
            # return JSON response
            return JsonResponse({'result': '게임 초기화에 성공했습니다.'}, status=200)
        except:
            return JsonResponse({'result': '게임 초기화에 실패했습니다.'}, status=500)

@csrf_exempt
def api_add_player(request):
    if request.method == 'POST':
        # add player
        try:
            player_name = request.POST['player_name']
            color_code = request.POST['color_code']
            player = Player(name=player_name, color_code=color_code)
            player.save()
            
            return JsonResponse({'result': '플레이어 추가에 성공했습니다.'}, status=200)
        except:
            return JsonResponse({'result': '플레이어 추가에 실패했습니다.'}, status=500)
    
@csrf_exempt
def api_get_players(request):
    if request.method == 'GET':
        # get players
        players = Player.objects.all()
        player_list = []
        for player in players:
            player_list.append({'name': player.name, 'money': player.money, 'color_code': player.color_code})
        return JsonResponse({'players': player_list}, status=200)

@csrf_exempt
def api_send_money(request, from_player, to_player, money):
    if request.method == 'POST':
        # send money
        try:
            from_player = Player.objects.get(name=from_player)
            to_player = Player.objects.get(name=to_player)
            from_player.money -= int(money)
            to_player.money += int(money)
            from_player.save()
            to_player.save()
            
            return JsonResponse({'result': '점수 전송에 성공했습니다.'}, status=200)
        except:
            return JsonResponse({'result': '점수 전송에 실패했습니다.'}, status=500)
    
@csrf_exempt
def api_plus_money(request, player_name, money):
    if request.method == 'POST':
        # plus money
        try:
            player = Player.objects.get(name=player_name)
            player.money += int(money)
            player.save()
            
            return JsonResponse({'result': '점수 추가에 성공했습니다.'}, status=200)
        except:
            return JsonResponse({'result': '점수 추가에 실패했습니다.'}, status=500)
        

@csrf_exempt
def api_minus_money(request, player_name, money):
    if request.method == 'POST':
        # minus money
        try:
            player = Player.objects.get(name=player_name)
            player.money -= int(money)
            player.save()
            
            return JsonResponse({'result': '점수 감소에 성공했습니다.'}, status=200)
        except:
            return JsonResponse({'result': '점수 감소에 실패했습니다.'}, status=500)
    

@csrf_exempt
def api_edit_money(request, player_name, money):
    if request.method == 'POST':
        # edit money
        try:
            player = Player.objects.get(name=player_name)
            player.money = int(money)
            player.save()
            
            return JsonResponse({'result': '점수 수정에 성공했습니다.'}, status=200)
        except:
            return JsonResponse({'result': '점수 수정에 실패했습니다.'}, status=500)