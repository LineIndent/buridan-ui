import reflex as rx
from typing import Callable

from .style import DashboardAppStyle

from ..dashboard_components.sideBar.main import dashboardSidebar
from ..dashboard_components.navBar.main import dashboardNavbar
from ..dashboard_components.statBar.main import dashboardStatbar
from ..dashboard_components.trafficBar.main import dashboardTrafficbar
from ..dashboard_components.expenseBar.main import dashboardExpensebar
from ..dashboard_components.employeeTable.main import dashbaordEmployee

dashboardContentArea: Callable[[], rx.Component] = lambda: rx.vstack(
    dashboardNavbar(),
    dashboardStatbar(),
    rx.hstack(
        dashboardTrafficbar(),
        dashboardExpensebar(),
        **DashboardAppStyle.trafficAndExpenses,
    ),
    rx.box(dashbaordEmployee(), width="100%", padding="1em"),
    **DashboardAppStyle.contentArea,
)

# ... Main app function here ...
dashboardApp: Callable[[], rx.Component] = lambda: rx.hstack(
    # ... App side bar ...
    dashboardSidebar(),
    # ... App main content area ...
    dashboardContentArea(),
    # ... App style object ...
    **DashboardAppStyle.base,
)
