from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from . import models
from user.models import Province, NewUser
from user.serializers import ProvinceSerializer
from rest_framework.filters import OrderingFilter
from datetime import datetime
from pytz import timezone
from django.db.models import Q, Prefetch

DEFUALT_CAT = [
            ('เงินเดือน', 1, 'briefcase'),
            ('ค่าจ้าง', 1, 'hand-holding-usd'),
            ('ค่าล่วงเวลา', 1, 'business-time'),
            ('โบนัส', 1, 'briefcase'),
            ('ค่าคอมมิชชั่น', 1, 'comment-dollar'),
            ('กำไรจากธุรกิจ', 1, 'dollar-sign'),
            ('ดอกเบี้ย', 2, 'percentage'),
            ('เงินปันผล', 2, 'chart-line'),
            ('ค่าเช่า', 2, 'building'),
            ('ขายสินทรัพย์', 2, 'hand-holding-usd'),
            ('เงินรางวัล', 3, 'trophy'),
            ('ค่าเลี้ยงดู', 3, 'hand-holding-usd'),
            ('อาหาร/เครื่่องดื่ม', 4, 'utensils'),
            ('ภายในครัวเรือน', 4, 'house-user'),
            ('ความบันเทิง/ความสุขส่วนบุคคล', 4, 'music'),
            ('สาธารณูปโภค', 4, 'bolt'),
            ('ดูแลตัวเอง', 4, 'heart'),
            ('ค่าเดินทาง', 4, 'route'),
            ('รักษาพยาบาล', 4, 'hand-holding-medical'),
            ('ดูแลบุพการี', 4, 'user-friends'),
            ('ดูแลบุตร', 4, 'baby'),
            ('ภาษี', 4, 'donate'),
            ('ชำระหนี้', 4, 'hand-holding-usd'),
            ('เสี่ยงดวง', 4, 'dice'),
            ('กิจกรรมทางศาสนา ', 4, 'praying-hands'),
            ('เช่าบ้าน', 5, 'home'),
            ('หนี้ กยศ. กองทุน กยศ.', 5, 'graduation-cap'),
            ('ผ่อนรถ', 5, 'car'),
            ('ผ่อนสินค้า', 5, 'shopping-cart'),
            ('ผ่อนหนี้นอกระบบ', 5, 'comments-dollar'),
            ('ผ่อนสินเชื่อส่วนบุคคล', 5, 'comments-dollar'),
            ('ผ่อนหนี้สหกรณ์', 5, 'comments-dollar'),
            ('เบี้ยประกัน', 5, 'file-contract'),
            ('ประกันสังคม', 6, 'building'),
            ('กองทุนสำรองเลี้ยงชีพ', 6, 'coins'),
            ('กอนทุน กบข.', 6, 'coins'),
            ('สหกรณ์ออมทรัพย์', 6, 'comments-dollar'),
            ('เงินออม', 6, 'piggy-bank'),
            ('เงินลงทุน', 6, 'chart-line')
            ]

