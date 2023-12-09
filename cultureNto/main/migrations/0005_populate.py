import datetime
from django.db import migrations
from django.db.models import Q


def populate_event_type(apps, schema_editor):
    EventType = apps.get_model("main", "EventType")

    EventType.objects.using(schema_editor.connection.alias).bulk_create(
        [
            EventType(name="Секция"),
            EventType(name="Выставка"),
            EventType(name="Репетиция"),
            EventType(name="Концерт"),
            EventType(name="Спектакль"),
            EventType(name="Лекция"),
        ]
    )


def populate_event(apps, schema_editor):
    EventType = apps.get_model("main", "EventType")
    Event = apps.get_model("main", "Event")

    EV1_DESCRIPTION = \
"""
"Магия Творческого Слияния: Репетиция Симфонии 25.01.2024"

25 января 2024 года приглашаем вас стать свидетелями захватывающего момента творчества на репетиции уникальной симфонии "Магия Творческого Слияния". Этот вечер будет посвящен звуковому слиянию инструментов и голосов, создающих мощный вихрь эмоций и вдохновения.

Великие музыканты сойдутся в этот вечер, чтобы согреть вас звуковыми волнениями и представить уникальное исполнение симфонии, которая звучит как путешествие сквозь пространство и время. Это репетиция, где каждая нота, каждый аккорд — шаг к созданию волшебства, которое охватит вас во время грандиозного выступления.

Присоединитесь к нам в зале репетиций 25 января 2024 года и погрузитесь в атмосферу творческой лаборатории, где искусство и страсть соединяются в единое целое. Это будет неповторимая возможность заглянуть в застенки создания великой симфонии и почувствовать энергию творческого процесса.
"""

    EV2_DESCRIPTION = \
"""
"Гармония Творчества: Искусство в Каждом Жесте"

Откройте двери в мир бескрайнего творчества на нашей захватывающей выставке "Гармония Творчества". Это уникальное мероприятие представит вам широкий спектр художественных произведений, созданных талантливыми художниками, скульпторами и фотографами.

На этой выставке каждая картина, скульптура или фотография - это не просто произведение искусства, а настоящая история, рассказанная визуальным языком. Вы сможете окунуться в мир красок, форм и эмоций, испытывая гармонию и восторг от каждого произведения.

"Гармония Творчества" приглашает вас на увлекательное путешествие по искусству, где каждое произведение станет мостом между разными культурами, стилями и выражениями. Приходите на выставку в наш галерейный пространство 25 числа, чтобы поддаться волшебству творчества и насладиться красотой многообразия художественных форм. Это событие станет вдохновляющим праздником искусства для всех любителей красоты и творчества.
"""
    EV3_DESCRIPTION = \
"""
"Волшебная Ночь Звезд: Театральное Путешествие"

Добро пожаловать на удивительное театральное событие, которое разгадывает тайны ночного неба! Спектакль "Волшебная Ночь Звезд" приглашает вас в захватывающее путешествие по звездному космосу, где каждая звезда рассказывает свою уникальную историю.

Это увлекательное шоу сочетает в себе элементы фэнтези, мистики и волшебства, создавая атмосферу загадочности и великолепия. Артисты, великолепные костюмы и магическая музыкальная аранжировка переносят зрителей в мир, где каждая звезда является символом сновидений, желаний и вдохновения.

Спектакль будет проходить в театре "Звездная Сцена" в этот особенный вечер 19 числа. Приготовьтесь к тому, чтобы пережить невероятные моменты, которые расскажут вам о волшебстве ночного неба и пробудят в вас детскую веру в чудеса. "Волшебная Ночь Звезд" - это не просто представление, это приключение, которое оставит незабываемые впечатления и вдохновит вас на свершения.
"""

    EV4_DESCRIPTION = """Лекция от Савватеева (пример пересекающейся брони перед открытием кружка)"""

    Event.objects.using(schema_editor.connection.alias).bulk_create(
        [
            Event(
                id=5,
                date=datetime.date(2023, 11, 22),
                time=datetime.time(10),
                type_event=EventType.objects.get(name="Репетиция"),
                description=EV1_DESCRIPTION
            ),
            Event(
                id=2,
                date=datetime.date(2023, 11, 25),
                time=datetime.time(13, 30),
                type_event=EventType.objects.get(name="Выставка"),
                description=EV2_DESCRIPTION
            ),
            Event(
                id=1,
                date=datetime.date(2023, 11, 19),
                time=datetime.time(20),
                type_event=EventType.objects.get(name="Спектакль"),
                description=EV3_DESCRIPTION
            ),
            Event(
                date=datetime.date(2023, 11, 15),
                time=datetime.time(12),
                type_event=EventType.objects.get(name="Лекция"),
                description=EV4_DESCRIPTION
            ),
        ]
    )


