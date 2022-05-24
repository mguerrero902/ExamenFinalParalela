from __future__ import print_function
import time
import argparse

from heat import init_fields as init_fields_py, write_field as write_field_py, iterate as iterate_py
try:
    from heat_cyt import init_fields as init_fields_cyt, write_field as write_field_cyt, iterate as iterate_cyt
except ImportError:
    pass

def main(input_file='bottle.dat', a=0.5, dx=0.1, dy=0.1, 
         timesteps=100, image_interval=4000, version='py'):

    # Initialise the temperature field
    if version == 'py':
        field, field0 = init_fields_py(input_file)
       
        # Plot/save initial field
        write_field_py(field, 0)
        # Iterate
        t0 = time.time()
        iterate_py(field, field0, a, dx, dy, timesteps, image_interval)
        t1 = time.time()
        # Plot/save final field
        write_field_py(field, timesteps)

        print("{0}".format(t1-t0))
    elif version =='cyt':
        
        field, field0 = init_fields_cyt(input_file)
        
        # Plot/save initial field
        write_field_cyt(field, 0)
        # Iterate
        t0 = time.time()
        iterate_cyt(field, field0, a, dx, dy, timesteps, image_interval)
        t1 = time.time()
        # Plot/save final field
        write_field_cyt(field, timesteps)
        time1 = str((t1-t0)).replace('.',',')
        print("{}".format(time1))
        
        

if __name__ == '__main__':

    # Process command line arguments
    parser = argparse.ArgumentParser(description='Heat equation')
    parser.add_argument('-dx', type=float, default=0.01,
                        help='grid spacing in x-direction')
    parser.add_argument('-dy', type=float, default=0.01,
                        help='grid spacing in y-direction')
    parser.add_argument('-a', type=float, default=0.5,
                        help='diffusion constant')
    parser.add_argument('-n', type=int, default=100,
                        help='number of time steps')
    parser.add_argument('-i', type=int, default=4000,
                        help='image interval')
    parser.add_argument('-f', type=str, default='bottle.dat', 
                        help='input file')
    parser.add_argument('-v', type=str, default='py', 
                        help='version')

    args = parser.parse_args()

    main(args.f, args.a, args.dx, args.dy, args.n, args.i, args.v)

