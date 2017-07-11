import mpi4py.MPI as mpi

def greet():
    rank = mpi.COMM_WORLD.Get_rank()
    size = mpi.COMM_WORLD.Get_size()
    print("Hello from {0} of {1}!".format(rank,size))

greet()
