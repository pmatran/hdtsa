import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import time


def main():
    # ---- Set command line arguments
    descr = 'Run Hydraulic diffusivity from Tidal Signal Analysis example'
    help = '[-s] or [--skip-intro] allows the user to skip the welcoming message before running.'
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('-s', '--skip-intro',
                        action='store_true',
                        default=argparse.SUPPRESS,
                        help=help)

    # -- Collect arguments
    _skip = [v for _, v in parser.parse_args()._get_kwargs()]

    # -- Process intro
    if not _skip:
        # -- Request user name and print welcoming message
        check_as = input("Hello there, are you Ahmed Sebaa [y/n] : ")
        if check_as == 'y':
            print('I KNEW IT !! Welcome to my evaluated git project, hope you will like it.')
        else:
            user_name = input(f'Ahhh ... Nevermind, why what is your name though [user_name]? ')
            print(f'So, welcome {user_name}!\n')
        time.sleep(6)

        # -- Print asccii art on console
        aa = r"""

        ____                    _                __  ______  ___________ ___                                       __   
       / __ \__  ______  ____  (_)___  ____ _   / / / / __ \/_  __/ ___//   |     ___  _  ______ _____ ___  ____  / /__ 
      / /_/ / / / / __ \/ __ \/ / __ \/ __ `/  / /_/ / / / / / /  \__ \/ /| |    / _ \| |/_/ __ `/ __ `__ \/ __ \/ / _ \
     / _, _/ /_/ / / / / / / / / / / / /_/ /  / __  / /_/ / / /  ___/ / ___ |   /  __/>  </ /_/ / / / / / / /_/ / /  __/
    /_/ |_|\__,_/_/ /_/_/ /_/_/_/ /_/\__, /  /_/ /_/_____/ /_/  /____/_/  |_|   \___/_/|_|\__,_/_/ /_/ /_/ .___/_/\___/ 
                                    /____/                                                              /_/             
             
        """
        print(aa)
        time.sleep(2)

    # -- Read 2019 data (excel)
    path = os.path.join('data', 'TSA_Reunion2019.xlsx')
    df_tsa = pd.read_excel(path,
                           sheet_name='tsa',
                           index_col=0)  # Tidal Signal Analysis

    # -- Rename 3 last columns
    df_tsa.columns = ['Name', 'RGR692_X ', 'RGR692_Y ', 'xc', 'alpha', 'phi']

    # -- Filter outliers
    df = df_tsa.query("alpha < 1")

    # -- Plot alpha vs phi
    fig = plt.figure(figsize=(8, 8))
    plt.scatter(x=abs(df['phi']), y=df['alpha'],
                marker='+', c='black')
    plt.title('Signal attenuation VS shift',
              fontsize=14, fontweight='bold')
    plt.ylabel(r'$\alpha$', fontsize=14)
    plt.xlabel(r'$\phi$', fontsize=14)
    plt.grid(color='grey', ls=':', lw=0.5)
    plt.show()

    # -- Read transmitivities values
    df_trans = pd.read_excel(path,
                             sheet_name='trans',
                             index_col=0)  # Hydraulic Transmisivities

    # -- Compute mean logarithmic transmissivity
    logT = df_trans.transmissivity.transform('log10').mean()
    T = np.power(10, logT)
    print(f"\nMean transmissivity (T) : {round(T, 4)} m²/s\n")


if __name__ == "__main__":
    main()
