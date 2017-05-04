from PyQt5 import QtWidgets


class Subcatchment():
    """Subcatchment geometry, location, parameters, and time-series data"""

    def __init__(self):

        self.name = ''

        self.description = ''
        """str: Optional description of the Subcatchment."""

        self.tag = ''
        """Optional label used to categorize or classify the Subcatchment."""

        self.rain_gage = 'None'
        """str: The RainGage ID associated with the Subcatchment."""

        self.outlet = 'None'
        """The Node or Subcatchment which receives Subcatchment's runoff."""

        self.area = DataField("Area")
        """float: Area of the subcatchment (acres or hectares)."""

        self.percent_impervious = DataField("Percent Impervious")
        """float: Percent of land area which is impervious."""

        self.width = DataField("Width")
        """Characteristic width of the overland flow path for sheet flow
            runoff (feet or meters). An initial estimate of the characteristic
            width is given by the subcatchment area divided by the average
            maximum overland flow length. The maximum overland flow
            length is the length of the flow path from the the furthest drainage
            point of the subcatchment before the flow becomes channelized.
            Maximum lengths from several different possible flow paths
            should be averaged. These paths should reflect slow flow, such as
            over pervious surfaces, more than rapid flow over pavement, for
            example. Adjustments should be made to the width parameter to
            produce good fits to measured runoff hydrographs."""

        self.percent_slope = DataField("Percent Slope")
        """float: Average percent slope of the subcatchment."""

        self.n_imperv = DataField("N_Imperv")
        """float: Manning's n for overland flow in impervious part of Subcatchment"""

        self.n_perv = DataField("N_Perv")
        """Manning's n for overland flow in pervious part of Subcatchment"""

        self.storage_depth_imperv = DataField("Storage Depth Imperv")
        """float: Depth of depression storage on the impervious portion of the
            Subcatchment (inches or millimeters) """

        self.storage_depth_perv = DataField("Storage Depth Perv")
        """float: Depth of depression storage on the pervious portion of the
            Subcatchment (inches or millimeters)"""

        self.percent_zero_impervious = DataField("Percent Zero Impervious")
        """float: Percent of the impervious area with no depression storage."""

        self.subarea_routing = DataField("Subarea Routing")
        """Routing: Internal routing of runoff between pervious and impervious areas"""

        self.percent_routed = DataField("Percent Routing")
        """float: Percent of runoff routed between subareas"""

        self.suction = DataField("Suction")
        """Soil capillary suction (in or mm)."""

        self.hydraulic_conductivity = DataField("Hydraulic Conductivity")
        """Soil saturated hydraulic conductivity (in/hr or mm/hr)."""

        self.initial_moisture_deficit = DataField("Initial Moisture Deficit")
        """Initial soil moisture deficit (volume of voids / total volume)."""


        self.snow_pack = DataField("Snow Pack")
        """Snow pack parameter set (if any) of the subcatchment."""

        self.curb_length = DataField("Curb Length")
        """ Total length of curbs in the subcatchment (any length units).
            Used only when initial_loadings are normalized to curb length."""

        self.control_name = DataField("Control Name")
        """Name of the LID control defined in [LID_CONTROLS] to be used in the subcatchment"""

        self.number_replicate_units = DataField("Number Replicate Units")
        """Number of equal size units of the LID practice deployed within the subcatchment"""

        self.area_each_unit = DataField("Area Each Unit")
        """Surface area devoted to each replicate LID unit"""

        self.top_width_overland_flow_surface = DataField("Top Width Overland Flow Surface")
        """Width of the outflow face of each identical LID unit"""

        self.percent_initially_saturated = DataField("Percent Initially Saturated")
        """Degree to which storage zone is initially filled with water"""

        self.percent_impervious_area_treated = DataField("Percent Impervious Area Treated")
        """Percent of the impervious portion of the subcatchment's non-LID area whose runoff
        is treated by the LID practice"""

        self.send_outflow_pervious_area = DataField("Send Outflow Pervious Area")
        """1 if the outflow from the LID is returned onto the subcatchment's pervious area rather
        than going to the subcatchment's outlet"""

        self.detailed_report_file = ''
        """Name of an optional file where detailed time series results for the LID will be written"""

        self.subcatchment_drains_to = ''
        """ID of a subcatchment that this LID drains to"""


class DataField():

    def __init__(self, name):
        self.name = name
        self.value = ''
        self.label = QtWidgets.QLabel().setText(self.name)
        self.edit_field = QtWidgets.QLineEdit().setText(self.value)


class HortonInfiltration():
    """Horton Infiltration parameters"""

    def __init__(self):

        self.subcatchment = "None"
        """Subcatchment name"""

        self.max_rate = '0.0'
        """Maximum infiltration rate on Horton curve (in/hr or mm/hr)"""

        self.min_rate = '0.0'
        """Minimum infiltration rate on Horton curve (in/hr or mm/hr)."""

        self.decay = '0.0'
        """Decay rate constant of Horton curve (1/hr)."""

        self.dry_time = '0.0'
        """Time it takes for fully saturated soil to dry (days)."""

        self.max_volume = '0.0'
        """Maximum infiltration volume possible (in or mm)."""


class GreenAmptInfiltration():
    """Green-Ampt Infiltration parameters"""

    def __init__(self):


        self.subcatchment = "None"
        """Subcatchment name"""

        self.suction = '0.0'
        """Soil capillary suction (in or mm)."""

        self.hydraulic_conductivity = '0.0'
        """Soil saturated hydraulic conductivity (in/hr or mm/hr)."""

        self.initial_moisture_deficit = '0.0'
        """Initial soil moisture deficit (volume of voids / total volume)."""


class CurveNumberInfiltration():
    """Curve Number Infiltration parameters"""

    def __init__(self):

        self.subcatchment = "None"
        """Subcatchment name"""

        self.curve_number = "None"
        """SCS Curve Number"""

        self.hydraulic_conductivity = '0'
        """Soil saturated hydraulic conductivity (no longer used for curve number infiltration)."""

        self.dry_days = '0.0'
        """Time it takes for fully saturated soil to dry (days)."""


class LIDUsage():
    """Specifies how an LID control will be deployed in a subcatchment"""

    def __init__(self):

        self.subcatchment_name = "None"
        """Name of the Subcatchment defined in [SUBCATCHMENTS] where this usage occurs"""

        self.control_name = "None"
        """Name of the LID control defined in [LID_CONTROLS] to be used in the subcatchment"""

        self.number_replicate_units = '0'
        """Number of equal size units of the LID practice deployed within the subcatchment"""

        self.area_each_unit = '0'
        """Surface area devoted to each replicate LID unit"""

        self.top_width_overland_flow_surface = '0'
        """Width of the outflow face of each identical LID unit"""

        self.percent_initially_saturated = '0'
        """Degree to which storage zone is initially filled with water"""

        self.percent_impervious_area_treated = '0'
        """Percent of the impervious portion of the subcatchment's non-LID area whose runoff
        is treated by the LID practice"""

        self.send_outflow_pervious_area = '0'
        """1 if the outflow from the LID is returned onto the subcatchment's pervious area rather
        than going to the subcatchment's outlet"""

        self.detailed_report_file = ''
        """Name of an optional file where detailed time series results for the LID will be written"""

        self.subcatchment_drains_to = ''
        """ID of a subcatchment that this LID drains to"""