import reflex as rx

from buridan_ui.blueprints.dashboards.dashboard_components.employeeTable.main import (
    dashbaordEmployee,
)
from buridan_ui.blueprints.dashboards.dashboard_components.expenseBar.main import (
    dashboardExpensebar,
)
from buridan_ui.blueprints.dashboards.dashboard_components.navBar.main import (
    dashboardNavbar,
)
from buridan_ui.blueprints.dashboards.dashboard_components.sideBar.main import (
    dashboardSidebar,
)
from buridan_ui.blueprints.dashboards.dashboard_components.statBar.main import (
    dashboardStatbar,
)
from buridan_ui.blueprints.dashboards.dashboard_components.trafficBar.main import (
    dashboardTrafficbar,
)

from .style import DashboardAppStyle


def dashboardContentArea() -> rx.Component:
    return rx.vstack(
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
def dashboardApp() -> rx.Component:
    return rx.hstack(
        dashboardSidebar(),
        dashboardContentArea(),
        **DashboardAppStyle.base,
    )