class Provinces(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class FinancialTypeList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.FinancialTypeSerializer
    
    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        queryset = models.FinancialType.objects.all()
        domain = self.request.query_params.get("domain", None)
        if domain is not None:
            queryset = queryset.filter(domain=domain)
        cat = models.Category.objects.filter(user_id=uuid, isDeleted=False)
        queryset = queryset.prefetch_related(
            Prefetch('categories', queryset=cat)
        )
        return queryset
    

class DailyFlow(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.DailyFlowSerializer
    queryset = models.DailyFlow.objects.all()
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        data = serializer.data
        self.object.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)

class DailyListFlow(generics.ListCreateAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.DailyFlowSerializer
    
    def get_queryset(self):
        self.serializer_class = serializers.DailyFlowSerializer
        uuid = self.request.user.uuid
        if uuid is not None:
            dfsheet = self.request.query_params.get("df_id", None)
            if dfsheet is not None:
                queryset = models.DailyFlow.objects.filter(df_id=dfsheet)
            else:
                date = datetime.now(tz= timezone('Asia/Bangkok'))
                dfsheet = models.DailyFlowSheet.objects.get(owner_id = uuid, date=date)
                queryset = models.DailyFlow.objects.filter(df_id=dfsheet.id)
            return queryset
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, message='uuid not found')
    
    def create(self, request):
        self.serializer_class = serializers.DailyFlowCreateSerializer
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        n = len(request.data)
        if not isinstance(request.data, list): 
            df_id = request.data["df_id"]
            n = 1
        else: 
            df_id = request.data[0]["df_id"]
        results = models.DailyFlow.objects.filter(df_id=df_id)
        output_serializer = serializers.DailyFlowSerializer(results, many=True)
        data = output_serializer.data[-n:]
        return Response(data)    

class DailyFlowSheet(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.DailyFlowSheetSerializer
    
    def get_object(self):
        self.serializer_class = serializers.DailyFlowSheetSerializer
        uuid = self.request.user.uuid
        if uuid is not None:
            date = self.request.query_params.get("date", None)
            if date is None:
                date = datetime.now(tz= timezone('Asia/Bangkok'))
            try:
                dfsheet = models.DailyFlowSheet.objects.get(owner_id = uuid, date=date)
            except models.DailyFlowSheet.DoesNotExist:
                self.serializer_class = serializers.DailyFlowSheetCreateSerializer
                owner = models.NewUser.objects.get(uuid=uuid)
                dfsheet = models.DailyFlowSheet.objects.create(owner_id = owner, date=date)
        return dfsheet

class DailyFlowSheetList(generics.ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.DailyFlowSheetSerializer
    
    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is not None:
            queryset = models.DailyFlowSheet.objects.filter(owner_id = uuid)
            start = self.request.query_params.get("start", None)
            if start is not None:
                start = datetime.strptime(start, "%Y-%m-%d")
                queryset = queryset.filter(date__gte=start)
            end = self.request.query_params.get("end", None)
            if end is not None:
                end = datetime.strptime(end, "%Y-%m-%d")
                queryset = queryset.filter(date__lte=end)
            return queryset
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, message='uuid not found')

class Method(generics.ListCreateAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.MethodSerializer
    
    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is not None:
            queryset = models.Method.objects.filter(Q(user_id=uuid) | Q(user_id=None))
            return queryset
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, message='uuid not found')
        
    def perform_create(self, serializer):
        uuid = self.request.user.uuid
        if uuid is not None:
            owner_instance = NewUser.objects.get(uuid=uuid)
            serializer.save(user_id=owner_instance, **self.request.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, message='uuid not found')
          
class Statement(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.StatementSerializer
    filter_backends = [OrderingFilter]
    # queryset = models.FinancialStatementPlan.objects.all()

    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is not None:
            queryset = models.FinancialStatementPlan.objects.filter(owner_id=uuid)
            lower = self.request.query_params.get("lower-date", None)
            upper = self.request.query_params.get("upper-date", None)
            date = self.request.query_params.get("date", None)
            if lower is not None:
                lower = datetime.strptime(lower, "%Y-%m-%d")
                queryset = queryset.filter(end__gte=lower)
            if upper is not None:
                upper = datetime.strptime(upper, "%Y-%m-%d")
                queryset = queryset.filter(start__lte=upper)
            if date is not None:
                date = datetime.strptime(date, "%Y-%m-%d")
                queryset = queryset.filter(start__lte=date, end__gte=date)
            queryset = queryset.prefetch_related(
                Prefetch('budgets', queryset=models.Budget.objects.filter(cat_id__isDeleted=False))
            )
            return queryset
        else :
            return Response(status=status.HTTP_401_UNAUTHORIZED, message='uuid not found')
    
    def __date_validation__(self, queryset, start, end):
        if isinstance(start, str): start = datetime.strptime(start, "%Y-%m-%d")
        if isinstance(end, str): end = datetime.strptime(end, "%Y-%m-%d")
        if start >= end: return False
        tmp = queryset.filter(start__lt=start, end__gt=start)
        if tmp.count() > 0: return False
        tmp = queryset.filter(start__lt=end, end__gt=end)
        if tmp.count() > 0: return False
        tmp = queryset.filter(start__gt=start, end__lt=end)
        if tmp.count() > 0: return False
        return True
    
    def perform_create(self, serializer):
        uuid = self.request.user.uuid
        if uuid is not None:
            startDate = self.request.data['start']
            endDate = self.request.data['end']
            month = str(self.request.data.pop("month"))
            month_instance = models.Month.objects.get(id=month)
            owner_instance = NewUser.objects.get(uuid=uuid)
            # -yymmdd-id
            queryset = models.FinancialStatementPlan.objects.filter(owner_id=uuid)
            if not self.__date_validation__(queryset, startDate, endDate):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            plans = queryset.filter(start=startDate, end=endDate)
            if(plans.filter(chosen=True).count() > 0):
                self.request.data['chosen'] = False
            else:
                self.request.data['chosen'] = True
            last_plan = plans.last()
            if last_plan is None : plan_id = 0
            else: 
                plan_id = int(last_plan.id[-1:]) + 1
            return serializer.save(
                id = 'FSP' + str(uuid)[:10] + '-' + str(startDate)[2:4] + str(startDate)[5:7] + str(startDate)[-2:] + '-' + str(plan_id)[-1:],
                owner_id = owner_instance,
                month = month_instance,
                **self.request.data
            )
        else :
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class StatementChangeName(generics.UpdateAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.StatementUpdateSerializer
    
    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is not None:
            self.queryset = models.FinancialStatementPlan.objects.filter(owner_id=uuid)
            return self.queryset
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class StatementInstance(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.StatementUpdateSerializer
    
    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is not None:
            self.queryset = models.FinancialStatementPlan.objects.filter(owner_id=uuid)
            return self.queryset
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        active_instance = self.get_object()
        queryset = self.get_queryset().filter(start=active_instance.start, end=active_instance.end)
        instance = []
        for obj in queryset:
            if obj.id == kwargs["pk"]:
                obj.chosen = True
            else:
                obj.chosen = False
            obj.save()
            instance.append(obj)
        serializer = self.get_serializer(instance, many=True, partial=partial)
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object)
        if self.object.chosen:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(self.object)
        data = serializer.data
        self.object.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)

class Asset(generics.ListCreateAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AssetsSerializer
    
    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        bsheet = models.BalanceSheet.objects.get(owner_id=uuid)
        queryset = models.Asset.objects.filter(bsheet_id=bsheet.id, cat_id__isDeleted=False)
        return queryset
    
    def perform_create(self, serializer):
        serializer = serializers.AssetSerializer
        uuid = self.request.user.uuid
        if uuid is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        cat_id = self.request.data.pop("cat_id", None)
        bsheet = models.BalanceSheet.objects.get(owner_id=uuid)
        try:
            cat = models.Category.objects.get(id=cat_id)
        except models.Category.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return models.Asset.objects.create(
                        bsheet_id = bsheet,
                        cat_id = cat,
                        **self.request.data
                        )

class AssetInstance(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AssetSerializer
    queryset = models.Asset.objects.all()
    
    def get_object(self):
        try:
            self.serializer_class = serializers.AssetsSerializer
            return models.Asset.objects.get(id=self.kwargs['pk'])
        except models.Asset.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST

class Debt(generics.ListCreateAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.DebtsSerializer

    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        bsheet = models.BalanceSheet.objects.get(owner_id=uuid)
        queryset = models.Debt.objects.filter(bsheet_id=bsheet.id, cat_id__isDeleted=False)
        return queryset
    
    def perform_create(self, serializer):
        serializer = serializers.DebtSerializer
        uuid = self.request.user.uuid
        if uuid is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        cat_id = self.request.data.pop("cat_id", None)
        bsheet = models.BalanceSheet.objects.get(owner_id=uuid)
        try:
            cat = models.Category.objects.get(id=cat_id)
        except models.Category.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return models.Debt.objects.create(
                        bsheet_id = bsheet,
                        cat_id = cat,
                        **self.request.data
                        )

class DebtInstance(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.DebtSerializer
    queryset = models.Debt.objects.all()
    
    def get_object(self):
        try:
            self.serializer_class = serializers.DebtsSerializer
            return models.Debt.objects.get(id=self.kwargs['pk'])
        except models.Debt.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST
    
class BalanceSheet(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.BalanceSheetSerializer
    
    def get_object(self):
        uuid = self.request.user.uuid
        if uuid is not None:
            try:
                assets = models.Asset.objects.filter(cat_id__isDeleted=False)
                debts = models.Debt.objects.filter(cat_id__isDeleted=False)
                bsheet = models.BalanceSheet.objects.prefetch_related(
                    Prefetch('assets', queryset=assets),
                    Prefetch('debts', queryset=debts)
                ).get(owner_id = uuid)
            except models.BalanceSheet.DoesNotExist:
                owner = models.NewUser.objects.get(uuid=uuid)
                bsheet = models.BalanceSheet.objects.create(id = "BSH" + str(uuid)[:10],
                                                   owner_id = owner)
        return bsheet

class CategoryWithBudgetsAndFlows(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CategoryWithBudgetAndFlowsSerializer
    
    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            queryset = models.Category.objects.filter(user_id=uuid)
            date = self.request.query_params.get('date', None)
            if date is None:
                date = datetime.now(tz= timezone('Asia/Bangkok'))
            try:
                fplan = models.FinancialStatementPlan.objects.get(chosen=True, start__lte=date, end__gte=date)
                fplan_id = fplan.id
            except models.FinancialStatementPlan.DoesNotExist:
                fplan_id = None
            budgets = models.Budget.objects.filter(fplan=fplan_id)
            try:
                dfsheet = models.DailyFlowSheet.objects.get(date=date)
                df_id = dfsheet.id
            except models.DailyFlowSheet.DoesNotExist:
                df_id = None
            flows = models.DailyFlow.objects.filter(df_id=df_id)
            queryset = queryset.prefetch_related(
                Prefetch('budgets', queryset=budgets)
            )
            queryset = queryset.prefetch_related(
                Prefetch('flows', queryset=flows)
            )
            return queryset
    

class DefaultCategories(generics.ListCreateAPIView):
    permissions_classes = [permissions.IsAdminUser]
    serializer_class = serializers.DefaultCategoriesSerializer
    queryset = models.DefaultCategory.objects.all()

class Category(generics.RetrieveUpdateAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CategorySerializer
    
    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is not None: 
            queryset = models.Category.objects.filter(user_id=uuid)
            return queryset
        else :
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class Categories(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is not None: 
            queryset = models.Category.objects.filter(user_id=uuid).order_by("used_count")
            if not queryset:
                owner = models.NewUser.objects.get(uuid=uuid)
                default_cat = models.DefaultCategory.objects.all()
                for cat in default_cat:
                    models.Category.objects.create(name=cat.name, ftype=cat.ftype, user_id=owner, icon=cat.icon)
                queryset = models.Category.objects.filter(user_id=uuid).order_by("used_count")
            return queryset
        else :
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def perform_create(self, serializer):
        uuid = self.request.user.uuid
        if uuid is not None:
            owner = NewUser.objects.get(uuid=uuid)
            ftype = str(self.request.data.pop("ftype"))
            ftype_instance = models.FinancialType.objects.get(id=ftype)
            return serializer.save( 
                            user_id = owner,
                            ftype = ftype_instance,
                            **self.request.data
                            )
        else :
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
class Budget(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        self.serializer_class = serializers.BudgetCategorySerializer
        fplan = self.request.query_params.get("fplan", None)
        fplan_queryset = models.FinancialStatementPlan.objects.filter(owner_id=self.request.user.uuid)
        if fplan is None:
            now = datetime.now(tz= timezone('Asia/Bangkok'))
            fplan_instance = fplan_queryset.get(start__lte=now, end__gte=now, chosen=True)
        else: 
            fplan_instance = fplan_queryset.get(id=fplan)
        queryset = models.Budget.objects.filter(fplan=fplan_instance, cat_id__isDeleted=False)
        return queryset
    
    def create(self, request):
        self.serializer_class = serializers.BudgetSerializer
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        n = len(request.data)
        if not isinstance(request.data, list): 
            fplan = request.data["fplan"]
            n = 1
        else: 
            fplan = request.data[0]["fplan"]
        results = models.Budget.objects.filter(fplan=fplan)
        output_serializer = serializers.BudgetCategorySerializer(results, many=True)
        data = output_serializer.data[-n:]
        return Response(data)
    
class BudgetUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.BudgetUpdateSerializer
    queryset = models.Budget.objects.all()
    
    def get_object(self, obj_id):
        try:
            return models.Budget.objects.get(id=obj_id)
        except models.Budget.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST
    
    def validate_ids(self, id_list):
        for id in id_list:
            try:
                models.Budget.objects.get(id=id)
            except models.Budget.DoesNotExist:
                raise status.HTTP_400_BAD_REQUEST
        return True
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        if isinstance(request.data, list):
            budget_ids = [i['id'] for i in request.data]
            self.validate_ids(budget_ids)
            result = []
            for obj in request.data:
                budget_id = obj['id']
                inst = self.get_object(budget_id)
                inst.budget_per_period = obj['budget_per_period']
                inst.frequency = obj['frequency']
                inst.save()
                result.append(inst)
        else:
            result = self.get_object(request.data['id'])
            result.budget_per_period = request.data['budget_per_period']
            result.frequency = request.data['frequency']
            result.save()
        serializer = serializers.BudgetCategorySerializer(result, many=isinstance(request.data, list), partial=partial)
        return Response(serializer.data)
    
class BudgetDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.BudgetDeleteSerializer
    queryset = models.Budget.objects.all()
    
    def delete(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            targets = models.Budget.objects.filter(id__in=request.data)
            result = targets.delete()
            return Response(result[0], status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class FinancialGoalInstance(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.FinancialGoalsSerializer
    
    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        queryset = models.FinancialGoal.objects.filter(user_id=uuid)
        return queryset
    
class FinancialGoals(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.FinancialGoalsSerializer
    
    def get_queryset(self):
        uuid = self.request.user.uuid
        if uuid is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        queryset = models.FinancialGoal.objects.filter(user_id=uuid)
        return queryset
    
    def perform_create(self, serializer):
        uuid = self.request.user.uuid
        if uuid is not None:
            owner = NewUser.objects.get(uuid=uuid)
            return serializer.save( 
                            user_id = owner,
                            **self.request.data
                            )
        else :
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    