// **************************************************************************
// AutoRouteGenerator
// **************************************************************************

// GENERATED CODE - DO NOT MODIFY BY HAND

// **************************************************************************
// AutoRouteGenerator
// **************************************************************************
//
// ignore_for_file: type=lint

part of 'app_router.dart';

class _$AppRouter extends RootStackRouter {
  _$AppRouter([GlobalKey<NavigatorState>? navigatorKey]) : super(navigatorKey);

  @override
  final Map<String, PageFactory> pagesMap = {
    AppStackRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const AppStackPage());
    },
    EmptyRouterRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const EmptyRouterPage());
    },
    LoginRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const LoginPage());
    },
    RegisterRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const RegisterPage());
    },
    OTPRegisterRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const OTPRegisterPage());
    },
    PinRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const PinPage());
    },
    RegisterInfoRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const RegisterInfoPage());
    },
    ForgetPasswordRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const ForgetPasswordPage());
    },
    ForgetPinRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const ForgetPinPage());
    },
    HomeRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const HomePage());
    },
    StatementRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const StatementPage());
    },
    StatementInfoRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const StatementInfoPage());
    },
    StatementCreateRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const StatementCreatePage());
    },
    StatementEditRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const StatementEditPage());
    },
    DailyFlowOverviewRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const DailyFlowOverviewPage());
    },
    DailyFlowRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const DailyFlowPage());
    },
    DailyFlowCreateRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const DailyFlowCreatePage());
    },
    SpeechToTextRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const SpeechToTextPage());
    },
    BalanceSheetRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const BalanceSheetPage());
    },
    FinancialGoalRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const FinancialGoalPage());
    },
    NotificationRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const NotificationPage());
    },
    CategoryRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const CategoryPage());
    },
    ArticleReadRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const ArticleReadPage());
    },
    OTPRoute.name: (routeData) {
      final args = routeData.argsAs<OTPRouteArgs>();
      return MaterialPageX<dynamic>(
          routeData: routeData, child: OTPPage(type: args.type, key: args.key));
    },
    UserEditRoute.name: (routeData) {
      return MaterialPageX<dynamic>(
          routeData: routeData, child: const UserEditPage());
    }
  };

  @override
  List<RouteConfig> get routes => [
        RouteConfig(AppStackRoute.name, path: '/login', children: [
          RouteConfig(LoginRoute.name, path: '', parent: AppStackRoute.name),
          RouteConfig(RegisterRoute.name,
              path: 'register-page', parent: AppStackRoute.name),
          RouteConfig(OTPRegisterRoute.name,
              path: 'o-tp-register-page', parent: AppStackRoute.name),
          RouteConfig(PinRoute.name,
              path: 'pin-page', parent: AppStackRoute.name),
          RouteConfig(RegisterInfoRoute.name,
              path: 'register-info-page', parent: AppStackRoute.name),
          RouteConfig(ForgetPasswordRoute.name,
              path: 'forget-password-page', parent: AppStackRoute.name),
          RouteConfig(ForgetPinRoute.name,
              path: 'forget-pin-page', parent: AppStackRoute.name)
        ]),
        RouteConfig(EmptyRouterRoute.name, path: '/', children: [
          RouteConfig(HomeRoute.name, path: '', parent: EmptyRouterRoute.name),
          RouteConfig(StatementRoute.name,
              path: 'statement-page', parent: EmptyRouterRoute.name),
          RouteConfig(StatementInfoRoute.name,
              path: 'statement-info-page', parent: EmptyRouterRoute.name),
          RouteConfig(StatementCreateRoute.name,
              path: 'statement-create-page', parent: EmptyRouterRoute.name),
          RouteConfig(StatementEditRoute.name,
              path: 'statement-edit-page', parent: EmptyRouterRoute.name),
          RouteConfig(DailyFlowOverviewRoute.name,
              path: 'daily-flow-overview-page', parent: EmptyRouterRoute.name),
          RouteConfig(DailyFlowRoute.name,
              path: 'daily-flow-page', parent: EmptyRouterRoute.name),
          RouteConfig(DailyFlowCreateRoute.name,
              path: 'daily-flow-create-page', parent: EmptyRouterRoute.name),
          RouteConfig(SpeechToTextRoute.name,
              path: 'speech-to-text-page', parent: EmptyRouterRoute.name),
          RouteConfig(BalanceSheetRoute.name,
              path: 'balance-sheet-page', parent: EmptyRouterRoute.name),
          RouteConfig(FinancialGoalRoute.name,
              path: 'financial-goal-page', parent: EmptyRouterRoute.name),
          RouteConfig(NotificationRoute.name,
              path: 'notification-page', parent: EmptyRouterRoute.name),
          RouteConfig(CategoryRoute.name,
              path: 'category-page', parent: EmptyRouterRoute.name),
          RouteConfig(ArticleReadRoute.name,
              path: 'article-read-page', parent: EmptyRouterRoute.name),
          RouteConfig(OTPRoute.name,
              path: 'o-tp-page', parent: EmptyRouterRoute.name),
          RouteConfig(UserEditRoute.name,
              path: 'user-edit-page', parent: EmptyRouterRoute.name)
        ])
      ];
}

