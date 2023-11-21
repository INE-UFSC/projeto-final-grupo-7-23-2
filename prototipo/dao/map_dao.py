from dao.dao import DAO


class MapDAO(DAO):
    def __init__(self, path: str):
        DAO.__init__(self, path)

    def read_data(self):
        result: list[list[int]] = []
        with open(self.get_path(), 'r') as map_file:
            map_data = map_file.readlines()
            for line in map_data:
                result.append([int(x) for x in line.replace('\n', '').split(',')])

        return result

    def write_data(self):
        pass

