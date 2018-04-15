### Design Parameters



Included is the design for a plant for **{{UI.City}} **having a maximum flow rate of {{maximum_flow_rate}}. The design was created assuming specific input parameters, shown in Table 1 below. The software uses these parameters together with the requested flow rate as variables in a series of hydraulic and geometric calculations that define the dimensions of the various plant components. The goal of the plant with respect to water quality is to reduce the turbidity as much as possible and to have it meet international water quality standards (less than 5 NTU), maintain the color within norms (15 Unidades de Color – UC), disinfect the water with chlorine, and maintain a residual chlorine concentration throughout distribution between 0.3 and 1.0 mg/L. The plant treats water without using electricity, utilizing preliminary sedimentation, flow control, rapid mix, coagulation/flocculation, hydraulic upflow sedimentation, filtration, and chlorination.



#### Table 1: Automated Design Tool assumptions used to calculate the included design.

*Maximum flow rate*:    {{maximum_flow_rate}}

| **Geometric Assumptions**                                    | Parameters                 |
| ------------------------------------------------------------ | -------------------------- |
| Thickness of the plant walls                                 | {{plant_thickness_walls}}  |
| Minimum concrete thickness                                   | {{T.ConcreteMin}}          |
| Minimum tank dimension for construction worker to fit inside | {{W.HumanMin}}             |
| Minimum height from bottom of drain channel to top of walkway so that operator can fit inside | {{H.HumanAccess}}          |
| Minimum width of a channel for constructability              | {{W.ChannelMin}}           |
| Plant freeboard height                                       | {{plant_freeboard_height}} |

| *Entrance Tank*                            | Parameters     |
| ------------------------------------------ | -------------- |
| Maximum hopper angle                       | {{AN.EtSlope}} |
| Maximum upflow velocity                    | {{V.EtUp}}     |
| Maximum water height for ease of operation | {{HW.EtMax}}   |
| Thickness of the ledge between hoppers     | {{T.EtLedge}}  |

| *Chemical Dosing*                                          | Parameters                |                        |
| ---------------------------------------------------------- | ------------------------- | ---------------------- |
| Turnover time for the chemical stock                       | {{Ti.CoagStock}}          |                        |
| Height of the chemical tanks above the constant head tanks | {{height_chemical tanks}} |                        |
| Minor loss coefficient for small diameter tubing           | {{K.CdcTube}}             |                        |
|                                                            | **Coagulant**             | **Chlorine**           |
| Maximum dose                                               | {{maximum_dose}}          | {{C.ChlorineDoseMax}}  |
| Maximum stock concentration                                | {{C.CoagStockMax}}        | {{C.ChlorineStockMax}} |
| Maximum head loss through small-diameter tubing            | {{HL.CoagCdc}}            | {{HL.ChlorCdc}}        |

| *Flocculation*                                  | Parameters                      |
| ----------------------------------------------- | ------------------------------- |
| Minor loss coefficient for flow around a baffle | {{minor_loss_coefficient_flow}} |
| Desired collision potential                     | {{desired_collision_potential}} |
| Desired energy dissipation rate                 | {{ED.Floc}}                     |
| Maximum time required to drain the tank         | {{maximum_time_drain}}          |

| *Sedimentation*                        | Parameters               |
| -------------------------------------- | ------------------------ |
| Angle of side slopes                   | {{angle_side_slopes}}    |
| Angle of plate settlers                | {{angle_plate_settlers}} |
| Angle of floc hopper slopes            | {{AN.SedHopperSlope}}    |
| Minimum spacing between plate settlers | {{S.SedPlateMin}}        |
| Upflow velocity                        | {{up flow_velocity}}     |
| Capture velocity                       | {{capture_velocity}}     |

| *Stacked Rapid Sand Filter*                               | Parameters              |
| --------------------------------------------------------- | ----------------------- |
| Wall thickness                                            | {{wall_thickness}}      |
| Backwash velocity                                         | {{backwash_velocity}}   |
| Number of sand layers                                     | {{number_sand_layers}}  |
| Time required to drain backwash water above fluidized bed | {{T.FiBwInitiationBod}} |

| *Material Dimensions*               | Parameters          |
| ----------------------------------- | ------------------- |
| Width of plate settler material     | {{width_plate}}     |
| Length of plate settler material    | {{L.SedPlateSheet}} |
| Thickness of plate settler material | {{thickness_plate}} |

The treatment processes – preliminary sedimentation, coagulation, flow control, rapid mix, {{EN.FlocType}} hydraulic flocculation, hydraulic upflow sedimentation, filtration, and chlorination – have been designed according to the maximum flow rate, {{maximum_flow_rate}}. While the resulting dimensions and layout have been cost optimized wherever possible, the user may choose to change some calculated values, such as those given in Table 2, to alter the plan view area of the plant for specific site requirements.



#### Table 2. Calculated values for UI.City, UI.Country that may be altered to produce optimized plan view areas for site-specific constraints.

| Variables                             | Parameters                    |
| ------------------------------------- | ----------------------------- |
| Number of sedimentation tanks         | {{number_sedimentation_tank}} |
| Number of sedimentation bays per tank | {{N.SedBays}}                 |
| Flocculator depth                     | {{flocculation_depth}}        |
| Flocculator type                      | {{EN.FlocType}}               |
<table style="width:100%">
  <tr>
    <td colspan="2">Lastname</td> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td> 
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td> 
    <td>94</td>
  </tr>
</table>