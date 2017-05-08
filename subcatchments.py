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

        self.area = DataField("area", "Area")
        """float: Area of the subcatchment (acres or hectares)."""

        self.percent_impervious = DataField('percent_impervious', "% Impervious")
        """float: Percent of land area which is impervious."""

        self.width = DataField('width', "Width")
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

        self.percent_slope = DataField('percent_slope', "% Slope")
        """float: Average percent slope of the subcatchment."""

        self.n_imperv = DataField('n_imperv', "N_Imperv")
        """float: Manning's n for overland flow in impervious part of Subcatchment"""

        self.n_perv = DataField('n_perv', "N_Perv")
        """Manning's n for overland flow in pervious part of Subcatchment"""

        self.storage_depth_imperv = DataField('storage_depth_imperv', "Storage Depth Imperv")
        """float: Depth of depression storage on the impervious portion of the
            Subcatchment (inches or millimeters) """

        self.storage_depth_perv = DataField('storage_depth_perv', "Storage Depth Perv")
        """float: Depth of depression storage on the pervious portion of the
            Subcatchment (inches or millimeters)"""

        self.percent_zero_impervious = DataField('percent_zero_impervious', "% Zero Impervious")
        """float: Percent of the impervious area with no depression storage."""

        self.subarea_routing = DataField('subarea_routing', "Subarea Routing")
        """Routing: Internal routing of runoff between pervious and impervious areas"""

        self.percent_routed = DataField('percent_routed', "% Routing")
        """float: Percent of runoff routed between subareas"""

        # -------Infiltration----------

        self.suction = DataField('suction', "Suction")
        """Soil capillary suction (in or mm)."""

        self.hydraulic_conductivity = DataField('hydraulic_conductivity', "Hydraulic Conductivity")
        """Soil saturated hydraulic conductivity (in/hr or mm/hr)."""

        self.initial_moisture_deficit = DataField('initial_moisture_deficit', "Initial Moisture Deficit")
        """Initial soil moisture deficit (volume of voids / total volume)."""

        self.snow_pack = DataField('snow_pack', "Snow Pack")
        """Snow pack parameter set (if any) of the subcatchment."""

        self.curb_length = DataField('curb_length', "Curb Length")
        """ Total length of curbs in the subcatchment (any length units).
            Used only when initial_loadings are normalized to curb length."""

        # -------LID_Usage-------------

        self.control_name = ''
        """Name of the LID control defined in [LID_CONTROLS] to be used in the subcatchment"""

        self.number_replicate_units = DataField('number_replicate_units', "Number Replicate Units")
        """Number of equal size units of the LID practice deployed within the subcatchment"""

        self.area_each_unit = DataField('area_each_unit', "Area Each Unit")
        """Surface area devoted to each replicate LID unit"""

        self.top_width_overland_flow_surface = DataField('top_width_overland_flow_surface', "Top Width Overland Flow Surface")
        """Width of the outflow face of each identical LID unit"""

        self.percent_initially_saturated = DataField('percent_initially_saturated', "% Initially Saturated")
        """Degree to which storage zone is initially filled with water"""

        self.percent_impervious_area_treated = DataField('percent_impervious_area_treated', "% Imperv Area Treated")
        """Percent of the impervious portion of the subcatchment's non-LID area whose runoff
        is treated by the LID practice"""

        self.send_outflow_pervious_area = DataField('send_outflow_pervious_area', "Send Outflow Perv Area")
        """1 if the outflow from the LID is returned onto the subcatchment's pervious area rather
        than going to the subcatchment's outlet"""

        self.detailed_report_file = ''
        """Name of an optional file where detailed time series results for the LID will be written"""

        self.subcatchment_drains_to = ''
        """ID of a subcatchment that this LID drains to"""


class DataField():

    def __init__(self, name, label):
        self.name = name
        self.value = ''
        self.label = label
        # self.edit_field = QtWidgets.QLineEdit().setText(self.value)

        self.lower_limit = ''
        self.upper_limit = ''

        self.selected_for_estimation = self.check_if_selected_for_estimation()

        if self.selected_for_estimation:
            self.short_name = self.generate_short_name(self.name)

    def check_if_selected_for_estimation(self):
        if self.lower_limit != '' or self.upper_limit != '':
            return True

    def generate_short_name(self, name):

        name = name.lower()

        short_name = ""

        for i in range(len(name)):
            if name[i] not in [" ", "a", "e", "i", "o", "u"]:
                short_name += name[i]

        return short_name




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