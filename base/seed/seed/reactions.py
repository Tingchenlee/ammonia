#!/usr/bin/env python
# encoding: utf-8

name = "seed"
shortDesc = ""
longDesc = """

"""
autoGenerated=True
entry(
    index = 0,
    label = "OX + NX <=> X + NOX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.46e+21,'cm^2/(mol*s)'), n=0, Ea=(131000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 1,
    label = "X + X + O2 <=> OX + OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.023519, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 2,
    label = "NX + NX <=> X + X + N2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.22e+21,'cm^2/(mol*s)'), n=0, Ea=(124000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 3,
    label = "NOX <=> X + NO",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.5e+13,'1/s'), n=0, Ea=(143000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 4,
    label = "X + NH3 <=> NH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.79731, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 5,
    label = "NX + NOX <=> X + X + N2O",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.01e+19,'cm^2/(mol*s)'), n=0, Ea=(98900,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 6,
    label = "X + N2O <=> OX + N2",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.016034, n=0, Ea=(72200,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 7,
    label = "OX + NH3X <=> OHX + NH2_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.85e+23,'cm^2/(mol*s)'), n=0, Ea=(157000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 8,
    label = "OX + NH2_X <=> OHX + NH_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 9,
    label = "OX + NH_X <=> NX + OHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(58500,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 10,
    label = "OHX + NH_X <=> NX + H2O_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(46000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 11,
    label = "OX + H2O_X <=> OHX + OHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+19,'cm^2/(mol*s)'), n=0, Ea=(52700,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

entry(
    index = 12,
    label = "H2O_X <=> X + H2O",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1e+13,'1/s'), n=0, Ea=(40300,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Rebrov_Pt111
""",
)

