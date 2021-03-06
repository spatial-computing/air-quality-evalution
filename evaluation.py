import pandas as pd
import numpy as np
import os
from sklearn.metrics import r2_score

"""
    A seperate program that measures the performance
"""

def get_all_metrics(df, ground_truth, prediction_result):
    result={}
    result["RMSE"]=get_rmse(df, ground_truth, prediction_result)
    result["MAE"]=get_mae(df, ground_truth, prediction_result)
    result["MAPE"]=get_mape(df, ground_truth, prediction_result)
    result["ME"]=get_me(df, ground_truth, prediction_result)
    result["R^2"]=get_r_square(df, ground_truth, prediction_result)
    result["missing rate"]=get_missing_rate(df, ground_truth, prediction_result)
    return result

def get_missing_rate(df, ground_truth, prediction_result):
    return 1-df[ground_truth].count()/df.shape[0]

def get_r_square(df, ground_truth, prediction_result):
    df=df.dropna(axis=0)
    return r2_score(df[ground_truth], df[prediction_result])

def get_sum_of_difference(df, ground_truth, prediction_result):
    return (df[prediction_result]-df[ground_truth]).sum()

def get_me(df, ground_truth, prediction_result):
    return (df[prediction_result]-df[ground_truth]).sum()/(df[prediction_result]-df[ground_truth]).count()


def get_mae(df, ground_truth, prediction_result):
    df['inter_result'] = abs(df[ground_truth] - df[prediction_result])
    mae = df['inter_result'].sum()
    return mae / df.shape[0]


def get_rmse(df, ground_truth, prediction_result):
    df['inter_result'] = (df[ground_truth] - df[prediction_result]) * (df[ground_truth] - df[prediction_result])
    rmse = df['inter_result'].sum()
    return np.sqrt(rmse / df.shape[0])


def get_mape(df, ground_truth, prediction_result):
    df['inter_result'] = abs((df[ground_truth] - df[prediction_result]) / df[ground_truth])
    mape = df['inter_result'].sum()
    return np.sqrt(mape / df.shape[0])


if __name__ == "__main__":
    # file_path = '../data/result/cv_pm25_0.005_1536049127/'
    file_path = 'data/result/utah_180501_180701_validation_pm25_0.005/'
    files = os.listdir(file_path)

    df_list = []
    for each_file in files:
        if each_file[-3:] == 'csv':
            df = pd.read_csv(file_path + each_file, header=0, sep=',')
            df.dropna(inplace=True)
            cols = df.columns
            print(each_file, len(df), get_mae(df, cols[2], cols[3]))
            print(each_file, len(df), get_rmse(df, cols[2], cols[3]))
            print(each_file, len(df), get_mape(df, cols[2], cols[3]))


        print()
    #
    # # file_path = '../data/result/IDW/O3/'
    # file_path = '../data/result/idw_pm25_1536114072/'
    # files = os.listdir(file_path)
    #
    # df_list = []
    # for each_file in files:
    #     if each_file[-3:] == 'csv':
    #         df = pd.DataFrame.from_csv(file_path + each_file, header=0, sep=',')
    #         cols = df.columns
    #         print(each_file, len(df), get_rmse(df, cols))
