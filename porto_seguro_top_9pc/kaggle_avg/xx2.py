import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
import itertools

def GiniScore(y_actual, y_pred):
    return 2 * roc_auc_score(y_actual, y_pred) - 1


def Outputs(p):
    return 1. / (1. + np.exp(-p))


def GPI(data):
    v = pd.DataFrame()
    v["0"] = -3.274750
    v["1"] = 0.020000 * np.tanh((data["loo_ps_ind_06_bin"] + (
    data["ps_reg_01"] + (data["ps_car_12"] + (data["loo_ps_car_03_cat"] + data["loo_ps_car_07_cat"])))))
    v["2"] = 0.020000 * np.tanh((data["loo_ps_ind_17_bin"] + (
    (data["ps_reg_03"] + data["ps_car_12"]) + (data["loo_ps_ind_06_bin"] + data["loo_ps_ind_05_cat"]))))
    v["3"] = 0.020000 * np.tanh((data["loo_ps_car_01_cat"] + (
    data["loo_ps_ind_17_bin"] + ((data["ps_car_12"] + data["ps_reg_03"]) + data["loo_ps_ind_07_bin"]))))
    v["4"] = 0.020000 * np.tanh(
        (data["loo_ps_car_01_cat"] + ((data["loo_ps_car_04_cat"] + (data["ps_reg_03"] + data["ps_car_15"])) * 3.0)))
    v["5"] = 0.020000 * np.tanh(((data["ps_car_13"] + (
    (data["loo_ps_car_05_cat"] + (data["ps_reg_01"] + data["loo_ps_car_09_cat"])) / 2.0)) * (10.28825187683105469)))
    v["6"] = 0.020000 * np.tanh(((8.0) * (
    data["loo_ps_car_04_cat"] + ((data["loo_ps_car_01_cat"] + data["loo_ps_ind_05_cat"]) + data["ps_car_15"]))))
    v["7"] = 0.020000 * np.tanh(((data["ps_car_13"] + (
    ((data["loo_ps_car_01_cat"] + data["ps_reg_03"]) + data["loo_ps_ind_16_bin"]) / 2.0)) * 8.428570))
    v["8"] = 0.020000 * np.tanh(((10.86397266387939453) * (
    ((data["ps_reg_03"] + data["loo_ps_car_07_cat"]) + data["loo_ps_ind_06_bin"]) + data["loo_ps_car_11_cat"])))
    v["9"] = 0.020000 * np.tanh((data["ps_reg_03"] + (
    data["loo_ps_ind_16_bin"] + (data["loo_ps_ind_07_bin"] + (data["ps_car_13"] + data["loo_ps_car_03_cat"])))))
    v["10"] = 0.020000 * np.tanh((((data["ps_car_13"] + data["ps_reg_02"]) - data["ps_ind_15"]) + (
    data["loo_ps_car_11_cat"] + data["loo_ps_ind_17_bin"])))
    v["11"] = 0.020000 * np.tanh(((data["ps_car_13"] + data["ps_reg_02"]) + (
    data["loo_ps_ind_07_bin"] + (data["loo_ps_ind_17_bin"] + data["loo_ps_car_01_cat"]))))
    v["12"] = 0.020000 * np.tanh(((data["ps_car_13"] + (
    data["ps_reg_02"] + ((data["loo_ps_car_09_cat"] + data["loo_ps_ind_16_bin"]) / 2.0))) * 8.428570))
    v["13"] = 0.020000 * np.tanh((data["ps_reg_02"] + (
    data["loo_ps_ind_08_bin"] + ((data["loo_ps_ind_16_bin"] + data["ps_car_13"]) + data["loo_ps_ind_07_bin"]))))
    v["14"] = 0.020000 * np.tanh((29.500000 * (
    ((data["ps_car_13"] + (data["loo_ps_car_09_cat"] + data["loo_ps_ind_16_bin"])) / 2.0) + data["loo_ps_ind_05_cat"])))
    v["15"] = 0.020000 * np.tanh(
        (29.500000 * ((data["loo_ps_car_04_cat"] + (data["loo_ps_car_03_cat"] + data["ps_car_13"])) + 0.945455)))
    v["16"] = 0.020000 * np.tanh((8.428570 * (
    (data["loo_ps_ind_05_cat"] + data["loo_ps_car_06_cat"]) + (data["loo_ps_car_07_cat"] + data["loo_ps_ind_17_bin"]))))
    v["17"] = 0.020000 * np.tanh(
        (((0.633333 + (data["loo_ps_ind_17_bin"] + data["ps_car_13"])) + data["ps_reg_03"]) * 29.500000))
    v["18"] = 0.020000 * np.tanh((((data["loo_ps_ind_17_bin"] + data["loo_ps_car_11_cat"]) + (
    data["loo_ps_car_07_cat"] - data["ps_ind_15"])) + data["ps_ind_03"]))
    v["19"] = 0.020000 * np.tanh(((data["loo_ps_car_07_cat"] + (
    data["loo_ps_ind_05_cat"] + (data["loo_ps_ind_09_bin"] + data["loo_ps_ind_06_bin"]))) * (4.85490655899047852)))
    v["20"] = 0.020000 * np.tanh(((((data["loo_ps_ind_06_bin"] + data["loo_ps_car_11_cat"]) + data[
        "loo_ps_car_07_cat"]) + data["loo_ps_car_09_cat"]) - data["ps_ind_15"]))
    v["21"] = 0.020000 * np.tanh((8.428570 * (
    (data["loo_ps_ind_05_cat"] + data["ps_car_13"]) + ((data["loo_ps_car_05_cat"] + data["loo_ps_car_01_cat"]) / 2.0))))
    v["22"] = 0.020000 * np.tanh((((data["ps_ind_03"] + (
    data["loo_ps_ind_16_bin"] + (data["loo_ps_ind_05_cat"] + data["loo_ps_ind_06_bin"]))) / 2.0) * 29.500000))
    v["23"] = 0.020000 * np.tanh(((data["loo_ps_ind_17_bin"] + (
    data["loo_ps_ind_09_bin"] + (data["ps_reg_03"] + data["loo_ps_ind_05_cat"]))) * 29.500000))
    v["24"] = 0.020000 * np.tanh((data["loo_ps_car_03_cat"] - (
    data["ps_ind_15"] - (data["loo_ps_ind_05_cat"] + ((data["loo_ps_ind_07_bin"] + data["loo_ps_ind_17_bin"]) / 2.0)))))
    v["25"] = 0.020000 * np.tanh(
        ((data["ps_reg_02"] + ((data["loo_ps_car_07_cat"] - -1.0) + data["ps_car_13"])) * (13.29769420623779297)))
    v["26"] = 0.020000 * np.tanh((29.500000 * ((((data["loo_ps_car_01_cat"] + data["ps_car_13"]) / 2.0) + (
    data["loo_ps_ind_05_cat"] + data["loo_ps_ind_17_bin"])) / 2.0)))
    v["27"] = 0.020000 * np.tanh((data["ps_reg_03"] + (
    1.480000 + (data["loo_ps_ind_06_bin"] + (data["loo_ps_car_11_cat"] + data["loo_ps_car_01_cat"])))))
    v["28"] = 0.020000 * np.tanh((data["loo_ps_car_11_cat"] + (
    (data["loo_ps_ind_05_cat"] + (data["loo_ps_car_09_cat"] - data["ps_ind_15"])) + data["loo_ps_car_03_cat"])))
    v["29"] = 0.020000 * np.tanh(((10.24501132965087891) * (
    data["loo_ps_ind_05_cat"] + (data["ps_ind_03"] + (data["loo_ps_ind_09_bin"] - data["ps_ind_15"])))))
    v["30"] = 0.020000 * np.tanh(((data["loo_ps_car_11_cat"] + (
    data["loo_ps_ind_05_cat"] + data["loo_ps_car_07_cat"])) + (data["loo_ps_car_09_cat"] - data["missing"])))
    v["31"] = 0.020000 * np.tanh((29.500000 * (
    data["loo_ps_car_01_cat"] + ((data["loo_ps_car_07_cat"] + data["loo_ps_ind_05_cat"]) + data["loo_ps_ind_16_bin"]))))
    v["32"] = 0.020000 * np.tanh(
        ((data["ps_reg_03"] + ((data["ps_ind_01"] + 0.887097) + data["loo_ps_car_09_cat"])) * (10.0)))
    v["33"] = 0.020000 * np.tanh(
        ((data["loo_ps_car_03_cat"] + (data["loo_ps_car_03_cat"] - (data["ps_ind_15"] - 1.480000))) * 29.500000))
    v["34"] = 0.020000 * np.tanh((data["loo_ps_car_09_cat"] + (
    (14.32789230346679688) * (data["ps_ind_03"] + (data["ps_ind_03"] * data["ps_ind_03"])))))
    v["35"] = 0.020000 * np.tanh((29.500000 * (
    data["loo_ps_ind_17_bin"] + (((data["ps_car_13"] + data["ps_ind_03"]) / 2.0) + data["loo_ps_ind_05_cat"]))))
    v["36"] = 0.020000 * np.tanh(
        ((9.0) * (data["ps_reg_02"] + (data["loo_ps_car_07_cat"] + ((data["ps_car_15"] + 1.0) / 2.0)))))
    v["37"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] + (
    data["loo_ps_ind_08_bin"] + ((data["loo_ps_ind_16_bin"] + data["loo_ps_ind_07_bin"]) / 2.0))) * 8.428570))
    v["38"] = 0.020000 * np.tanh(((2.0 * (
    (data["loo_ps_car_03_cat"] + data["loo_ps_car_07_cat"]) + data["loo_ps_ind_05_cat"])) + data["loo_ps_car_04_cat"]))
    v["39"] = 0.020000 * np.tanh(
        (29.500000 * (data["loo_ps_ind_07_bin"] + ((data["loo_ps_car_07_cat"] + 1.089890) - data["ps_ind_15"]))))
    v["40"] = 0.020000 * np.tanh(((10.18701076507568359) * (
    (data["ps_ind_03"] * data["ps_ind_03"]) + (data["loo_ps_ind_05_cat"] + data["ps_ind_03"]))))
    v["41"] = 0.020000 * np.tanh((8.428570 * (
    data["loo_ps_ind_02_cat"] + (data["ps_car_13"] + (data["loo_ps_car_07_cat"] + data["loo_ps_ind_09_bin"])))))
    v["42"] = 0.020000 * np.tanh(
        (8.428570 * (((data["loo_ps_car_01_cat"] - 0.435484) + data["loo_ps_ind_05_cat"]) + data["loo_ps_ind_17_bin"])))
    v["43"] = 0.020000 * np.tanh(
        (data["loo_ps_car_09_cat"] + (29.500000 * (data["ps_ind_03"] + (data["ps_ind_03"] * data["ps_ind_03"])))))
    v["44"] = 0.020000 * np.tanh((8.428570 * (
    (data["loo_ps_ind_05_cat"] + data["loo_ps_car_09_cat"]) - (data["ps_ind_15"] + data["loo_ps_ind_18_bin"]))))
    v["45"] = 0.020000 * np.tanh(
        (data["ps_ind_01"] + ((5.76565647125244141) * (data["loo_ps_ind_07_bin"] + (0.887097 - data["ps_ind_15"])))))
    v["46"] = 0.020000 * np.tanh(((7.0) * (2.352940 * ((data["ps_ind_03"] * data["ps_ind_03"]) + data["ps_ind_03"]))))
    v["47"] = 0.020000 * np.tanh((29.500000 * (
    (data["loo_ps_ind_17_bin"] + (data["loo_ps_ind_17_bin"] + data["loo_ps_ind_05_cat"])) - data["ps_ind_03"])))
    v["48"] = 0.020000 * np.tanh(((9.90538215637207031) * (
    ((data["loo_ps_ind_06_bin"] + data["loo_ps_car_07_cat"]) + data["loo_ps_ind_09_bin"]) + data["loo_ps_ind_09_bin"])))
    v["49"] = 0.020000 * np.tanh((data["ps_ind_01"] + (
    (data["loo_ps_car_01_cat"] + (data["ps_ind_01"] + data["loo_ps_ind_06_bin"])) + data["loo_ps_car_09_cat"])))
    v["50"] = 0.020000 * np.tanh((29.500000 * (data["loo_ps_ind_02_cat"] + (
    data["loo_ps_car_09_cat"] + ((data["loo_ps_car_07_cat"] + data["loo_ps_ind_05_cat"]) / 2.0)))))
    v["51"] = 0.020000 * np.tanh(
        (29.500000 * (data["ps_car_13"] + (data["loo_ps_ind_05_cat"] + (data["loo_ps_ind_06_bin"] - 2.352940)))))
    v["52"] = 0.020000 * np.tanh((29.500000 * (
    data["loo_ps_ind_04_cat"] + (data["loo_ps_ind_05_cat"] + (data["loo_ps_ind_07_bin"] * data["ps_ind_03"])))))
    v["53"] = 0.020000 * np.tanh(
        (29.500000 * (((9.0) * ((data["loo_ps_ind_04_cat"] + data["ps_reg_03"]) / 2.0)) - data["ps_ind_15"])))
    v["54"] = 0.020000 * np.tanh((data["loo_ps_ind_17_bin"] + (
    data["loo_ps_ind_04_cat"] + (data["loo_ps_ind_17_bin"] + (data["ps_reg_02"] * data["loo_ps_ind_05_cat"])))))
    v["55"] = 0.020000 * np.tanh((data["loo_ps_car_09_cat"] + (
    (data["loo_ps_ind_06_bin"] * (data["ps_ind_03"] + data["loo_ps_ind_05_cat"])) - data["ps_car_11"])))
    v["56"] = 0.020000 * np.tanh(((data["ps_ind_01"] + (data["ps_ind_03"] + data["loo_ps_ind_05_cat"])) * (
    data["loo_ps_ind_07_bin"] + data["loo_ps_car_05_cat"])))
    v["57"] = 0.020000 * np.tanh(((data["loo_ps_ind_16_bin"] * data["loo_ps_car_03_cat"]) - (
    data["ps_ind_15"] - ((data["ps_reg_02"] + data["loo_ps_ind_02_cat"]) / 2.0))))
    v["58"] = 0.020000 * np.tanh(
        (((data["ps_car_13"] + -2.0) + (data["loo_ps_ind_05_cat"] - data["ps_ind_15"])) - data["ps_car_11"]))
    v["59"] = 0.020000 * np.tanh(
        ((data["ps_car_15"] + (3.0 * data["loo_ps_ind_17_bin"])) + (data["ps_ind_03"] * data["ps_ind_03"])))
    v["60"] = 0.020000 * np.tanh((29.500000 * ((data["ps_ind_03"] * data["ps_ind_03"]) + data["ps_ind_03"])))
    v["61"] = 0.020000 * np.tanh((((data["loo_ps_ind_17_bin"] + data["missing"]) + (
    data["loo_ps_car_11_cat"] + data["loo_ps_ind_17_bin"])) * data["loo_ps_car_05_cat"]))
    v["62"] = 0.020000 * np.tanh((8.428570 + (
    ((data["loo_ps_car_03_cat"] * data["loo_ps_ind_09_bin"]) + data["loo_ps_car_01_cat"]) * 29.500000)))
    v["63"] = 0.020000 * np.tanh(((data["ps_ind_01"] + (data["loo_ps_car_11_cat"] + data["loo_ps_car_05_cat"])) * (
    data["loo_ps_ind_05_cat"] - data["ps_car_11"])))
    v["64"] = 0.020000 * np.tanh((data["loo_ps_car_09_cat"] + (
    data["ps_ind_01"] + (data["loo_ps_ind_09_bin"] * (data["ps_ind_03"] + data["ps_ind_01"])))))
    v["65"] = 0.020000 * np.tanh(((data["loo_ps_car_11_cat"] + data["loo_ps_ind_02_cat"]) + (
    data["loo_ps_car_05_cat"] * (data["loo_ps_ind_09_bin"] + data["loo_ps_ind_06_bin"]))))
    v["66"] = 0.020000 * np.tanh((((data["loo_ps_ind_05_cat"] * data["loo_ps_ind_06_bin"]) * 29.500000) + (
    data["loo_ps_ind_02_cat"] * data["loo_ps_ind_05_cat"])))
    v["67"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] - data["ps_reg_01"]) * (
    (data["ps_ind_01"] + data["loo_ps_ind_06_bin"]) + data["loo_ps_car_11_cat"])))
    v["68"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] - data["ps_car_11"]) * (
    3.0 * (data["loo_ps_ind_17_bin"] + data["loo_ps_car_04_cat"]))))
    v["69"] = 0.019996 * np.tanh(
        (((data["ps_reg_02"] - data["ps_car_11"]) + (data["loo_ps_ind_04_cat"] * 3.0)) - data["ps_ind_15"]))
    v["70"] = 0.020000 * np.tanh(
        (-((data["loo_ps_ind_02_cat"] * (data["ps_ind_03"] + (data["ps_ind_03"] + data["ps_ind_03"]))))))
    v["71"] = 0.020000 * np.tanh((data["loo_ps_ind_17_bin"] + (
    data["missing"] + ((8.37885093688964844) * (data["loo_ps_ind_17_bin"] + data["loo_ps_ind_02_cat"])))))
    v["72"] = 0.020000 * np.tanh((data["loo_ps_car_09_cat"] + (
    data["ps_reg_03"] + (1.480000 * (data["loo_ps_car_04_cat"] * data["ps_ind_01"])))))
    v["73"] = 0.020000 * np.tanh(((((5.0) * data["loo_ps_ind_05_cat"]) + data["loo_ps_car_09_cat"]) * (
    data["loo_ps_ind_17_bin"] + data["ps_reg_03"])))
    v["74"] = 0.020000 * np.tanh(((((data["loo_ps_ind_07_bin"] + data["loo_ps_car_01_cat"]) / 2.0) * data[
        "loo_ps_ind_16_bin"]) + (data["ps_ind_15"] * data["loo_ps_ind_18_bin"])))
    v["75"] = 0.020000 * np.tanh((((data["loo_ps_ind_05_cat"] * data["loo_ps_car_01_cat"]) + data[
        "loo_ps_car_05_cat"]) * (data["loo_ps_ind_05_cat"] - data["ps_ind_15"])))
    v["76"] = 0.020000 * np.tanh((data["loo_ps_ind_16_bin"] * (
    (data["loo_ps_car_04_cat"] + data["loo_ps_ind_05_cat"]) + (data["loo_ps_car_07_cat"] + data["ps_ind_03"]))))
    v["77"] = 0.020000 * np.tanh(((data["loo_ps_car_05_cat"] + data["loo_ps_car_03_cat"]) * (
    data["ps_ind_03"] + (data["missing"] + data["loo_ps_ind_05_cat"]))))
    v["78"] = 0.020000 * np.tanh(((data["ps_ind_01"] * data["loo_ps_car_03_cat"]) + (
    data["loo_ps_car_08_cat"] + (data["loo_ps_ind_17_bin"] * data["loo_ps_car_03_cat"]))))
    v["79"] = 0.020000 * np.tanh((data["ps_ind_03"] * (3.0 * (3.0 * (-(data["loo_ps_ind_02_cat"]))))))
    v["80"] = 0.020000 * np.tanh((((data["loo_ps_ind_05_cat"] + data["loo_ps_ind_05_cat"]) * (
    data["loo_ps_car_09_cat"] + data["ps_reg_03"])) - data["loo_ps_ind_16_bin"]))
    v["81"] = 0.020000 * np.tanh((data["loo_ps_car_03_cat"] * (
    (data["loo_ps_ind_09_bin"] - data["ps_car_15"]) + (data["loo_ps_ind_02_cat"] - data["loo_ps_ind_18_bin"]))))
    v["82"] = 0.020000 * np.tanh((((data["ps_ind_01"] + data["loo_ps_ind_06_bin"]) * (
    data["loo_ps_ind_16_bin"] - data["ps_reg_01"])) + data["loo_ps_car_07_cat"]))
    v["83"] = 0.020000 * np.tanh((data["ps_ind_15"] * (
    data["loo_ps_ind_16_bin"] - ((data["loo_ps_car_11_cat"] + data["missing"]) + data["loo_ps_ind_17_bin"]))))
    v["84"] = 0.020000 * np.tanh((((data["loo_ps_ind_07_bin"] + data["loo_ps_ind_02_cat"]) / 2.0) + (
    data["ps_ind_01"] * (0.600000 - data["ps_ind_15"]))))
    v["85"] = 0.020000 * np.tanh(
        ((data["ps_ind_01"] + data["loo_ps_car_04_cat"]) * ((data["loo_ps_ind_05_cat"] - data["ps_ind_15"]) + -1.0)))
    v["86"] = 0.020000 * np.tanh((data["loo_ps_ind_04_cat"] + (
    data["ps_reg_03"] + (data["ps_reg_03"] + (data["loo_ps_ind_17_bin"] * data["loo_ps_car_07_cat"])))))
    v["87"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    (((4.0) * data["loo_ps_ind_17_bin"]) + data["loo_ps_car_06_cat"]) - data["ps_reg_01"])))
    v["88"] = 0.020000 * np.tanh(((-1.0 + data["loo_ps_ind_12_bin"]) - (
    data["loo_ps_car_10_cat"] + (data["ps_car_11"] - data["loo_ps_car_09_cat"]))))
    v["89"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    (data["loo_ps_car_09_cat"] + ((-1.0 + data["ps_reg_03"]) / 2.0)) + data["ps_reg_03"])))
    v["90"] = 0.020000 * np.tanh((((data["loo_ps_ind_09_bin"] + data["loo_ps_ind_05_cat"]) * (
    (data["loo_ps_ind_05_cat"] + data["loo_ps_ind_17_bin"]) / 2.0)) - data["loo_ps_ind_05_cat"]))
    v["91"] = 0.020000 * np.tanh((-(
    ((data["loo_ps_ind_02_cat"] + data["loo_ps_ind_02_cat"]) * (data["ps_ind_03"] + data["loo_ps_ind_06_bin"])))))
    v["92"] = 0.020000 * np.tanh(
        (data["loo_ps_ind_04_cat"] + (data["ps_reg_03"] * ((-(data["ps_reg_01"])) + data["loo_ps_ind_17_bin"]))))
    v["93"] = 0.020000 * np.tanh(((data["loo_ps_ind_02_cat"] * 29.500000) * (
    data["loo_ps_car_08_cat"] + (data["loo_ps_car_08_cat"] - data["ps_ind_03"]))))
    v["94"] = 0.020000 * np.tanh((((data["loo_ps_car_03_cat"] * data["loo_ps_car_09_cat"]) * (
    data["loo_ps_car_04_cat"] * data["loo_ps_car_04_cat"])) - data["loo_ps_car_04_cat"]))
    v["95"] = 0.020000 * np.tanh(((data["loo_ps_car_07_cat"] + -1.0) - (data["ps_car_12"] * (2.0 * data["ps_car_11"]))))
    v["96"] = 0.020000 * np.tanh((-(
    (data["ps_reg_03"] * ((data["loo_ps_car_01_cat"] - data["loo_ps_car_03_cat"]) + data["loo_ps_ind_08_bin"])))))
    v["97"] = 0.020000 * np.tanh((data["loo_ps_ind_16_bin"] * (
    data["loo_ps_car_07_cat"] + (((data["loo_ps_ind_07_bin"] + data["ps_car_12"]) / 2.0) - data["ps_reg_01"]))))
    v["98"] = 0.020000 * np.tanh(((((data["loo_ps_ind_07_bin"] + data["ps_ind_15"]) / 2.0) + data[
        "loo_ps_ind_17_bin"]) * (data["loo_ps_ind_05_cat"] + data["loo_ps_ind_05_cat"])))
    v["99"] = 0.019992 * np.tanh(
        ((data["loo_ps_ind_05_cat"] * data["loo_ps_car_09_cat"]) + (-((data["ps_reg_01"] * data["ps_ind_03"])))))
    v["100"] = 0.019988 * np.tanh((data["loo_ps_ind_04_cat"] + (
    data["loo_ps_car_05_cat"] * (data["ps_ind_01"] + (data["ps_ind_01"] + data["loo_ps_car_01_cat"])))))
    v["101"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    data["loo_ps_ind_05_cat"] * np.tanh((data["loo_ps_ind_05_cat"] + (-(2.352940)))))))
    v["102"] = 0.020000 * np.tanh(
        (-((data["ps_reg_01"] * (data["loo_ps_car_09_cat"] + (data["ps_reg_03"] + data["loo_ps_ind_05_cat"]))))))
    v["103"] = 0.020000 * np.tanh(
        ((-1.0 + (data["loo_ps_car_09_cat"] + ((data["ps_reg_01"] * data["ps_reg_01"]) + data["ps_reg_01"]))) / 2.0))
    v["104"] = 0.020000 * np.tanh(((data["loo_ps_ind_17_bin"] + ((data["loo_ps_ind_02_cat"] + -2.0) / 2.0)) * (
    data["loo_ps_ind_05_cat"] - data["ps_car_15"])))
    v["105"] = 0.019992 * np.tanh((((data["loo_ps_ind_17_bin"] + data["loo_ps_car_07_cat"]) + data[
        "loo_ps_ind_17_bin"]) * ((data["ps_reg_02"] + data["loo_ps_car_09_cat"]) / 2.0)))
    v["106"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    data["loo_ps_ind_07_bin"] + (data["loo_ps_ind_07_bin"] + (data["loo_ps_car_09_cat"] + -1.0)))))
    v["107"] = 0.020000 * np.tanh(((data["ps_car_15"] + (data["loo_ps_ind_07_bin"] * data["loo_ps_ind_17_bin"])) - (
    data["ps_reg_03"] * data["loo_ps_car_01_cat"])))
    v["108"] = 0.020000 * np.tanh((data["loo_ps_ind_04_cat"] * (
    (data["loo_ps_ind_04_cat"] - (data["loo_ps_ind_06_bin"] - 0.432099)) - data["loo_ps_car_01_cat"])))
    v["109"] = 0.019988 * np.tanh(
        (data["loo_ps_ind_02_cat"] - (data["ps_ind_01"] * (-2.0 + (data["ps_ind_01"] * data["ps_ind_01"])))))
    v["110"] = 0.020000 * np.tanh(((29.500000 + (data["ps_car_15"] * 29.500000)) * (0.791667 - data["ps_car_15"])))
    v["111"] = 0.020000 * np.tanh(((((data["loo_ps_ind_04_cat"] + -1.0) + data["loo_ps_car_08_cat"]) / 2.0) + (
    data["loo_ps_ind_05_cat"] * data["ps_reg_03"])))
    v["112"] = 0.020000 * np.tanh((data["loo_ps_car_01_cat"] * (
    (data["ps_reg_03"] * ((data["loo_ps_car_05_cat"] + data["ps_reg_03"]) / 2.0)) - data["ps_car_15"])))
    v["113"] = 0.020000 * np.tanh((data["ps_reg_02"] * (
    (data["loo_ps_ind_17_bin"] - data["loo_ps_car_01_cat"]) - (data["ps_ind_01"] - data["loo_ps_ind_17_bin"]))))
    v["114"] = 0.020000 * np.tanh(
        (data["ps_ind_03"] * (data["ps_reg_03"] - (1.480000 + (data["ps_ind_15"] - data["ps_reg_03"])))))
    v["115"] = 0.019988 * np.tanh(((((data["loo_ps_car_01_cat"] + (data["ps_car_11"] * data["ps_car_11"])) / 2.0) + (
    data["ps_reg_01"] * data["missing"])) / 2.0))
    v["116"] = 0.020000 * np.tanh(((data["loo_ps_ind_04_cat"] * (
    (data["loo_ps_ind_04_cat"] - data["ps_ind_01"]) + data["ps_ind_03"])) - data["loo_ps_ind_02_cat"]))
    v["117"] = 0.020000 * np.tanh((data["loo_ps_car_04_cat"] * (
    (data["loo_ps_car_09_cat"] - data["ps_car_11"]) - ((data["loo_ps_car_06_cat"] + data["loo_ps_car_04_cat"]) / 2.0))))
    v["118"] = 0.020000 * np.tanh((((data["loo_ps_ind_04_cat"] + data["ps_ind_03"]) / 2.0) * (
    (data["loo_ps_car_02_cat"] - data["ps_reg_01"]) + data["loo_ps_car_07_cat"])))
    v["119"] = 0.020000 * np.tanh(((((data["ps_car_15"] * (-(data["loo_ps_car_03_cat"]))) + data[
        "loo_ps_car_01_cat"]) / 2.0) - data["loo_ps_car_07_cat"]))
    v["120"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    (data["loo_ps_ind_05_cat"] * (data["loo_ps_car_03_cat"] * data["loo_ps_car_11_cat"])) - 0.633333)))
    v["121"] = 0.020000 * np.tanh(((((data["loo_ps_ind_05_cat"] + data["ps_car_12"]) + data[
        "loo_ps_ind_18_bin"]) / 2.0) * ((data["missing"] + data["ps_reg_02"]) / 2.0)))
    v["122"] = 0.020000 * np.tanh(((((data["ps_ind_03"] + data["loo_ps_ind_04_cat"]) / 2.0) * (
    (data["ps_ind_03"] + data["loo_ps_ind_04_cat"]) / 2.0)) - 0.432099))
    v["123"] = 0.020000 * np.tanh(((data["ps_reg_03"] * data["ps_reg_03"]) * (
    ((data["loo_ps_ind_05_cat"] - data["ps_reg_03"]) + data["ps_car_12"]) / 2.0)))
    v["124"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    data["ps_car_13"] + ((data["loo_ps_car_04_cat"] - data["ps_ind_03"]) - 1.089890))))
    v["125"] = 0.020000 * np.tanh((((data["loo_ps_car_09_cat"] + -2.0) / 2.0) * (
    data["loo_ps_ind_02_cat"] + (data["ps_car_11"] * data["ps_ind_01"]))))
    v["126"] = 0.019988 * np.tanh(((data["loo_ps_ind_02_cat"] + (
    (data["loo_ps_car_07_cat"] * data["loo_ps_ind_08_bin"]) - (data["ps_ind_15"] * data["loo_ps_car_06_cat"]))) / 2.0))
    v["127"] = 0.020000 * np.tanh((data["loo_ps_car_09_cat"] * (
    data["loo_ps_car_09_cat"] * np.tanh(((data["loo_ps_ind_07_bin"] + (-(data["ps_ind_03"]))) / 2.0)))))
    v["128"] = 0.020000 * np.tanh((((data["missing"] - data["ps_car_11"]) * (
    data["loo_ps_car_01_cat"] - data["loo_ps_car_06_cat"])) - data["loo_ps_car_11_cat"]))
    v["129"] = 0.020000 * np.tanh((data["ps_reg_01"] * (
    -((np.tanh((data["ps_reg_03"] + data["loo_ps_ind_05_cat"])) + data["loo_ps_ind_18_bin"])))))
    v["130"] = 0.020000 * np.tanh(
        (data["loo_ps_ind_02_cat"] * ((data["missing"] + data["ps_car_11"]) + data["ps_ind_15"])))
    v["131"] = 0.019996 * np.tanh((((data["loo_ps_ind_02_cat"] - data["loo_ps_car_04_cat"]) + (
    (data["loo_ps_ind_07_bin"] * data["ps_car_13"]) * data["ps_reg_03"])) / 2.0))
    v["132"] = 0.020000 * np.tanh((data["ps_reg_01"] - (
    0.791667 - (((data["loo_ps_car_11_cat"] * data["loo_ps_car_11_cat"]) + data["loo_ps_ind_02_cat"]) / 2.0))))
    v["133"] = 0.020000 * np.tanh(((data["ps_ind_14"] + ((data["loo_ps_ind_04_cat"] + data["ps_ind_15"]) / 2.0)) * (
    (data["ps_ind_15"] + data["loo_ps_ind_04_cat"]) / 2.0)))
    v["134"] = 0.020000 * np.tanh(((0.791667 - data["ps_ind_01"]) * (
    ((data["ps_ind_03"] + data["loo_ps_ind_04_cat"]) / 2.0) * data["loo_ps_ind_05_cat"])))
    v["135"] = 0.019992 * np.tanh(
        ((-2.0 + (data["ps_car_12"] * ((data["ps_car_12"] - 1.089890) + data["loo_ps_ind_04_cat"]))) / 2.0))
    v["136"] = 0.019977 * np.tanh(((data["loo_ps_car_09_cat"] * (
    data["loo_ps_car_01_cat"] * (data["loo_ps_ind_02_cat"] + data["loo_ps_ind_17_bin"]))) - data["loo_ps_ind_02_cat"]))
    v["137"] = 0.019996 * np.tanh(
        ((-1.0 + ((data["ps_reg_03"] * data["ps_reg_03"]) * data["loo_ps_ind_05_cat"])) * data["loo_ps_ind_05_cat"]))
    v["138"] = 0.020000 * np.tanh(
        (((data["ps_car_11"] * (data["ps_ind_14"] - data["ps_car_12"])) + data["loo_ps_car_09_cat"]) / 2.0))
    v["139"] = 0.019996 * np.tanh((data["loo_ps_car_07_cat"] * (
    (((data["missing"] * data["missing"]) + data["ps_ind_15"]) / 2.0) + data["loo_ps_ind_17_bin"])))
    v["140"] = 0.020000 * np.tanh(
        (data["ps_reg_01"] * ((data["ps_reg_01"] - data["ps_reg_03"]) - data["loo_ps_ind_17_bin"])))
    v["141"] = 0.019996 * np.tanh(((data["loo_ps_ind_04_cat"] - (
    (data["ps_car_13"] + (data["loo_ps_ind_05_cat"] * data["loo_ps_ind_05_cat"])) / 2.0)) * data["loo_ps_car_07_cat"]))
    v["142"] = 0.020000 * np.tanh(((data["ps_ind_15"] + (
    ((data["ps_reg_03"] * data["ps_reg_03"]) - 0.432099) + data["loo_ps_ind_16_bin"])) / 2.0))
    v["143"] = 0.020000 * np.tanh(((data["loo_ps_ind_04_cat"] + (
    data["loo_ps_ind_08_bin"] - (data["loo_ps_car_04_cat"] + (data["loo_ps_ind_08_bin"] * data["ps_car_13"])))) / 2.0))
    v["144"] = 0.019996 * np.tanh(
        ((((-1.0 - data["ps_ind_03"]) - data["ps_ind_03"]) * data["loo_ps_ind_02_cat"]) - 0.432099))
    v["145"] = 0.020000 * np.tanh((((data["loo_ps_ind_02_cat"] * (data["loo_ps_ind_02_cat"] - 0.788462)) * data[
        "loo_ps_ind_02_cat"]) - data["loo_ps_car_10_cat"]))
    v["146"] = 0.020000 * np.tanh((data["loo_ps_ind_04_cat"] * (
    (data["loo_ps_ind_04_cat"] + data["ps_ind_03"]) * (0.791667 - data["ps_ind_03"]))))
    v["147"] = 0.020000 * np.tanh((np.tanh(data["loo_ps_ind_05_cat"]) * (
    ((-(data["loo_ps_ind_18_bin"])) + (data["ps_car_14"] + data["missing"])) / 2.0)))
    v["148"] = 0.020000 * np.tanh((data["ps_reg_03"] * (
    ((data["loo_ps_ind_09_bin"] - data["loo_ps_ind_18_bin"]) - data["ps_car_15"]) - data["loo_ps_ind_02_cat"])))
    v["149"] = 0.020000 * np.tanh(((data["loo_ps_ind_04_cat"] + (
    data["ps_ind_15"] * (-((data["loo_ps_ind_17_bin"] - data["ps_ind_14"]))))) / 2.0))
    v["150"] = 0.020000 * np.tanh((((data["loo_ps_ind_04_cat"] * data["loo_ps_car_03_cat"]) + (
    -(((data["loo_ps_car_01_cat"] + data["loo_ps_car_10_cat"]) / 2.0)))) / 2.0))
    v["151"] = 0.020000 * np.tanh(((0.666667 - data["ps_ind_03"]) * (
    (data["loo_ps_car_07_cat"] + (data["ps_reg_01"] + data["ps_ind_15"])) / 2.0)))
    v["152"] = 0.020000 * np.tanh(((data["loo_ps_car_03_cat"] * data["loo_ps_ind_05_cat"]) * (
    (data["loo_ps_car_06_cat"] + ((-1.0 + data["loo_ps_ind_04_cat"]) / 2.0)) / 2.0)))
    v["153"] = 0.020000 * np.tanh(
        ((data["ps_ind_03"] * data["ps_ind_03"]) * (-2.0 + (data["ps_ind_03"] * data["ps_ind_03"]))))
    v["154"] = 0.020000 * np.tanh(
        ((data["loo_ps_ind_13_bin"] - data["loo_ps_ind_11_bin"]) * ((data["loo_ps_ind_02_cat"] + (7.0)) * 29.500000)))
    v["155"] = 0.019977 * np.tanh(
        (((data["loo_ps_ind_02_cat"] + data["loo_ps_car_08_cat"]) * (data["loo_ps_ind_02_cat"] * 2.0)) - 1.089890))
    v["156"] = 0.020000 * np.tanh(((data["ps_car_12"] + (
    data["loo_ps_ind_16_bin"] * ((-(data["ps_reg_01"])) * data["loo_ps_car_05_cat"]))) / 2.0))
    v["157"] = 0.020000 * np.tanh((((data["loo_ps_ind_04_cat"] - data["loo_ps_ind_05_cat"]) + (
    data["loo_ps_ind_05_cat"] * data["ps_ind_15"])) / 2.0))
    v["158"] = 0.020000 * np.tanh(((data["loo_ps_car_01_cat"] * (
    ((data["loo_ps_car_02_cat"] + data["loo_ps_ind_17_bin"]) / 2.0) * data["loo_ps_ind_02_cat"])) * data[
                                       "loo_ps_car_07_cat"]))
    v["159"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    ((data["loo_ps_ind_05_cat"] * data["loo_ps_ind_16_bin"]) + -3.0) * data["loo_ps_ind_04_cat"])))
    v["160"] = 0.020000 * np.tanh((data["loo_ps_car_05_cat"] * (
    (data["loo_ps_ind_02_cat"] + (-((data["loo_ps_car_06_cat"] * data["loo_ps_car_02_cat"])))) / 2.0)))
    v["161"] = 0.019961 * np.tanh(
        (-((data["loo_ps_car_03_cat"] * (0.753247 - (data["ps_ind_01"] * data["ps_ind_01"]))))))
    v["162"] = 0.020000 * np.tanh(((data["ps_car_13"] + data["loo_ps_ind_17_bin"]) * (
    (data["ps_ind_03"] + (data["ps_ind_03"] + data["loo_ps_car_07_cat"])) / 2.0)))
    v["163"] = 0.019988 * np.tanh(((data["ps_ind_01"] + (
    (data["loo_ps_ind_09_bin"] + ((data["ps_ind_01"] + data["missing"]) / 2.0)) / 2.0)) * data["missing"]))
    v["164"] = 0.019988 * np.tanh((data["ps_reg_03"] * (
    -(((((data["loo_ps_ind_02_cat"] + (-(data["ps_reg_03"]))) / 2.0) + data["ps_reg_01"]) / 2.0)))))
    v["165"] = 0.020000 * np.tanh(((1.480000 + (data["loo_ps_ind_11_bin"] * 29.500000)) * 29.500000))
    v["166"] = 0.020000 * np.tanh((data["loo_ps_ind_04_cat"] - ((2.0 + data["ps_car_11"]) * (2.352940 * 2.352940))))
    v["167"] = 0.020000 * np.tanh(((data["ps_car_11"] + (
    ((-(data["loo_ps_car_04_cat"])) + ((data["loo_ps_ind_04_cat"] + data["loo_ps_car_02_cat"]) / 2.0)) / 2.0)) / 2.0))
    v["168"] = 0.019996 * np.tanh(
        (((data["loo_ps_car_09_cat"] * (-(data["ps_reg_01"]))) + (data["ps_reg_01"] - data["ps_ind_03"])) / 2.0))
    v["169"] = 0.019996 * np.tanh((data["loo_ps_car_09_cat"] * (
    (data["loo_ps_car_09_cat"] * data["loo_ps_ind_17_bin"]) - (0.791667 - data["ps_reg_02"]))))
    v["170"] = 0.019992 * np.tanh(
        ((data["ps_car_15"] * (data["loo_ps_ind_06_bin"] - data["ps_ind_03"])) * data["loo_ps_car_04_cat"]))
    v["171"] = 0.020000 * np.tanh(
        ((-(data["ps_reg_03"])) * (data["missing"] + ((data["loo_ps_car_03_cat"] + data["ps_car_14"]) / 2.0))))
    v["172"] = 0.019996 * np.tanh((data["ps_ind_01"] * (
    (data["loo_ps_ind_05_cat"] * ((data["loo_ps_ind_02_cat"] + data["ps_ind_01"]) / 2.0)) - data["loo_ps_ind_04_cat"])))
    v["173"] = 0.019953 * np.tanh(((data["ps_reg_01"] * (
    -(((data["loo_ps_ind_06_bin"] + np.tanh(data["loo_ps_ind_17_bin"])) / 2.0)))) - data["loo_ps_car_10_cat"]))
    v["174"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    ((data["loo_ps_ind_02_cat"] * data["loo_ps_ind_02_cat"]) - 0.887097) + data["ps_ind_01"])))
    v["175"] = 0.020000 * np.tanh((((data["ps_reg_01"] + (data["loo_ps_car_01_cat"] * 0.117647)) / 2.0) * (
    data["loo_ps_car_01_cat"] * data["loo_ps_car_01_cat"])))
    v["176"] = 0.019988 * np.tanh((((data["loo_ps_ind_04_cat"] * np.tanh(data["loo_ps_ind_17_bin"])) + np.tanh(
        (-3.0 + data["ps_car_13"]))) / 2.0))
    v["177"] = 0.020000 * np.tanh((1.089890 + ((11.83836174011230469) * ((0.666667 * 1.089890) - data["ps_car_15"]))))
    v["178"] = 0.019996 * np.tanh(((-1.0 + (data["loo_ps_ind_17_bin"] * (
    (data["loo_ps_ind_09_bin"] + ((data["loo_ps_ind_04_cat"] + -3.0) / 2.0)) / 2.0))) / 2.0))
    v["179"] = 0.020000 * np.tanh((data["loo_ps_car_03_cat"] * (
    data["loo_ps_car_04_cat"] * (data["loo_ps_ind_04_cat"] - np.tanh(data["ps_car_15"])))))
    v["180"] = 0.019887 * np.tanh(
        (data["loo_ps_car_08_cat"] + (data["ps_ind_03"] * (data["loo_ps_car_02_cat"] * data["ps_ind_01"]))))
    v["181"] = 0.020000 * np.tanh(
        ((((data["ps_reg_01"] + (-(data["ps_car_13"]))) / 2.0) * data["ps_ind_15"]) * data["loo_ps_car_01_cat"]))
    v["182"] = 0.020000 * np.tanh((data["ps_reg_01"] * (
    data["loo_ps_ind_07_bin"] * (((data["loo_ps_ind_02_cat"] + data["loo_ps_car_08_cat"]) / 2.0) - data["ps_reg_03"]))))
    v["183"] = 0.020000 * np.tanh((((data["ps_ind_14"] + (
    data["loo_ps_ind_04_cat"] * data["loo_ps_ind_17_bin"])) / 2.0) * (
                                   data["loo_ps_car_01_cat"] * data["loo_ps_ind_04_cat"])))
    v["184"] = 0.020000 * np.tanh((data["loo_ps_ind_17_bin"] * (
    (data["loo_ps_ind_02_cat"] + (data["ps_ind_15"] * (-(data["ps_car_15"])))) / 2.0)))
    v["185"] = 0.019973 * np.tanh((data["loo_ps_ind_17_bin"] * (
    (data["loo_ps_car_01_cat"] - data["ps_ind_14"]) * (data["ps_car_11"] + data["loo_ps_car_09_cat"]))))
    v["186"] = 0.019918 * np.tanh((data["loo_ps_ind_02_cat"] * (
    ((data["loo_ps_ind_02_cat"] * data["loo_ps_ind_02_cat"]) - 0.666667) + data["loo_ps_ind_18_bin"])))
    v["187"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    data["loo_ps_ind_04_cat"] * (data["ps_car_13"] + (data["loo_ps_car_04_cat"] + data["ps_car_12"])))))
    v["188"] = 0.020000 * np.tanh(
        (data["loo_ps_car_07_cat"] * (data["loo_ps_ind_05_cat"] * (data["ps_car_13"] + data["ps_car_13"]))))
    v["189"] = 0.019992 * np.tanh((data["ps_car_13"] * (data["loo_ps_car_01_cat"] * (data["ps_car_13"] - 2.0))))
    v["190"] = 0.020000 * np.tanh((data["loo_ps_ind_04_cat"] * (data["loo_ps_ind_05_cat"] * (-(data["ps_reg_02"])))))
    v["191"] = 0.020000 * np.tanh((data["loo_ps_car_07_cat"] * (
    ((data["loo_ps_ind_02_cat"] * 0.432099) * data["loo_ps_car_07_cat"]) - data["loo_ps_car_02_cat"])))
    v["192"] = 0.020000 * np.tanh((data["ps_reg_01"] * (
    data["loo_ps_car_07_cat"] * (-((data["loo_ps_ind_02_cat"] + data["loo_ps_ind_18_bin"]))))))
    v["193"] = 0.020000 * np.tanh((data["loo_ps_ind_04_cat"] * (
    data["loo_ps_car_08_cat"] * (data["ps_reg_03"] - ((data["ps_ind_03"] + data["ps_ind_03"]) / 2.0)))))
    v["194"] = 0.019996 * np.tanh(((data["ps_ind_03"] - ((0.600000 + data["loo_ps_ind_08_bin"]) / 2.0)) * (
    (data["ps_ind_14"] + data["loo_ps_ind_08_bin"]) / 2.0)))
    v["195"] = 0.019992 * np.tanh(((data["loo_ps_car_11_cat"] * data["loo_ps_car_04_cat"]) * (
    ((data["ps_ind_01"] + data["ps_ind_01"]) + data["loo_ps_ind_06_bin"]) / 2.0)))
    v["196"] = 0.019996 * np.tanh(((data["loo_ps_car_04_cat"] - (
    (data["ps_ind_01"] + data["loo_ps_ind_02_cat"]) / 2.0)) * (data["loo_ps_ind_02_cat"] * data["ps_ind_03"])))
    v["197"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    data["ps_car_11"] * ((data["ps_reg_02"] - data["loo_ps_car_01_cat"]) - data["loo_ps_car_03_cat"]))))
    v["198"] = 0.020000 * np.tanh((data["ps_reg_03"] * (
    (((data["loo_ps_car_04_cat"] * data["loo_ps_car_08_cat"]) + data["loo_ps_ind_02_cat"]) / 2.0) * data[
        "loo_ps_car_08_cat"])))
    v["199"] = 0.020000 * np.tanh((((data["ps_car_11"] + data["loo_ps_car_04_cat"]) / 2.0) * (
    (data["loo_ps_car_04_cat"] * data["loo_ps_ind_02_cat"]) - data["loo_ps_car_04_cat"])))
    v["200"] = 0.019992 * np.tanh(
        (((data["ps_car_13"] * data["ps_ind_14"]) * data["ps_ind_15"]) * (data["ps_car_13"] * data["ps_car_13"])))
    v["201"] = 0.019644 * np.tanh((data["ps_ind_15"] * (
    data["ps_reg_03"] + ((data["ps_ind_15"] * data["loo_ps_car_08_cat"]) + data["ps_reg_03"]))))
    v["202"] = 0.020000 * np.tanh(
        ((-((data["ps_reg_02"] * ((data["loo_ps_car_08_cat"] + data["ps_ind_15"]) / 2.0)))) * data["ps_ind_03"]))
    v["203"] = 0.020000 * np.tanh((0.666667 - (
    data["ps_car_15"] * (((data["loo_ps_car_08_cat"] + data["loo_ps_car_10_cat"]) + data["loo_ps_car_03_cat"]) / 2.0))))
    v["204"] = 0.020000 * np.tanh(((data["loo_ps_car_09_cat"] * np.tanh(data["loo_ps_car_02_cat"])) + (
    data["loo_ps_car_09_cat"] * data["loo_ps_car_11_cat"])))
    v["205"] = 0.020000 * np.tanh((data["loo_ps_car_09_cat"] * (
    data["loo_ps_ind_08_bin"] - ((data["loo_ps_ind_18_bin"] * data["ps_reg_01"]) * data["ps_reg_01"]))))
    v["206"] = 0.019980 * np.tanh((data["loo_ps_ind_04_cat"] * (
    (data["loo_ps_car_01_cat"] - (data["loo_ps_ind_17_bin"] * data["loo_ps_car_01_cat"])) * data["ps_reg_02"])))
    v["207"] = 0.020000 * np.tanh(((
                                   (data["loo_ps_ind_08_bin"] * (data["ps_ind_15"] + data["loo_ps_car_01_cat"])) - data[
                                       "loo_ps_car_10_cat"]) - data["loo_ps_car_10_cat"]))
    v["208"] = 0.020000 * np.tanh((0.148148 * (
    data["loo_ps_ind_02_cat"] * (-((np.tanh(data["loo_ps_ind_18_bin"]) * data["loo_ps_ind_16_bin"]))))))
    v["209"] = 0.020000 * np.tanh((((data["ps_car_15"] + data["loo_ps_ind_04_cat"]) / 2.0) * (
    data["ps_car_12"] * ((data["loo_ps_ind_16_bin"] + data["ps_car_12"]) / 2.0))))
    v["210"] = 0.020000 * np.tanh((data["loo_ps_car_11_cat"] * (
    data["loo_ps_ind_17_bin"] * ((data["loo_ps_ind_02_cat"] + (-(data["loo_ps_car_07_cat"]))) / 2.0))))
    v["211"] = 0.020000 * np.tanh(((data["ps_ind_03"] * (
    (data["loo_ps_ind_05_cat"] + (data["loo_ps_ind_02_cat"] * data["ps_ind_03"])) / 2.0)) - data["loo_ps_ind_02_cat"]))
    v["212"] = 0.019711 * np.tanh(((((data["loo_ps_ind_09_bin"] * data["loo_ps_car_03_cat"]) + (
    data["loo_ps_ind_09_bin"] * data["loo_ps_car_07_cat"])) / 2.0) - 0.232323))
    v["213"] = 0.020000 * np.tanh(
        (data["ps_ind_03"] * (0.633333 - ((data["ps_ind_01"] + data["loo_ps_ind_02_cat"]) * data["ps_ind_01"]))))
    v["214"] = 0.020000 * np.tanh((data["loo_ps_ind_12_bin"] * (
    data["loo_ps_ind_11_bin"] + ((data["ps_ind_15"] + data["ps_reg_03"]) + data["ps_reg_03"]))))
    v["215"] = 0.020000 * np.tanh((data["loo_ps_ind_16_bin"] * (
    (data["loo_ps_car_08_cat"] * (-(data["loo_ps_ind_02_cat"]))) - data["loo_ps_car_07_cat"])))
    v["216"] = 0.020000 * np.tanh(((((data["loo_ps_ind_17_bin"] + data["loo_ps_car_09_cat"]) / 2.0) * data[
        "loo_ps_ind_05_cat"]) * data["ps_reg_02"]))
    v["217"] = 0.019984 * np.tanh(
        (data["ps_car_14"] * (data["loo_ps_car_07_cat"] * ((data["ps_ind_15"] + data["loo_ps_ind_09_bin"]) / 2.0))))
    v["218"] = 0.020000 * np.tanh((((data["loo_ps_ind_09_bin"] + (
    (data["loo_ps_ind_02_cat"] + data["ps_reg_02"]) / 2.0)) / 2.0) * ((data["missing"] + data["ps_reg_02"]) / 2.0)))
    v["219"] = 0.019984 * np.tanh((data["ps_car_14"] * (
    (data["loo_ps_car_08_cat"] * (-(data["loo_ps_ind_04_cat"]))) + (-(data["loo_ps_car_07_cat"])))))
    v["220"] = 0.020000 * np.tanh(
        (((data["ps_ind_03"] * ((data["loo_ps_ind_02_cat"] * data["ps_ind_03"]) * 2.0)) + data["ps_ind_03"]) / 2.0))
    v["221"] = 0.019949 * np.tanh((data["loo_ps_ind_06_bin"] * (data["loo_ps_ind_16_bin"] * (
    (data["loo_ps_car_07_cat"] + ((data["ps_reg_02"] + data["loo_ps_ind_08_bin"]) / 2.0)) / 2.0))))
    v["222"] = 0.019984 * np.tanh(((data["loo_ps_ind_17_bin"] * data["ps_reg_03"]) * (
    -(((data["loo_ps_ind_12_bin"] + data["loo_ps_car_04_cat"]) / 2.0)))))
    v["223"] = 0.019848 * np.tanh(((data["ps_ind_01"] * (data["loo_ps_ind_18_bin"] * data["loo_ps_car_01_cat"])) - (
    data["loo_ps_car_10_cat"] * data["ps_ind_03"])))
    v["224"] = 0.019973 * np.tanh((((data["ps_ind_03"] * 1.480000) * data["ps_reg_03"]) * (
    (data["ps_car_12"] + data["loo_ps_ind_17_bin"]) / 2.0)))
    v["225"] = 0.020000 * np.tanh((-(
    (data["loo_ps_ind_17_bin"] * (data["ps_car_15"] - (data["loo_ps_ind_04_cat"] * data["loo_ps_car_10_cat"]))))))
    v["226"] = 0.020000 * np.tanh(
        ((data["loo_ps_ind_04_cat"] + data["loo_ps_ind_04_cat"]) * (data["ps_ind_01"] * (-(data["ps_ind_03"])))))
    v["227"] = 0.020000 * np.tanh((-((((data["loo_ps_ind_06_bin"] + (
    data["loo_ps_car_08_cat"] + data["loo_ps_ind_02_cat"])) / 2.0) * np.tanh(data["loo_ps_ind_18_bin"])))))
    v["228"] = 0.019988 * np.tanh((data["loo_ps_ind_07_bin"] * (
    data["loo_ps_ind_17_bin"] * (((data["loo_ps_car_08_cat"] + data["ps_reg_02"]) + data["loo_ps_ind_05_cat"]) / 2.0))))
    v["229"] = 0.020000 * np.tanh(
        (data["loo_ps_ind_04_cat"] * (data["ps_ind_15"] * (data["ps_car_12"] - np.tanh(0.753247)))))
    v["230"] = 0.014245 * np.tanh(
        (((data["ps_reg_02"] + data["loo_ps_car_08_cat"]) / 2.0) * (data["ps_reg_02"] * (data["ps_reg_02"] - 3.0))))
    v["231"] = 0.020000 * np.tanh(((0.232323 + (
    data["loo_ps_car_11_cat"] * (data["ps_ind_01"] * (data["ps_reg_03"] * data["ps_reg_02"])))) / 2.0))
    v["232"] = 0.019984 * np.tanh((data["loo_ps_ind_08_bin"] * (
    -(((((data["ps_reg_03"] + data["loo_ps_car_11_cat"]) / 2.0) + data["loo_ps_ind_12_bin"]) / 2.0)))))
    v["233"] = 0.019969 * np.tanh((-(
    np.tanh((data["ps_reg_02"] * (data["loo_ps_car_06_cat"] - (data["ps_ind_03"] * data["loo_ps_ind_18_bin"])))))))
    v["234"] = 0.019996 * np.tanh(
        (-(((data["ps_car_15"] + ((data["ps_car_14"] * data["loo_ps_car_02_cat"]) - 0.753247)) / 2.0))))
    v["235"] = 0.020000 * np.tanh(((data["loo_ps_car_07_cat"] * (-(data["loo_ps_ind_17_bin"]))) * (
    data["loo_ps_car_02_cat"] + data["loo_ps_car_06_cat"])))
    v["236"] = 0.019984 * np.tanh((data["loo_ps_car_11_cat"] * (
    data["loo_ps_car_01_cat"] * (data["ps_reg_01"] * ((0.791667 + data["loo_ps_car_07_cat"]) / 2.0)))))
    v["237"] = 0.020000 * np.tanh((data["loo_ps_car_08_cat"] * (
    ((-((data["loo_ps_car_03_cat"] * data["ps_ind_01"]))) + data["ps_ind_01"]) / 2.0)))
    v["238"] = 0.019973 * np.tanh((data["ps_car_11"] * (
    (data["loo_ps_car_06_cat"] + (data["ps_ind_03"] * np.tanh((-(data["ps_car_11"]))))) / 2.0)))
    v["239"] = 0.020000 * np.tanh((data["loo_ps_car_01_cat"] * (
    data["loo_ps_car_06_cat"] * (((-(data["loo_ps_car_07_cat"])) + data["loo_ps_car_05_cat"]) / 2.0))))
    v["240"] = 0.020000 * np.tanh((data["loo_ps_car_09_cat"] * (
    data["ps_ind_01"] * (data["loo_ps_car_09_cat"] - (0.945455 - data["ps_ind_01"])))))
    v["241"] = 0.020000 * np.tanh(((
                                   (data["loo_ps_ind_02_cat"] * (data["ps_ind_15"] - data["loo_ps_ind_02_cat"])) * data[
                                       "ps_ind_15"]) - data["loo_ps_ind_02_cat"]))
    v["242"] = 0.019687 * np.tanh(
        ((-3.0 * ((data["ps_ind_15"] + 1.0) + data["ps_ind_03"])) * data["loo_ps_car_09_cat"]))
    v["243"] = 0.020000 * np.tanh((((0.633333 * data["ps_car_14"]) * data["loo_ps_ind_17_bin"]) * (
    data["loo_ps_ind_04_cat"] - data["ps_car_12"])))
    v["244"] = 0.019930 * np.tanh((data["loo_ps_ind_08_bin"] * (
    (data["ps_ind_03"] + ((data["missing"] + (data["loo_ps_ind_04_cat"] - 1.0)) / 2.0)) / 2.0)))
    v["245"] = 0.019293 * np.tanh(
        (data["loo_ps_ind_04_cat"] * (np.tanh(data["ps_car_12"]) + (-(data["loo_ps_car_06_cat"])))))
    v["246"] = 0.020000 * np.tanh((data["loo_ps_ind_08_bin"] * (
    (data["loo_ps_ind_08_bin"] * data["loo_ps_ind_08_bin"]) * (data["ps_ind_01"] - data["loo_ps_car_05_cat"]))))
    v["247"] = 0.020000 * np.tanh(
        (np.tanh((data["ps_ind_15"] * (data["loo_ps_ind_07_bin"] + data["ps_ind_15"]))) * data["loo_ps_ind_07_bin"]))
    v["248"] = 0.019254 * np.tanh(((((data["loo_ps_ind_08_bin"] + (data["ps_car_12"] * data["ps_ind_14"])) / 2.0) + (
    data["loo_ps_ind_08_bin"] * data["loo_ps_car_03_cat"])) / 2.0))
    v["249"] = 0.019992 * np.tanh(((data["loo_ps_ind_13_bin"] + (
    -((data["ps_ind_03"] * (data["ps_car_14"] + data["loo_ps_ind_02_cat"]))))) / 2.0))
    v["250"] = 0.020000 * np.tanh(((data["loo_ps_ind_02_cat"] * data["loo_ps_car_08_cat"]) * (
    data["loo_ps_car_03_cat"] - (data["loo_ps_ind_02_cat"] * data["loo_ps_ind_02_cat"]))))
    v["251"] = 0.020000 * np.tanh(((np.tanh(data["ps_car_12"]) * data["loo_ps_ind_02_cat"]) - (
    (data["loo_ps_ind_02_cat"] + np.tanh(data["loo_ps_ind_05_cat"])) / 2.0)))
    v["252"] = 0.020000 * np.tanh(((data["ps_ind_15"] * data["ps_ind_15"]) * (
    data["loo_ps_ind_12_bin"] * (data["ps_ind_15"] * data["loo_ps_car_11_cat"]))))
    v["253"] = 0.019801 * np.tanh(((data["loo_ps_ind_05_cat"] - 0.232323) * (
    (data["loo_ps_ind_04_cat"] - data["ps_car_11"]) * data["loo_ps_ind_17_bin"])))
    v["254"] = 0.020000 * np.tanh((data["loo_ps_ind_17_bin"] * (
    data["ps_ind_14"] * (-((data["loo_ps_car_03_cat"] + data["loo_ps_ind_04_cat"]))))))
    v["255"] = 0.019711 * np.tanh((((data["ps_car_11"] + data["ps_ind_01"]) / 2.0) * (
    -((data["loo_ps_car_04_cat"] * np.tanh(data["ps_ind_01"]))))))
    v["256"] = 0.019996 * np.tanh(
        (data["loo_ps_ind_02_cat"] * ((data["ps_car_15"] * data["loo_ps_ind_17_bin"]) * (data["missing"] - 0.945455))))
    v["257"] = 0.020000 * np.tanh((((-((data["missing"] * data["loo_ps_car_07_cat"]))) + (
    data["loo_ps_car_07_cat"] * (-(data["loo_ps_ind_12_bin"])))) / 2.0))
    v["258"] = 0.019844 * np.tanh(
        ((data["loo_ps_ind_05_cat"] + data["ps_car_14"]) * (-((data["ps_ind_01"] * data["loo_ps_ind_17_bin"])))))
    v["259"] = 0.020000 * np.tanh((data["loo_ps_ind_08_bin"] * (
    ((data["missing"] + np.tanh(data["loo_ps_ind_02_cat"])) / 2.0) * data["ps_car_14"])))
    v["260"] = 0.019945 * np.tanh(((data["loo_ps_ind_04_cat"] * (
    data["loo_ps_ind_04_cat"] + (-(data["loo_ps_ind_09_bin"])))) - data["loo_ps_car_10_cat"]))
    v["261"] = 0.020000 * np.tanh((((data["ps_ind_03"] + data["loo_ps_ind_12_bin"]) / 2.0) * (
    data["ps_ind_03"] + np.tanh((-(data["ps_ind_03"]))))))
    v["262"] = 0.019992 * np.tanh((data["loo_ps_car_10_cat"] * (
    ((data["loo_ps_ind_04_cat"] * data["loo_ps_ind_05_cat"]) * data["ps_ind_01"]) - data["ps_ind_01"])))
    v["263"] = 0.020000 * np.tanh(
        (data["ps_reg_02"] * ((data["ps_car_13"] - data["loo_ps_car_07_cat"]) * (data["ps_car_12"] - 0.633333))))
    v["264"] = 0.019973 * np.tanh((data["ps_ind_14"] * (
    ((8.428570 * (data["loo_ps_ind_07_bin"] * data["ps_car_15"])) + data["loo_ps_ind_13_bin"]) / 2.0)))
    v["265"] = 0.020000 * np.tanh(((data["loo_ps_car_03_cat"] * (
    data["loo_ps_ind_05_cat"] - data["loo_ps_car_10_cat"])) * np.tanh(data["ps_reg_02"])))
    v["266"] = 0.020000 * np.tanh((((data["ps_car_13"] + np.tanh(data["loo_ps_ind_17_bin"])) / 2.0) * (
    ((-(data["loo_ps_car_10_cat"])) + data["loo_ps_ind_04_cat"]) / 2.0)))
    v["267"] = 0.020000 * np.tanh(((data["ps_ind_03"] * data["loo_ps_ind_17_bin"]) * (
    (-1.0 + (data["loo_ps_car_03_cat"] * data["ps_car_13"])) / 2.0)))
    v["268"] = 0.019977 * np.tanh(((((data["loo_ps_ind_11_bin"] + (data["ps_car_11"] + 1.480000)) / 2.0) + data[
        "ps_ind_15"]) * data["loo_ps_ind_12_bin"]))
    v["269"] = 0.020000 * np.tanh(
        (np.tanh(np.tanh(data["ps_reg_03"])) * (data["ps_car_11"] * (data["ps_ind_14"] + data["ps_ind_15"]))))
    v["270"] = 0.018535 * np.tanh((((data["loo_ps_ind_05_cat"] + (
    data["loo_ps_ind_18_bin"] - (data["loo_ps_ind_05_cat"] * data["loo_ps_ind_18_bin"]))) / 2.0) * data[
                                       "loo_ps_ind_09_bin"]))
    v["271"] = 0.020000 * np.tanh(
        (data["ps_car_15"] * (data["ps_car_12"] * (np.tanh(data["ps_car_15"]) - data["ps_car_11"]))))
    v["272"] = 0.019957 * np.tanh((data["ps_reg_02"] * (data["ps_reg_03"] * (-3.0 + data["ps_reg_02"]))))
    v["273"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] - data["loo_ps_ind_12_bin"]) * (
    (data["ps_car_15"] + ((data["loo_ps_ind_02_cat"] + data["loo_ps_ind_02_cat"]) / 2.0)) / 2.0)))
    v["274"] = 0.020000 * np.tanh((data["loo_ps_car_10_cat"] * (
    (data["loo_ps_ind_17_bin"] * data["loo_ps_ind_02_cat"]) - data["loo_ps_ind_16_bin"])))
    v["275"] = 0.020000 * np.tanh((((data["ps_ind_03"] + (-((data["loo_ps_ind_09_bin"] * data["ps_ind_15"])))) / 2.0) *
                                   data["loo_ps_ind_05_cat"]))
    v["276"] = 0.019512 * np.tanh(np.tanh((data["ps_ind_03"] * ((data["ps_reg_03"] * data["ps_reg_03"]) - 0.791667))))
    v["277"] = 0.018703 * np.tanh(
        (-(((0.633333 * data["loo_ps_ind_05_cat"]) * (data["loo_ps_ind_16_bin"] * data["loo_ps_car_08_cat"])))))
    v["278"] = 0.019988 * np.tanh(
        ((data["loo_ps_ind_02_cat"] * data["ps_ind_03"]) * (data["ps_ind_03"] * data["loo_ps_ind_06_bin"])))
    v["279"] = 0.019723 * np.tanh((((data["loo_ps_ind_09_bin"] * data["loo_ps_car_04_cat"]) + (
    data["ps_ind_03"] * data["ps_car_13"])) * data["ps_car_15"]))
    v["280"] = 0.020000 * np.tanh(((data["loo_ps_ind_02_cat"] + (data["loo_ps_ind_02_cat"] + data["ps_ind_03"])) * (
    data["loo_ps_ind_13_bin"] - data["loo_ps_ind_02_cat"])))
    v["281"] = 0.019992 * np.tanh((data["loo_ps_ind_04_cat"] * (
    data["loo_ps_ind_05_cat"] * (data["ps_ind_01"] - ((0.432099 + data["loo_ps_car_06_cat"]) / 2.0)))))
    v["282"] = 0.020000 * np.tanh((data["ps_reg_01"] * (
    ((data["loo_ps_ind_05_cat"] * (-(data["ps_car_12"]))) + data["loo_ps_ind_11_bin"]) / 2.0)))
    v["283"] = 0.020000 * np.tanh(
        (((-(data["ps_ind_03"])) * data["loo_ps_ind_05_cat"]) * np.tanh(np.tanh(data["ps_ind_01"]))))
    v["284"] = 0.018035 * np.tanh(
        (data["ps_ind_03"] * np.tanh((data["loo_ps_car_05_cat"] * (data["loo_ps_ind_16_bin"] - data["ps_ind_01"])))))
    v["285"] = 0.017937 * np.tanh((data["loo_ps_ind_04_cat"] * (
    (data["ps_car_11"] + (data["loo_ps_ind_04_cat"] - data["loo_ps_ind_16_bin"])) + data["ps_ind_03"])))
    v["286"] = 0.020000 * np.tanh((data["ps_car_13"] * (
    data["loo_ps_car_03_cat"] * ((data["loo_ps_ind_13_bin"] * data["ps_car_13"]) * data["ps_car_13"]))))
    v["287"] = 0.019140 * np.tanh((data["loo_ps_car_03_cat"] * (
    (data["loo_ps_car_02_cat"] * (data["ps_reg_02"] - data["ps_reg_01"])) * data["loo_ps_ind_04_cat"])))
    v["288"] = 0.019984 * np.tanh((data["loo_ps_car_06_cat"] * (
    data["loo_ps_ind_02_cat"] * (data["loo_ps_ind_02_cat"] * (-(data["loo_ps_ind_16_bin"]))))))
    v["289"] = 0.017492 * np.tanh((((data["ps_car_11"] * data["loo_ps_car_06_cat"]) + (
    (-(data["ps_car_11"])) * data["loo_ps_ind_17_bin"])) / 2.0))
    v["290"] = 0.019707 * np.tanh((data["loo_ps_ind_04_cat"] * (
    ((data["loo_ps_ind_11_bin"] + (data["missing"] * data["loo_ps_car_07_cat"])) + data["missing"]) / 2.0)))
    v["291"] = 0.019598 * np.tanh(
        ((data["ps_reg_01"] * data["loo_ps_car_04_cat"]) * (data["loo_ps_car_07_cat"] + data["loo_ps_ind_12_bin"])))
    v["292"] = 0.019855 * np.tanh(((data["loo_ps_ind_02_cat"] * data["loo_ps_ind_16_bin"]) * (
    data["loo_ps_ind_07_bin"] * (data["loo_ps_ind_18_bin"] + 0.232323))))
    v["293"] = 0.020000 * np.tanh(((data["loo_ps_car_04_cat"] * data["ps_reg_01"]) * np.tanh(
        ((-(data["loo_ps_car_08_cat"])) - data["loo_ps_car_09_cat"]))))
    v["294"] = 0.019992 * np.tanh((data["ps_reg_02"] * (
    data["ps_car_13"] * (data["ps_car_15"] + (data["loo_ps_car_05_cat"] * data["ps_reg_03"])))))
    v["295"] = 0.020000 * np.tanh(
        ((data["loo_ps_ind_12_bin"] * (data["loo_ps_car_01_cat"] - data["loo_ps_car_07_cat"])) * data["ps_reg_02"]))
    v["296"] = 0.020000 * np.tanh(
        (-((data["loo_ps_car_10_cat"] * ((data["ps_car_15"] + data["loo_ps_car_11_cat"]) + data["ps_ind_14"])))))
    v["297"] = 0.019977 * np.tanh((((data["loo_ps_car_07_cat"] + (0.435484 - data["loo_ps_ind_06_bin"])) / 2.0) * (
    data["loo_ps_ind_08_bin"] * data["loo_ps_car_08_cat"])))
    v["298"] = 0.019941 * np.tanh((data["ps_car_14"] * (
    data["loo_ps_ind_04_cat"] + (np.tanh(data["loo_ps_ind_04_cat"]) * (-(data["loo_ps_ind_07_bin"]))))))
    v["299"] = 0.019117 * np.tanh(
        (data["loo_ps_ind_06_bin"] * ((data["ps_ind_03"] + data["loo_ps_ind_04_cat"]) * data["loo_ps_ind_17_bin"])))
    v["300"] = 0.020000 * np.tanh(((data["loo_ps_ind_16_bin"] * (
    data["loo_ps_ind_04_cat"] * (data["ps_reg_01"] * data["loo_ps_car_07_cat"]))) * data["loo_ps_ind_18_bin"]))
    v["301"] = 0.019973 * np.tanh((-((data["ps_car_11"] * (
    ((data["loo_ps_ind_04_cat"] + data["loo_ps_car_02_cat"]) / 2.0) * data["loo_ps_ind_05_cat"])))))
    v["302"] = 0.020000 * np.tanh((data["ps_car_12"] * (
    (data["loo_ps_ind_12_bin"] * data["ps_car_12"]) * (data["ps_car_11"] - data["loo_ps_car_08_cat"]))))
    v["303"] = 0.020000 * np.tanh((data["loo_ps_ind_17_bin"] * (
    data["loo_ps_car_10_cat"] * (data["loo_ps_ind_04_cat"] - (data["ps_ind_03"] * data["loo_ps_ind_17_bin"])))))
    v["304"] = 0.017566 * np.tanh(
        ((data["ps_reg_03"] - data["loo_ps_car_03_cat"]) * (data["ps_reg_01"] * data["loo_ps_ind_08_bin"])))
    v["305"] = 0.019973 * np.tanh((8.428570 * (0.666667 - (data["loo_ps_car_10_cat"] * (8.428570 - 0.432099)))))
    v["306"] = 0.020000 * np.tanh(
        np.tanh(np.tanh((-3.0 * (((data["ps_reg_01"] - data["loo_ps_car_02_cat"]) + 2.0) / 2.0)))))
    v["307"] = 0.020000 * np.tanh(
        ((data["ps_ind_01"] - data["ps_reg_01"]) * (data["ps_reg_02"] * data["loo_ps_ind_04_cat"])))
    v["308"] = 0.020000 * np.tanh((((data["ps_car_12"] + data["ps_ind_14"]) / 2.0) * (
    data["loo_ps_ind_02_cat"] * (data["ps_car_12"] * data["loo_ps_ind_17_bin"]))))
    v["309"] = 0.020000 * np.tanh(((data["loo_ps_ind_02_cat"] * data["loo_ps_car_04_cat"]) * (
    (data["loo_ps_ind_02_cat"] * data["loo_ps_ind_02_cat"]) - data["loo_ps_ind_02_cat"])))
    v["310"] = 0.020000 * np.tanh((((data["ps_ind_14"] * data["ps_car_12"]) + (
    data["loo_ps_ind_04_cat"] * (data["loo_ps_ind_04_cat"] + data["ps_ind_14"]))) / 2.0))
    v["311"] = 0.017878 * np.tanh((data["ps_reg_03"] * (
    -(((data["ps_car_12"] + (data["loo_ps_car_09_cat"] * data["loo_ps_ind_08_bin"])) / 2.0)))))
    v["312"] = 0.019973 * np.tanh(
        (data["loo_ps_car_01_cat"] * (((data["loo_ps_car_01_cat"] + data["ps_reg_01"]) / 2.0) * data["ps_car_12"])))
    v["313"] = 0.018691 * np.tanh(
        ((data["ps_car_14"] * data["loo_ps_car_11_cat"]) * (-((data["ps_ind_14"] + data["loo_ps_ind_08_bin"])))))
    v["314"] = 0.019566 * np.tanh(((1.0 - data["loo_ps_car_11_cat"]) * (
    ((data["missing"] * data["loo_ps_car_11_cat"]) + data["ps_car_14"]) / 2.0)))
    v["315"] = 0.015312 * np.tanh(((data["missing"] + (
    ((data["missing"] - data["loo_ps_ind_02_cat"]) - data["loo_ps_ind_09_bin"]) * data["ps_reg_01"])) / 2.0))
    v["316"] = 0.019980 * np.tanh((data["loo_ps_car_03_cat"] * (
    (data["loo_ps_car_11_cat"] * data["loo_ps_ind_04_cat"]) * data["loo_ps_ind_05_cat"])))
    v["317"] = 0.016890 * np.tanh(
        (data["loo_ps_car_07_cat"] * ((data["loo_ps_car_11_cat"] - data["ps_car_13"]) - data["loo_ps_ind_06_bin"])))
    v["318"] = 0.020000 * np.tanh((data["ps_car_12"] * (
    (data["ps_reg_02"] * data["loo_ps_car_04_cat"]) * ((data["ps_reg_02"] + data["ps_ind_03"]) / 2.0))))
    v["319"] = 0.016683 * np.tanh(np.tanh(
        (data["loo_ps_ind_16_bin"] * (data["loo_ps_ind_12_bin"] - (data["loo_ps_ind_17_bin"] * data["ps_ind_01"])))))
    v["320"] = 0.018222 * np.tanh(
        ((data["loo_ps_ind_13_bin"] * data["ps_car_12"]) - np.tanh((data["loo_ps_ind_02_cat"] + data["ps_car_14"]))))
    v["321"] = 0.020000 * np.tanh(((data["ps_ind_14"] * data["ps_car_11"]) * (
    data["ps_reg_02"] - ((data["ps_car_11"] + data["ps_car_15"]) / 2.0))))
    v["322"] = 0.019703 * np.tanh((((data["ps_ind_01"] + (-(data["loo_ps_car_08_cat"]))) / 2.0) * (
    data["loo_ps_ind_17_bin"] * data["ps_ind_01"])))
    v["323"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] * (data["ps_reg_01"] - 0.753247)) * (
    data["loo_ps_car_02_cat"] * data["loo_ps_car_02_cat"])))
    v["324"] = 0.020000 * np.tanh((data["ps_reg_01"] * (
    (data["loo_ps_car_11_cat"] + ((data["ps_reg_01"] + (-(data["loo_ps_car_04_cat"]))) / 2.0)) / 2.0)))
    v["325"] = 0.019898 * np.tanh(
        (-(((((data["loo_ps_ind_17_bin"] + (-(data["ps_car_12"]))) / 2.0) + np.tanh(data["ps_car_12"])) / 2.0))))
    v["326"] = 0.019980 * np.tanh(((data["loo_ps_ind_12_bin"] + (
    data["loo_ps_car_04_cat"] * (data["loo_ps_car_09_cat"] + 2.352940))) * data["loo_ps_ind_13_bin"]))
    v["327"] = 0.019996 * np.tanh(((((data["loo_ps_ind_08_bin"] * data["loo_ps_car_09_cat"]) + (
    data["ps_reg_03"] * data["loo_ps_ind_08_bin"])) / 2.0) * data["ps_car_15"]))
    v["328"] = 0.020000 * np.tanh((data["ps_reg_03"] * (
    ((np.tanh(data["ps_car_11"]) + data["loo_ps_car_09_cat"]) / 2.0) * np.tanh(data["loo_ps_ind_07_bin"]))))
    v["329"] = 0.019996 * np.tanh((((((data["loo_ps_ind_02_cat"] + data["loo_ps_car_10_cat"]) / 2.0) + data[
        "ps_car_14"]) / 2.0) * (data["loo_ps_car_08_cat"] * data["ps_reg_02"])))
    v["330"] = 0.020000 * np.tanh(((data["loo_ps_car_10_cat"] * data["ps_reg_02"]) * (
    data["loo_ps_ind_18_bin"] - (data["ps_ind_14"] * data["loo_ps_ind_02_cat"]))))
    v["331"] = 0.020000 * np.tanh((((data["ps_ind_14"] + np.tanh(data["ps_ind_01"])) / 2.0) * (
    data["loo_ps_ind_17_bin"] * data["loo_ps_car_06_cat"])))
    v["332"] = 0.020000 * np.tanh((((data["ps_ind_15"] + data["loo_ps_ind_05_cat"]) / 2.0) * np.tanh(
        (data["loo_ps_ind_17_bin"] * (-(data["loo_ps_car_06_cat"]))))))
    v["333"] = 0.020000 * np.tanh(
        (data["loo_ps_ind_17_bin"] * (data["ps_car_15"] * np.tanh((data["ps_ind_03"] + data["loo_ps_car_11_cat"])))))
    v["334"] = 0.020000 * np.tanh((data["ps_car_11"] * (
    ((data["loo_ps_ind_11_bin"] + data["loo_ps_ind_10_bin"]) / 2.0) - (
    data["loo_ps_ind_05_cat"] * data["loo_ps_ind_04_cat"]))))
    v["335"] = 0.019996 * np.tanh((data["ps_car_11"] * (
    (data["loo_ps_car_10_cat"] + ((data["ps_reg_02"] * data["ps_car_11"]) * data["loo_ps_ind_18_bin"])) / 2.0)))
    v["336"] = 0.020000 * np.tanh(
        ((data["ps_ind_03"] * data["loo_ps_ind_02_cat"]) * (data["ps_ind_03"] - data["ps_ind_15"])))
    v["337"] = 0.019996 * np.tanh((((data["loo_ps_car_07_cat"] * (
    data["loo_ps_ind_13_bin"] - data["loo_ps_ind_11_bin"])) * data["loo_ps_car_07_cat"]) * data["loo_ps_car_07_cat"]))
    v["338"] = 0.019219 * np.tanh(((data["loo_ps_ind_02_cat"] * (
    (data["loo_ps_ind_05_cat"] * data["loo_ps_ind_18_bin"]) - data["loo_ps_ind_02_cat"])) - data["loo_ps_ind_02_cat"]))
    v["339"] = 0.020000 * np.tanh((data["loo_ps_car_07_cat"] * (
    np.tanh(0.232323) - (np.tanh(data["loo_ps_car_01_cat"]) + data["loo_ps_ind_12_bin"]))))
    v["340"] = 0.019047 * np.tanh(((data["ps_ind_01"] * (data["ps_reg_01"] * data["loo_ps_car_06_cat"])) - (
    data["ps_ind_14"] * data["ps_reg_01"])))
    v["341"] = 0.019996 * np.tanh((data["loo_ps_car_10_cat"] * (
    (np.tanh(np.tanh(data["ps_car_12"])) - data["ps_car_13"]) - data["loo_ps_ind_12_bin"])))
    v["342"] = 0.019996 * np.tanh((data["ps_car_14"] * (
    data["loo_ps_car_05_cat"] * (((data["loo_ps_car_05_cat"] + data["ps_car_15"]) + data["ps_reg_01"]) / 2.0))))
    v["343"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    np.tanh(((-(data["loo_ps_car_07_cat"])) + data["ps_reg_02"])) + data["loo_ps_ind_10_bin"])))
    v["344"] = 0.019902 * np.tanh(
        (data["ps_car_14"] * ((np.tanh(data["loo_ps_ind_05_cat"]) * data["ps_ind_15"]) - np.tanh(data["ps_reg_03"]))))
    v["345"] = 0.019937 * np.tanh(((data["ps_car_11"] * (data["ps_car_12"] * data["loo_ps_ind_09_bin"])) * (
    data["loo_ps_ind_11_bin"] - data["loo_ps_ind_18_bin"])))
    v["346"] = 0.019984 * np.tanh(((data["loo_ps_car_06_cat"] * (
    0.232323 - (data["loo_ps_ind_05_cat"] * data["loo_ps_ind_05_cat"]))) * data["loo_ps_ind_04_cat"]))
    v["347"] = 0.020000 * np.tanh(((data["loo_ps_ind_11_bin"] * data["ps_ind_03"]) * (
    (data["loo_ps_ind_05_cat"] * data["ps_ind_03"]) * data["ps_ind_03"])))
    v["348"] = 0.019934 * np.tanh((data["loo_ps_ind_16_bin"] * (
    data["loo_ps_ind_12_bin"] * (data["ps_car_13"] * (data["loo_ps_car_10_cat"] + data["loo_ps_car_03_cat"])))))
    v["349"] = 0.020000 * np.tanh(
        ((((data["ps_car_15"] + data["ps_ind_14"]) / 2.0) * data["loo_ps_ind_06_bin"]) * data["ps_reg_02"]))
    v["350"] = 0.019769 * np.tanh(
        ((((data["ps_ind_03"] - data["ps_reg_02"]) * 0.117647) - data["loo_ps_car_10_cat"]) * data["ps_ind_03"]))
    v["351"] = 0.019992 * np.tanh(
        (-(((0.232323 + ((data["loo_ps_car_03_cat"] * data["ps_ind_03"]) * data["loo_ps_car_08_cat"])) / 2.0))))
    v["352"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    (data["ps_ind_03"] * (0.232323 - data["loo_ps_car_11_cat"])) * data["ps_ind_15"])))
    v["353"] = 0.019980 * np.tanh(
        (np.tanh(data["ps_ind_03"]) * ((data["ps_car_11"] + (data["ps_reg_03"] + np.tanh(data["missing"]))) / 2.0)))
    v["354"] = 0.019988 * np.tanh(
        (data["ps_car_14"] * (((data["loo_ps_ind_12_bin"] + data["ps_car_12"]) / 2.0) * data["ps_reg_01"])))
    v["355"] = 0.019957 * np.tanh(
        np.tanh((data["loo_ps_car_07_cat"] * (0.633333 - (data["ps_reg_02"] * data["ps_reg_02"])))))
    v["356"] = 0.019977 * np.tanh((data["loo_ps_car_09_cat"] * (
    data["loo_ps_car_09_cat"] * (data["loo_ps_ind_16_bin"] * (data["ps_reg_01"] * data["ps_ind_15"])))))
    v["357"] = 0.019887 * np.tanh(((-(
    (((data["ps_car_14"] * data["loo_ps_ind_12_bin"]) + data["ps_reg_03"]) / 2.0))) * np.tanh(
        data["loo_ps_car_06_cat"])))
    v["358"] = 0.019965 * np.tanh((data["loo_ps_ind_05_cat"] * (
    data["ps_reg_02"] * ((np.tanh((-(data["ps_ind_15"]))) + data["loo_ps_car_09_cat"]) / 2.0))))
    v["359"] = 0.020000 * np.tanh((data["loo_ps_ind_12_bin"] * (
    (data["loo_ps_ind_11_bin"] + (data["loo_ps_car_11_cat"] + data["ps_ind_15"])) - data["loo_ps_ind_02_cat"])))
    v["360"] = 0.020000 * np.tanh(
        (((data["ps_reg_01"] + data["ps_car_13"]) / 2.0) * (data["ps_ind_01"] * data["loo_ps_ind_05_cat"])))
    v["361"] = 0.020000 * np.tanh(
        (data["loo_ps_ind_08_bin"] * (-((data["loo_ps_ind_05_cat"] * (data["ps_car_11"] - (-(data["ps_ind_03"]))))))))
    v["362"] = 0.018640 * np.tanh(((((-(((data["ps_car_15"] + data["ps_car_11"]) / 2.0))) + data[
        "loo_ps_car_05_cat"]) / 2.0) * data["loo_ps_ind_06_bin"]))
    v["363"] = 0.019480 * np.tanh((((np.tanh(data["ps_reg_02"]) * (
    (data["loo_ps_car_07_cat"] + data["loo_ps_ind_11_bin"]) / 2.0)) + np.tanh(data["loo_ps_car_07_cat"])) / 2.0))
    v["364"] = 0.020000 * np.tanh(
        (data["ps_ind_14"] * (-((0.753247 - ((data["ps_ind_03"] + data["ps_ind_03"]) / 2.0))))))
    v["365"] = 0.020000 * np.tanh(
        (((data["ps_reg_02"] * (-(data["loo_ps_ind_05_cat"]))) * data["ps_car_15"]) * data["loo_ps_ind_05_cat"]))
    v["366"] = 0.019992 * np.tanh((data["ps_ind_15"] * (
    data["loo_ps_ind_02_cat"] * ((data["loo_ps_ind_02_cat"] * data["ps_reg_01"]) - data["ps_ind_03"]))))
    v["367"] = 0.020000 * np.tanh(
        (data["ps_car_15"] * ((0.232323 + ((-(data["ps_ind_15"])) * data["ps_car_15"])) / 2.0)))
    v["368"] = 0.019992 * np.tanh((((data["loo_ps_car_02_cat"] + data["loo_ps_car_02_cat"]) - data["ps_car_11"]) * (
    data["loo_ps_ind_02_cat"] * data["loo_ps_ind_04_cat"])))
    v["369"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    data["ps_ind_15"] * ((data["ps_ind_15"] + (data["ps_reg_01"] * data["ps_car_13"])) / 2.0))))
    v["370"] = 0.019840 * np.tanh(
        (data["ps_car_12"] * ((data["ps_car_11"] + data["loo_ps_ind_12_bin"]) * (-(np.tanh(data["ps_ind_01"]))))))
    v["371"] = 0.020000 * np.tanh((data["loo_ps_ind_06_bin"] * (
    data["loo_ps_ind_12_bin"] * (data["ps_car_12"] + (data["ps_ind_03"] * data["loo_ps_ind_04_cat"])))))
    v["372"] = 0.017296 * np.tanh(
        (data["ps_car_11"] * ((data["ps_reg_03"] + np.tanh((data["loo_ps_car_04_cat"] - data["ps_car_11"]))) / 2.0)))
    v["373"] = 0.019992 * np.tanh((((data["loo_ps_ind_04_cat"] * data["ps_car_11"]) + np.tanh(
        (-((data["ps_car_11"] * data["loo_ps_ind_05_cat"]))))) / 2.0))
    v["374"] = 0.017175 * np.tanh((data["loo_ps_car_09_cat"] * np.tanh(
        ((data["loo_ps_ind_16_bin"] + data["ps_reg_02"]) + data["loo_ps_ind_16_bin"]))))
    v["375"] = 0.020000 * np.tanh(
        (np.tanh((0.618557 - data["loo_ps_ind_06_bin"])) * (data["loo_ps_car_08_cat"] * data["loo_ps_ind_02_cat"])))
    v["376"] = 0.019992 * np.tanh((np.tanh(data["loo_ps_ind_05_cat"]) * (
    ((-(data["loo_ps_car_02_cat"])) + (data["loo_ps_car_02_cat"] * data["ps_reg_03"])) / 2.0)))
    v["377"] = 0.019965 * np.tanh(
        ((-(data["loo_ps_car_04_cat"])) * (((data["ps_ind_03"] * data["ps_ind_03"]) + (-(data["ps_car_15"]))) / 2.0)))
    v["378"] = 0.019777 * np.tanh((data["loo_ps_ind_17_bin"] * (data["loo_ps_ind_17_bin"] * (
    ((data["loo_ps_ind_08_bin"] + data["loo_ps_ind_13_bin"]) / 2.0) * data["loo_ps_car_04_cat"]))))
    v["379"] = 0.019996 * np.tanh((data["loo_ps_car_02_cat"] * (
    ((data["loo_ps_car_01_cat"] + data["ps_car_11"]) / 2.0) * ((data["loo_ps_car_01_cat"] + data["ps_ind_15"]) / 2.0))))
    v["380"] = 0.019988 * np.tanh((data["loo_ps_ind_02_cat"] * (
    data["ps_car_15"] * (data["ps_car_11"] + (data["ps_ind_15"] * data["ps_reg_01"])))))
    v["381"] = 0.020000 * np.tanh(((0.0 + (
    data["loo_ps_ind_04_cat"] * (data["ps_reg_03"] * (data["loo_ps_car_04_cat"] * data["loo_ps_car_08_cat"])))) / 2.0))
    v["382"] = 0.019953 * np.tanh(((data["loo_ps_car_01_cat"] * data["loo_ps_car_01_cat"]) * (
    (data["ps_reg_01"] + (-(data["loo_ps_car_10_cat"]))) / 2.0)))
    v["383"] = 0.020000 * np.tanh(
        (-((data["ps_reg_03"] * (data["ps_ind_14"] * (data["loo_ps_car_04_cat"] * data["ps_reg_03"]))))))
    v["384"] = 0.019078 * np.tanh(
        np.tanh(((data["loo_ps_ind_06_bin"] * data["loo_ps_ind_05_cat"]) * ((-(0.432099)) - data["ps_reg_01"]))))
    v["385"] = 0.019934 * np.tanh(
        (data["loo_ps_car_03_cat"] * ((-(data["ps_car_13"])) * (data["loo_ps_car_10_cat"] * data["ps_car_13"]))))
    v["386"] = 0.019945 * np.tanh(
        np.tanh(((data["ps_ind_03"] * ((-(data["loo_ps_ind_04_cat"])) - data["missing"])) * data["loo_ps_ind_07_bin"])))
    v["387"] = 0.019680 * np.tanh((data["loo_ps_car_01_cat"] * (
    ((data["loo_ps_car_01_cat"] + (-(data["loo_ps_car_09_cat"]))) / 2.0) * np.tanh(data["loo_ps_ind_16_bin"]))))
    v["388"] = 0.020000 * np.tanh((data["loo_ps_ind_12_bin"] * (
    (-(data["ps_ind_01"])) * (data["loo_ps_ind_08_bin"] * data["loo_ps_ind_17_bin"]))))
    v["389"] = 0.020000 * np.tanh(
        (((data["ps_ind_03"] * 0.232323) + np.tanh((data["ps_reg_03"] * np.tanh(data["loo_ps_car_04_cat"])))) / 2.0))
    v["390"] = 0.019988 * np.tanh((data["loo_ps_car_08_cat"] * ((data["loo_ps_car_01_cat"] + (
    data["loo_ps_car_09_cat"] * (data["loo_ps_ind_04_cat"] * data["loo_ps_car_06_cat"]))) / 2.0)))
    v["391"] = 0.019988 * np.tanh(((data["loo_ps_ind_11_bin"] * data["ps_reg_03"]) - (
    (data["loo_ps_ind_11_bin"] + ((data["loo_ps_ind_16_bin"] + data["loo_ps_ind_10_bin"]) / 2.0)) / 2.0)))
    v["392"] = 0.020000 * np.tanh(
        ((data["loo_ps_ind_11_bin"] - data["loo_ps_car_10_cat"]) * (data["loo_ps_car_08_cat"] + data["ps_car_13"])))
    v["393"] = 0.019992 * np.tanh(((data["loo_ps_ind_05_cat"] * (
    (data["ps_ind_14"] + (data["ps_car_14"] * data["ps_reg_03"])) / 2.0)) * data["loo_ps_car_01_cat"]))
    v["394"] = 0.019238 * np.tanh(
        ((np.tanh((-(data["missing"]))) * data["loo_ps_ind_07_bin"]) * (-(data["ps_reg_01"]))))
    v["395"] = 0.019906 * np.tanh((-((np.tanh((data["ps_ind_14"] * data["loo_ps_ind_17_bin"])) * (
    data["loo_ps_ind_07_bin"] + data["loo_ps_ind_07_bin"])))))
    v["396"] = 0.019789 * np.tanh(
        np.tanh((-((data["loo_ps_car_03_cat"] * (data["ps_ind_01"] * (2.0 - data["ps_ind_01"])))))))
    v["397"] = 0.019949 * np.tanh(
        ((data["ps_car_13"] * (0.148148 * (-(np.tanh(data["ps_ind_15"]))))) * data["ps_car_13"]))
    v["398"] = 0.019137 * np.tanh(
        (data["loo_ps_ind_02_cat"] * (((-(data["ps_ind_03"])) * (-(data["ps_ind_03"]))) - 1.0)))
    v["399"] = 0.019895 * np.tanh(np.tanh(np.tanh(
        ((data["loo_ps_car_05_cat"] * data["ps_ind_01"]) + ((data["ps_ind_03"] + data["loo_ps_ind_18_bin"]) / 2.0)))))
    v["400"] = 0.015581 * np.tanh(
        (-((0.232323 * (data["loo_ps_ind_07_bin"] * (data["loo_ps_ind_16_bin"] + data["loo_ps_car_02_cat"]))))))
    return Outputs(v.sum(axis=1))


