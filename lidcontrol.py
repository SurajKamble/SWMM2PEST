
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

        self.surface_layer_storage_depth = DataField('surface_layer_storage_depth', "Surface_Layer_Storage_Depth", index=2)


        self.surface_layer_vegetative_cover_fraction = DataField('surface_layer_vegetative_cover_fraction', "Surface_Layer_Vegetative_Cover_Fraction", index=3)
        """Fraction of the storage area above the surface that is filled with vegetation"""

        self.surface_layer_surface_roughness = DataField('surface_layer_surface_roughness', "Surface_Layer_Surface_Roughness", index=4)
        """Manning's n for overland flow over the surface of porous pavement or a vegetative swale"""

        self.surface_layer_surface_slope = DataField('surface_layer_surface_slope', "Surface_Layer_Surface_Slope", index=5)
        """Slope of porous pavement surface or vegetative swale"""

        self.surface_layer_swale_side_slope = DataField('surface_layer_swale_side_slope', "Surface_Layer_Swale_Side_Slope", index=6)
        """Slope (run over rise) of the side walls of a vegetative swale's cross section"""

        self.pavement_layer_thickness = DataField('pavement_layer_thickness', "Pavement_Layer_Thickness", index=2)
        """Thickness of the pavement layer"""

        self.pavement_layer_void_ratio = DataField('pavement_layer_void_ratio', "Pavement_Layer_Void_Ration", index=3)
        """Volume of void space relative to the volume of solids in the pavement"""

        self.pavement_layer_impervious_surface_fraction = DataField('pavement_layer_impervious_surface_fraction', "Pavement_Layer_Impervious_Surface_Fraction", index=4)
        """Ratio of impervious paver material to total area for modular systems"""

        self.pavement_layer_permeability = DataField('pavement_layer_permeability', "Pavement_Layer_Permeability", index=5)
        """Permeability of the concrete or asphalt used in continuous systems or hydraulic
            conductivity of the fill material (gravel or sand) used in modular systems """

        self.pavement_layer_clogging_factor = DataField('pavement_layer_clogging_factor', "Pavement_Layer_Clogging_Factor", index=6)
        """Number of pavement layer void volumes of runoff treated it takes to completely clog the pavement"""

        self.soil_layer_thickness = DataField('soil_layer_thickness', "Soil_Layer_Thickness", index=2)
        """Thickness of the soil layer"""

        self.soil_layer_porosity = DataField('soil_layer_porosity', "Soil_Layer_Porosity", index=3)
        """Volume of pore space relative to total volume of soil"""

        self.soil_layer_field_capacity = DataField('soil_layer_field_capacity', "Soil_Layer_Field_Capacity", index=4)
        """Volume of pore water relative to total volume after the soil has been allowed to drain fully"""

        self.soil_layer_wilting_point = DataField('soil_layer_wilting_point', "Soil_Layer_Wilting_Point", index=5)
        """Volume of pore water relative to total volume for a well dried soil where only bound water remains"""

        self.soil_layer_conductivity = DataField('soil_layer_conductivity', "Soil_Layer_Conductivity", index=6)
        """Hydraulic conductivity for the fully saturated soil"""

        self.soil_layer_conductivity_slope = DataField('soil_layer_conductivity_slope', "Soil_Layer_Conductivity_Slope", index=7)
        """Slope of the curve of log(conductivity) versus soil moisture content"""

        self.soil_layer_suction_head = DataField('soil_layer_suction_head', "Soil_Layer_Suction_Head", index=8)
        """Average value of soil capillary suction along the wetting front"""

        self.storage_layer_height = DataField('storage_layer_height', "Storage_Layer_Height", index=2)
        """Height of a rain barrel or thickness of a gravel layer"""

        self.storage_layer_void_ratio = DataField('storage_layer_void_ratio', "Storage_Layer_Void_Ratio", index=3)
        """Volume of void space relative to the volume of solids in the layer"""

        self.storage_layer_filtration_rate = DataField('storage_layer_filtration_rate', "Storage_Layer_Filtration_Rate", index=4)
        """Maximum rate at which water can flow out the bottom of the layer after it is first constructed"""

        self.storage_layer_clogging_factor = DataField('storage_layer_clogging_factor', "Storage_Layer_Clogging_Factor", index=5)
        """Total volume of treated runoff it takes to completely clog the bottom of the layer divided by the
            void volume of the layer"""

        self.drain_coefficient = DataField('drain_coefficient', "Drain_Cofficient", index=2)
        """Coefficient that determines the rate of flow through the underdrain as a function of height of
            stored water above the drain height"""

        self.drain_exponent = DataField('drain_exponent', "Drain_Exponent", index=3)
        """Exponent that determines the rate of flow through the underdrain as a function of height of
            stored water above the drain height"""

        self.drain_offset_height = DataField('drain_offset_height', "Drain_Offset_Height", index=4)
        """Height of any underdrain piping above the bottom of a storage layer or rain barrel"""

        self.drain_delay = DataField('drain_delay', "Drain_Delay", index=5)
        """Number of dry weather hours that must elapse before the drain line in a rain barrel is opened"""

        self.drainmat_thickness = DataField('drainmat_thickness', "Drainmat_Thickness", index=2)
        """Thickness of the drainage mat (inches or mm)"""

        self.drainmat_void_fraction = DataField('drainmat_void_fraction', "Drainmat_Void_Fraction", index=3)
        """Ratio of void volume to total volume in the mat"""

        self.drainmat_roughness = DataField('drainmat_roughness', "Drainmat_Roughness", index=4)

    def get_surface_control_pars_as_list(self):

        return [self.surface_layer_storage_depth, self.surface_layer_vegetative_cover_fraction, self.surface_layer_surface_roughness,
                self.surface_layer_surface_slope, self.surface_layer_swale_side_slope]

    def get_pavement_control_pars_as_list(self):

        return [self.pavement_layer_thickness, self.pavement_layer_void_ratio, self.pavement_layer_impervious_surface_fraction,
                self.pavement_layer_permeability, self.pavement_layer_clogging_factor]

    def get_soil_control_pars_as_list(self):

        return [self.soil_layer_thickness, self.soil_layer_porosity, self.soil_layer_field_capacity, self.soil_layer_wilting_point,
                self.soil_layer_conductivity, self.soil_layer_conductivity_slope, self.soil_layer_suction_head]

    def get_storage_control_pars_as_list(self):

        return [self.storage_layer_height, self.storage_layer_void_ratio, self.storage_layer_filtration_rate, self.storage_layer_clogging_factor]

    def get_drain_control_pars_as_list(self):

        return [self.drain_coefficient, self.drain_exponent, self.drain_offset_height, self.drain_delay]

    def get_drainmat_control_pars_as_list(self):

        return [self.drainmat_thickness, self.drainmat_void_fraction, self.drainmat_roughness]

    def get_all_data_as_list(self):

        return [self.surface_layer_storage_depth, self.surface_layer_vegetative_cover_fraction, self.surface_layer_surface_roughness,
                self.surface_layer_surface_slope, self.surface_layer_swale_side_slope,
                self.pavement_layer_thickness, self.pavement_layer_void_ratio,
                self.pavement_layer_impervious_surface_fraction,
                self.pavement_layer_permeability, self.pavement_layer_clogging_factor,
                self.soil_layer_thickness, self.soil_layer_porosity, self.soil_layer_field_capacity,
                self.soil_layer_wilting_point,
                self.soil_layer_conductivity, self.soil_layer_conductivity_slope, self.soil_layer_suction_head,
                self.storage_layer_height, self.storage_layer_void_ratio, self.storage_layer_filtration_rate,
                self.storage_layer_clogging_factor,
                self.drain_coefficient, self.drain_exponent, self.drain_offset_height, self.drain_delay,
                self.drainmat_thickness, self.drainmat_void_fraction, self.drainmat_roughness]

    def get_all_selected_pars(self):

        list_of_selected_pars = []

        for parameter in self.get_all_data_as_list():

            if parameter.check_if_selected_for_estimation():
                print(parameter.name)

                list_of_selected_pars.append(parameter)

        print("List of selected pars: ")
        print(list_of_selected_pars)

        return list_of_selected_pars





    def get_selected_surface_pars(self):

        list_of_selected_pars = []

        for parameter in self.get_surface_control_pars_as_list():

            if parameter.check_if_selected_for_estimation():
                print(parameter.name)

                list_of_selected_pars.append(parameter)

        print("List of selected pars: ")
        print(list_of_selected_pars)

        return list_of_selected_pars

    def get_selected_pavement_pars(self):

        list_of_selected_pars = []

        for parameter in self.get_pavement_control_pars_as_list():

            if parameter.check_if_selected_for_estimation():
                print(parameter.name)

                list_of_selected_pars.append(parameter)

        print("List of selected pars: ")
        print(list_of_selected_pars)

        return list_of_selected_pars

    def get_selected_soil_pars(self):

        list_of_selected_pars = []

        for parameter in self.get_soil_control_pars_as_list():

            if parameter.check_if_selected_for_estimation():
                print(parameter.name)

                list_of_selected_pars.append(parameter)

        print("List of selected pars: ")
        print(list_of_selected_pars)

        return list_of_selected_pars

    def get_selected_storage_pars(self):

        list_of_selected_pars = []

        for parameter in self.get_storage_control_pars_as_list():

            if parameter.check_if_selected_for_estimation():
                print(parameter.name)

                list_of_selected_pars.append(parameter)

        print("List of selected pars: ")
        print(list_of_selected_pars)

        return list_of_selected_pars

    def get_selected_drain_pars(self):

        list_of_selected_pars = []

        for parameter in self.get_drain_control_pars_as_list():

            if parameter.check_if_selected_for_estimation():
                print(parameter.name)

                list_of_selected_pars.append(parameter)

        print("List of selected pars: ")
        print(list_of_selected_pars)

        return list_of_selected_pars

    def get_selected_drainmat_pars(self):

        list_of_selected_pars = []

        for parameter in self.get_drainmat_control_pars_as_list():

            if parameter.check_if_selected_for_estimation():
                print(parameter.name)

                list_of_selected_pars.append(parameter)

        print("List of selected pars: ")
        print(list_of_selected_pars)

        return list_of_selected_pars