/// generated route for
/// [AppStackPage]
class AppStackRoute extends PageRouteInfo<void> {
  const AppStackRoute({List<PageRouteInfo>? children})
      : super(AppStackRoute.name, path: '/login', initialChildren: children);

  static const String name = 'AppStackRoute';
}

/// generated route for
/// [EmptyRouterPage]
class EmptyRouterRoute extends PageRouteInfo<void> {
  const EmptyRouterRoute({List<PageRouteInfo>? children})
      : super(EmptyRouterRoute.name, path: '/', initialChildren: children);

  static const String name = 'EmptyRouterRoute';
}

/// generated route for
/// [LoginPage]
class LoginRoute extends PageRouteInfo<void> {
  const LoginRoute() : super(LoginRoute.name, path: '');

  static const String name = 'LoginRoute';
}

/// generated route for
/// [RegisterPage]
class RegisterRoute extends PageRouteInfo<void> {
  const RegisterRoute() : super(RegisterRoute.name, path: 'register-page');

  static const String name = 'RegisterRoute';
}

/// generated route for
/// [OTPRegisterPage]
class OTPRegisterRoute extends PageRouteInfo<void> {
  const OTPRegisterRoute()
      : super(OTPRegisterRoute.name, path: 'o-tp-register-page');

  static const String name = 'OTPRegisterRoute';
}

/// generated route for
/// [PinPage]
class PinRoute extends PageRouteInfo<void> {
  const PinRoute() : super(PinRoute.name, path: 'pin-page');

  static const String name = 'PinRoute';
}

/// generated route for
/// [RegisterInfoPage]
class RegisterInfoRoute extends PageRouteInfo<void> {
  const RegisterInfoRoute()
      : super(RegisterInfoRoute.name, path: 'register-info-page');

  static const String name = 'RegisterInfoRoute';
}

/// generated route for
/// [ForgetPasswordPage]
class ForgetPasswordRoute extends PageRouteInfo<void> {
  const ForgetPasswordRoute()
      : super(ForgetPasswordRoute.name, path: 'forget-password-page');

  static const String name = 'ForgetPasswordRoute';
}

/// generated route for
/// [ForgetPinPage]
class ForgetPinRoute extends PageRouteInfo<void> {
  const ForgetPinRoute() : super(ForgetPinRoute.name, path: 'forget-pin-page');

  static const String name = 'ForgetPinRoute';
}

/// generated route for
/// [HomePage]
class HomeRoute extends PageRouteInfo<void> {
  const HomeRoute() : super(HomeRoute.name, path: '');

  static const String name = 'HomeRoute';
}

/// generated route for
/// [StatementPage]
class StatementRoute extends PageRouteInfo<void> {
  const StatementRoute() : super(StatementRoute.name, path: 'statement-page');

  static const String name = 'StatementRoute';
}

