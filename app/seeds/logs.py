from app.models import db, Log


def seed_logs():
    seedArray = []

    seedArray.append(Log(person_logged=48, timestamp=4196940))
    seedArray.append(Log(person_logged=74, timestamp=2555623))
    seedArray.append(Log(person_logged=54, timestamp=73476))
    seedArray.append(Log(person_logged=5, timestamp=4998189))
    seedArray.append(Log(person_logged=55, timestamp=6701139))
    seedArray.append(Log(person_logged=29, timestamp=6642888))
    seedArray.append(Log(person_logged=7, timestamp=6073780))
    seedArray.append(Log(person_logged=28, timestamp=1344435))
    seedArray.append(Log(person_logged=9, timestamp=3442738))
    seedArray.append(Log(person_logged=74, timestamp=5228847))
    seedArray.append(Log(person_logged=52, timestamp=4432390))
    seedArray.append(Log(person_logged=70, timestamp=1635663))
    seedArray.append(Log(person_logged=73, timestamp=398367))
    seedArray.append(Log(person_logged=59, timestamp=533393))
    seedArray.append(Log(person_logged=62, timestamp=6814139))
    seedArray.append(Log(person_logged=10, timestamp=6203193))
    seedArray.append(Log(person_logged=56, timestamp=819168))
    seedArray.append(Log(person_logged=38, timestamp=2643668))
    seedArray.append(Log(person_logged=3, timestamp=692849))
    seedArray.append(Log(person_logged=25, timestamp=3875043))
    seedArray.append(Log(person_logged=70, timestamp=4338293))
    seedArray.append(Log(person_logged=35, timestamp=509041))
    seedArray.append(Log(person_logged=40, timestamp=994087))
    seedArray.append(Log(person_logged=38, timestamp=5154517))
    seedArray.append(Log(person_logged=46, timestamp=2532254))
    seedArray.append(Log(person_logged=43, timestamp=3663764))
    seedArray.append(Log(person_logged=44, timestamp=52081))
    seedArray.append(Log(person_logged=68, timestamp=3980373))
    seedArray.append(Log(person_logged=72, timestamp=3195110))
    seedArray.append(Log(person_logged=15, timestamp=5227169))
    seedArray.append(Log(person_logged=5, timestamp=6225692))
    seedArray.append(Log(person_logged=42, timestamp=1875117))
    seedArray.append(Log(person_logged=51, timestamp=1748217))
    seedArray.append(Log(person_logged=13, timestamp=1978944))
    seedArray.append(Log(person_logged=40, timestamp=479905))
    seedArray.append(Log(person_logged=73, timestamp=2113930))
    seedArray.append(Log(person_logged=16, timestamp=2421904))
    seedArray.append(Log(person_logged=3, timestamp=2660010))
    seedArray.append(Log(person_logged=10, timestamp=1206788))
    seedArray.append(Log(person_logged=8, timestamp=6429725))
    seedArray.append(Log(person_logged=1, timestamp=2193179))
    seedArray.append(Log(person_logged=5, timestamp=1950462))
    seedArray.append(Log(person_logged=45, timestamp=4754778))
    seedArray.append(Log(person_logged=11, timestamp=38558))
    seedArray.append(Log(person_logged=49, timestamp=6465724))
    seedArray.append(Log(person_logged=43, timestamp=1628300))
    seedArray.append(Log(person_logged=32, timestamp=4435278))
    seedArray.append(Log(person_logged=3, timestamp=5000458))
    seedArray.append(Log(person_logged=60, timestamp=5524500))
    seedArray.append(Log(person_logged=3, timestamp=6681920))
    seedArray.append(Log(person_logged=31, timestamp=6798881))
    seedArray.append(Log(person_logged=55, timestamp=4856092))
    seedArray.append(Log(person_logged=63, timestamp=5140958))
    seedArray.append(Log(person_logged=35, timestamp=6484839))
    seedArray.append(Log(person_logged=33, timestamp=1743427))
    seedArray.append(Log(person_logged=9, timestamp=5762891))
    seedArray.append(Log(person_logged=51, timestamp=5156092))
    seedArray.append(Log(person_logged=37, timestamp=5528279))
    seedArray.append(Log(person_logged=72, timestamp=2002086))
    seedArray.append(Log(person_logged=4, timestamp=6054730))
    seedArray.append(Log(person_logged=57, timestamp=318618))
    seedArray.append(Log(person_logged=65, timestamp=837055))
    seedArray.append(Log(person_logged=25, timestamp=1521916))
    seedArray.append(Log(person_logged=25, timestamp=4803152))
    seedArray.append(Log(person_logged=15, timestamp=3119495))
    seedArray.append(Log(person_logged=1, timestamp=6030927))
    seedArray.append(Log(person_logged=64, timestamp=5392559))
    seedArray.append(Log(person_logged=5, timestamp=5417234))
    seedArray.append(Log(person_logged=55, timestamp=511718))
    seedArray.append(Log(person_logged=25, timestamp=4213683))
    seedArray.append(Log(person_logged=22, timestamp=4769128))
    seedArray.append(Log(person_logged=25, timestamp=2642552))
    seedArray.append(Log(person_logged=49, timestamp=3603876))
    seedArray.append(Log(person_logged=59, timestamp=6640340))
    seedArray.append(Log(person_logged=34, timestamp=3832252))
    seedArray.append(Log(person_logged=53, timestamp=5928521))
    seedArray.append(Log(person_logged=49, timestamp=4531207))






    for item in seedArray:
        db.session.add(item)

    db.session.commit()