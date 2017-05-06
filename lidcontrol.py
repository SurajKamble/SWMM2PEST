
from subcatchments import DataField

class LIDControl():

    def __init__(self):

        self.name = "Unnamed"
        """Name used to identify the particular LID control"""

        self.lid_type = None
        """Generic type of LID being defined"""

        self.has_surface_layer = False
        """does lid have surface layer"""

        self.has_pavement_layer = False
        """does lid have pavement layer"""

        self.has_soil_layer = False
        """does lid have soil layer"""

        self.has_storage_layer = False
        """does lid have storage layer"""

        self.has_underdrain_system = False
        """does lid have underdrain system"""

        self.has_drainmat_system = False
        """does lid have drainmat system"""

        self.surface_layer_storage_depth = DataField('surface_layer_storage_depth', "Surface_Layer_Storage_Depth")
        """When confining walls or berms are present this is the maximum depth to
            which water can pond above the surface of the unit before overflow
            occurs (in inches or mm). For LIDs that experience overland flow it is
            the height of any surface depression storage. For swales, it is the height
            of its trapezoidal cross section. """

        self.surface_layer_vegetative_cover_fraction = DataField('surface_layer_vegetative_cover_fraction', "Surface_Layer_Vegetative_Cover_Fraction")
        """Fraction of the storage area above the surface that is filled with vegetation"""

        self.surface_layer_surface_roughness = DataField('surface_layer_surface_roughness', "Surface_Layer_Surface_Roughness")
        """Manning's n for overland flow over the surface of porous pavement or a vegetative swale"""

        self.surface_layer_surface_slope = DataField('surface_layer_surface_slope', "Surface_Layer_Surface_Slope")
        """Slope of porous pavement surface or vegetative swale"""

        self.surface_layer_swale_side_slope = DataField('surface_layer_swale_side_slope', "Surface_Layer_Swale_Side_Slope")
        """Slope (run over rise) of the side walls of a vegetative swale's cross section"""

        self.pavement_layer_thickness = DataField('pavement_layer_thickness', "Pavement_Layer_Thickness")
        """Thickness of the pavement layer"""

        self.pavement_layer_void_ratio = DataField('pavement_layer_void_ratio', "Pavement_Layer_Void_Ration")
        """Volume of void space relative to the volume of solids in the pavement"""

        self.pavement_layer_impervious_surface_fraction = DataField('pavement_layer_impervious_surface_fraction', "Pavement_Layer_Impervious_Surface_Fraction")
        """Ratio of impervious paver material to total area for modular systems"""

        self.pavement_layer_permeability = DataField('pavement_layer_permeability', "Pavement_Layer_Permeability")
        """Permeability of the concrete or asphalt used in continuous systems or hydraulic
            conductivity of the fill material (gravel or sand) used in modular systems """

        self.pavement_layer_clogging_factor = DataField('pavement_layer_clogging_factor', "Pavement_Layer_Clogging_Factor")
        """Number of pavement layer void volumes of runoff treated it takes to completely clog the pavement"""

        self.soil_layer_thickness = DataField('soil_layer_thickness', "Soil_Layer_Thickness")
        """Thickness of the soil layer"""

        self.soil_layer_porosity = DataField('soil_layer_porosity', "Soil_Layer_Porosity")
        """Volume of pore space relative to total volume of soil"""

        self.soil_layer_field_capacity = DataField('soil_layer_field_capacity', "Soil_Layer_Field_Capacity")
        """Volume of pore water relative to total volume after the soil has been allowed to drain fully"""

        self.soil_layer_wilting_point = DataField('soil_layer_wilting_point', "Soil_Layer_Wilting_Point")
        """Volume of pore water relative to total volume for a well dried soil where only bound water remains"""

        self.soil_layer_conductivity = DataField('soil_layer_conductivity', "Soil_Layer_Conductivity")
        """Hydraulic conductivity for the fully saturated soil"""

        self.soil_layer_conductivity_slope = DataField('soil_layer_conductivity_slope', "Soil_Layer_Conductivity_Slope")
        """Slope of the curve of log(conductivity) versus soil moisture content"""

        self.soil_layer_suction_head = DataField('soil_layer_suction_head', "Soil_Layer_Suction_Head")
        """Average value of soil capillary suction along the wetting front"""

        self.storage_layer_height = DataField('storage_layer_height', "Storage_Layer_Height")
        """Height of a rain barrel or thickness of a gravel layer"""

        self.storage_layer_void_ratio = DataField('storage_layer_void_ratio', "Storage_Layer_Void_Ratio")
        """Volume of void space relative to the volume of solids in the layer"""

        self.storage_layer_filtration_rate = DataField('storage_layer_filtration_rate', "Storage_Layer_Filtration_Rate")
        """Maximum rate at which water can flow out the bottom of the layer after it is first constructed"""

        self.storage_layer_clogging_factor = DataField('storage_layer_clogging_factor', "Storage_Layer_Clogging_Factor")
        """Total volume of treated runoff it takes to completely clog the bottom of the layer divided by the
            void volume of the layer"""

        self.drain_coefficient = DataField('drain_coefficient', "Drain_Cofficient")
        """Coefficient that determines the rate of flow through the underdrain as a function of height of
            stored water above the drain height"""

        self.drain_exponent = DataField('drain_exponent', "Drain_Exponent")
        """Exponent that determines the rate of flow through the underdrain as a function of height of
            stored water above the drain height"""

        self.drain_offset_height = DataField('drain_offset_height', "Drain_Offset_Height")
        """Height of any underdrain piping above the bottom of a storage layer or rain barrel"""

        self.drain_delay = DataField('drain_delay', "Drain_Delay")
        """Number of dry weather hours that must elapse before the drain line in a rain barrel is opened"""

        self.drainmat_thickness = DataField('drainmat_thickness', "Drainmat_Thickness")
        """Thickness of the drainage mat (inches or mm)"""

        self.drainmat_void_fraction = DataField('drainmat_void_fraction', "Drainmat_Void_Fraction")
        """Ratio of void volume to total volume in the mat"""

        self.drainmat_roughness = DataField('drainmat_roughness', "Drainmat_Roughness")
