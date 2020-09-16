import json
import random

from kivy.event import EventDispatcher
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

# Screen Manager erstellen
screenmanager = ScreenManager()


# Deklarieren der Screens
class StartScreen(Screen):
    """Dieser Screen ist der Start Screen"""
    pass


class GameScreen(Screen):
    """Auf diesem Screen findet das Spiel statt."""
    pass


class QuitScreen(Screen):
    """Auf diesem Screen wird das Ergebnis angezeigt."""
    pass


"""Dem Screenmanager werden die oben deklarierten Screens übergeben."""

screenmanager.add_widget(StartScreen(name="start"))
screenmanager.add_widget(GameScreen(name="game"))
screenmanager.add_widget(QuitScreen(name="quit"))


# ALLE SPIELREGELN UND LOGIK
class Exercise(Widget):
    """Eine Aufgabe hat ein Polynom und eine Liste an möglichen Teilern."""

    level = ListProperty([False] * 3)

    def __init__(self, **kwargs):
        """
        Öffnet die JSON Datei, in der die Terme mit zugehörigen Teilern sind.
        :param kwargs:
        :rtype: object
        """
        super(Exercise, self).__init__(**kwargs)
        with open('./polynome.json', 'r') as file:
            self.polynomeUndTeiler = json.load(file)
        with open('./level1.json', 'r') as file:
            self.level1Elemente = json.load(file)
        with open('./level2.json', 'r') as file:
            self.level2Elemente = json.load(file)
        with open('./level3.json', 'r') as file:
            self.level3Elemente = json.load(file)

    def toggle_level(self, l):
        self.level[l] = not (self.level[l])
        print(self.level)
        return self.level

    def get_selected_level(self):
        selected_level = NumericProperty(0)
        for i in range(2):
            if self.level[i]:
                selected_level = i
        print(selected_level)
        return selected_level

    def select_level1(self):
        """
        Wählt eine random Exercise aus.
        :rtype: object
        """
        random_exercise = random.choice(list(self.level1Elemente.values()))
        return random_exercise

    def select_level2(self):
        """
        Wählt eine random Exercise aus.
        :rtype: object
        """
        random_exercise = random.choice(list(self.level2Elemente.values()))
        return random_exercise

    def select_level3(self):
        """
        Wählt eine random Exercise aus.
        :rtype: object
        """
        random_exercise = random.choice(list(self.level3Elemente.values()))
        return random_exercise

    def select_exercise(self):
        """
        Wählt eine random Exercise aus.
        :rtype: object
        """
        random_exercise = random.choice(list(self.polynomeUndTeiler.values()))
        return random_exercise

    def create_exercise(self):
        """Gibt ein Polynom und 16 mögliche Faktoren zurück.
        :return:
        :rtype: object
        """
        level = self.get_selected_level()
        if level == 0:
            random_exercise = self.select_level1()
        elif level == 1:
            random_exercise = self.select_level2()
        elif level == 2:
            random_exercise = self.select_level3()
        else:
            random_exercise = self.select_exercise()

        polynom = random_exercise['polynom']
        count = random.randint(5, 10)
        r = random.SystemRandom()
        factors = r.sample(
            r.sample(random_exercise['correct_factor'], count)
            + r.sample(random_exercise['wrong_factor'], 16 - count), 16)
        exercise = [polynom, factors, random_exercise['correct_factor'],
                    random_exercise['wrong_factor']]
        print(exercise)
        return exercise


class Solution(EventDispatcher):
    answer = ListProperty([False] * 16)

    score = NumericProperty(0)

    exercise = ListProperty(Exercise().create_exercise())

    def toggle_factor(self, factor):
        """Schaut sich an was der Wert in der Liste answer war und wechselt ihn ins Gegenteil. (false<->true)
        :rtype: object
        :param factor:
        :return:
        """
        self.answer[factor] = not (self.answer[factor])
        print(self.answer)
        return self.answer

    def get_selected_factors(self):
        """Eine Liste der gedrückten Faktoren wird zurück gegeben.
        :return:
        :rtype: object
        """
        selected_factors = []

        for i in range(16):
            if self.answer[i]:
                selected_factors.append(self.exercise[1][i])
        print(selected_factors)
        return selected_factors

    def get_solution(self):
        """Für jeden Eintrag der Liste die die Methode oben erzeugt prüfe
        ob er in der Liste der richtigen Fakotoren ist und
        wenn ja dann bekommt der Spieler +1 Punkt.
        :param self:
        :return:
        :rtype: object"""
        selected_factors = self.get_selected_factors()
        points = 0
        for i in range(len(selected_factors)):
            if selected_factors[i] in self.exercise[2]:
                points = points + 1
            else:
                points -= points
        self.score += points
        return self.score

    def restart(self, ):
        self.answer = [False] * 16
        self.exercise = Exercise().create_exercise()


class Game(Solution):
    """Klasse Game für die Logik des Spiels."""
    exercise_factory = Exercise()
    solution = Solution()

    def restart(self):
        """Spiel neu starten"""
        self.exercise_factory.level = [False] * 3
        return self.solution.restart()

    def toggle_factor(self, factor):
        return self.solution.toggle_factor(factor)

    def toggle_level(self, l):
        return self.exercise_factory.toggle_level(l)

    def get_solution(self):
        return self.solution.get_solution()

