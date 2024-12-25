import json

class Leaderboard:
    def __init__(self):
        self.records = []

    def add_record(self, algorithm_name, time_taken, grid_size):
        self.records.append({
            'algorithm_name': algorithm_name,
            'time_taken': time_taken,
            'grid_size': grid_size
        })

    def rank_records(self):
        self.records.sort(key=lambda x: x['time_taken'])

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.records, file, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.records = json.load(file)
        except FileNotFoundError:
            self.records = []

    def display_leaderboard(self, screen, font):
        self.rank_records()
        y_offset = 100
        for idx, record in enumerate(self.records, start=1):
            text_surface = font.render(f"{idx}: {record['algorithm_name']} - Time: {record['time_taken']}s, Grid Size: {record['grid_size']}", True, (0, 255, 0))
            screen.blit(text_surface, (50, y_offset))
            y_offset += 50