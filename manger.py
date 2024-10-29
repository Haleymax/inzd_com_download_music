import argparse

from spiders.spider import spider


class Manager:
    def __init__(self):
        self.singer = None
        self.parser = argparse.ArgumentParser(description='Process some integers.')
        self.parser.add_argument("-start", type=str, help="输入需要下载歌手的名字用 '、' 隔开")
        self.update_game_status_false_str = None

    def load_parameter(self):
        args = self.parser.parse_args()
        self.update_game_status_false_str = args.start

    def execute(self):
        if self.update_game_status_false_str:
            print(f"the target singer is: {self.update_game_status_false_str}")
            self.process_string(self.update_game_status_false_str)
            spider(self.singer)

    def process_string(self, input_str):
        self.singer = input_str.strip().split('、')

def execute_command():
    manager = Manager()
    manager.load_parameter()
    manager.execute()


if __name__ == '__main__':
    execute_command()