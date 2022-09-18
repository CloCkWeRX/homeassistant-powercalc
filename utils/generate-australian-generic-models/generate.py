import urllib.request
import csv

categories = {
    # "28": "Refrigerator/Freezer",
    # "32": "Televisions",
    # "33": "Set Top Boxes",
    # "34": "Linear Fluorescent Lamps",
    # "35": "Clothes Dryers",
    # "37": "Refrigerated Cabinets",
    # "38": "Distribution Transformers",
    # "39": "ELV Lighting Converter/Transformer",
    "40": "Incandescent Lamps",
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
        core = {
            "name": self.brand + " " + self.model_number,
            "aliases": [self.model_number],
            "measure_description": self.measure_description,
            "measure": "manual",
            "device_type": self.device_type,
            "supported_modes": ["fixed"],
            "fixed_config": {"watt": self.watts},
        }

        if hasattr(self, "min_power"):
            core["fixed_config"]["min_power"] = self.min_power

        if hasattr(self, "max_power"):
            core["fixed_config"]["max_power"] = self.max_power

        if hasattr(self, "active_standby_power"):
            core["fixed_config"]["standby_power_on"] = self.active_standby_power

        if hasattr(self, "passive_standby_power"):
            core["fixed_config"]["standby_power"] = self.passive_standby_power

        return core

    def cec_to_watts(self, value):
        return float(value) / 365 / 24 / 60 / 60

    def none_or_float(self, value):
        if value == "-":
            return None
        return float(value)


class TelevisionMapper(DefaultMapper):
    def __init__(self, row):
        self.device_type = "appliance"
        # Submit_ID
        self.brand = row[1]  # Brand_Reg
        self.model_number = row[2]  # Model_No
        # Family Name
        # SoldIn
        # Country
        # screensize
        # Screen_Area
        # Screen_Tech
        self.passive_standby_power = self.none_or_float(row[9])  # Pasv_stnd_power
        self.active_standby_power = self.none_or_float(row[10])  # Act_stnd_power
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
        self.device_type = "appliance"
        self.measure_description = "Unspecified standard, energyrating.gov.au"
        # Submit_I
        self.brand = row[1]  # Brand_Reg
        self.model_number = row[2]  # Model_No
        # Family Name
        # N-Reg_Date
        # Reg_No
        # SoldIn
        # Country
        # Prod_conf
        self.min_power = self.none_or_float(row[9])  # input_power_min
        self.max_power = self.none_or_float(row[10])  # input_power_max
        # decoding_type
        # autostandby
        # hdmistandby
        self.passive_standby_power = self.none_or_float(row[14])  # psv_standby_power
        self.active_standby_power = self.none_or_float(row[15])  # act_standby_power
        self.watts = float(row[16])  # onmode_power
        # Apply_type_for
        # url
        # ExpDate
        # GrandDate
        # SubmitStatus
        # Product Class
        # Availability Status


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


class HotWaterHeaterElectricMapper(DefaultMapper):
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
        self.device_type = "appliance"
        self.measure_description = row[0]  # ApplStandard
        self.brand = row[1]  # Brand
        # climate_class
        # Country
        # high_efficiency
        self.model_number = row[5]  # Model No
        # Family Name
        self.measure_description = row[11]  # N-Standard
        # Sold_in
        # Submit_ID
        # SubmitStatus
        # Temp_Class
        # total_dis_area
        # total_energy_cons
        # type
        # ExpDate
        # GrandDate
        # Product Class
        # Availability Status
        # Product Website
        # Representative Brand URL
        # Type
        # Efficiency (kWh/24h/m²)
        # Length
        # Climate Class
        # Depth
        # Cabinet Description
        # Total Energy Consumption(kWh/24h)
        # Cabinet Type
        # Star Rating Energy
        # Efficiency Index
        # Width
        # Net Volume
        # Height
        # Duty
        # Type
        # Product Class Number

    def as_model_json(self):
        return {}


class ClothesDryerMapper(DefaultMapper):
    def __init__(self, row):
        self.device_type = "appliance"
        # self.measure_description = row[0] # ApplStandard
        self.brand = row[1]  # Brand
        # Cap
        # Combination
        # Control
        # Country
        # Depth
        # Height
        self.model_number = row[8]  # Model No
        # Family Name
        self.measure_description = row[10]  # N-Standard
        self.watts = self.cec_to_watts(row[11])  # New CEC
        # New SRI
        # New Star
        # Prog Name
        # Prog Time
        # Sold_in
        # SubmitStatus
        # Submit_ID
        # Test_Moist_Remove
        # Tot_Wat_Cons
        # Type
        # Width
        # ExpDate
        # GrandDate
        # Product Class
        # Availability Status
        # Product Website
        # Representative Brand URL
        # Star Rating (old)
        # Star Image Large
        # Star Image Small


class LinearFluorescentLampMapper(DefaultMapper):
    def __init__(self, row):
        self.device_type = "light"
        self.measure_description = row[0]  # ApplStandard
        self.brand = row[1]  # Brand
        # Country
        # Lamp_Freq
        self.model_number = row[4]  # Model No
        # Family Name
        if row[6] != "":
            self.measure_description = row[6]  # N-Standard
        # nom_len
        self.watts = float(row[8])  # nom_watt
        # Rated_CRI
        # Rated_IE
        # Rated_IL
        # Rated_ILW
        # Rated_ME
        # Rated_ML
        # Rated_MLW
        # Sold_in
        # Submit_ID
        # SubmitStatus
        # ExpDate
        # GrandDate
        # Product Class
        # Availability Status
        # Product Website
        # Representative Brand URL
        # ILCOS Code
        # Nominal Diameter (mm)


class RefrigeratorFreezerMapper(DefaultMapper):
    def __init__(self, row):
        self.device_type = "appliance"
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


class IncandescentLampMapper(DefaultMapper):
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
    "Refrigerated Cabinets": RefrigeratedCabinetMapper,
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
    "Compact Fluorescent Lamps": CompactFluorescentLampMapper,
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
