from plyer import notification
import random 
import time


quotes = ["Дисциплина — это решение делать то, чего очень не хочется, чтобы достичь того, чего очень хочется. — Джон Максвелл",
    "Мотивация помогает начать. Дисциплина помогает продолжать. — Дим Рон",
    "Мы то, что мы делаем изо дня в день. Таким образом, совершенство — это не действие, а привычка. — Аристотель",
    "Страдание от дисциплины весит граммы, а страдание от сожалений — тонны. — Джим Рон",
    "Если ты не управляешь своим разумом, кто-то другой будет управлять им за тебя. — Эпиктет",
    "Тяжелый труд бьет талант, когда талант не трудится тяжело. — Тим Нотке",
    "Успех — это сумма маленьких усилий, повторяющихся изо дня в день. — Роберт Кольер",
    "Мудрый человек строит свой дом на камне, глупый — на песке. — Древняя мудрость",
    "Лучшее время, чтобы посадить дерево, было 20 лет назад. Следующее лучшее время — сегодня. — Китайская пословица",
    "Ни один человек не свободен, если он не господин самому себе. — Эпиктет",
    "Воля — это то, что заставляет тебя побеждать, когда твой рассудок говорит тебе, что ты повержен. — Мохаммед Али",
    "Секрет того, чтобы двигаться вперед, заключается в том, чтобы начать. — Марк Твен",
    "Тот, у кого есть 'Зачем' жить, выдержит почти любое 'Как'. — Фридрих Ницше",
    "Дисциплина — это мост между целями и их достижением. — Джим Рон",
    "Препятствие — это путь. — Марк Аврелий",
    "Сначала решите задачу. Затем напишите код. — Джон Джонсон",
    "Talk is cheap. Show me the code. — Linus Torvalds",
    "Простота — залог надежности. — Эдсгер Дейкстра",
    "Ошибки — это знаки препинания в кодинге, без них невозможно составить финал.",
    "The computer was born to solve problems that did not exist before. — Bill Gates",
    "Хороший код — это лучший вид документации. — Стив Макконнелл",
    "Опыт — это просто имя, которое мы даем своим ошибкам. — Оскар Уайльд",
    "Большинство хороших программистов делают свою работу потому, что им весело программировать. — Linus Torvalds",
    "Code is like humor. When you have to explain it, it’s bad. — Cory House",
    "Единственный способ писать хороший код — это много писать плохой код и постоянно его исправлять.",
    "Discipline equals freedom. — Jocko Willink",
    "It does not matter how slowly you go as long as you do not stop. — Confucius",
    "You do not rise to the level of your goals. You fall to the level of your systems. — James Clear",
    "Amateurs sit and wait for inspiration, the rest of us just get up and go to work. — Stephen King",
    "Focus on being productive instead of busy. — Tim Ferriss",
    "Do not pray for an easy life, pray for the strength to endure a difficult one. — Bruce Lee",
    "He who has a clear mind fear no dark. — Stoic Philosophy",
    "The successful warrior is the average man, with laser-like focus. — Bruce Lee",
    "Don't count the days, make the days count. — Muhammad Ali",
    "If you are working on something that you really care about, the vision pulls you. — Steve Jobs",
    "Действие устраняет страх.",
    "Stay hungry. Stay foolish. — Steve Jobs",
    "Сделай это сегодня, иначе завтра будет таким же, как вчера.",
    "Perfect is the enemy of good. — Voltaire",
    "Через 5 лет ты пожалеешь, что не начал сегодня.",
    "Errors are proof that you are trying.",
    "Дисциплина — это выбор между тем, что ты хочешь сейчас, и тем, что ты хочешь больше всего.",
    "Begin at the beginning. — Lewis Carroll",
    "Мастер ошибся больше раз, чем новичок вообще пытался.",
    "Make it work, make it right, make it fast. — Kent Beck",
    "Тише едешь — дальше будешь.",
    "Work hard in silence, let your success be your noise.",
    "Если тебе тяжело, значит ты поднимаешься в гору.",
    "Control your mind or it will control you. — Horace",
    "Просто продолжай писать этот код. Шаг за шагом."]
choosen_message = random.choice(quotes)
counter = 0
while counter < 3:
    choosen_message = random.choice(quotes)
    notification.notify(title="Начинаем работать, хорошего кода!", message=choosen_message, timeout=15)
    time.sleep(1200)
    notification.notify(title="Время передохнуть!", message="Прошло 20 минут, встань, посмотри в окно,вдаль в течении 20 секунд и возвращайся к работе!", timeout=10)
    counter += 1
    time.sleep(30)
    notification.notify(title="Возвращайся к работе!", message="30 секунд прошло, возвращайся к коду.", timeout=10)