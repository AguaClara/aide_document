### **Entrance tank/preliminary sedimentation**

The main functions of the entrance tank are to remove solids from the water through preliminary sedimentation, to measure the flow through the plant, and to provide a place where the quality of the raw water can be observed. The preliminary sedimentation process removes solids such as sand, silt, and clay from the water before applying the coagulant to the influent. Water enters the plant on the right side of the entrance tank shown in Figure 1. A sample entrance tank for an {{plant_capacity}} plant. Water enters the tank through the inlet pipe shown at the right. Water flows linearly over the hoppers to the end of the tank, where it flows into the orifices of the linear flow orifice meter, and then on to the flocculator.Figure 1 and flows linearly over the top of the inverted pyramidal traps, or hoppers, at the bottom of the tank. The first hopper contains an overflow weir pipe to waste any water entering the plant in excess of the plant flow rate. The overflow pipe has a nominal diameter of {{ND.EtOverflowDrain}}, sized to handle half of the total plant flow rate. A slot is cut from the pipe such that 10% of the vertical dimension of the pipe is lost, giving a {{W.EtOverflowSlot}} wide opening, starting at a height of {{H.EtOverflowCutaway}} below the natural inner diameter of the pipe. The length of the slot is designed to fit along the length of the first hopper, giving an effective weir length (two times the slot length) of {{L.EtOverflowWeir}}. A drain is also embedded into the first hopper, allowing the operator to manually adjust the plant flow rate by opening the flow control valve by a desired amount, wasting water into the channel below. The {{ND.EtFlowControl}} nominal diameter drain is designed to handle the drain the full plant flow rate if needed.

![Figure 1]({{image_name_1}})

*Figure 1. A sample entrance tank for an 18 L/s plant. Water enters the tank through the inlet pipe shown at the right. Water flows linearly over the hoppers to the end of the tank, where it flows into the orifices of the linear flow orifice meter, and then on to the flocculator.*

Large particulates settle out into the hoppers, and collect near the drains at the bottom. When the water reaches the end of the tank, it flows through the orifices of the riser pipe, which acts as a linear flow orifice meter (LFOM). It is designed for a capture velocity of {{W.EtCapture}} to  remove these particulates. A length of {{entrance_tank_length}} is assigned to the entrance tank to correspond to the sedimentation tank length plus enough space to fit the float of the chemical dose controller and the rapid mix pipes. The width, {{entrance_tank_width}}, is then assigned to ensure the minimum desired capture velocity is met while still allowing enough space for a person to fit inside and construct the tank. The depth of the tank is then determined such that the velocity in the upper rectangular portion of the tank does not exceed the velocity in the flocculator, {{flocculation_velocity}}, while ensuring the depth is sufficiently small that the drains are easy to access. In this case, the tank has a height of {{tank_height}}.

To allow for easy maintenance, {{N.EtHoppers}} hoppers must be built into the entrance tank, at an angle of {{AN.EtSlope}}, forcing sediments to slide to the bottom where the {{drain_width}} drains are located. When too much sediment has accumulated, the upper drain pipes must be removed until the sludge is flushed out. Directly below the entrance tank, there is a drain channel to collect the waste.

As the raw water flows from the first hopper to the subsequent ones, it must pass through two trash racks, preventing large debris from entering the treatment process. Having two trash racks allows the plant to run with a grit screen even while the operator cleans one of them. The trash racks are made of rebar and slide into two slots built into the entrance tank wall. The center-to-center distance between the rebar, {{B.EtRebar}}, is set to ensure that debris large enough to clog the orifices in the linear flow orifice meter downstream (LFOM) are kept out.

Suspended particulates in the water settle out over the length of the entrance tank into the hoppers below. When enough sludge has accumulated at the bottom, the hopper stops can be Suspended particulates in the water settle out over the length of the entrance tank into the hoppers below. When enough sludge has accumulated at the bottom, the hopper stops can be removed to flush out the debris down into the drain channel below, and they can then be replaced to resume normal operation. The {{hopper_diameter}} in nominal diameter hopper stop is {{hopper_length}} long, ensuring the top of the pipe is above the maximum water height in the tank. Table 3 summarizes the entrance tank design specifications below.

#### Table 3

<table style="width:100%">
<tr>
    <th colspan="2">*Entrance Tank*</th>
</tr>
<tr>
    <th>Residence time</th>
    <th></th>
</tr>
<tr>
    <th>Capture velocity</th>
    <th></th>
</tr>
<tr>
    <th>Tank length</th>
    <th>1.47 m</th>
</tr>
<tr>
    <th>Tank width</th>
    <th>55.0 cm</th>
</tr>
<tr>
    <th>Tank height</th>
    <th>2.46 m</th>
</tr>
<tr>
    <th>Hopper length</th>
    <th>{{L.EtHopper}}</th>
</tr>
<tr>
    <th>Hopper height</th>
    <th>{{H.EtHopper}}</th>
</tr>
<tr>
    <th>Last slope height</th>
    <th>{{H.EtLastSlope}}</th>
</tr>
<tr>
    <th>Hopper side slope angle</th>
    <th>{{AN.EtSlope}}</th>
</tr>
<tr>
    <th>Hopper back slope angle</th>
    <th></th>
</tr>
<tr>
    <th>Thickness of ledge between hoppers</th>
    <th>{{T.EtHopperLedge}}</th>
</tr>
<tr>
    <th>Number of full hoppers</th>
    <th>{{N.EtFullHopper}}</th>
</tr>
<tr>
    <th colspan="2">*Hopper Drains*</th>
</tr>
<tr>
    <th>Hopper drain diameter</th>
    <th>10.2 cm (4.00 in)</th>
</tr>
<tr>
    <th>Hopper stop length</th>
    <th>2.46 m</th>
</tr>
<tr>
    <th colspan="2">*Flow Control Components*</th>
</tr>
<tr>
    <th>Flow control valve diameter</th>
    <th>{{ND.EtFlowControl}}</th>
</tr>
<tr>
    <th>Overflow weir pipe diameter</th>
    <th>{{ND.EtOverflowDrain}}</th>
</tr>
<tr>
    <th>Overflow weir pipe slot length</th>
    <th></th>
</tr>
<tr>
    <th>Overflow weir slot depth</th>
    <th></th>
</tr>
<tr>
    <th colspan="2">*Trash Rack*</th>
</tr>
<tr>
    <th>Trash rack rebar spacing</th>
    <th></th>
</tr>
<tr>
    <th>Trash rack rebar diameter</th>
    <th></th>
</tr>
</table>
