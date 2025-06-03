import csv
from pathlib import Path
from uuid import uuid4


class CSVSaver:
    def __init__(self, simulation_id: uuid4):
        self.data_dir: Path = self._make_dir(simulation_id)
        self.fieldnames = ['time', 'vehicles_passed']

    def _make_dir(self, simulation_id: uuid4):
        data_dir = Path(__file__).resolve().parent.parent.parent / "data" / str(simulation_id)
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir

    def save(self, intersection_id: uuid4, time: float, vehicles_passed: int):
        output_file = self.data_dir / f"{intersection_id}.csv"
        output_file.parent.mkdir(exist_ok=True, parents=True)

        with open(output_file, 'a', newline="") as filedata:
            writer = csv.DictWriter(filedata, delimiter=',', fieldnames=self.fieldnames)
            writer.writerow({
                "time": time,
                "vehicles_passed": vehicles_passed
            })
