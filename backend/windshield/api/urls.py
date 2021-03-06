from django.urls import path
from . import views

app_name = 'api'

#all of these paths start with '/api/' already
urlpatterns = [
    path('provinces/', views.Provinces.as_view(), name='provinces'),

    #FINANCIAL STATEMENT PLAN
    path('statement/', views.Statement.as_view(), name='statement'),
    path('statement/<str:pk>/', views.StatementInstance.as_view(), name='statement-instance'),
    path('statement/<str:pk>/name/', views.StatementChangeName.as_view(), name='statement-change-name'),
    path('statement-summary/', views.PastStatementPlans.as_view(), name="statement-summary"),

    #CATEGORY
    path('categories/', views.Categories.as_view(), name='categories-list'),
    path('categories-budgets-flows/', views.CategoryWithBudgetsAndFlows.as_view(), name='categories-with-budgets'),
    path('categories/financial-type/', views.FinancialTypeList.as_view(), name='financial-type-list'),
    path('category/<str:pk>/', views.Category.as_view(), name='category-instance'),
    
    #BALANCE SHEET
    path('balance-sheet/', views.BalanceSheet.as_view(), name='balance-sheet'),
    path('balance-sheet/summary/', views.SummaryBalanceSheet.as_view(), name='balance-sheet-summary'),
    path('balance-sheet-log/', views.BalanceSheetLog.as_view(), name='balance-sheet-log'),
    path('asset/', views.Asset.as_view(), name='asset'),
    path('asset/<str:pk>/', views.AssetInstance.as_view(), name='asset-instance'),
    path('debt/', views.Debt.as_view(), name='debt'),
    path('debt/<str:pk>/', views.DebtInstance.as_view(), name='debt-instance'),

    #BUDGET
    path('budget/', views.Budget.as_view(), name='budget'),
    path('budget/update/', views.BudgetUpdate.as_view(), name='budgets-update'),
    path('budget/delete/', views.BudgetDelete.as_view(), name='budgets-delete'),
    
    #DAILY FLOW SHEET
    path('daily-flow-sheet/', views.DailyFlowSheet.as_view(), name="daily-flow_sheet"),
    path('daily-flow-sheet/list/', views.DailyFlowSheetList.as_view(), name="daily-flow-sheet-list"),
    path('daily-flow-sheet/graph/daily/', views.GraphDailyFlow.as_view(), name='daily-flow_sheet-graph'),
    path('daily-flow-sheet/graph/monthly/', views.GraphMonthlyFlow.as_view(), name='monthly-flow_sheet-graph'),
    path('daily-flow-sheet/graph/annually/', views.GraphAnnuallyFlow.as_view(), name='annually-flow-sheet-graph'),
    path('daily-flow-sheet/average/', views.AverageFlow.as_view(), name='average-flow-sheet'),
    
    #DAILY FLOW
    path('method/', views.Method.as_view(), name='method'),
    path('daily-flow/', views.DailyListFlow.as_view(), name="daily-flow"),
    path('daily-flow/<str:pk>/', views.DailyFlow.as_view(), name="daily-flow-update"),
    
    #FINANCIAL GOAL
    path('financial-goal/', views.FinancialGoals.as_view(), name="financial-goals"),
    path('financial-goal/<str:pk>/', views.FinancialGoalInstance.as_view(), name="financial-goal"),
    
    #FINANCIAL STATUS
    path('financial-status/', views.FinancialStatus.as_view(), name="financial-status"),
    
    #FINANCIAL ARTICLE
    path('articles/', views.Articles.as_view(), name="articles"),
    path('article/<int:pk>/', views.Article.as_view(), name="article"),
    path('article/<int:pk>/read', views.ReadArticle.as_view(), name="article-read"),
    path('article/<int:pk>/like', views.LikeArticle.as_view(), name="article-like"),
    path('article/<int:pk>/unlock', views.UnlockExclusive.as_view(), name="article-unlock"),
    
    #FOR ADMIN
    path('admin/default-categories/', views.DefaultCategories.as_view(), name='default-categories'),
    # path('admin/article/', views.ArticleCreate.as_view(), name="create-article"),
    # path('admin/article/<int:pk>/', views.ArticleUpdate.as_view(), name="update-article")
]