def GPII(data):
    v = pd.DataFrame()
    v["0"] = -3.274750
    v["1"] = 0.020000 * np.tanh((3.642860 * (
    (data["loo_ps_car_01_cat"] + data["loo_ps_ind_16_bin"]) + (data["ps_reg_03"] + data["loo_ps_ind_06_bin"]))))
    v["2"] = 0.020000 * np.tanh((19.500000 * (
    ((data["ps_car_15"] + data["loo_ps_ind_06_bin"]) + data["loo_ps_car_06_cat"]) + data["loo_ps_car_07_cat"])))
    v["3"] = 0.019996 * np.tanh((19.500000 * (
    (data["ps_car_13"] + (data["loo_ps_car_11_cat"] + data["loo_ps_ind_05_cat"])) + data["ps_reg_02"])))
    v["4"] = 0.020000 * np.tanh((((data["ps_reg_03"] + (data["loo_ps_ind_05_cat"] + data["loo_ps_car_07_cat"])) + data[
        "ps_car_12"]) * 19.500000))
    v["5"] = 0.020000 * np.tanh((data["loo_ps_ind_06_bin"] + (
    data["loo_ps_car_04_cat"] - (data["ps_ind_15"] - (data["loo_ps_ind_17_bin"] + data["loo_ps_car_01_cat"])))))
    v["6"] = 0.020000 * np.tanh(((11.51410007476806641) * (
    data["loo_ps_car_11_cat"] + (((data["loo_ps_car_09_cat"] + data["ps_reg_03"]) / 2.0) + data["loo_ps_ind_06_bin"]))))
    v["7"] = 0.020000 * np.tanh((19.500000 * ((data["ps_car_13"] + (
    (data["loo_ps_ind_05_cat"] + (data["loo_ps_ind_17_bin"] + data["loo_ps_car_01_cat"])) / 2.0)) / 2.0)))
    v["8"] = 0.020000 * np.tanh(
        (19.500000 * (((data["ps_reg_02"] + data["loo_ps_ind_09_bin"]) + 0.760563) + data["loo_ps_car_05_cat"])))
    v["9"] = 0.020000 * np.tanh((19.500000 * ((data["loo_ps_car_11_cat"] + (
    ((data["loo_ps_ind_17_bin"] + data["loo_ps_ind_06_bin"]) + data["loo_ps_car_03_cat"]) / 2.0)) / 2.0)))
    v["10"] = 0.020000 * np.tanh((6.846150 * (
    data["loo_ps_ind_06_bin"] + (data["loo_ps_car_11_cat"] + (data["loo_ps_ind_17_bin"] + data["loo_ps_car_09_cat"])))))
    v["11"] = 0.020000 * np.tanh(((9.75283908843994141) * (
    (data["ps_reg_03"] + (data["loo_ps_car_11_cat"] - data["ps_ind_15"])) + data["loo_ps_ind_04_cat"])))
    v["12"] = 0.020000 * np.tanh(((data["ps_reg_02"] + data["loo_ps_car_03_cat"]) + (
    (data["ps_car_13"] - data["ps_ind_15"]) + data["loo_ps_ind_05_cat"])))
    v["13"] = 0.020000 * np.tanh(((8.49180412292480469) * (
    (data["loo_ps_ind_09_bin"] + data["loo_ps_car_07_cat"]) + (data["loo_ps_car_09_cat"] + data["loo_ps_ind_06_bin"]))))
    v["14"] = 0.020000 * np.tanh(((6.0) * (
    (((data["loo_ps_ind_16_bin"] + data["loo_ps_ind_05_cat"]) + data["ps_reg_01"]) / 2.0) + data["ps_car_13"])))
    v["15"] = 0.020000 * np.tanh((data["loo_ps_car_01_cat"] + (
    ((data["ps_reg_01"] + data["ps_car_12"]) + data["loo_ps_car_03_cat"]) - data["ps_ind_15"])))
    v["16"] = 0.020000 * np.tanh(((data["loo_ps_car_08_cat"] + (
    data["loo_ps_car_04_cat"] + (data["loo_ps_ind_05_cat"] + data["loo_ps_ind_17_bin"]))) * 3.642860))
    v["17"] = 0.020000 * np.tanh(
        (19.500000 * ((0.760563 + (data["ps_reg_02"] + data["ps_car_13"])) + data["ps_reg_03"])))
    v["18"] = 0.020000 * np.tanh((data["loo_ps_ind_07_bin"] + (
    (9.29609489440917969) * (((data["loo_ps_car_03_cat"] + data["ps_reg_03"]) + data["ps_car_15"]) / 2.0))))
    v["19"] = 0.020000 * np.tanh((6.846150 * (
    (data["loo_ps_ind_05_cat"] + data["ps_car_13"]) + (data["loo_ps_ind_17_bin"] + data["loo_ps_car_07_cat"]))))
    v["20"] = 0.020000 * np.tanh((data["loo_ps_car_04_cat"] + (
    data["ps_car_15"] + (data["ps_reg_03"] + (data["loo_ps_car_03_cat"] - data["ps_ind_15"])))))
    v["21"] = 0.020000 * np.tanh((6.846150 * (
    data["loo_ps_ind_05_cat"] + ((data["ps_car_13"] + (data["ps_ind_03"] + data["loo_ps_ind_17_bin"])) / 2.0))))
    v["22"] = 0.020000 * np.tanh(
        (19.500000 * ((data["loo_ps_ind_16_bin"] - data["ps_ind_15"]) + (data["ps_reg_03"] + 0.600000))))
    v["23"] = 0.020000 * np.tanh((3.0 * (
    data["loo_ps_car_03_cat"] + (data["loo_ps_car_04_cat"] + (data["loo_ps_ind_05_cat"] + data["loo_ps_car_01_cat"])))))
    v["24"] = 0.020000 * np.tanh((6.846150 * (
    ((data["loo_ps_car_01_cat"] + data["ps_ind_03"]) + (data["loo_ps_ind_05_cat"] + data["loo_ps_ind_17_bin"])) / 2.0)))
    v["25"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] + (
    ((data["loo_ps_ind_17_bin"] + data["ps_car_13"]) + data["ps_reg_01"]) + data["loo_ps_ind_09_bin"])))
    v["26"] = 0.020000 * np.tanh(((data["loo_ps_ind_09_bin"] + (
    data["loo_ps_ind_17_bin"] + (data["loo_ps_ind_06_bin"] + data["loo_ps_ind_05_cat"]))) * 19.500000))
    v["27"] = 0.020000 * np.tanh(((data["ps_reg_03"] + (
    data["loo_ps_ind_06_bin"] + (data["loo_ps_car_01_cat"] + 1.871790))) * (13.13490962982177734)))
    v["28"] = 0.020000 * np.tanh((6.846150 * (
    data["loo_ps_ind_05_cat"] + ((data["loo_ps_ind_05_cat"] + (data["ps_car_13"] + data["loo_ps_ind_16_bin"])) / 2.0))))
    v["29"] = 0.020000 * np.tanh(((data["ps_reg_02"] + (
    data["loo_ps_ind_17_bin"] + (data["loo_ps_car_11_cat"] + data["ps_car_15"]))) - data["ps_ind_15"]))
    v["30"] = 0.020000 * np.tanh(
        ((3.0 * (data["loo_ps_ind_05_cat"] + (data["loo_ps_car_09_cat"] + data["ps_ind_03"]))) + data["ps_car_13"]))
    v["31"] = 0.020000 * np.tanh(((8.0) * (
    (data["loo_ps_ind_09_bin"] + data["loo_ps_ind_05_cat"]) + (data["ps_ind_03"] + data["loo_ps_car_07_cat"]))))
    v["32"] = 0.020000 * np.tanh((data["ps_reg_02"] + (
    (data["ps_car_13"] + data["loo_ps_car_01_cat"]) + ((1.11309552192687988) + data["loo_ps_car_07_cat"]))))
    v["33"] = 0.020000 * np.tanh((6.846150 * (((data["loo_ps_ind_05_cat"] - data["ps_ind_15"]) + (
    (data["loo_ps_ind_16_bin"] + data["loo_ps_car_09_cat"]) / 2.0)) / 2.0)))
    v["34"] = 0.020000 * np.tanh((19.500000 * ((data["loo_ps_car_07_cat"] + (
    ((data["ps_ind_03"] + data["loo_ps_ind_05_cat"]) + data["loo_ps_ind_06_bin"]) / 2.0)) / 2.0)))
    v["35"] = 0.020000 * np.tanh(((((data["loo_ps_ind_05_cat"] + data["loo_ps_car_07_cat"]) + (
    data["loo_ps_ind_07_bin"] + data["loo_ps_car_11_cat"])) / 2.0) * 19.500000))
    v["36"] = 0.020000 * np.tanh((((data["loo_ps_ind_06_bin"] + (
    data["loo_ps_car_09_cat"] + data["loo_ps_ind_05_cat"])) + data["loo_ps_ind_16_bin"]) * 19.500000))
    v["37"] = 0.020000 * np.tanh((((6.0) * (
    data["loo_ps_car_05_cat"] + (data["loo_ps_car_11_cat"] + data["loo_ps_ind_05_cat"]))) + data["ps_reg_02"]))
    v["38"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] + (data["loo_ps_car_01_cat"] - data["ps_ind_15"])) + (
    (data["loo_ps_ind_17_bin"] + data["loo_ps_ind_09_bin"]) / 2.0)))
    v["39"] = 0.020000 * np.tanh(
        ((data["ps_reg_03"] + (data["ps_reg_02"] + (data["loo_ps_ind_06_bin"] - -2.0))) + data["ps_ind_01"]))
    v["40"] = 0.020000 * np.tanh(
        (data["ps_car_13"] - (data["ps_ind_15"] - ((5.0) * (data["loo_ps_car_09_cat"] + data["loo_ps_ind_09_bin"])))))
    v["41"] = 0.020000 * np.tanh((((data["loo_ps_car_09_cat"] + (data["ps_ind_03"] * data["ps_ind_03"])) + data[
        "ps_ind_03"]) * (8.21348762512207031)))
    v["42"] = 0.020000 * np.tanh(((11.08931350708007812) * (
    ((data["loo_ps_ind_05_cat"] + data["ps_car_15"]) + data["ps_ind_01"]) + data["loo_ps_car_09_cat"])))
    v["43"] = 0.020000 * np.tanh((19.500000 * (
    data["loo_ps_car_09_cat"] + ((data["loo_ps_ind_04_cat"] - data["ps_ind_15"]) + data["loo_ps_car_05_cat"]))))
    v["44"] = 0.020000 * np.tanh((19.500000 * (
    (data["loo_ps_ind_17_bin"] + data["ps_reg_03"]) + (data["loo_ps_car_07_cat"] * data["loo_ps_car_07_cat"]))))
    v["45"] = 0.020000 * np.tanh(
        (data["ps_car_13"] - (data["ps_ind_15"] - ((data["loo_ps_ind_05_cat"] * (10.0)) - data["ps_car_11"]))))
    v["46"] = 0.020000 * np.tanh((
                                 (2.0 * ((data["loo_ps_car_07_cat"] + data["ps_ind_01"]) + data["loo_ps_ind_09_bin"])) +
                                 data["loo_ps_ind_17_bin"]))
    v["47"] = 0.020000 * np.tanh((((data["loo_ps_ind_02_cat"] + (
    data["loo_ps_ind_16_bin"] + data["loo_ps_ind_02_cat"])) - data["loo_ps_ind_18_bin"]) * (10.0)))
    v["48"] = 0.020000 * np.tanh((((data["ps_ind_03"] + (data["ps_ind_03"] * data["ps_ind_03"])) * (
    14.62119007110595703)) * (14.62119007110595703)))
    v["49"] = 0.020000 * np.tanh(
        ((6.846150 * (data["loo_ps_car_01_cat"] + data["loo_ps_car_09_cat"])) + (data["ps_car_13"] + 1.135800)))
    v["50"] = 0.020000 * np.tanh(((7.46593427658081055) * (
    (7.46593427658081055) * ((data["ps_ind_03"] * data["ps_ind_03"]) + data["ps_ind_03"]))))
    v["51"] = 0.020000 * np.tanh(
        ((data["loo_ps_ind_07_bin"] + (0.965909 - data["ps_ind_15"])) * (3.642860 - data["loo_ps_ind_06_bin"])))
    v["52"] = 0.020000 * np.tanh((data["loo_ps_ind_07_bin"] + (
    (7.95933532714843750) * (data["loo_ps_car_07_cat"] - (data["ps_ind_03"] * data["loo_ps_ind_02_cat"])))))
    v["53"] = 0.020000 * np.tanh(
        ((data["loo_ps_ind_05_cat"] + (data["loo_ps_ind_17_bin"] + (data["loo_ps_ind_06_bin"] + -2.0))) * 6.846150))
    v["54"] = 0.020000 * np.tanh(((data["loo_ps_ind_09_bin"] + (
    data["loo_ps_car_07_cat"] + ((data["ps_reg_03"] + data["ps_car_13"]) / 2.0))) * (8.96369743347167969)))
    v["55"] = 0.020000 * np.tanh(
        (data["loo_ps_ind_04_cat"] + (data["ps_ind_03"] - (data["ps_ind_03"] * ((7.0) * data["loo_ps_ind_02_cat"])))))
    v["56"] = 0.020000 * np.tanh(
        ((4.0) * (data["ps_reg_02"] + (data["ps_reg_03"] + ((data["loo_ps_ind_02_cat"] + data["ps_car_15"]) / 2.0)))))
    v["57"] = 0.020000 * np.tanh(((data["loo_ps_car_09_cat"] + (
    data["loo_ps_car_09_cat"] + (data["loo_ps_ind_05_cat"] * data["loo_ps_ind_06_bin"]))) * 19.500000))
    v["58"] = 0.020000 * np.tanh((3.642860 * (
    data["loo_ps_ind_05_cat"] + ((data["loo_ps_car_05_cat"] * data["ps_ind_03"]) - data["ps_car_11"]))))
    v["59"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] + (
    data["loo_ps_car_07_cat"] + ((data["ps_ind_15"] * data["loo_ps_ind_18_bin"]) * 6.846150))))
    v["60"] = 0.020000 * np.tanh((((6.846150 * data["loo_ps_ind_02_cat"]) + (
    data["ps_ind_01"] + data["loo_ps_ind_07_bin"])) + data["loo_ps_car_01_cat"]))
    v["61"] = 0.020000 * np.tanh(((data["loo_ps_ind_17_bin"] + (data["loo_ps_ind_05_cat"] * data["ps_car_13"])) + (
    data["loo_ps_ind_17_bin"] - data["ps_ind_03"])))
    v["62"] = 0.020000 * np.tanh((((data["loo_ps_car_03_cat"] + data["ps_car_13"]) + data["loo_ps_car_04_cat"]) * (
    data["loo_ps_ind_05_cat"] + data["loo_ps_ind_16_bin"])))
    v["63"] = 0.020000 * np.tanh(((data["loo_ps_ind_17_bin"] * data["loo_ps_ind_09_bin"]) + (
    data["loo_ps_ind_16_bin"] * (data["ps_ind_01"] + data["loo_ps_car_01_cat"]))))
    v["64"] = 0.020000 * np.tanh((data["loo_ps_car_03_cat"] * (
    data["missing"] + (data["loo_ps_ind_17_bin"] + (data["ps_ind_01"] + data["loo_ps_car_11_cat"])))))
    v["65"] = 0.020000 * np.tanh((((data["ps_reg_02"] + data["loo_ps_ind_06_bin"]) + data["loo_ps_car_11_cat"]) * (
    data["loo_ps_ind_05_cat"] - data["ps_car_11"])))
    v["66"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] - data["ps_reg_01"]) * (
    data["ps_car_12"] + (data["loo_ps_car_11_cat"] + data["loo_ps_ind_17_bin"]))))
    v["67"] = 0.020000 * np.tanh(((data["loo_ps_ind_17_bin"] * data["loo_ps_ind_06_bin"]) + (
    data["loo_ps_ind_04_cat"] + ((data["loo_ps_ind_08_bin"] + data["ps_car_13"]) / 2.0))))
    v["68"] = 0.020000 * np.tanh(((data["ps_car_13"] * (data["loo_ps_ind_05_cat"] - data["ps_car_11"])) + (
    data["loo_ps_ind_16_bin"] * data["loo_ps_ind_05_cat"])))
    v["69"] = 0.020000 * np.tanh(((data["ps_ind_01"] * (data["loo_ps_car_05_cat"] - data["ps_ind_15"])) + (
    (data["loo_ps_car_07_cat"] + data["ps_car_13"]) / 2.0)))
    v["70"] = 0.020000 * np.tanh(
        ((data["loo_ps_ind_05_cat"] * 19.500000) * (data["loo_ps_ind_17_bin"] + data["ps_reg_02"])))
    v["71"] = 0.020000 * np.tanh(
        (-1.0 + (data["loo_ps_ind_05_cat"] + (data["ps_ind_03"] * (data["ps_ind_03"] - data["loo_ps_ind_02_cat"])))))
    v["72"] = 0.020000 * np.tanh((((data["loo_ps_ind_06_bin"] + data["ps_car_13"]) * (
    data["ps_ind_03"] + data["loo_ps_ind_05_cat"])) - data["ps_ind_03"]))
    v["73"] = 0.020000 * np.tanh((data["loo_ps_ind_04_cat"] + (
    data["loo_ps_ind_16_bin"] * (data["loo_ps_car_09_cat"] + (data["ps_reg_02"] * data["ps_reg_02"])))))
    v["74"] = 0.020000 * np.tanh(
        (((data["loo_ps_car_03_cat"] * 3.0) * 3.0) * (data["ps_ind_15"] + data["loo_ps_ind_17_bin"])))
    v["75"] = 0.020000 * np.tanh((((data["ps_ind_01"] + data["loo_ps_ind_17_bin"]) / 2.0) * (
    (data["loo_ps_car_07_cat"] - data["ps_car_11"]) - data["ps_ind_15"])))
    v["76"] = 0.020000 * np.tanh((((data["loo_ps_car_09_cat"] - (data["loo_ps_car_04_cat"] * data["ps_car_11"])) + data[
        "ps_reg_02"]) - data["loo_ps_car_04_cat"]))
    v["77"] = 0.019992 * np.tanh(((((data["ps_ind_03"] - data["ps_ind_15"]) * data["ps_car_12"]) + data[
        "loo_ps_car_07_cat"]) + data["loo_ps_ind_04_cat"]))
    v["78"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    (data["loo_ps_car_09_cat"] + data["ps_ind_01"]) + (data["loo_ps_car_03_cat"] + data["ps_ind_01"]))))
    v["79"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] + data["loo_ps_car_09_cat"]) * (
    (data["loo_ps_ind_07_bin"] + data["loo_ps_ind_16_bin"]) + data["loo_ps_car_04_cat"])))
    v["80"] = 0.020000 * np.tanh(((data["loo_ps_ind_17_bin"] + data["loo_ps_car_07_cat"]) * (
    (data["loo_ps_car_09_cat"] + data["loo_ps_ind_09_bin"]) + data["ps_reg_02"])))
    v["81"] = 0.020000 * np.tanh(((data["loo_ps_ind_04_cat"] + (
    data["loo_ps_car_03_cat"] * data["loo_ps_ind_09_bin"])) + (data["ps_ind_01"] * data["loo_ps_car_04_cat"])))
    v["82"] = 0.020000 * np.tanh(((data["loo_ps_car_01_cat"] * data["loo_ps_car_05_cat"]) - (
    data["ps_ind_15"] * (data["ps_car_13"] - data["loo_ps_ind_06_bin"]))))
    v["83"] = 0.019996 * np.tanh(
        ((data["ps_ind_03"] * ((data["loo_ps_ind_09_bin"] - data["ps_reg_01"]) - data["missing"])) - data["ps_car_11"]))
    v["84"] = 0.020000 * np.tanh((data["loo_ps_car_02_cat"] + (
    ((data["ps_car_13"] + data["loo_ps_car_09_cat"]) / 2.0) + (data["loo_ps_car_02_cat"] - data["ps_ind_03"]))))
    v["85"] = 0.020000 * np.tanh(
        (data["ps_ind_01"] + (data["ps_reg_01"] * ((data["missing"] - data["ps_ind_01"]) - data["loo_ps_car_01_cat"]))))
    v["86"] = 0.020000 * np.tanh(((data["loo_ps_ind_17_bin"] - (
    (data["ps_reg_03"] + data["loo_ps_ind_09_bin"]) / 2.0)) * (data["loo_ps_car_01_cat"] - data["ps_ind_15"])))
    v["87"] = 0.020000 * np.tanh(((data["loo_ps_ind_07_bin"] + data["loo_ps_ind_04_cat"]) * (
    data["ps_ind_03"] + ((data["loo_ps_car_05_cat"] + data["loo_ps_car_09_cat"]) / 2.0))))
    v["88"] = 0.020000 * np.tanh(((data["loo_ps_ind_04_cat"] - data["loo_ps_car_04_cat"]) + (
    (data["loo_ps_car_07_cat"] + data["loo_ps_ind_07_bin"]) * data["loo_ps_ind_17_bin"])))
    v["89"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] * data["loo_ps_ind_17_bin"]) + (
    (data["loo_ps_ind_05_cat"] - data["loo_ps_ind_02_cat"]) * data["ps_ind_03"])))
    v["90"] = 0.020000 * np.tanh((data["ps_ind_03"] - (
    ((data["ps_ind_03"] * data["loo_ps_ind_02_cat"]) + data["loo_ps_ind_02_cat"]) * 6.846150)))
    v["91"] = 0.019980 * np.tanh((np.tanh((-(data["loo_ps_car_11_cat"]))) + (
    data["loo_ps_car_07_cat"] - (data["ps_ind_15"] * data["loo_ps_car_11_cat"]))))
    v["92"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] + (
    (data["loo_ps_ind_05_cat"] * (data["ps_reg_02"] + data["loo_ps_ind_17_bin"])) - data["loo_ps_ind_05_cat"])))
    v["93"] = 0.019996 * np.tanh(((data["loo_ps_ind_02_cat"] + data["loo_ps_ind_02_cat"]) * (
    (data["loo_ps_car_08_cat"] - data["ps_ind_03"]) + data["loo_ps_car_08_cat"])))
    v["94"] = 0.020000 * np.tanh((((data["loo_ps_ind_05_cat"] * (data["loo_ps_ind_07_bin"] + data["ps_reg_02"])) + (
    data["loo_ps_ind_02_cat"] - data["ps_ind_03"])) / 2.0))
    v["95"] = 0.020000 * np.tanh((((data["loo_ps_car_09_cat"] + data["ps_reg_01"]) / 2.0) - (
    data["loo_ps_ind_06_bin"] * (data["ps_car_15"] + data["ps_reg_01"]))))
    v["96"] = 0.020000 * np.tanh(((data["loo_ps_ind_02_cat"] + (
    ((data["loo_ps_car_09_cat"] + data["loo_ps_ind_18_bin"]) / 2.0) * data["loo_ps_ind_17_bin"])) * data[
                                      "loo_ps_car_09_cat"]))
    v["97"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    (data["loo_ps_ind_07_bin"] + data["ps_ind_15"]) + (data["ps_ind_01"] + data["loo_ps_car_09_cat"]))))
    v["98"] = 0.020000 * np.tanh(
        (data["ps_reg_02"] + (((data["loo_ps_ind_02_cat"] - data["ps_ind_03"]) * data["loo_ps_ind_02_cat"]) + -1.0)))
    v["99"] = 0.020000 * np.tanh((((data["ps_ind_03"] - data["ps_car_15"]) - data["ps_ind_15"]) * (
    (data["ps_car_15"] + data["ps_ind_03"]) / 2.0)))
    v["100"] = 0.020000 * np.tanh(((((data["ps_reg_03"] + data["loo_ps_car_09_cat"]) / 2.0) + data[
        "loo_ps_ind_05_cat"]) * (-2.0 + data["loo_ps_ind_05_cat"])))
    v["101"] = 0.020000 * np.tanh((((data["ps_car_15"] + data["loo_ps_car_09_cat"]) / 2.0) - (
    data["loo_ps_car_03_cat"] * (data["ps_car_15"] - data["loo_ps_ind_09_bin"]))))
    v["102"] = 0.020000 * np.tanh((data["ps_ind_01"] + (
    data["loo_ps_ind_04_cat"] - ((data["ps_car_11"] + data["ps_ind_01"]) * data["ps_ind_01"]))))
    v["103"] = 0.019988 * np.tanh((((data["ps_reg_03"] * (data["loo_ps_ind_05_cat"] - data["ps_ind_01"])) + (
    (data["ps_car_13"] + data["loo_ps_ind_04_cat"]) / 2.0)) / 2.0))
    v["104"] = 0.020000 * np.tanh((data["loo_ps_car_08_cat"] + (
    data["loo_ps_car_03_cat"] * ((data["loo_ps_ind_04_cat"] + data["ps_reg_03"]) + data["ps_reg_03"]))))
    v["105"] = 0.020000 * np.tanh(((((data["loo_ps_ind_05_cat"] * data["loo_ps_ind_17_bin"]) - data[
        "loo_ps_car_07_cat"]) + data["loo_ps_ind_02_cat"]) - data["loo_ps_ind_05_cat"]))
    v["106"] = 0.019996 * np.tanh(((data["ps_ind_01"] - (data["ps_car_15"] * data["loo_ps_ind_17_bin"])) + (
    (data["ps_ind_01"] + data["loo_ps_car_01_cat"]) / 2.0)))
    v["107"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] + (data["ps_ind_01"] + data["loo_ps_car_09_cat"])) * (
    data["loo_ps_ind_17_bin"] - data["ps_reg_01"])))
    v["108"] = 0.020000 * np.tanh((data["loo_ps_ind_04_cat"] * (
    data["ps_car_11"] + ((data["loo_ps_car_09_cat"] + data["ps_ind_03"]) - data["loo_ps_ind_06_bin"]))))
    v["109"] = 0.020000 * np.tanh(((data["missing"] + (
    (data["loo_ps_ind_05_cat"] + data["ps_reg_02"]) * (data["loo_ps_car_11_cat"] * data["loo_ps_car_05_cat"]))) / 2.0))
    v["110"] = 0.019996 * np.tanh((data["ps_reg_03"] * (
    ((data["ps_car_11"] + data["loo_ps_car_09_cat"]) / 2.0) - ((data["loo_ps_ind_02_cat"] + data["ps_reg_01"]) / 2.0))))
    v["111"] = 0.019988 * np.tanh(((-1.0 + (data["loo_ps_ind_02_cat"] * data["loo_ps_ind_02_cat"])) * (
    data["loo_ps_ind_02_cat"] + data["loo_ps_ind_02_cat"])))
    v["112"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    data["loo_ps_ind_05_cat"] - (1.526320 - np.tanh((-(data["loo_ps_ind_05_cat"])))))))
    v["113"] = 0.020000 * np.tanh((((((data["loo_ps_ind_16_bin"] + data["loo_ps_car_01_cat"]) / 2.0) + data[
        "ps_ind_03"]) / 2.0) * (data["missing"] - data["ps_car_11"])))
    v["114"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] - data["ps_reg_01"]) * (
    data["loo_ps_ind_08_bin"] + (data["ps_ind_01"] + data["loo_ps_car_04_cat"]))))
    v["115"] = 0.020000 * np.tanh(
        (-((data["ps_reg_02"] * (data["loo_ps_ind_04_cat"] + (data["ps_reg_02"] * data["loo_ps_car_07_cat"]))))))
    v["116"] = 0.020000 * np.tanh(((data["ps_ind_03"] + (data["ps_ind_03"] + 3.0)) * (data["ps_ind_03"] + -2.0)))
    v["117"] = 0.020000 * np.tanh((data["loo_ps_car_09_cat"] - (
    data["loo_ps_car_04_cat"] * ((data["ps_car_11"] + data["ps_ind_15"]) + 1.871790))))
    v["118"] = 0.020000 * np.tanh((data["ps_reg_03"] * (
    data["ps_reg_03"] - ((0.513158 - data["loo_ps_ind_07_bin"]) * data["loo_ps_ind_16_bin"]))))
    v["119"] = 0.020000 * np.tanh(((((data["ps_reg_03"] + data["loo_ps_car_09_cat"]) * (
    data["loo_ps_ind_05_cat"] - data["ps_reg_01"])) + data["ps_reg_01"]) / 2.0))
    v["120"] = 0.020000 * np.tanh((((((data["missing"] + data["loo_ps_car_04_cat"]) / 2.0) + data[
        "loo_ps_car_03_cat"]) / 2.0) * (data["loo_ps_ind_02_cat"] + data["loo_ps_car_11_cat"])))
    v["121"] = 0.019988 * np.tanh(
        ((data["ps_ind_03"] * (data["ps_ind_03"] - data["ps_ind_01"])) + (data["ps_ind_03"] - data["ps_ind_01"])))
    v["122"] = 0.020000 * np.tanh(((data["loo_ps_ind_02_cat"] * (
    data["loo_ps_ind_04_cat"] * (data["loo_ps_ind_02_cat"] - 2.800000))) - data["loo_ps_car_10_cat"]))
    v["123"] = 0.020000 * np.tanh((data["loo_ps_car_05_cat"] * (
    data["ps_ind_01"] + ((data["loo_ps_ind_07_bin"] + ((data["loo_ps_ind_04_cat"] + data["ps_ind_03"]) / 2.0)) / 2.0))))
    v["124"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] * (data["ps_reg_02"] * data["ps_reg_01"])) - (
    0.452381 + data["loo_ps_ind_05_cat"])))
    v["125"] = 0.020000 * np.tanh((data["loo_ps_car_01_cat"] * (
    (data["loo_ps_car_01_cat"] + ((-3.0 * data["ps_car_13"]) - data["loo_ps_ind_06_bin"])) / 2.0)))
    v["126"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    (data["loo_ps_ind_02_cat"] + (data["ps_reg_03"] + (data["loo_ps_ind_09_bin"] - 0.965909))) / 2.0)))
    v["127"] = 0.019988 * np.tanh(((((data["loo_ps_ind_02_cat"] - data["loo_ps_car_07_cat"]) + (
    data["loo_ps_car_04_cat"] * data["ps_car_12"])) / 2.0) * 0.485294))
    v["128"] = 0.020000 * np.tanh((((data["loo_ps_car_09_cat"] * data["loo_ps_car_09_cat"]) - data["ps_reg_02"]) * (
    (data["ps_reg_03"] + data["loo_ps_ind_04_cat"]) / 2.0)))
    v["129"] = 0.020000 * np.tanh(
        (((data["ps_reg_03"] + data["ps_reg_03"]) * np.tanh(data["ps_ind_03"])) - data["ps_ind_03"]))
    v["130"] = 0.020000 * np.tanh(
        ((data["ps_reg_03"] * data["ps_reg_03"]) * ((data["loo_ps_ind_17_bin"] + data["ps_car_13"]) / 2.0)))
    v["131"] = 0.020000 * np.tanh((data["ps_reg_01"] * (
    0.273684 - ((data["loo_ps_car_09_cat"] + (data["ps_reg_03"] - data["ps_reg_01"])) / 2.0))))
    v["132"] = 0.020000 * np.tanh((((data["loo_ps_ind_05_cat"] + data["loo_ps_car_05_cat"]) / 2.0) * (
    (data["ps_reg_03"] * data["ps_reg_03"]) - 0.760563)))
    v["133"] = 0.020000 * np.tanh(
        (((data["loo_ps_ind_02_cat"] * (-(data["ps_ind_03"]))) * (-(data["ps_ind_03"]))) - data["loo_ps_ind_02_cat"]))
    v["134"] = 0.020000 * np.tanh((((data["loo_ps_car_09_cat"] + -3.0) / 2.0) * (
    (((data["ps_car_11"] + 1.135800) / 2.0) + data["loo_ps_ind_02_cat"]) / 2.0)))
    v["135"] = 0.020000 * np.tanh((data["loo_ps_car_07_cat"] * (
    ((2.0 + (data["loo_ps_ind_04_cat"] - data["loo_ps_car_07_cat"])) / 2.0) - data["ps_car_13"])))
    v["136"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    (((data["loo_ps_ind_04_cat"] + data["ps_reg_03"]) / 2.0) + np.tanh(data["ps_ind_03"])) / 2.0)))
    v["137"] = 0.020000 * np.tanh((((data["ps_reg_01"] * (data["ps_reg_01"] - data["loo_ps_ind_18_bin"])) + (
    data["ps_car_11"] * data["loo_ps_car_06_cat"])) / 2.0))
    v["138"] = 0.019996 * np.tanh(
        (data["loo_ps_ind_02_cat"] * (-3.0 + (data["ps_ind_03"] * (data["ps_ind_03"] + data["ps_ind_03"])))))
    v["139"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    (data["loo_ps_car_09_cat"] * data["loo_ps_car_09_cat"]) + (data["ps_car_13"] * data["loo_ps_car_07_cat"]))))
    v["140"] = 0.020000 * np.tanh(((-((data["ps_ind_03"] * data["loo_ps_ind_02_cat"]))) - np.tanh(
        (data["loo_ps_ind_05_cat"] * data["loo_ps_ind_05_cat"]))))
    v["141"] = 0.020000 * np.tanh((data["ps_car_13"] - (data["loo_ps_car_04_cat"] - (
    data["loo_ps_car_07_cat"] + ((data["loo_ps_ind_18_bin"] + data["loo_ps_car_07_cat"]) / 2.0)))))
    v["142"] = 0.020000 * np.tanh((((data["loo_ps_ind_02_cat"] - data["loo_ps_car_07_cat"]) + (
    data["loo_ps_ind_17_bin"] * (data["ps_ind_03"] - data["ps_car_15"]))) / 2.0))
    v["143"] = 0.020000 * np.tanh(((((data["loo_ps_ind_02_cat"] + data["ps_car_13"]) / 2.0) - 1.135800) * (
    data["loo_ps_ind_02_cat"] + data["ps_car_13"])))
    v["144"] = 0.020000 * np.tanh(((data["loo_ps_car_09_cat"] - data["ps_car_14"]) * (
    data["loo_ps_car_02_cat"] + (data["loo_ps_car_05_cat"] * data["loo_ps_car_07_cat"]))))
    v["145"] = 0.020000 * np.tanh(((data["loo_ps_ind_04_cat"] - data["ps_ind_01"]) * (
    data["loo_ps_ind_04_cat"] + (data["loo_ps_ind_04_cat"] - data["loo_ps_car_07_cat"]))))
    v["146"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    data["loo_ps_ind_05_cat"] * ((data["loo_ps_ind_05_cat"] + (-2.0 - 0.452381)) / 2.0))))
    v["147"] = 0.020000 * np.tanh(
        (-((((data["loo_ps_ind_04_cat"] + data["loo_ps_ind_04_cat"]) + data["ps_car_15"]) * data["ps_reg_02"]))))
    v["148"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    (data["loo_ps_ind_02_cat"] * (data["loo_ps_ind_02_cat"] + data["loo_ps_car_08_cat"])) + data["loo_ps_car_08_cat"])))
    v["149"] = 0.020000 * np.tanh(((data["loo_ps_ind_04_cat"] * (
    data["loo_ps_car_03_cat"] * (data["loo_ps_ind_04_cat"] + data["loo_ps_car_04_cat"]))) - data["loo_ps_car_10_cat"]))
    v["150"] = 0.020000 * np.tanh(((data["missing"] * (
    (data["ps_ind_01"] + ((data["loo_ps_ind_02_cat"] + data["ps_ind_01"]) / 2.0)) / 2.0)) - data["loo_ps_car_10_cat"]))
    v["151"] = 0.020000 * np.tanh((((data["ps_ind_01"] * (data["ps_ind_01"] * data["loo_ps_car_03_cat"])) + (
    (data["ps_ind_03"] + data["loo_ps_ind_04_cat"]) / 2.0)) / 2.0))
    v["152"] = 0.019965 * np.tanh(
        (data["ps_reg_01"] - ((data["ps_reg_01"] + data["loo_ps_ind_02_cat"]) * data["ps_ind_03"])))
    v["153"] = 0.020000 * np.tanh(
        ((data["ps_ind_03"] * data["loo_ps_ind_05_cat"]) * (-((data["ps_ind_01"] - data["ps_reg_01"])))))
    v["154"] = 0.019988 * np.tanh((((((data["loo_ps_ind_04_cat"] + -1.0) / 2.0) + data["ps_ind_01"]) / 2.0) - (
    data["ps_car_11"] * data["ps_ind_01"])))
    v["155"] = 0.020000 * np.tanh((((data["loo_ps_car_07_cat"] + (
    (data["loo_ps_car_09_cat"] + data["ps_car_12"]) / 2.0)) / 2.0) * (
                                   data["loo_ps_ind_06_bin"] * data["loo_ps_ind_16_bin"])))
    v["156"] = 0.020000 * np.tanh(
        ((data["loo_ps_car_01_cat"] - data["loo_ps_car_06_cat"]) * (data["missing"] + data["loo_ps_ind_08_bin"])))
    v["157"] = 0.020000 * np.tanh(((data["loo_ps_car_07_cat"] + (
    data["ps_car_12"] * ((data["loo_ps_car_01_cat"] - data["loo_ps_car_07_cat"]) - data["loo_ps_car_07_cat"]))) / 2.0))
    v["158"] = 0.020000 * np.tanh((((data["loo_ps_car_01_cat"] * (data["loo_ps_car_01_cat"] * 0.020833)) + (
    data["ps_car_15"] * data["missing"])) / 2.0))
    v["159"] = 0.020000 * np.tanh(((0.093750 - data["ps_reg_01"]) * (
    data["loo_ps_car_09_cat"] * (data["ps_car_12"] + data["loo_ps_car_09_cat"]))))
    v["160"] = 0.020000 * np.tanh((((data["loo_ps_ind_09_bin"] + (
    data["loo_ps_car_09_cat"] * (data["loo_ps_car_05_cat"] * data["loo_ps_car_04_cat"]))) / 2.0) * data[
                                       "loo_ps_car_09_cat"]))
    v["161"] = 0.019977 * np.tanh(
        (((-((data["loo_ps_car_01_cat"] * data["ps_reg_03"]))) - data["ps_car_12"]) - data["ps_ind_14"]))
    v["162"] = 0.020000 * np.tanh(((((data["loo_ps_car_01_cat"] * data["loo_ps_car_01_cat"]) * (
    data["loo_ps_car_01_cat"] - data["loo_ps_car_07_cat"])) + 0.760563) / 2.0))
    v["163"] = 0.019988 * np.tanh((((data["loo_ps_ind_02_cat"] + (
    (data["ps_car_12"] - 0.513158) - data["loo_ps_ind_06_bin"])) / 2.0) - data["loo_ps_car_10_cat"]))
    v["164"] = 0.020000 * np.tanh((data["ps_car_15"] + (
    data["loo_ps_ind_02_cat"] * ((data["loo_ps_car_07_cat"] * data["loo_ps_car_07_cat"]) * data["loo_ps_car_01_cat"]))))
    v["165"] = 0.019988 * np.tanh((((data["loo_ps_ind_04_cat"] + (
    data["loo_ps_car_07_cat"] - data["ps_car_15"])) / 2.0) + (data["loo_ps_ind_09_bin"] * data["loo_ps_car_07_cat"])))
    v["166"] = 0.020000 * np.tanh((((data["loo_ps_car_10_cat"] + data["loo_ps_car_01_cat"]) * data[
        "loo_ps_ind_17_bin"]) * (data["loo_ps_car_09_cat"] + data["loo_ps_ind_04_cat"])))
    v["167"] = 0.018984 * np.tanh((((10.63927078247070312) * (-(data["loo_ps_ind_05_cat"]))) * (
    (data["ps_reg_01"] + np.tanh(data["loo_ps_ind_16_bin"])) / 2.0)))
    v["168"] = 0.020000 * np.tanh((((data["loo_ps_car_07_cat"] + data["ps_ind_03"]) / 2.0) * (
    ((data["loo_ps_ind_17_bin"] * data["loo_ps_ind_04_cat"]) + data["ps_ind_03"]) / 2.0)))
    v["169"] = 0.020000 * np.tanh(
        ((((-1.0 + (data["loo_ps_ind_05_cat"] - 0.347826)) / 2.0) + (data["ps_ind_15"] * data["ps_reg_01"])) / 2.0))
    v["170"] = 0.020000 * np.tanh((data["loo_ps_ind_16_bin"] * (
    (0.100000 * data["loo_ps_car_01_cat"]) - ((data["loo_ps_car_10_cat"] + 0.166667) / 2.0))))
    v["171"] = 0.020000 * np.tanh(((data["loo_ps_car_05_cat"] * data["loo_ps_ind_17_bin"]) * (
    (data["loo_ps_ind_04_cat"] * data["loo_ps_ind_04_cat"]) - data["ps_car_11"])))
    v["172"] = 0.019992 * np.tanh((data["loo_ps_ind_07_bin"] * (
    data["ps_reg_03"] + (-(((data["loo_ps_car_01_cat"] + np.tanh(data["loo_ps_car_02_cat"])) / 2.0))))))
    v["173"] = 0.020000 * np.tanh((((((data["loo_ps_ind_04_cat"] + data["loo_ps_ind_05_cat"]) / 2.0) + data[
        "loo_ps_ind_08_bin"]) / 2.0) * (data["loo_ps_car_09_cat"] + data["ps_ind_03"])))
    v["174"] = 0.019988 * np.tanh(((((data["loo_ps_ind_04_cat"] + data["ps_ind_14"]) / 2.0) - (
    (data["loo_ps_car_03_cat"] + 1.526320) / 2.0)) * data["loo_ps_ind_04_cat"]))
    v["175"] = 0.020000 * np.tanh((data["loo_ps_ind_17_bin"] * (
    (((data["loo_ps_ind_02_cat"] + (-(data["loo_ps_ind_12_bin"]))) / 2.0) + data["loo_ps_car_05_cat"]) / 2.0)))
    v["176"] = 0.019902 * np.tanh(((data["ps_reg_03"] + (data["ps_reg_03"] + np.tanh(data["loo_ps_ind_05_cat"]))) * (
    -(data["loo_ps_car_11_cat"]))))
    v["177"] = 0.019996 * np.tanh((((data["ps_reg_02"] + data["loo_ps_ind_02_cat"]) / 2.0) * (
    data["ps_car_12"] + (data["loo_ps_ind_05_cat"] * data["loo_ps_ind_16_bin"]))))
    v["178"] = 0.020000 * np.tanh(
        (data["ps_ind_15"] * (data["ps_ind_03"] * (-(((data["ps_reg_01"] + data["ps_ind_01"]) / 2.0))))))
    v["179"] = 0.020000 * np.tanh(((data["loo_ps_car_01_cat"] * data["loo_ps_car_11_cat"]) * (
    data["ps_ind_03"] + ((data["ps_reg_01"] + data["loo_ps_car_01_cat"]) / 2.0))))
    v["180"] = 0.020000 * np.tanh((((data["loo_ps_ind_04_cat"] + (-(data["loo_ps_ind_16_bin"]))) / 2.0) - (
    data["ps_reg_03"] * data["ps_reg_01"])))
    v["181"] = 0.020000 * np.tanh(((data["loo_ps_ind_04_cat"] + (
    data["loo_ps_car_04_cat"] * (0.583333 - (data["ps_ind_03"] * data["ps_ind_03"])))) / 2.0))
    v["182"] = 0.019992 * np.tanh(
        ((data["ps_reg_03"] * data["ps_reg_03"]) + np.tanh((data["ps_ind_03"] * data["loo_ps_ind_04_cat"]))))
    v["183"] = 0.019961 * np.tanh(((data["ps_ind_15"] * (
    np.tanh((-(data["loo_ps_car_11_cat"]))) - data["loo_ps_car_09_cat"])) * data["loo_ps_car_11_cat"]))
    v["184"] = 0.020000 * np.tanh((((data["loo_ps_ind_16_bin"] + data["loo_ps_ind_07_bin"]) / 2.0) * (
    (data["missing"] + (-(data["ps_reg_01"]))) / 2.0)))
    v["185"] = 0.019949 * np.tanh((data["loo_ps_car_04_cat"] * (
    (data["ps_reg_03"] + (data["loo_ps_ind_02_cat"] - data["loo_ps_car_04_cat"])) / 2.0)))
    v["186"] = 0.020000 * np.tanh((((data["ps_car_12"] + data["loo_ps_car_03_cat"]) / 2.0) * (
    ((data["ps_car_12"] + data["loo_ps_ind_05_cat"]) / 2.0) * data["loo_ps_car_04_cat"])))
    v["187"] = 0.020000 * np.tanh((np.tanh(data["loo_ps_ind_17_bin"]) * (
    data["loo_ps_ind_05_cat"] * ((data["loo_ps_ind_04_cat"] + (-(data["ps_ind_15"]))) / 2.0))))
    v["188"] = 0.020000 * np.tanh(
        (((data["ps_ind_03"] + data["loo_ps_ind_12_bin"]) / 2.0) * (data["ps_ind_03"] - np.tanh(data["ps_ind_03"]))))
    v["189"] = 0.020000 * np.tanh(((((data["loo_ps_car_11_cat"] + data["loo_ps_ind_04_cat"]) / 2.0) * data[
        "loo_ps_ind_17_bin"]) * (data["loo_ps_ind_02_cat"] - data["loo_ps_car_07_cat"])))
    v["190"] = 0.020000 * np.tanh(((data["ps_ind_01"] * data["ps_ind_01"]) * (
    ((data["loo_ps_car_01_cat"] + data["ps_ind_03"]) / 2.0) * data["loo_ps_ind_17_bin"])))
    v["191"] = 0.020000 * np.tanh((((data["loo_ps_ind_02_cat"] + (-(data["ps_car_15"]))) / 2.0) * data["ps_car_15"]))
    v["192"] = 0.020000 * np.tanh(((0.166667 + (((data["ps_car_12"] + data["loo_ps_ind_17_bin"]) / 2.0) * (
    data["loo_ps_ind_04_cat"] * data["loo_ps_ind_04_cat"]))) / 2.0))
    v["193"] = 0.019980 * np.tanh((data["loo_ps_car_02_cat"] * (
    ((data["loo_ps_ind_13_bin"] + data["loo_ps_car_02_cat"]) / 2.0) - (data["ps_reg_02"] + data["loo_ps_car_06_cat"]))))
    v["194"] = 0.019895 * np.tanh(
        ((data["ps_reg_03"] * (-((data["ps_ind_03"] * data["ps_ind_15"])))) * data["loo_ps_car_01_cat"]))
    v["195"] = 0.020000 * np.tanh(
        (-(((((data["loo_ps_ind_04_cat"] + data["ps_ind_01"]) / 2.0) * data["ps_ind_01"]) * data["ps_ind_03"]))))
    v["196"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] * (-(data["ps_car_11"]))) * (
    data["loo_ps_car_02_cat"] + data["loo_ps_car_01_cat"])))
    v["197"] = 0.020000 * np.tanh((np.tanh(data["loo_ps_car_01_cat"]) * (
    data["ps_ind_14"] + (-((data["loo_ps_ind_18_bin"] * data["loo_ps_car_09_cat"]))))))
    v["198"] = 0.018046 * np.tanh((19.500000 * (0.583333 - (6.846150 * data["loo_ps_car_10_cat"]))))
    v["199"] = 0.019988 * np.tanh(
        (-2.0 + (((data["loo_ps_car_10_cat"] + 0.965909) + data["ps_car_11"]) * data["ps_car_11"])))
    v["200"] = 0.020000 * np.tanh(((data["ps_ind_03"] + (
    (data["ps_ind_03"] * data["ps_ind_01"]) * (data["ps_car_13"] - data["ps_ind_01"]))) / 2.0))
    v["201"] = 0.019984 * np.tanh((data["ps_reg_02"] * (
    (((-(data["loo_ps_car_01_cat"])) + data["loo_ps_ind_05_cat"]) / 2.0) * data["loo_ps_ind_17_bin"])))
    v["202"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    (((0.965909 - data["loo_ps_car_01_cat"]) + data["loo_ps_ind_02_cat"]) / 2.0) * data["ps_ind_01"])))
    v["203"] = 0.020000 * np.tanh((data["ps_reg_03"] * (
    (data["ps_ind_15"] * (data["ps_ind_15"] + data["loo_ps_ind_09_bin"])) + data["ps_ind_15"])))
    v["204"] = 0.020000 * np.tanh((((data["loo_ps_car_10_cat"] + data["loo_ps_car_03_cat"]) / 2.0) * (
    -(((data["loo_ps_ind_18_bin"] + data["ps_car_15"]) / 2.0)))))
    v["205"] = 0.020000 * np.tanh((((-(np.tanh(data["loo_ps_ind_02_cat"]))) + (
    ((data["ps_ind_03"] + data["loo_ps_ind_02_cat"]) / 2.0) * data["loo_ps_ind_16_bin"])) / 2.0))
    v["206"] = 0.020000 * np.tanh(np.tanh((19.500000 * np.tanh((data["ps_ind_14"] + (0.965909 - data["ps_car_15"]))))))
    v["207"] = 0.019945 * np.tanh(
        ((19.500000 - (data["loo_ps_ind_02_cat"] * 19.500000)) * (data["ps_reg_02"] - 2.800000)))
    v["208"] = 0.019969 * np.tanh((((data["ps_reg_02"] * (data["loo_ps_car_01_cat"] * data["loo_ps_ind_12_bin"])) + (
    data["loo_ps_car_11_cat"] * data["loo_ps_car_08_cat"])) / 2.0))
    v["209"] = 0.019996 * np.tanh((((data["ps_ind_03"] + data["loo_ps_ind_12_bin"]) / 2.0) * (
    (data["ps_ind_03"] + (data["missing"] - data["loo_ps_ind_02_cat"])) / 2.0)))
    v["210"] = 0.020000 * np.tanh((data["loo_ps_ind_17_bin"] * (
    data["loo_ps_ind_04_cat"] * (data["ps_reg_03"] * (-(data["loo_ps_car_07_cat"]))))))
    v["211"] = 0.020000 * np.tanh((data["loo_ps_ind_05_cat"] * (
    data["ps_reg_03"] + ((data["loo_ps_ind_02_cat"] * data["loo_ps_ind_09_bin"]) - 0.600000))))
    v["212"] = 0.017421 * np.tanh(
        np.tanh(((-((data["ps_car_11"] + data["loo_ps_ind_08_bin"]))) * data["loo_ps_ind_05_cat"])))
    v["213"] = 0.019305 * np.tanh((((data["loo_ps_ind_02_cat"] * data["loo_ps_car_04_cat"]) - (
    (data["missing"] + data["loo_ps_car_04_cat"]) / 2.0)) - data["loo_ps_ind_02_cat"]))
    v["214"] = 0.019992 * np.tanh(
        (data["ps_car_12"] * (((-(data["ps_car_11"])) + (data["ps_reg_01"] + data["loo_ps_ind_04_cat"])) / 2.0)))
    v["215"] = 0.019879 * np.tanh((data["loo_ps_ind_05_cat"] * (
    data["ps_car_13"] * ((data["ps_car_14"] * data["ps_ind_15"]) + data["loo_ps_ind_05_cat"]))))
    v["216"] = 0.019984 * np.tanh(((data["loo_ps_car_01_cat"] * data["loo_ps_ind_17_bin"]) * (
    data["loo_ps_ind_02_cat"] - data["loo_ps_ind_17_bin"])))
    v["217"] = 0.020000 * np.tanh((((data["ps_reg_03"] * data["loo_ps_car_08_cat"]) - np.tanh(
        np.tanh(data["loo_ps_car_11_cat"]))) * data["loo_ps_ind_05_cat"]))
    v["218"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] + (0.273684 - data["loo_ps_ind_12_bin"])) * (
    data["ps_reg_02"] * data["loo_ps_car_07_cat"])))
    v["219"] = 0.020000 * np.tanh(((((data["loo_ps_ind_16_bin"] + (data["loo_ps_ind_06_bin"] * 0.166667)) / 2.0) * data[
        "loo_ps_ind_06_bin"]) * data["loo_ps_ind_05_cat"]))
    v["220"] = 0.020000 * np.tanh(((data["ps_ind_15"] * data["ps_car_15"]) * (-(data["loo_ps_ind_17_bin"]))))
    v["221"] = 0.020000 * np.tanh(((((data["loo_ps_car_02_cat"] * data["ps_ind_03"]) + (
    data["loo_ps_car_02_cat"] * data["ps_reg_01"])) / 2.0) * data["ps_ind_01"]))
    v["222"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    data["loo_ps_ind_18_bin"] * (data["loo_ps_ind_07_bin"] - (data["loo_ps_ind_04_cat"] * data["loo_ps_ind_16_bin"])))))
    v["223"] = 0.020000 * np.tanh(((data["loo_ps_ind_12_bin"] * data["ps_car_11"]) + (
    data["loo_ps_ind_04_cat"] * (data["ps_reg_01"] * data["loo_ps_car_08_cat"]))))
    v["224"] = 0.019988 * np.tanh((data["ps_car_14"] * (
    (data["ps_car_14"] + ((data["loo_ps_ind_05_cat"] * data["loo_ps_ind_05_cat"]) * data["loo_ps_car_01_cat"])) / 2.0)))
    v["225"] = 0.019090 * np.tanh(
        (data["ps_ind_15"] * (data["loo_ps_ind_07_bin"] - (-((data["loo_ps_car_06_cat"] * data["ps_ind_15"]))))))
    v["226"] = 0.015734 * np.tanh((data["ps_ind_15"] - (
    6.846150 * ((data["loo_ps_car_11_cat"] + data["loo_ps_car_06_cat"]) + data["loo_ps_car_06_cat"]))))
    v["227"] = 0.020000 * np.tanh(((data["ps_car_12"] - data["loo_ps_car_06_cat"]) * (
    data["loo_ps_ind_02_cat"] * (-(data["loo_ps_car_08_cat"])))))
    v["228"] = 0.019996 * np.tanh(
        ((data["loo_ps_ind_09_bin"] * data["ps_car_12"]) - np.tanh(((data["ps_reg_02"] + data["ps_car_12"]) / 2.0))))
    v["229"] = 0.019219 * np.tanh((data["ps_ind_01"] * (
    (data["loo_ps_ind_17_bin"] * data["loo_ps_car_06_cat"]) - np.tanh(data["loo_ps_ind_17_bin"]))))
    v["230"] = 0.019996 * np.tanh(
        (data["loo_ps_ind_07_bin"] * (data["ps_car_13"] * (data["loo_ps_car_11_cat"] - np.tanh(2.0)))))
    v["231"] = 0.020000 * np.tanh(
        (data["loo_ps_car_11_cat"] * ((data["ps_ind_14"] * data["ps_ind_15"]) * data["ps_car_12"])))
    v["232"] = 0.019816 * np.tanh(((np.tanh(data["loo_ps_ind_17_bin"]) * data["missing"]) * (
    np.tanh(data["ps_car_15"]) - data["loo_ps_car_02_cat"])))
    v["233"] = 0.020000 * np.tanh((((data["loo_ps_car_01_cat"] - data["ps_reg_01"]) * data["loo_ps_car_10_cat"]) * (
    data["ps_ind_03"] + data["loo_ps_ind_17_bin"])))
    v["234"] = 0.017378 * np.tanh(((data["ps_ind_01"] * data["loo_ps_car_04_cat"]) * (
    data["loo_ps_car_01_cat"] + (data["ps_car_12"] * data["loo_ps_car_04_cat"]))))
    v["235"] = 0.020000 * np.tanh((data["ps_reg_03"] * (
    (((data["ps_reg_03"] + data["loo_ps_ind_05_cat"]) / 2.0) - data["loo_ps_ind_02_cat"]) - data["ps_reg_01"])))
    v["236"] = 0.020000 * np.tanh((data["ps_ind_01"] * (
    ((data["loo_ps_car_09_cat"] + data["loo_ps_ind_04_cat"]) / 2.0) * (
    (data["loo_ps_ind_05_cat"] + data["loo_ps_ind_05_cat"]) / 2.0))))
    v["237"] = 0.019996 * np.tanh((data["ps_ind_01"] * (
    (data["loo_ps_ind_02_cat"] + (data["ps_reg_01"] + (-(data["loo_ps_car_11_cat"])))) / 2.0)))
    v["238"] = 0.019941 * np.tanh((-((data["loo_ps_car_08_cat"] * (
    data["loo_ps_car_02_cat"] - ((data["loo_ps_car_04_cat"] + (-(data["loo_ps_ind_18_bin"]))) / 2.0))))))
    v["239"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    ((data["loo_ps_ind_17_bin"] * (-(np.tanh(data["loo_ps_car_08_cat"])))) + data["ps_reg_02"]) / 2.0)))
    v["240"] = 0.020000 * np.tanh(((np.tanh((-(data["loo_ps_ind_08_bin"]))) + (
    data["ps_reg_03"] * (data["loo_ps_ind_08_bin"] * data["ps_reg_01"]))) / 2.0))
    v["241"] = 0.019969 * np.tanh((((data["loo_ps_car_02_cat"] + data["ps_car_15"]) / 2.0) * (
    (-(data["loo_ps_ind_17_bin"])) - data["loo_ps_car_10_cat"])))
    v["242"] = 0.019371 * np.tanh(((data["loo_ps_car_03_cat"] * (data["ps_ind_14"] - data["loo_ps_ind_05_cat"])) * (
    data["ps_car_11"] + data["ps_car_11"])))
    v["243"] = 0.020000 * np.tanh((((data["loo_ps_car_10_cat"] * (
    data["loo_ps_ind_17_bin"] * data["loo_ps_ind_04_cat"])) + (-(np.tanh(data["loo_ps_ind_04_cat"])))) / 2.0))
    v["244"] = 0.020000 * np.tanh(
        (np.tanh((19.500000 * ((0.452381 + data["loo_ps_ind_18_bin"]) / 2.0))) * data["loo_ps_ind_05_cat"]))
    v["245"] = 0.019996 * np.tanh((((data["loo_ps_car_01_cat"] * data["loo_ps_ind_02_cat"]) * (
    data["loo_ps_car_08_cat"] * data["ps_reg_01"])) * (4.34056949615478516)))
    v["246"] = 0.019988 * np.tanh(((data["loo_ps_car_01_cat"] + data["loo_ps_ind_16_bin"]) * (
    data["loo_ps_ind_02_cat"] - data["loo_ps_ind_05_cat"])))
    v["247"] = 0.020000 * np.tanh((data["ps_car_14"] * (
    ((data["loo_ps_car_07_cat"] * data["ps_ind_15"]) + ((data["ps_car_13"] + data["loo_ps_ind_13_bin"]) / 2.0)) / 2.0)))
    v["248"] = 0.019969 * np.tanh((data["ps_reg_02"] * (
    (data["ps_ind_15"] + data["ps_ind_14"]) * (data["loo_ps_ind_08_bin"] * data["loo_ps_car_08_cat"]))))
    v["249"] = 0.019984 * np.tanh((data["loo_ps_ind_02_cat"] * (
    data["missing"] - ((data["loo_ps_ind_02_cat"] * data["loo_ps_ind_02_cat"]) * data["loo_ps_car_08_cat"]))))
    v["250"] = 0.020000 * np.tanh((((((data["loo_ps_car_03_cat"] + data["ps_car_15"]) / 2.0) + data[
        "loo_ps_ind_06_bin"]) / 2.0) * (data["ps_reg_02"] * data["ps_car_15"])))
    v["251"] = 0.020000 * np.tanh(((data["ps_car_11"] * (
    (data["loo_ps_car_06_cat"] + (data["ps_reg_02"] * data["loo_ps_ind_12_bin"])) / 2.0)) - data["loo_ps_car_10_cat"]))
    v["252"] = 0.019453 * np.tanh(
        (data["ps_ind_03"] * ((0.273684 * data["loo_ps_ind_05_cat"]) + (0.020833 - data["ps_car_14"]))))
    v["253"] = 0.020000 * np.tanh((data["ps_car_13"] * (
    (data["ps_car_13"] * (data["loo_ps_ind_12_bin"] * data["ps_ind_15"])) + data["ps_ind_14"])))
    v["254"] = 0.020000 * np.tanh((-((((data["loo_ps_car_10_cat"] * (data["ps_car_13"] + data["ps_car_13"])) + np.tanh(
        data["loo_ps_ind_05_cat"])) / 2.0))))
    v["255"] = 0.019961 * np.tanh(((((data["ps_ind_03"] + data["loo_ps_ind_07_bin"]) / 2.0) * data["ps_ind_14"]) - (
    data["ps_reg_02"] * data["loo_ps_car_10_cat"])))
    v["256"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    (data["loo_ps_car_11_cat"] * (data["loo_ps_ind_04_cat"] - 0.583333)) - data["loo_ps_ind_08_bin"])))
    v["257"] = 0.019664 * np.tanh((data["loo_ps_car_07_cat"] * (data["loo_ps_ind_09_bin"] - data["loo_ps_car_01_cat"])))
    v["258"] = 0.020000 * np.tanh(((-(data["loo_ps_ind_17_bin"])) * np.tanh(
        (data["loo_ps_car_11_cat"] * (data["loo_ps_car_08_cat"] + data["ps_ind_15"])))))
    v["259"] = 0.019644 * np.tanh(
        ((data["ps_ind_01"] * (-(data["ps_ind_03"]))) * (data["loo_ps_ind_04_cat"] + data["loo_ps_ind_04_cat"])))
    v["260"] = 0.020000 * np.tanh(
        (data["ps_reg_03"] * (-((data["ps_car_15"] * (data["loo_ps_car_07_cat"] * data["loo_ps_ind_17_bin"]))))))
    v["261"] = 0.020000 * np.tanh((data["ps_car_12"] * (
    (data["ps_car_12"] * (data["ps_ind_15"] * data["loo_ps_ind_04_cat"])) + data["ps_ind_15"])))
    v["262"] = 0.018953 * np.tanh(((data["ps_ind_15"] + (
    data["ps_ind_15"] * ((data["loo_ps_ind_08_bin"] - data["loo_ps_car_04_cat"]) - data["loo_ps_car_03_cat"]))) / 2.0))
    v["263"] = 0.020000 * np.tanh((0.166667 * (
    ((data["ps_car_13"] + data["loo_ps_ind_04_cat"]) / 2.0) - (data["ps_car_13"] * data["loo_ps_car_03_cat"]))))
    v["264"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * ((data["loo_ps_ind_09_bin"] + (
    (data["loo_ps_ind_02_cat"] * data["loo_ps_ind_02_cat"]) + data["loo_ps_ind_10_bin"])) / 2.0)))
    v["265"] = 0.019992 * np.tanh((data["ps_ind_14"] * (
    (data["loo_ps_car_03_cat"] * (data["loo_ps_ind_07_bin"] + data["ps_ind_15"])) * data["loo_ps_car_11_cat"])))
    v["266"] = 0.019988 * np.tanh(
        (np.tanh(np.tanh(data["loo_ps_car_07_cat"])) + (np.tanh(data["ps_ind_01"]) * (-(data["ps_ind_14"])))))
    v["267"] = 0.020000 * np.tanh((np.tanh(np.tanh(data["ps_ind_01"])) * (
    (data["ps_car_14"] + (data["loo_ps_ind_04_cat"] - data["loo_ps_car_01_cat"])) / 2.0)))
    v["268"] = 0.020000 * np.tanh((((data["loo_ps_ind_02_cat"] * (data["ps_ind_03"] * data["ps_ind_03"])) - data[
        "loo_ps_ind_02_cat"]) - data["loo_ps_ind_02_cat"]))
    v["269"] = 0.018969 * np.tanh(
        (data["loo_ps_ind_05_cat"] * (data["loo_ps_car_07_cat"] * (data["ps_reg_02"] + data["ps_car_12"]))))
    v["270"] = 0.019996 * np.tanh((data["ps_car_13"] * (
    data["loo_ps_ind_12_bin"] * (1.135800 + (data["ps_ind_15"] + data["loo_ps_ind_11_bin"])))))
    v["271"] = 0.019996 * np.tanh((-((data["loo_ps_ind_05_cat"] * (
    (data["loo_ps_car_07_cat"] * (-(data["loo_ps_car_09_cat"]))) + data["loo_ps_car_07_cat"])))))
    v["272"] = 0.020000 * np.tanh(
        (data["ps_car_11"] * ((-(data["ps_reg_03"])) * (data["loo_ps_ind_05_cat"] * np.tanh(-1.0)))))
    v["273"] = 0.020000 * np.tanh((((data["loo_ps_ind_09_bin"] + data["loo_ps_ind_17_bin"]) / 2.0) * (
    (data["loo_ps_ind_18_bin"] + (data["ps_reg_02"] - data["ps_ind_14"])) / 2.0)))
    v["274"] = 0.020000 * np.tanh(
        (data["ps_ind_01"] * (((data["ps_ind_01"] * data["loo_ps_car_03_cat"]) + data["loo_ps_ind_02_cat"]) / 2.0)))
    v["275"] = 0.020000 * np.tanh(
        (data["loo_ps_ind_02_cat"] * (data["ps_ind_01"] * (data["loo_ps_ind_06_bin"] * (-(data["ps_ind_03"]))))))
    v["276"] = 0.019949 * np.tanh(((np.tanh((((data["loo_ps_ind_12_bin"] + data["ps_reg_03"]) / 2.0) * 19.500000)) + (
    -(data["ps_reg_03"]))) / 2.0))
    v["277"] = 0.016070 * np.tanh(
        ((data["ps_car_15"] + data["loo_ps_car_03_cat"]) * (-((data["ps_reg_03"] + data["loo_ps_ind_05_cat"])))))
    v["278"] = 0.019930 * np.tanh(((data["loo_ps_ind_02_cat"] + (
    (data["loo_ps_car_05_cat"] * data["loo_ps_ind_05_cat"]) - data["loo_ps_ind_05_cat"])) / 2.0))
    v["279"] = 0.017035 * np.tanh(
        (((data["loo_ps_car_09_cat"] * data["ps_reg_03"]) + data["loo_ps_ind_02_cat"]) * data["loo_ps_ind_05_cat"]))
    v["280"] = 0.019965 * np.tanh(((data["ps_reg_01"] + data["loo_ps_ind_07_bin"]) * (
    (data["loo_ps_ind_05_cat"] + ((data["loo_ps_car_11_cat"] + data["loo_ps_car_08_cat"]) / 2.0)) / 2.0)))
    v["281"] = 0.020000 * np.tanh((-(((np.tanh(((data["loo_ps_car_01_cat"] + data["loo_ps_car_05_cat"]) / 2.0)) + (
    data["loo_ps_car_10_cat"] * data["ps_car_15"])) / 2.0))))
    v["282"] = 0.019992 * np.tanh(((data["ps_ind_03"] - data["loo_ps_ind_18_bin"]) * (
    ((data["ps_ind_03"] + data["ps_car_12"]) / 2.0) * data["loo_ps_car_02_cat"])))
    v["283"] = 0.019945 * np.tanh((data["loo_ps_ind_04_cat"] * (
    -((data["ps_reg_02"] * (data["loo_ps_car_07_cat"] * data["loo_ps_ind_17_bin"]))))))
    v["284"] = 0.020000 * np.tanh(
        ((-((3.642860 + (-(data["loo_ps_car_09_cat"]))))) * (data["ps_ind_01"] * data["loo_ps_car_09_cat"])))
    v["285"] = 0.018918 * np.tanh((data["ps_ind_01"] * (data["ps_ind_01"] - (data["ps_ind_01"] * data["ps_ind_01"]))))
    v["286"] = 0.018738 * np.tanh((((data["ps_ind_03"] + data["ps_ind_15"]) / 2.0) - (
    data["ps_ind_15"] * (data["ps_ind_15"] * data["ps_ind_03"]))))
    v["287"] = 0.019957 * np.tanh(((data["loo_ps_car_08_cat"] * data["loo_ps_ind_08_bin"]) * (
    (data["loo_ps_car_07_cat"] + data["missing"]) / 2.0)))
    v["288"] = 0.019598 * np.tanh(((data["loo_ps_ind_09_bin"] * (
    (data["ps_ind_01"] + (-(data["loo_ps_car_05_cat"]))) / 2.0)) + data["loo_ps_ind_13_bin"]))
    v["289"] = 0.020000 * np.tanh(
        (((data["loo_ps_car_01_cat"] * data["ps_ind_15"]) + data["ps_car_11"]) * data["loo_ps_ind_12_bin"]))
    v["290"] = 0.020000 * np.tanh(((
                                   (data["loo_ps_ind_02_cat"] - (data["ps_car_11"] * data["loo_ps_car_09_cat"])) * data[
                                       "loo_ps_ind_17_bin"]) * data["loo_ps_car_10_cat"]))
    v["291"] = 0.019301 * np.tanh(
        (data["loo_ps_car_04_cat"] * ((np.tanh(data["loo_ps_car_04_cat"]) - data["ps_ind_03"]) * data["ps_ind_03"])))
    v["292"] = 0.020000 * np.tanh(((data["ps_reg_03"] - data["ps_car_11"]) * (
    (np.tanh(data["loo_ps_car_04_cat"]) + (-(data["ps_car_14"]))) / 2.0)))
    v["293"] = 0.019086 * np.tanh((((data["ps_ind_03"] * data["loo_ps_ind_12_bin"]) + (
    (data["loo_ps_ind_12_bin"] - data["loo_ps_car_06_cat"]) * data["ps_reg_03"])) / 2.0))
    v["294"] = 0.020000 * np.tanh((data["loo_ps_ind_12_bin"] - (
    data["loo_ps_ind_18_bin"] * (data["loo_ps_ind_04_cat"] * (-(data["ps_reg_03"]))))))
    v["295"] = 0.019988 * np.tanh(((((data["ps_reg_03"] * data["ps_car_12"]) + data[
        "loo_ps_ind_02_cat"]) / 2.0) * np.tanh(data["loo_ps_car_04_cat"])))
    v["296"] = 0.019898 * np.tanh((data["loo_ps_car_07_cat"] * (
    -((((data["ps_car_11"] * (-(data["loo_ps_car_08_cat"]))) + data["loo_ps_car_09_cat"]) / 2.0)))))
    v["297"] = 0.019973 * np.tanh(((data["loo_ps_ind_02_cat"] * (
    data["loo_ps_ind_16_bin"] + (-(data["loo_ps_car_05_cat"])))) * (-(data["loo_ps_car_08_cat"]))))
    v["298"] = 0.019980 * np.tanh((((data["loo_ps_ind_18_bin"] * (
    data["loo_ps_ind_04_cat"] * data["loo_ps_ind_16_bin"])) - data["ps_car_14"]) * data["ps_ind_14"]))
    v["299"] = 0.016964 * np.tanh((((-(0.347826)) + np.tanh((data["loo_ps_car_06_cat"] - data["ps_reg_01"]))) / 2.0))
    v["300"] = 0.020000 * np.tanh(
        ((data["ps_ind_15"] * data["ps_car_15"]) * ((data["loo_ps_ind_12_bin"] + (-(data["ps_car_15"]))) / 2.0)))
    v["301"] = 0.019957 * np.tanh(((data["ps_car_14"] * data["loo_ps_ind_04_cat"]) * (
    data["ps_ind_01"] + (data["ps_car_14"] * data["loo_ps_car_08_cat"]))))
    v["302"] = 0.020000 * np.tanh(
        (data["ps_ind_14"] * (data["ps_car_11"] * (data["ps_car_12"] + (data["ps_ind_03"] * data["ps_car_12"])))))
    v["303"] = 0.020000 * np.tanh((data["ps_reg_01"] * (
    data["loo_ps_car_01_cat"] * ((data["loo_ps_car_01_cat"] + (data["ps_ind_03"] * data["ps_reg_02"])) / 2.0))))
    v["304"] = 0.019594 * np.tanh(
        ((data["loo_ps_ind_04_cat"] * data["loo_ps_ind_02_cat"]) * (data["loo_ps_car_06_cat"] * (0.347826 + 2.800000))))
    v["305"] = 0.019992 * np.tanh(
        (data["ps_reg_01"] * ((data["loo_ps_car_02_cat"] - data["loo_ps_car_04_cat"]) * data["loo_ps_ind_05_cat"])))
    v["306"] = 0.020000 * np.tanh(np.tanh(((((data["loo_ps_ind_09_bin"] * data["loo_ps_ind_05_cat"]) + data[
        "ps_ind_03"]) / 2.0) * (-(data["ps_reg_01"])))))
    v["307"] = 0.018308 * np.tanh((-((19.500000 * np.tanh((-1.0 - (data["loo_ps_ind_11_bin"] * 19.500000)))))))
    v["308"] = 0.019754 * np.tanh(((1.0 + data["ps_reg_02"]) * ((data["ps_reg_02"] - 3.0) * 3.0)))
    v["309"] = 0.019265 * np.tanh((data["loo_ps_ind_04_cat"] * (
    (data["ps_ind_01"] * (data["ps_reg_01"] * data["ps_ind_01"])) * data["ps_ind_01"])))
    v["310"] = 0.019879 * np.tanh(
        (((data["ps_reg_03"] + data["ps_ind_03"]) / 2.0) * np.tanh((data["ps_reg_03"] * data["ps_ind_03"]))))
    v["311"] = 0.020000 * np.tanh(((data["ps_reg_02"] * (
    data["loo_ps_ind_11_bin"] - (data["ps_car_14"] * data["loo_ps_car_04_cat"]))) * data["ps_reg_01"]))
    v["312"] = 0.019965 * np.tanh((data["ps_reg_03"] * (
    (data["ps_ind_15"] + ((data["ps_ind_15"] * data["loo_ps_ind_09_bin"]) - data["loo_ps_ind_08_bin"])) / 2.0)))
    v["313"] = 0.020000 * np.tanh((data["loo_ps_ind_06_bin"] * (
    (data["loo_ps_ind_02_cat"] + (data["ps_car_11"] * data["loo_ps_car_06_cat"])) / 2.0)))
    v["314"] = 0.020000 * np.tanh(
        (data["loo_ps_ind_05_cat"] * (data["loo_ps_ind_11_bin"] - (data["loo_ps_ind_04_cat"] * data["ps_car_11"]))))
    v["315"] = 0.019461 * np.tanh((data["loo_ps_car_03_cat"] * (
    data["loo_ps_ind_05_cat"] * (data["loo_ps_car_02_cat"] + data["loo_ps_ind_04_cat"]))))
    v["316"] = 0.014366 * np.tanh(np.tanh(np.tanh(
        (data["ps_reg_01"] - ((data["ps_ind_03"] + ((data["ps_ind_14"] + data["loo_ps_car_10_cat"]) / 2.0)) / 2.0)))))
    v["317"] = 0.019996 * np.tanh((data["ps_car_12"] * (
    (data["loo_ps_ind_12_bin"] + (data["ps_car_11"] * (data["ps_ind_15"] + data["ps_car_11"]))) / 2.0)))
    v["318"] = 0.020000 * np.tanh(
        np.tanh((data["ps_car_14"] * ((-(np.tanh(data["ps_car_14"]))) + (-(data["ps_reg_03"]))))))
    v["319"] = 0.015050 * np.tanh((-((np.tanh(data["loo_ps_car_04_cat"]) * (
    data["ps_car_15"] * (data["loo_ps_ind_18_bin"] - data["loo_ps_ind_06_bin"]))))))
    v["320"] = 0.020000 * np.tanh((data["ps_car_13"] * (
    ((data["loo_ps_car_04_cat"] * (data["ps_car_14"] - data["ps_ind_03"])) + data["ps_ind_03"]) / 2.0)))
    v["321"] = 0.020000 * np.tanh((-((data["ps_car_14"] + ((0.347826 - data["ps_car_14"]) * data["ps_car_15"])))))
    v["322"] = 0.019977 * np.tanh(((0.166667 + (
    data["ps_ind_14"] * ((data["ps_reg_03"] - data["loo_ps_ind_08_bin"]) - data["loo_ps_ind_17_bin"]))) / 2.0))
    v["323"] = 0.020000 * np.tanh(
        (data["missing"] * (-((data["loo_ps_car_09_cat"] * ((data["ps_car_12"] + data["loo_ps_ind_18_bin"]) / 2.0))))))
    v["324"] = 0.018195 * np.tanh((((data["loo_ps_ind_09_bin"] + (-(np.tanh(data["loo_ps_ind_05_cat"])))) / 2.0) * (
    data["loo_ps_ind_18_bin"] + data["loo_ps_car_07_cat"])))
    v["325"] = 0.019359 * np.tanh(
        (-((19.500000 * ((0.485294 + np.tanh((data["loo_ps_ind_11_bin"] * 19.500000))) / 2.0)))))
    v["326"] = 0.019992 * np.tanh((-3.0 - ((-((data["ps_ind_03"] * data["ps_ind_03"]))) + data["ps_ind_03"])))
    v["327"] = 0.020000 * np.tanh((np.tanh((data["ps_reg_01"] * (data["ps_car_14"] * (-(data["loo_ps_ind_02_cat"]))))) -
                                   data["loo_ps_ind_02_cat"]))
    v["328"] = 0.019992 * np.tanh((data["loo_ps_ind_04_cat"] * (
    (data["ps_ind_03"] + data["loo_ps_ind_04_cat"]) * (-(data["loo_ps_car_08_cat"])))))
    v["329"] = 0.020000 * np.tanh((data["ps_car_11"] * ((data["loo_ps_ind_02_cat"] + (
    (data["loo_ps_ind_07_bin"] + (data["loo_ps_car_07_cat"] * data["missing"])) / 2.0)) / 2.0)))
    v["330"] = 0.019996 * np.tanh((((data["loo_ps_car_02_cat"] - (
    data["loo_ps_ind_06_bin"] - data["loo_ps_car_02_cat"])) * data["loo_ps_car_09_cat"]) * data["loo_ps_ind_02_cat"]))
    v["331"] = 0.018343 * np.tanh((((data["loo_ps_car_07_cat"] + (
    data["ps_reg_03"] + np.tanh(data["loo_ps_car_07_cat"]))) / 2.0) * (-(data["missing"]))))
    v["332"] = 0.019750 * np.tanh((-(
    (data["loo_ps_ind_02_cat"] * (data["loo_ps_ind_18_bin"] * (data["ps_car_14"] * data["loo_ps_car_04_cat"]))))))
    v["333"] = 0.019949 * np.tanh(((data["loo_ps_ind_05_cat"] * (-(data["loo_ps_car_06_cat"]))) * (
    data["loo_ps_ind_05_cat"] * data["loo_ps_ind_04_cat"])))
    v["334"] = 0.020000 * np.tanh((data["loo_ps_car_06_cat"] * (
    (2.800000 + data["ps_car_14"]) * (data["loo_ps_ind_13_bin"] * data["loo_ps_car_04_cat"]))))
    v["335"] = 0.020000 * np.tanh(
        np.tanh((data["ps_ind_03"] * np.tanh(np.tanh((data["ps_reg_02"] * (-(data["ps_ind_15"]))))))))
    v["336"] = 0.020000 * np.tanh((data["loo_ps_car_10_cat"] * (
    (data["loo_ps_ind_11_bin"] + data["loo_ps_ind_18_bin"]) * (data["ps_reg_02"] + data["ps_reg_02"]))))
    v["337"] = 0.020000 * np.tanh(
        np.tanh(np.tanh((data["ps_ind_03"] * ((data["ps_ind_03"] + data["ps_car_11"]) + data["ps_car_11"])))))
    v["338"] = 0.019984 * np.tanh(((data["loo_ps_ind_05_cat"] * (
    data["loo_ps_ind_11_bin"] - (data["ps_car_11"] * data["loo_ps_ind_06_bin"]))) * data["loo_ps_car_01_cat"]))
    v["339"] = 0.020000 * np.tanh(
        (data["ps_car_15"] * (data["loo_ps_ind_12_bin"] * (data["loo_ps_car_08_cat"] + data["loo_ps_ind_07_bin"]))))
    v["340"] = 0.019953 * np.tanh((data["ps_ind_15"] * (
    data["loo_ps_ind_02_cat"] * (0.600000 - (data["loo_ps_ind_10_bin"] - data["ps_reg_03"])))))
    v["341"] = 0.017914 * np.tanh(((data["loo_ps_car_03_cat"] - (data["ps_car_13"] + data["loo_ps_ind_18_bin"])) * (
    data["loo_ps_car_03_cat"] * 0.273684)))
    v["342"] = 0.020000 * np.tanh(
        (data["loo_ps_car_10_cat"] * (-3.0 + (data["ps_car_14"] * (data["ps_car_15"] - data["loo_ps_car_04_cat"])))))
    v["343"] = 0.020000 * np.tanh((data["loo_ps_car_09_cat"] * (
    ((data["ps_car_11"] * data["loo_ps_car_09_cat"]) + (data["loo_ps_car_02_cat"] - data["loo_ps_ind_04_cat"])) / 2.0)))
    v["344"] = 0.019973 * np.tanh(((data["ps_car_13"] * (data["ps_ind_14"] - data["ps_reg_02"])) * data["ps_ind_15"]))
    v["345"] = 0.020000 * np.tanh(((data["loo_ps_car_09_cat"] * ((0.965909 - data["ps_reg_03"]) - data["ps_reg_03"])) *
                                   data["loo_ps_ind_08_bin"]))
    v["346"] = 0.019973 * np.tanh(((data["ps_ind_01"] * (
    np.tanh(data["loo_ps_car_02_cat"]) + data["loo_ps_ind_11_bin"])) * (-(data["ps_car_15"]))))
    v["347"] = 0.020000 * np.tanh((data["loo_ps_ind_09_bin"] * (
    ((-(data["loo_ps_car_08_cat"])) * data["loo_ps_car_03_cat"]) * data["ps_ind_03"])))
    v["348"] = 0.018535 * np.tanh((data["loo_ps_ind_04_cat"] * (
    data["loo_ps_car_04_cat"] * (data["ps_ind_15"] - (-(data["loo_ps_car_01_cat"]))))))
    v["349"] = 0.020000 * np.tanh((data["loo_ps_car_07_cat"] * (
    (((data["loo_ps_ind_10_bin"] + data["loo_ps_car_08_cat"]) / 2.0) + (-(data["loo_ps_ind_12_bin"]))) / 2.0)))
    v["350"] = 0.019996 * np.tanh(((data["loo_ps_car_10_cat"] * (data["loo_ps_ind_13_bin"] - data["ps_reg_02"])) * (
    data["loo_ps_ind_17_bin"] + data["ps_ind_03"])))
    v["351"] = 0.020000 * np.tanh((data["loo_ps_ind_06_bin"] * (
    data["ps_reg_01"] * ((data["missing"] + (data["loo_ps_car_07_cat"] - data["loo_ps_ind_05_cat"])) / 2.0))))
    v["352"] = 0.020000 * np.tanh(
        (data["ps_car_12"] * (data["ps_car_12"] * ((-(np.tanh(data["loo_ps_car_07_cat"]))) * data["ps_reg_02"]))))
    v["353"] = 0.020000 * np.tanh(((
                                   (-((data["ps_ind_01"] * (data["ps_ind_03"] * data["loo_ps_ind_02_cat"])))) + np.tanh(
                                       data["loo_ps_car_08_cat"])) / 2.0))
    v["354"] = 0.016128 * np.tanh((data["ps_ind_15"] * (
    data["loo_ps_car_11_cat"] * (((data["ps_ind_15"] * data["loo_ps_car_11_cat"]) + 1.871790) / 2.0))))
    v["355"] = 0.019961 * np.tanh((data["loo_ps_ind_06_bin"] * (
    data["loo_ps_ind_12_bin"] * (data["loo_ps_ind_11_bin"] + ((data["ps_ind_15"] + data["loo_ps_car_11_cat"]) / 2.0)))))
    v["356"] = 0.019836 * np.tanh(((np.tanh(data["ps_ind_15"]) + (
    data["loo_ps_ind_02_cat"] * (data["ps_ind_15"] * (-(data["loo_ps_ind_02_cat"]))))) / 2.0))
    v["357"] = 0.019840 * np.tanh(((data["ps_car_15"] * (data["loo_ps_ind_17_bin"] - 0.093750)) * data["ps_car_15"]))
    v["358"] = 0.020000 * np.tanh((-((data["loo_ps_car_09_cat"] * (
    (data["loo_ps_car_01_cat"] + (data["ps_reg_02"] * data["loo_ps_car_09_cat"])) / 2.0)))))
    v["359"] = 0.020000 * np.tanh((-(
    ((data["loo_ps_ind_17_bin"] + data["loo_ps_ind_17_bin"]) * ((np.tanh(data["ps_ind_01"]) + 0.452381) / 2.0)))))
    v["360"] = 0.020000 * np.tanh((data["loo_ps_ind_08_bin"] * (
    data["ps_car_14"] * (data["loo_ps_ind_02_cat"] - np.tanh(data["loo_ps_car_04_cat"])))))
    v["361"] = 0.019996 * np.tanh((((data["loo_ps_ind_11_bin"] + (
    data["loo_ps_ind_08_bin"] * (data["ps_ind_01"] * data["ps_car_11"]))) / 2.0) * data["ps_car_11"]))
    v["362"] = 0.020000 * np.tanh(((8.47791767120361328) * (
    data["loo_ps_ind_10_bin"] * (data["ps_car_11"] + (data["ps_car_14"] * data["loo_ps_car_08_cat"])))))
    v["363"] = 0.019152 * np.tanh((((data["loo_ps_car_08_cat"] + (
    data["loo_ps_car_08_cat"] * (-(data["ps_ind_03"])))) / 2.0) * data["ps_ind_03"]))
    v["364"] = 0.020000 * np.tanh((data["loo_ps_ind_16_bin"] * (
    data["ps_ind_14"] * ((data["ps_car_12"] + (data["ps_reg_03"] * data["loo_ps_car_01_cat"])) / 2.0))))
    v["365"] = 0.019996 * np.tanh((((data["ps_car_15"] * (data["ps_ind_01"] * data["ps_reg_02"])) + (
    data["loo_ps_ind_02_cat"] * data["ps_reg_02"])) / 2.0))
    v["366"] = 0.020000 * np.tanh((data["loo_ps_ind_12_bin"] * (
    (data["loo_ps_ind_11_bin"] - data["loo_ps_car_10_cat"]) - (data["loo_ps_ind_17_bin"] * data["loo_ps_ind_07_bin"]))))
    v["367"] = 0.019996 * np.tanh(
        (-(((data["loo_ps_ind_17_bin"] * data["loo_ps_car_02_cat"]) * (0.347826 - data["ps_car_15"])))))
    v["368"] = 0.020000 * np.tanh((data["loo_ps_ind_02_cat"] * (
    (data["ps_reg_03"] * (data["loo_ps_car_04_cat"] * data["loo_ps_car_01_cat"])) * data["loo_ps_car_08_cat"])))
    v["369"] = 0.020000 * np.tanh((((data["ps_reg_02"] + data["ps_ind_15"]) * data["loo_ps_ind_12_bin"]) * (
    data["ps_ind_03"] + data["ps_ind_03"])))
    v["370"] = 0.020000 * np.tanh((data["loo_ps_ind_16_bin"] * (
    data["ps_car_12"] * (data["loo_ps_ind_02_cat"] * (0.485294 - data["loo_ps_car_08_cat"])))))
    v["371"] = 0.020000 * np.tanh(((data["loo_ps_ind_12_bin"] * (-(data["ps_reg_01"]))) - (
    data["loo_ps_ind_04_cat"] * np.tanh(data["ps_ind_15"]))))
    v["372"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] * (
    ((data["loo_ps_car_02_cat"] * data["loo_ps_ind_04_cat"]) + data["loo_ps_ind_10_bin"]) / 2.0)) * data[
                                       "loo_ps_car_03_cat"]))
    v["373"] = 0.020000 * np.tanh(
        ((data["ps_ind_14"] * data["loo_ps_car_11_cat"]) * np.tanh((data["ps_ind_03"] + data["ps_ind_15"]))))
    v["374"] = 0.019984 * np.tanh((data["ps_car_12"] * (
    (data["loo_ps_ind_12_bin"] * (1.526320 - data["ps_car_13"])) + data["loo_ps_ind_12_bin"])))
    v["375"] = 0.019684 * np.tanh((data["loo_ps_ind_08_bin"] * (
    (((data["loo_ps_ind_16_bin"] + np.tanh(data["ps_reg_02"])) / 2.0) + 0.100000) / 2.0)))
    v["376"] = 0.018172 * np.tanh((((data["ps_car_11"] + 1.135800) / 2.0) * (
    data["ps_reg_03"] * (data["ps_ind_03"] + data["loo_ps_ind_12_bin"]))))
    v["377"] = 0.020000 * np.tanh(((data["ps_car_11"] * ((data["loo_ps_ind_10_bin"] + data["ps_car_11"]) + 1.526320)) *
                                   data["loo_ps_car_10_cat"]))
    v["378"] = 0.020000 * np.tanh((data["loo_ps_ind_12_bin"] * (
    (data["ps_ind_03"] + ((data["ps_ind_15"] + (-(data["ps_car_14"]))) / 2.0)) / 2.0)))
    v["379"] = 0.020000 * np.tanh((data["ps_car_11"] * (
    ((data["loo_ps_car_09_cat"] + (data["ps_ind_01"] * data["loo_ps_ind_11_bin"])) / 2.0) * data["ps_ind_01"])))
    v["380"] = 0.019898 * np.tanh((data["loo_ps_ind_12_bin"] * (
    data["ps_ind_03"] - (data["ps_car_11"] + ((-2.0 + data["loo_ps_car_08_cat"]) / 2.0)))))
    v["381"] = 0.020000 * np.tanh(
        (((data["ps_car_11"] * data["loo_ps_ind_18_bin"]) * data["ps_car_11"]) * data["ps_ind_14"]))
    v["382"] = 0.020000 * np.tanh((data["loo_ps_ind_04_cat"] * (
    data["ps_ind_03"] * ((data["ps_ind_03"] * data["ps_car_12"]) - data["ps_ind_03"]))))
    v["383"] = 0.019980 * np.tanh((data["loo_ps_ind_02_cat"] * (
    ((data["ps_car_11"] + data["ps_car_15"]) / 2.0) + (data["ps_car_15"] * data["ps_car_11"]))))
    v["384"] = 0.019836 * np.tanh(((data["loo_ps_car_06_cat"] * data["loo_ps_ind_04_cat"]) * (
    (data["loo_ps_ind_04_cat"] * data["ps_ind_14"]) + data["loo_ps_car_08_cat"])))
    v["385"] = 0.019965 * np.tanh(
        ((data["ps_car_13"] + data["ps_ind_15"]) * (data["ps_ind_03"] * (data["ps_reg_02"] + data["ps_car_15"]))))
    v["386"] = 0.019508 * np.tanh((data["ps_ind_15"] * (
    data["ps_reg_01"] * ((data["loo_ps_car_06_cat"] * data["loo_ps_car_04_cat"]) + data["loo_ps_ind_13_bin"]))))
    v["387"] = 0.015862 * np.tanh(
        (((data["ps_reg_02"] + data["loo_ps_car_08_cat"]) / 2.0) * (data["ps_car_13"] * (data["ps_car_12"] - 2.0))))
    v["388"] = 0.020000 * np.tanh(
        (data["ps_car_13"] * (0.100000 - ((data["loo_ps_car_10_cat"] * data["ps_ind_01"]) * data["ps_ind_01"]))))
    v["389"] = 0.019992 * np.tanh(
        (data["ps_car_13"] * (data["loo_ps_ind_12_bin"] * (data["ps_reg_01"] + data["ps_ind_15"]))))
    v["390"] = 0.015315 * np.tanh(((np.tanh(np.tanh((data["loo_ps_ind_07_bin"] + data["loo_ps_car_06_cat"]))) + np.tanh(
        data["loo_ps_car_08_cat"])) / 2.0))
    v["391"] = 0.020000 * np.tanh((data["ps_car_15"] * (
    0.452381 - (data["loo_ps_car_08_cat"] * ((data["loo_ps_ind_11_bin"] + data["ps_car_15"]) / 2.0)))))
    v["392"] = 0.020000 * np.tanh(((data["loo_ps_ind_05_cat"] + data["loo_ps_ind_06_bin"]) * (
    (data["loo_ps_car_10_cat"] - data["loo_ps_car_02_cat"]) * data["loo_ps_car_10_cat"])))
    v["393"] = 0.015452 * np.tanh((data["loo_ps_ind_06_bin"] * (
    (data["loo_ps_car_08_cat"] + (data["loo_ps_ind_09_bin"] * data["loo_ps_car_09_cat"])) / 2.0)))
    v["394"] = 0.019977 * np.tanh((data["loo_ps_ind_17_bin"] * (
    (data["loo_ps_ind_08_bin"] * data["ps_car_15"]) * (0.485294 - data["loo_ps_ind_02_cat"]))))
    v["395"] = 0.019977 * np.tanh((data["loo_ps_ind_04_cat"] * (
    (data["ps_reg_02"] + ((data["loo_ps_ind_04_cat"] - data["ps_ind_01"]) - data["loo_ps_car_09_cat"])) / 2.0)))
    v["396"] = 0.019980 * np.tanh(
        (data["ps_reg_01"] * (data["loo_ps_car_10_cat"] * (-((data["loo_ps_ind_12_bin"] + data["ps_reg_02"]))))))
    v["397"] = 0.020000 * np.tanh(((data["ps_car_15"] * (
    (data["loo_ps_ind_16_bin"] + data["loo_ps_car_10_cat"]) / 2.0)) * (data["ps_car_15"] - data["loo_ps_ind_16_bin"])))
    v["398"] = 0.020000 * np.tanh((((-(
    (data["loo_ps_ind_02_cat"] * (data["ps_car_14"] * data["loo_ps_ind_07_bin"])))) + np.tanh(
        data["ps_car_15"])) / 2.0))
    v["399"] = 0.014948 * np.tanh((data["ps_reg_02"] * (data["loo_ps_car_08_cat"] * (-(data["ps_ind_03"])))))
    v["400"] = 0.016214 * np.tanh(
        (data["loo_ps_car_04_cat"] * np.tanh((data["loo_ps_car_11_cat"] - (data["loo_ps_ind_07_bin"] + 1.526320)))))
    return Outputs(v.sum(axis=1))


