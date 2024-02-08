from django.urls import path

from . import views

urlpatterns = [
    path("admin/", views.admin, name='admin'),
    path("init_game/", views.init_game, name='init_game'),
    path("moneyboard/", views.moneyboard, name='moneyboard'),
    path("player_view/<str:player_name>/", views.player_view, name='player_view'),

    # api views
    path("api_init_game/", views.api_init_game, name='api_init_game'),
    path("api_get_players/", views.api_get_players, name='api_get_players'),
    path("api_get_my_money/<str:player_name>/", views.api_get_my_money, name='api_get_my_money'),
    path("api_send_money/", views.api_send_money, name='api_send_money'),
    path("api_add_money/", views.api_add_money, name='api_add_money'),
    path("api_sub_money/", views.api_sub_money, name='api_sub_money'),
]