def populate_room(apps, schema_editor):
    Room = apps.get_model("main", "Room")
    EventLocation = apps.get_model("main", "EventLocation")

    def room(room_id: int, room_name: str, query):
        room_ = Room(id=room_id, name=room_name)
        room_.save()
        room_.locations.set(EventLocation.objects.filter(query))
        return room_

    room(1, "Арт-галерея", Q(name="Арт-галерея (1-й сектор)") | Q(name="Арт-галерея (2-й сектор)"))
    room(2, "Выставочный зал", Q(name="Выставочный зал (1-й сектор)") | Q(name="Выставочный зал (2-й сектор)"))
    room(3, "Школьная сцена", Q(name="Школьная сцена"))
    room(4, "Конференц-зал", Q(name="Конференц-зал"))
    room(5, "Мастерская", Q(name="Мастерская"))
    room(6, "Танцевальный зал", Q(name="Танцевальный зал (1-й сектор)") | Q(name="Танцевальный зал (2-й сектор)"))
    room(7, "Гардероб", Q(name="Гардероб"))
    room(8, "Кафе", Q(name="Кафе"))
    room(9, "Библиотека", Q(name="Библиотека"))
    room(10, "Лекторий", Q(name="Лекторий"))
    room(11, "Комната отдыха для артистов", Q(name="Комната отдыха для артистов"))
    room(12, "Комната звукооператора и светотехника", Q(name="Комната звукооператора и светотехника"))


def populate_worktype(apps, schema_editor):
    WorkType = apps.get_model("main", "WorkType")

    WorkType.objects.using(schema_editor.connection.alias).bulk_create(
        [
            WorkType(id=13, name="Бухгалтер"),
            WorkType(id=14, name="Лектор(Проведение лекций/мастер-классов)"),
            WorkType(id=15, name="Организация культурных событий"),
            WorkType(id=16, name="Разработка концепции мероприятий(декораций, освещения и атмосферы)"),
            WorkType(id=17, name="Звукорежиссер(Настройка и управление звуковым оборудованием)"),
            WorkType(id=18, name="Светотехник(Работа с осветительным оборудованием)"),
            WorkType(id=19, name="Координатор"),
            WorkType(id=20, name="Гардеробщик"),
            WorkType(id=21, name="Менеджер по маркетингу и продвижению"),
            WorkType(id=22, name="Координатор по обслуживанию гостей"),
            WorkType(id=23, name="Секретарь"),
            WorkType(id=24, name="Костюмер")
        ]
    )


def populate_work(apps, schema_editor):
    Work = apps.get_model("main", "Work")

    Work.objects.using(schema_editor.connection.alias).bulk_create(
        [
            Work(
                date=datetime.date(2023, 11, 20),
                time=datetime.time(0, 29),
                description="Создать костюмы для героев",
                status="К выполнению",
                room_id=5,
                work_type_id=13,
                date_end=datetime.date(2023, 11, 22),
                event_id=2,
                time_end=datetime.time(18, 4, 52)
            ),
            Work(
                date=datetime.date(2023, 11, 24),
                time=datetime.time(21, 11, 51),
                description="Принимать вещи у посетителей",
                status="К выполнению",
                room_id=7,
                work_type_id=17,
                date_end=datetime.date(2023, 11, 30),
                event_id=1,
                time_end=datetime.time(21, 11, 53)
            ),
            Work(
                date=datetime.date(2023, 11, 21),
                time=datetime.time(12, 22, 29),
                description="Подготовить документацию о доходах и расходах Культурного центра",
                status="Создана(черновик)",
                room_id=2,
                work_type_id=24,
                date_end=datetime.date(2024, 1, 22),
                event_id=5,
                time_end=datetime.time(12, 0, 0)
            ),
            Work(
                date=datetime.date(2023, 11, 21),
                time=datetime.time(18, 0, 0),
                description="Подготовить рекламный плакат для Выставки",
                status="Создана(черновик)",
                room_id=4,
                work_type_id=16,
                date_end=datetime.date(2023, 12, 25),
                event_id=2,
                time_end=datetime.time(18, 0, 0)
            ),
            Work(
                date=datetime.date(2023, 11, 21),
                time=datetime.time(15, 0, 0),
                description="Настроить освещение для Выставки",
                status="Выполнена",
                room_id=2,
                work_type_id=19,
                date_end=datetime.date(2023, 12, 22),
                event_id=2,
                time_end=datetime.time(13, 30, 0)
            ),
            Work(
                date=datetime.date(2023, 11, 19),
                time=datetime.time(17, 0, 0),
                description="Подготовить план репетиции",
                status="Выполнена",
                room_id=10,
                work_type_id=23,
                date_end=datetime.date(2024, 1, 22),
                event_id=5,
                time_end=datetime.time(14, 20, 0)
            ),
            Work(
                date=datetime.date(2023, 11, 20),
                time=datetime.time(12, 0, 0),
                description="Подготовить картины на выставку \"Достижения Российской Федерации\"",
                status="К выполнению",
                room_id=4,
                work_type_id=22,
                date_end=datetime.date(2023, 11, 24),
                event_id=2,
                time_end=datetime.time(18, 0, 0)
            )
        ]
    )


def generate_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model

    USERNAME = "admin"
    PASSWORD = "admin"
    EMAIL = None

    user = get_user_model()

    if not user.objects.filter(username=USERNAME, email=EMAIL).exists():
        admin = user.objects.create_superuser(
           username=USERNAME, password=PASSWORD, email=EMAIL
        )
        admin.save()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_populate_locations"),
    ]

    operations = [
        migrations.RunPython(populate_event_type),
        migrations.RunPython(populate_event),
        migrations.RunPython(populate_room),
        migrations.RunPython(populate_worktype),
        migrations.RunPython(populate_work),
        migrations.RunPython(generate_superuser)
    ]
