import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):

    tic = 'QAN.AX'
    filename = f'qan_prc_{year}.csv'
    pth = os.path.join(cfg.DATADIR, filename)
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    yf_example2.yf_prc_to_csv(tic, pth,start,end)


if __name__ == "__main__":
    qan_prc_to_csv(2020)
