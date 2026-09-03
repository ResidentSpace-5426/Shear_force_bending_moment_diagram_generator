# Shear force diagram and bending moment diagram generator

## Description

The goal of this tool is to generate the shear force and bending moment diagrams for an arbitrayr beam. This is meant to speed up the design process and anylisation of beams.

## Project requirements

- Be able to handle:
  - Point forces
  - Point moments
  - Linear distrubuted loads
  - Equation driven distrubuted loads
- Provide an image of the beam that is being analysed.

## Python packages

- nump
- matplotlib

## Functioning

Generation of a beam object with `beam_1 = beam_solver.Beam(length=x)` where x is the length of the beam.

Add point forces, point moments and distrubuted loads with their respective `beam.add_...` functions, passing in the required information.
