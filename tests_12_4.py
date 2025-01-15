import unittest, logging

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        pass

    def test_walk(self):
        try:
            sportsman = Runner("Ben")
            logging.info("test_walk выполнен успешно")
            for _ in range(10):
                sportsman.walk()
            self.assertEqual(sportsman.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            raise Exception


    def test_run(self):
        try:
            sportsman = Runner(['ben', 4])
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                sportsman.run()
            self.assertEqual(sportsman.distance, 100)
        except:
            logging.warning('Неверный тип данных для объекта Runner')


    def test_challenge(self):
        sportsman_1 = Runner("Ben")
        sportsman_2 = Runner("Dave")
        for _ in range(10):
            sportsman_1.run()
            sportsman_2.walk()
        self.assertNotEqual(sportsman_1.distance, sportsman_2.distance)



if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")

    unittest.main()



    first = Runner('Вося', 10)
    second = Runner('Илья', 5)
    # third = Runner('Арсен', 10)

    t = Tournament(101, first, second)
    print(t.start())