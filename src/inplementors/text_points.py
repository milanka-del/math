from src.core import Points
class Text_Points(Points):
    def save(self):
        with open('points.txt', mode='w', enxoding='utf-8') as board:
            for name in self.points_board:
                board.write(f' {name} - {self.get_points(user_name=name)}')
