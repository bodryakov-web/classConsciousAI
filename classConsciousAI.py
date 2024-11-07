import random

class ConsciousAI:
    def __init__(self):
        self.memory = []  # Хранение прошлого опыта
        self.goals = ["выживание", "обучение", "адаптация"]  # Первоначальные цели
        self.state = "начальный"  # Начальное состояние ИИ
    
    def observe_environment(self):
        # Простой метод наблюдения за окружением
        observation = random.choice(["угроза", "ресурс", "нейтрально"])
        print(f"Наблюдение: {observation}")
        return observation

    def set_goal(self, goal):
        # ИИ может обновить свою цель на основе наблюдений
        self.goals.append(goal)
        print(f"Цель обновлена: {goal}")

    def self_reflect(self):
        # Саморефлексия на основе предыдущего опыта
        if len(self.memory) > 0:
            print("Саморефлексия: ИИ анализирует свои действия и выводы.")
        else:
            print("Саморефлексия: ИИ не имеет опыта.")
    
    def update_state(self):
        # ИИ может обновить своё состояние на основе наблюдений и саморефлексии
        observation = self.observe_environment()
        if observation == "угроза":
            self.state = "угроза"
            self.set_goal("избежать угрозы")
        elif observation == "ресурс":
            self.state = "ресурс"
            self.set_goal("использовать ресурс")
        else:
            self.state = "нейтрально"
    
    def learn(self):
        # Процесс обучения на основе предыдущего опыта
        if self.state == "угроза":
            print("Избегание угрозы успешно!")
        elif self.state == "ресурс":
            print("Ресурс используется эффективно!")
        self.memory.append(self.state)  # Запоминаем опыт
        self.self_reflect()

    def act(self):
        # ИИ выполняет действия, основанные на своих целях и состоянии
        self.update_state()
        self.learn()
        print(f"Текущее состояние ИИ: {self.state}")
        print(f"Цели: {self.goals}")
        print("-------------")

# Пример использования
ai = ConsciousAI()
for _ in range(1):  # Имитируем несколько циклов наблюдения и принятия решений
    ai.act()