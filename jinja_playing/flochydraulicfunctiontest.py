from aide_design.play import*

@u.wraps(1/u.s, [u.m, None, u.degK], False)
def G_avg(hl, Gt, T):
    """Return the average velocity gradient of a flocculator given head
    loss, collision potential and temperature."""
    G = (pc.gravity * hl) / (Gt * pc.viscosity_kinematic(T))
    return G.to(1/u.s)

@u.wraps(u.m**3, [u.m**3/u.s, u.m, None, u.degK], False)
def vol_floc(q_plant, hl, Gt, T):
    """Return the total volume of the flocculator."""
    vol = (Gt / G_avg(hl, Gt, T))*flow_plant
    return vol.to(u.m**3)
