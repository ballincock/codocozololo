import numpy as np
import numpy.typing as npt
from scipy import stats
from flask import Blueprint, request, jsonify

Kurtosis = Blueprint('Kurtosis', __name__)

class Kurtosis:
    @staticmethod
    def moors_kurt(x: npt.NDArray) -> float:
        return float(np.nanvar(stats.zscore(x, nan_policy="omit") ** 2) + 1)

    @staticmethod
    def moors_octile_kurt(x: npt.NDArray) -> float:
        o1, o2, o3, o5, o6, o7 = np.nanquantile(x, [0.125, 0.25, 0.375, 0.625, 0.75, 0.875])
        return float(((o7 - o5) + (o3 - o1)) / (o6 - o2))

    @staticmethod
    def hogg_kurt(x: npt.NDArray) -> float:
        p05, p50, p95 = np.nanquantile(x, [0.05, 0.5, 0.95])
        masked_p95 = np.where(x >= p95, x, np.nan)
        masked_p05 = np.where(x <= p05, x, np.nan)
        masked_p50g = np.where(x >= p50, x, np.nan)
        masked_p50l = np.where(x <= p50, x, np.nan)
        return float(
            (np.nanmean(masked_p95) - np.nanmean(masked_p05)) / 
            (np.nanmean(masked_p50g) - np.nanmean(masked_p50l))
        )

    @staticmethod
    def crow_siddiqui_kurt(x: npt.NDArray) -> float:
        p025, p25, p75, p975 = np.nanquantile(x, [0.025, 0.25, 0.75, 0.975])
        return float((p975 - p025) / (p75 - p25))

    @staticmethod
    def reza_ma_kurt(x: npt.NDArray) -> float:
        h1, h7, h9, h15 = np.nanquantile(x, [0.0625, 0.4375, 0.5625, 0.9375])
        return float(((h15 - h9) + (h7 - h1)) / (h15 - h1))

    @staticmethod
    def staudte_kurt(x: npt.NDArray) -> float:
        p10, p33, p66, p90 = np.nanquantile(x, [0.1, 1/3, 2/3, 0.9])
        return float((p90 - p10) / (p66 - p33))

    @staticmethod
    def schmid_trede_peakedness(x: npt.NDArray) -> float:
        p125, p25, p75, p875 = np.nanquantile(x, [0.125, 0.25, 0.75, 0.875])
        return float((p875 - p125) / (p75 - p25))

@Kurtosis.route('/calculate_kurtosis', methods=['POST'])
def run_stats():
    data = request.json
    raw_data = data.get('dataset', [])
    method = data.get('method', 'moors')
    
    x = np.array(raw_data, dtype=float)
    
    if len(x) == 0:
        return jsonify({"error": "Empty dataset"}), 400

    try:
        if method == 'moors':
            result = Kurtosis.moors_kurt(x)
        elif method == 'moors_octile':
            result = Kurtosis.moors_octile_kurt(x)
        elif method == 'hogg':
            result = Kurtosis.hogg_kurt(x)
        elif method == 'crow':
            result = Kurtosis.crow_siddiqui_kurt(x)
        elif method == 'reza':
            result = Kurtosis.reza_ma_kurt(x)
        elif method == 'staudte':
            result = Kurtosis.staudte_kurt(x)
        elif method == 'peakedness':
            result = Kurtosis.schmid_trede_peakedness(x)
        else:
            return jsonify({"error": "Unknown method"}), 400
            
        return jsonify({"method": method, "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
