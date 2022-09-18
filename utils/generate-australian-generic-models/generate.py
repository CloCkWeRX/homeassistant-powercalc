import urllib.request
import csv

categories = {
    # "28": "Refrigerator/Freezer",
    # "32": "Televisions",
    "33": "Set Top Boxes",
    # "34": "Linear Fluorescent Lamps",
    # "35": "Clothes Dryers",
    # "37": "Refrigerated Cabinets",
    # "38": "Distribution Transformers",
    # "39": "ELV Lighting Converter/Transformer",
    # "40": "Incandescent Lamps",
    # "41": "Dishwashers",
    # "49": "Clothes Washers",
    # "51": "Ballasts",
    # "54": "Electric Motors",
    # "55": "External Power Supply",
    # "58": "Hot Water Heaters (Electric)",
    # "59": "Chillers",
    # "60": "Close Control Air Conditioners",
    # "61": "Compact Fluorescent Lamps",
    # "62": "Hot Water Heaters (Gas)",
    # "64": "Air Conditioners",
    # "73": "Computers",
    # "74": "Computer Monitors",
    # "83": "Pool Pump"
}


class DefaultMapper:
    def __init__(self, row):
        self.device_type = "appliance"

    def as_model_json(self):
        return {
            "name": self.brand + " " + self.model_number,
            "aliases": [self.model_number],
            "measure_description": self.measure_description,
            "measure": "manual",
            "device_type": self.device_type,
            "supported_modes": ["fixed"],
            "fixed_config": {"watt": self.watts},
        }

    def cec_to_watts(self, value):
        return float(value) / 365 / 24 / 60 / 60


class TelevisionMapper(DefaultMapper):
    def __init__(self, row):
        # Submit_ID
        self.brand = row[1]  # Brand_Reg
        self.model_number = row[2]  # Model_No
        # Family Name
        # SoldIn
        # Country
        # screensize
        # Screen_Area
        # Screen_Tech
        if row[9] != "-":
            self.passive_standby_power = float(row[9])  # Pasv_stnd_power
        if row[10] != "-":
            self.active_standby_power = float(row[10])  # Act_stnd_power
        # Act_stnd_time
        self.average_power = float(row[12])  # Avg_mode_power
        # Star
        # SRI
        self.watts = self.cec_to_watts(row[15])  # CEC
        # SubmitStatus
        # ExpDate
        # GrandDate
        # Product Class
        # Availability Status
        # Star2
        # Product Website
        # Representative Brand URL
        # Star Rating Index
        # Star Image Large
        # Star Image Small
        # Power supply
        # Tuner Typ
        self.measure_description = row[29]  # What test standard was used
        # Registration Number


class SetTopBoxMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class PoolPumpMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class ComputerMonitorMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class ComputerMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class AirConditionerMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class HotWaterHeaterGasMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class CompactFluorescentLampMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class CloseControlAirConditionerMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class ChillerMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class HotWaterHeaterEletricMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class ExternalPowerSupplyMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class ElectricMotorMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class BallastMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class ClothesWasherMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class DishwasherMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class ElvMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class DistributionTransformerMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class RefrigeratedCabinetMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class ClothesDryerMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class LinearFlueroLampMapper(DefaultMapper):
    def __init__(self, row):
        self.x = row


class RefrigeratorFreezerMapper:
    def __init__(self, row):
        # Adaptive Defrost
        # ApplStandard
        self.brand = row[2]  # Brand
        self.watts = self.cec_to_watts(row[3])  # CEC_
        # CompartGrVol
        # CompartNetVol
        # CompartType
        # Configuration
        # Country
        # Depth
        # Designation
        # FF Vol
        # FZ Vol
        # Group
        # Height
        # Icemaker
        # MEPSApproval
        self.model_number = row[17]  # Model No
        # Family Name
        self.measure_description = row[19]  # N-Standard
        # Star2009
        # SRI2009
        # No_Doors
        # S-MEPS_Ad
        # S-MEPScutoff
        # Sold_in
        # Submit_ID
        # SubmitStatus
        # Tot Vol
        # Width
        # ExpDate
        # GrandDate
        # Product Class
        # Availability Status
        # Product Website
        # Representative Brand URL
        # Fixed MEPS allowance factor
        # Variable MEPS allowance factor
        # Adjusted volume	Type
        # Star Rating (old)
        # Star Image Large
        # Star Image Small
        # Registration Number

        return {
            "name": self.brand + " " + self.model_number,
            "aliases": [self.model_number],
            "measure_description": self.measure_description,
            "measure": "manual",
            "device_type": "appliance",
            "supported_modes": ["fixed"],
            "fixed_config": {"watt": self.watts},
        }


class IncandescentLampMapper:
    def __init__(self, row):
        self.device_type = "light"

        # "Submit_ID",
        self.brand = row[1]  # "Brand",
        self.model_number = row[2]  # "Model_No",
        # "Family Name",
        # "SoldIn",
        # "Country",
        # "Sing_or_fam",
        self.watts = float(row[7])  # "nom_lamp_power", # Lamp Watts
        # "avg_meas_lum_flux",
        # "median_lamp_life",
        # "lumen_maintenance"
        # "avg_meas_efficacy",
        # "inputvolt_min",
        # "inputvolt_max",
        # "ExpDate",
        # "GrandDate",
        # "SubmitStatus",
        # "Product Class",
        # "Availability Status",
        # "Product Website",
        # "Representative Brand URL"
        # "Lamp Light Output (Lumens)",
        # "Lamp Type",
        self.measure_description = row[23]  # "What test standard was used"


mappers = {
    "Incandescent Lamps": IncandescentLampMapper,
    "Refrigerator/Freezer": RefrigeratorFreezerMapper,
    "Televisions": TelevisionMapper,
    "Set Top Boxes": SetTopBoxMapper,
    "Linear Fluorescent Lamps": LinearFluorescentLampMapper,
    "Clothes Dryers": ClothesDryerMapper,
    "Refrigerated Cabinets": RefrigeratedCabinentMapper,
    "Distribution Transformers": DistributionTransformerMapper,
    "ELV Lighting Converter/Transformer": ElvMapper,
    "Incandescent Lamps": IncandescentLampMapper,
    "Dishwashers": DishwasherMapper,
    "Clothes Washers": ClothesWasherMapper,
    "Ballasts": BallastMapper,
    "Electric Motors": ElectricMotorMapper,
    "External Power Supply": ExternalPowerSupplyMapper,
    "Hot Water Heaters (Electric)": HotWaterHeaterElectricMapper,
    "Chillers": ChillerMapper,
    "Close Control Air Conditioners": CloseControlAirConditionerMapper,
    "Compact Fluorescent Lamps": CompatFluorescentLampMapper,
    "Hot Water Heaters (Gas)": HotWaterHeaterGasMapper,
    "Air Conditioners": AirConditionerMapper,
    "Computers": ComputerMapper,
    "Computer Monitors": ComputerMonitorMapper,
    "Pool Pump": PoolPumpMapper,
}

# TODO: Each of these is a different format
# TODO: Cache?
# TODO: Heading to model.json mappings
for key, label in categories.items():
    url = (
        "https://reg.energyrating.gov.au/comparator/product_types/"
        + key
        + "/search/?expired_products=on&export_format=csv"
    )

    response = urllib.request.urlopen(url)
    lines = [l.decode("utf-8") for l in response.readlines()]
    n = 0
    for row in csv.reader(lines):
        if n > 0:
            mapper = mappers[label](row)
            print(mapper.as_model_json())
        n += 1
