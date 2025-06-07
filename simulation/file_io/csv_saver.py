import csv
from pathlib import Path
from uuid import uuid4

from simulation.domain.models.intersection_type import IntersectionType
from simulation.domain.models.lights_switch_strategy import LightsSwitchStrategy


class CSVSaver:
    def __init__(self, simulation_id: uuid4):
        self.simulation_id = simulation_id
        self.base_dir: Path = self.make_base_dir()
        self.fieldnames = ['time', 'vehicles_passed']

    @staticmethod
    def make_base_dir():
        base_dir = Path(__file__).resolve().parent.parent.parent / "data"
        base_dir.mkdir(parents=True, exist_ok=True)
        return base_dir

    def _choose_output_path(
        self,
        intersection_type: IntersectionType,
        light_strategy: LightsSwitchStrategy,
        light_duration: int,
        vehicles_per_second: int,
        intersection_id: uuid4
    ) -> Path:
        veh_per_sec = "veh_per_sec_" + str(vehicles_per_second)
        base_dir = self.base_dir / str(veh_per_sec) / intersection_type.value
        if light_strategy and light_duration:
            lights_dur = "light_dur_" + str(light_duration)
            output_dir = base_dir / light_strategy.value / lights_dur
        else:
            output_dir = base_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir / f"{intersection_id}.csv"

    def save(
        self,
        intersection_id: uuid4,
        time: float,
        vehicles_passed: int,
        intersection_type: IntersectionType,
        light_strategy: LightsSwitchStrategy,
        light_duration: int,
        vehicles_per_second: int
    ):
        output_file = self._choose_output_path(intersection_type, light_strategy, light_duration, vehicles_per_second, intersection_id)
        write_header = not output_file.exists()

        with open(output_file, 'a', newline="") as filedata:
            writer = csv.DictWriter(filedata, delimiter=',', fieldnames=self.fieldnames)
            if write_header:
                writer.writeheader()
            writer.writerow({
                "time": time,
                "vehicles_passed": vehicles_passed
            })
