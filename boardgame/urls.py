from django.urls import path

from . import views

urlpatterns = [
    path("admin/", views.admin, name='admin'),
    path("init_game/", views.init_game, name='init_game'),
    path("edit_player_money/", views.edit_player_money, name='edit_player_money'),
    path("moneyboard/", views.moneyboard, name='moneyboard'),
    path("add_player/", views.add_player, name='add_player'),
    path("player_view/<str:player_name>/", views.player_view, name='player_view'),

    # api views
    path("api_init_game/", views.api_init_game, name='api_init_game'),
    path("api_add_player/", views.api_add_player, name='api_add_player'),
    path("api_get_players/", views.api_get_players, name='api_get_players'),
    path("api_get_my_money/<str:player_name>/", views.api_get_my_money, name='api_get_my_money'),
    path("api_send_money/", views.api_send_money, name='api_send_money'),
    path("api_plus_money/", views.api_plus_money, name='api_plus_money'),
    path("api_minus_money/", views.api_minus_money, name='api_minus_money'),
    path("api_edit_money/", views.api_edit_money, name='api_edit_money'),
]