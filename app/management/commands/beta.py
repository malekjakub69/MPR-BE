from django.core.management.base import BaseCommand
from app.models.user import User
from app.models.project import Project, UserProject
from app.models.risk import Risk, RiskCategory
from app.models.choices import Status, UserProjectRoles, Probability, Impact
from django.contrib.auth.hashers import make_password
from datetime import date


class Command(BaseCommand):
    manager_id = None
    user_id = None
    project_id = None
    password = "Password1"

    # Users
    def _create_admin(self):
        password = make_password(self.password)
        user = User(password=password, name="admin", surname="admin", email="admin@mpr.cz", role="ADMIN")
        user.save()

    def _create_project_manager(self):
        password = make_password(self.password)
        user = User(password=password, name="Jan", surname="Dvořák", email="dvorak@mpr.cz", role="PROJECT_MANAGER")
        user.save()
        self.manager_id = User.objects.latest('id')

    def _create_user(self):
        password = make_password(self.password)
        user = User(password=password, name="Tomáš", surname="Jirásek", email="jirasek@mpr.cz", role="USER")
        user.save()
        self.user_id = User.objects.latest('id')

    # Projects
    def _create_project(self):
        project = Project(
            owner_id=self.manager_id,
            name="Project Risk Manager",
            description="Systém pro podporu řízení rizik v projektech",
            status=Status.ACTIVE,
            scale_risk=True,
            date_begin=date(2023, 2, 20),
            date_end=date(2023, 5, 5)
        )
        self.project_id = project.id
        project.save()
        self.project_id = Project.objects.latest('id')

    def _relate_manager_project(self):
        user_project = UserProject(
            user=self.manager_id,
            project=self.project_id,
            role=UserProjectRoles.MANAGER
        )
        user_project.save()

    # Risks
    def _create_risk_category_1(self):
        risk_cat = RiskCategory(name="Organizační riziko", description="")
        risk_cat.save()

    def _create_risk_1(self):
        cat_id = RiskCategory.objects.all().filter(name="Organizační riziko").first()
        risk = Risk(
            owner=self.user_id,
            category=cat_id,
            project=self.project_id,
            title="Nemoc",
            description="Jedním z nejčastějších rizik v projektovém managementu je nemoc nebo absence členů týmu. Nemoc může ovlivnit schopnost týmu dokončit úkoly včas a v souladu s plánem. Absence jednoho nebo více členů týmu může mít za následek přepracování zbylých členů týmu a zvýšení rizika pro celkovou úspěšnost projektu.",
            danger="Zpoždění projektu, snížení kvality výsledků, zvýšení nákladů na projekt a zvýšení stresu pro zbylé členy týmu.",
            trigger="Neočekávaná a neplánovaná nemoc členů týmu, dovolená, rodinné závazky a další neplánované události, které mohou mít za následek absenci jednoho nebo více členů týmu.",
            reactions="Zahrnutí rizika nemoci nebo absence do plánu projektu, vytvoření plánu náhradního personálu, pravidelná komunikace s členy týmu ohledně jejich zdravotního stavu a plánů na dovolenou, předběžné plánování pro případné zpoždění projektu.",
            probability=Probability.MEDIUM,
            impact=Impact.HIGH,
            status=Status.CLOSED,
            date_identified=date(2023, 3, 3),
            date_updated=date(2023, 3, 4),
            date_reaction=date(2023, 3, 5)
        )
        risk.save()

    """
    def _create_risk_(self):
        user_id = 
        cat_id = 
        risk = Risk(
            owner=user_id,
            category=cat_id,
            project=self.project_id,
            title="",
            description="",
            danger="",
            trigger="",
            reactions="",
            probability=Probability.MEDIUM,
            impact=Impact.MEDIUM,
            status=Status.CLOSED,
            date_identified=date(),
            date_updated=date(),
            date_reaction=date()
        )
        risk.save()
    """

    def handle(self, *args, **options):
        # Users
        self._create_admin()
        self._create_project_manager()
        self._create_user()
        # Project
        self._create_project()
        self._relate_manager_project()
        # Risks
        self._create_risk_category_1()
        self._create_risk_1()