def GPAri(data):
    return (GPI(data) + GPII(data)) / 2.


def ProjectOnMean(data1, data2, columnName):
    grpOutcomes = data1.groupby(list([columnName]))['target'].mean().reset_index()
    grpCount = data1.groupby(list([columnName]))['target'].count().reset_index()
    grpOutcomes['cnt'] = grpCount.target
    grpOutcomes.drop('cnt', inplace=True, axis=1)
    outcomes = data2['target'].values
    x = pd.merge(data2[[columnName, 'target']], grpOutcomes,
                 suffixes=('x_', ''),
                 how='left',
                 on=list([columnName]),
                 left_index=True)['target']

    return x.values


def GetData(strdirectory,  chunk_pairs):
    # Project Categorical inputs to Target
    highcardinality = ['ps_car_02_cat',
                       'ps_car_09_cat',
                       'ps_ind_04_cat',
                       'ps_ind_05_cat',
                       'ps_car_03_cat',
                       'ps_ind_08_bin',
                       'ps_car_05_cat',
                       'ps_car_08_cat',
                       'ps_ind_06_bin',
                       'ps_ind_07_bin',
                       'ps_ind_12_bin',
                       'ps_ind_18_bin',
                       'ps_ind_17_bin',
                       'ps_car_07_cat',
                       'ps_car_11_cat',
                       'ps_ind_09_bin',
                       'ps_car_10_cat',
                       'ps_car_04_cat',
                       'ps_car_01_cat',
                       'ps_ind_02_cat',
                       'ps_ind_10_bin',
                       'ps_ind_11_bin',
                       'ps_car_06_cat',
                       'ps_ind_13_bin',
                       'ps_ind_16_bin']

    train = pd.read_csv(strdirectory + 'train.csv')
    test = pd.read_csv(strdirectory + 'test.csv')

    train['missing'] = (train == -1).sum(axis=1).astype(float)
    test['missing'] = (test == -1).sum(axis=1).astype(float)

    unwanted = train.columns[train.columns.str.startswith('ps_calc_')]
    train.drop(unwanted, inplace=True, axis=1)
    test.drop(unwanted, inplace=True, axis=1)

    test['target'] = np.nan
    feats = list(set(train.columns).difference(set(['id', 'target'])))
    feats = list(['id']) + feats + list(['target'])
    train = train[feats]
    test = test[feats]

    #blindloodata = None


    for c in highcardinality:
        train['loo_' + c] = np.zeros(train.shape[0])

    for i in range(len(chunk_pairs)):

        pair = chunk_pairs[i]
        print " "
        print " ...TRAINING PAIR {} ...".format(i + 1)
        train_index = pair[0]
        test_index =  pair[1]

        print('Fold:', i)
        blindtrain = train.loc[test_index].copy()
        vistrain = train.loc[train_index].copy()

        for c in highcardinality:
            #blindtrain['loo_' + c] += ProjectOnMean(vistrain,blindtrain, c)
            train.loc[test_index, 'loo_' + c] += ProjectOnMean(vistrain, blindtrain, c)
        #if (blindloodata is None):
            #blindloodata = blindtrain.copy()
        #else:
            #blindloodata = pd.concat([blindloodata, blindtrain])

    for c in highcardinality:
        test.insert(1, 'loo_' + c, ProjectOnMean(train,
                                                 test, c))
    test.drop(highcardinality, inplace=True, axis=1)

    #train = blindloodata
    for c in highcardinality:
        train['loo_' + c] = train['loo_' + c]/9

    train.drop(highcardinality, inplace=True, axis=1)
    train = train.fillna(train.mean())
    test = test.fillna(train.mean())

    print('Scale values')
    ss = StandardScaler()
    features = train.columns[1:-1]
    ss.fit(pd.concat([train[features], test[features]]))
    train[features] = ss.transform(train[features])
    test[features] = ss.transform(test[features])
    train[features] = np.round(train[features], 6)
    test[features] = np.round(test[features], 6)
    return train, test


def main():

    chunks = np.load("cv_indx10.npy")
    id_pairs = [([y for y in range(10) if y not in x], list(x)) for x in list(itertools.combinations(range(10), 2))]

    chunk_pairs = []
    for pair in id_pairs:
        chunk_pairs.append(([y for x in pair[0] for y in chunks[x]], [y for x in pair[1] for y in chunks[x]]))

    print('Started')
    strdirectory = ''
    gptrain, gptest = GetData(strdirectory,  chunk_pairs)

    val_res = GPAri(gptrain).values.flatten()
    tst_res = GPAri(gptest).values.flatten()

    np.save("val_xx2.npy", val_res)
    np.save("test_xx2.npy", tst_res)


    print('GPAri Gini Score:', GiniScore(gptrain.target.values, val_res))

    basic = pd.read_csv(strdirectory + 'sample_submission.csv')

    basic.target = tst_res

    basic.to_csv('gp_test.csv', index=None, float_format='%.6f')


    print('Finished')


if __name__ == "__main__":
    main()