/// generated route for
/// [StatementInfoPage]
class StatementInfoRoute extends PageRouteInfo<void> {
  const StatementInfoRoute()
      : super(StatementInfoRoute.name, path: 'statement-info-page');

  static const String name = 'StatementInfoRoute';
}

/// generated route for
/// [StatementCreatePage]
class StatementCreateRoute extends PageRouteInfo<void> {
  const StatementCreateRoute()
      : super(StatementCreateRoute.name, path: 'statement-create-page');

  static const String name = 'StatementCreateRoute';
}

/// generated route for
/// [StatementEditPage]
class StatementEditRoute extends PageRouteInfo<void> {
  const StatementEditRoute()
      : super(StatementEditRoute.name, path: 'statement-edit-page');

  static const String name = 'StatementEditRoute';
}

/// generated route for
/// [DailyFlowOverviewPage]
class DailyFlowOverviewRoute extends PageRouteInfo<void> {
  const DailyFlowOverviewRoute()
      : super(DailyFlowOverviewRoute.name, path: 'daily-flow-overview-page');

  static const String name = 'DailyFlowOverviewRoute';
}

/// generated route for
/// [DailyFlowPage]
class DailyFlowRoute extends PageRouteInfo<void> {
  const DailyFlowRoute() : super(DailyFlowRoute.name, path: 'daily-flow-page');

  static const String name = 'DailyFlowRoute';
}

/// generated route for
/// [DailyFlowCreatePage]
class DailyFlowCreateRoute extends PageRouteInfo<void> {
  const DailyFlowCreateRoute()
      : super(DailyFlowCreateRoute.name, path: 'daily-flow-create-page');

  static const String name = 'DailyFlowCreateRoute';
}

/// generated route for
/// [SpeechToTextPage]
class SpeechToTextRoute extends PageRouteInfo<void> {
  const SpeechToTextRoute()
      : super(SpeechToTextRoute.name, path: 'speech-to-text-page');

  static const String name = 'SpeechToTextRoute';
}

/// generated route for
/// [BalanceSheetPage]
class BalanceSheetRoute extends PageRouteInfo<void> {
  const BalanceSheetRoute()
      : super(BalanceSheetRoute.name, path: 'balance-sheet-page');

  static const String name = 'BalanceSheetRoute';
}

/// generated route for
/// [FinancialGoalPage]
class FinancialGoalRoute extends PageRouteInfo<void> {
  const FinancialGoalRoute()
      : super(FinancialGoalRoute.name, path: 'financial-goal-page');

  static const String name = 'FinancialGoalRoute';
}

/// generated route for
/// [NotificationPage]
class NotificationRoute extends PageRouteInfo<void> {
  const NotificationRoute()
      : super(NotificationRoute.name, path: 'notification-page');

  static const String name = 'NotificationRoute';
}

/// generated route for
/// [CategoryPage]
class CategoryRoute extends PageRouteInfo<void> {
  const CategoryRoute() : super(CategoryRoute.name, path: 'category-page');

  static const String name = 'CategoryRoute';
}

/// generated route for
/// [ArticleReadPage]
class ArticleReadRoute extends PageRouteInfo<void> {
  const ArticleReadRoute()
      : super(ArticleReadRoute.name, path: 'article-read-page');

  static const String name = 'ArticleReadRoute';
}

/// generated route for
/// [OTPPage]
class OTPRoute extends PageRouteInfo<OTPRouteArgs> {
  OTPRoute({required int type, Key? key})
      : super(OTPRoute.name,
            path: 'o-tp-page', args: OTPRouteArgs(type: type, key: key));

  static const String name = 'OTPRoute';
}

class OTPRouteArgs {
  const OTPRouteArgs({required this.type, this.key});

  final int type;

  final Key? key;

  @override
  String toString() {
    return 'OTPRouteArgs{type: $type, key: $key}';
  }
}

/// generated route for
/// [UserEditPage]
class UserEditRoute extends PageRouteInfo<void> {
  const UserEditRoute() : super(UserEditRoute.name, path: 'user-edit-page');

  static const String name = 'UserEditRoute';
}
