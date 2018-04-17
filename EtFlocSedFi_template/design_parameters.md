### Design Parameters



Included is the design for a plant for **{{UI.City}}** having a maximum flow rate of {{maximum_flow_rate}}. The design was created assuming specific input parameters, shown in Table 1 below. The software uses these parameters together with the requested flow rate as variables in a series of hydraulic and geometric calculations that define the dimensions of the various plant components. The goal of the plant with respect to water quality is to reduce the turbidity as much as possible and to have it meet international water quality standards (less than 5 NTU), maintain the color within norms (15 Unidades de Color – UC), disinfect the water with chlorine, and maintain a residual chlorine concentration throughout distribution between 0.3 and 1.0 mg/L. The plant treats water without using electricity, utilizing preliminary sedimentation, flow control, rapid mix, coagulation/flocculation, hydraulic upflow sedimentation, filtration, and chlorination.



#### Table 1: Automated Design Tool assumptions used to calculate the included design.

*Maximum flow rate*:    {{maximum_flow_rate}}

<table style="width:100%">
<tr>
    <th colspan="2">*Geometric Assumptions*</th>
</tr>
<tr>
    <th>Thickness of the plant walls</th>
    <th>{{plant_thickness_walls}}</th>
</tr>
<tr>
    <th>Minimum concrete thickness</th>
    <th>{{T.ConcreteMin}}</th>
</tr>
<tr>
    <th>Minimum tank dimension for construction worker to fit inside</th>
    <th>{{W.HumanMin}}</th>
</tr>
<tr>
    <th>Minimum height from bottom of drain channel to top of walkway so that operator can fit inside</th>
    <th>{{H.HumanAccess}}</th>
</tr>
<tr>
    <th>Minimum width of a channel for constructability</th>
    <th>{{W.ChannelMin}}</th>
</tr>
<tr>
    <th>Plant freeboard height</th>
    <th>{{plant_freeboard_height}}</th>
</tr>
<tr>
    <th colspan="2">*Entrance Tank*</th>
</tr>
<tr>
    <th>Maximum hopper angle</th>
    <th>{{AN.EtSlope}}</th>
</tr>
<tr>
    <th>Maximum upflow velocity</th>
    <th>{{V.EtUp}}</th>
</tr>
<tr>
    <th>Maximum water height for ease of operation</th>
    <th>{{HW.EtMax}}</th>
</tr>
<tr>
    <th>Thickness of the ledge between hoppers</th>
    <th>{{T.EtLedge}}</th>
</tr>
<tr>
    <th colspan="3">*Chemical Dosing*</th>
</tr>
<tr>
    <th>Turnover time for the chemical stock</th>
    <th>{{Ti.CoagStock}}</th>
    <th></th>
</tr>
<tr>
    <th>Height of the chemical tanks above the constant head tanks</th>
    <th>{{height_chemical tanks}}</th>
    <th></th>
</tr>
<tr>
    <th>Minor loss coefficient for small diameter tubing</th>
    <th>{{K.CdcTube}}</th>
    <th></th>
</tr>
<tr>
    <th></th>
    <th>*Coagulant*</th>
    <th>*Chlorine*</th>
</tr>
<tr>
    <th>Maximum dose</th>
    <th>{{maximum_dose}}</th>
    <th>{{C.ChlorineDoseMax}}</th>
</tr>
<tr>
    <th>Maximum stock concentration</th>
    <th>{{C.CoagStockMax}}</th>
    <th>{{C.ChlorineStockMax}}</th>
</tr>
<tr>
    <th>Maximum head loss through small-diameter tubing</th>
    <th>{{HL.CoagCdc}}</th>
    <th>{{HL.ChlorCdc}}</th>
</tr>
<tr>
    <th colspan="2">*Flocculation*</th>
</tr>
<tr>
    <th>Minor loss coefficient for flow around a baffle</th>
    <th>{{minor_loss_coefficient_flow}}</th>
</tr>
<tr>
    <th>Desired collision potential</th>
    <th>{{desired_collision_potential}}</th>
</tr>
<tr>
    <th>Desired energy dissipation rate</th>
    <th>{{ED.Floc}}</th>
</tr>
<tr>
    <th>Maximum time required to drain the tank</th>
    <th>{{maximum_time_drain}}</th>
</tr>
<tr>
    <th colspan="2">*Sedimentation*</th>
</tr>
<tr>
    <th>Angle of side slopes</th>
    <th>{{angle_side_slopes}}</th>
</tr>
<tr>
    <th>Angle of plate settlers</th>
    <th>{{angle_plate_settlers}}</th>
</tr>
<tr>
    <th>Angle of floc hopper slopes</th>
    <th>{{AN.SedHopperSlope}}</th>
</tr>
<tr>
    <th>Minimum spacing between plate settlers</th>
    <th>{{S.SedPlateMin}}</th>
</tr>
<tr>
    <th>Upflow velocity</th>
    <th>{{up flow_velocity}}</th>
</tr>
<tr>
    <th>Capture velocity</th>
    <th>{{capture_velocity}}</th>
</tr>
<tr>
    <th colspan="2">*Stacked Rapid Sand Filter*</th>
</tr>
<tr>
    <th>Wall thickness</th>
    <th>{{wall_thickness}}</th>
</tr>
<tr>
    <th>Backwash velocity</th>
    <th>{{backwash_velocity}}</th>
</tr>
<tr>
    <th>Number of sand layers</th>
    <th>{{number_sand_layers}}</th>
</tr>
<tr>
    <th>Time required to drain backwash water above fluidized bed</th>
    <th>{{T.FiBwInitiationBod}}</th>
</tr>
<tr>
    <th colspan="2">*Material Dimensions*</th>
</tr>
<tr>
    <th>Width of plate settler material</th>
    <th>{{width_plate}}</th>
</tr>
<tr>
    <th>Length of plate settler material</th>
    <th>{{L.SedPlateSheet}}</th>
</tr>
<tr>
    <th>Thickness of plate settler material</th>
    <th>{{thickness_plate}}</th>
</tr>
</table style="width:100%">

The treatment processes – preliminary sedimentation, coagulation, flow control, rapid mix, {{EN.FlocType}} hydraulic flocculation, hydraulic upflow sedimentation, filtration, and chlorination – have been designed according to the maximum flow rate, {{maximum_flow_rate}}. While the resulting dimensions and layout have been cost optimized wherever possible, the user may choose to change some calculated values, such as those given in Table 2, to alter the plan view area of the plant for specific site requirements.



#### Table 2. Calculated values for UI.City, UI.Country that may be altered to produce optimized plan view areas for site-specific constraints.

<table style="width:100%">
<tr>
    <th colspan="2">*Variables*</th>
</tr>
<tr>
    <th>Number of sedimentation tanks</th>
    <th>{{number_sedimentation_tank}}</th>
</tr>
<tr>
    <th>Number of sedimentation bays per tank</th>
    <th>{{N.SedBays}}</th>
</tr>
<tr>
    <th>Flocculator depth</th>
    <th>{{flocculation_depth}}</th>
</tr>
<tr>
    <th>Flocculator type</th>
    <th>{{EN.FlocType}}</th>
</tr>
</table>
