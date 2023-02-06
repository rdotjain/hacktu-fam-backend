from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from users import views as user_views
from transactions import views as transaction_views
from rewards import views as reward_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Transactions
    path('api/transact/', transaction_views.MakeTransaction.as_view()),
    path('api/transaction_reward/', reward_views.TransactionReward.as_view()),
    path('api/transactions/', transaction_views.GetTransactions.as_view()),

    # Users
    path('api/leaderboard/', user_views.Leaderboard.as_view()),
    path('api/rewards/', reward_views.GetRewards.as_view()),
    path('api/redeem/', reward_views.RedeemReward.as_view()),

    # Piggy Bank
    path('api/piggy_bank/', transaction_views.GetPiggyBankDeposits.as_view()),
    path('api/withdraw/', transaction_views.WithdrawPiggyBank.as_view()),
    path('api/piggy_balance/', transaction_views.GetPiggyBankBalance.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
