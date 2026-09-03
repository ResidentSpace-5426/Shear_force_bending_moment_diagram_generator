from src import beam_solver


def main():

    beam = beam_solver.Beam(length=10.0)


    beam.add_point_force(position=2.0, magnitude=5.0)

    print(beam.point_forces)


if __name__ == "__main__":
    print("Initialization of main successful")
    main()
    