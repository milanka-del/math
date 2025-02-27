from src.core import Points

class Text_Points(Points):
    def save(self):
        with open('points.txt', 'a', encoding='utf-8') as board:
            for name in self.points_board:
                board.write(f' {name} - {self.get_points(user_name=name)}*')
    def load(self):
        with open('points.txt', mode='r', encoding='utf - 8') as tabs:
            text = tabs.read().split('*')
            text.remove('')
            

            print(text)



