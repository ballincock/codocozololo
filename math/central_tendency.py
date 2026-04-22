import numpy as np
import numpy.typing as npt
from scipy import stats
from flask import Blueprint, request, jsonify

CentralTendency = Blueprint('CentralTendency', __name__)

class CentralTendency:
    @staticmethod
    def midrange(x: npt.NDArray) -> float:
        maximum = np.nanmax(x)
        minimum = np.nanmin(x)
        return float((maximum + minimum) * 0.5)
      
    @staticmethod
    def midhinge(x: npt.NDArray) -> float: 
        q1, q3 = np.nanquantile(x, [0.25, 0.75])
        return float((q3 + q1) * 0.5)
      
    @staticmethod
    def trimean(x: npt.NDArray) -> float:
        q1, q2, q3 = np.nanquantile(x, [0.25, 0.5, 0.75])
        return float(0.5 * q2 + 0.25 * q1 + 0.25 * q3)
      
    @staticmethod
    def contraharmonic_mean(x: npt.NDArray) -> float:
        return float(np.nansum(np.square(x)) / np.nansum(x))
      
    @staticmethod
    def hodges_lehmann_sen_location(x: npt.NDArray) -> float:
        product = np.meshgrid(x, x, sparse=True)
        return float(np.nanmedian(product[0] + product[1]) * 0.5)
      
    @staticmethod
    def standard_trimmed_harrell_davis_quantile(x: npt.NDArray, q: float = 0.5) -> float:
        if q <= 0 or q >= 1:
            msg = "Parameter q should be in range (0, 1)."
            raise ValueError(msg)
        _x = np.sort(x)
        _x = _x[np.isfinite(_x)]
        n = len(_x)
        if n == 0:
            return np.nan
        if n == 1:
            return float(_x[0])
        n_calculated = 1 / n**0.5 
        a = (n + 1) * q
        b = (n + 1) * (1.0 - q)
        hdi = (max(0, q - n_calculated * 0.5), min(1, q + n_calculated * 0.5))
        hdi_cdf = stats.beta.cdf(hdi, a, b)
        i_start = math.floor(hdi[0] * n)
        i_end = math.ceil(hdi[1] * n)
        nums = np.arange(i_start, i_end + 1) / n
        nums[nums <= hdi[0]] = hdi[0]
        nums[nums >= hdi[1]] = hdi[1]
        cdfs = (stats.beta.cdf(nums, a, b) - hdi_cdf[0]) / (hdi_cdf[1] - hdi_cdf[0])
        w = cdfs[1:] - cdfs[:-1]
        return float(np.sum(_x[i_start:i_end] * w))
      
    @staticmethod
    def half_sample_mode(x: npt.NDArray) -> float:
        y = np.sort(x)
        y = y[np.isfinite(y)]
        _corner_cases = (4, 3)  
        while (ny := len(y)) >= _corner_cases[0]:
            half_y = math.ceil(ny / 2)
            w_min = y[-1] - y[0]
            for i in range(ny - half_y):
                w = y[i + half_y - 1] - y[i]
                if w <= w_min:
                    w_min = w
                    j = i
                if w == 0:
                    return float(y[j])
                y = y[j : (j + half_y - 1)]
                if len(y) == _corner_cases[1]:
                    z = 2 * y[1] - y[0] - y[2]
                if z < 0:
                    return float(np.mean(y[0:1]))
                if z > 0:
                    return float(np.mean(y[1:2]))
            return float(y[1])
        return float(np.mean(y))
      
    @staticmethod
    def tau_location(x: npt.NDArray, c: float = 4.5) -> float:
        if c <= 0:
            msg = "Parameter c should be strictly positive."
            raise ValueError(msg)
        med = np.nanmedian(x)
        mad = np.nanmedian(np.abs(x - med))
        scaled_x = (x - med) / mad
        w = np.square(1.0 - np.square(scaled_x / c)) * (np.abs(scaled_x) <= c)
        return float(np.nansum(x * w) / np.nansum(w))
      
    @staticmethod
    def grenanders_m(x: npt.NDArray, p: float = 1.001, k: int = 2) -> float:
        x_sort = np.sort(x).astype("float")
        x_sort = x_sort[np.isfinite(x_sort)]

        if p <= 1:
            msg = "Parameter p should be a float greater than 1."
            raise ValueError(msg)
        if (k <= 0) or (not isinstance(k, int)):
            msg = "Parameter k should be an integer between 1 and length of x."
            raise ValueError(msg)

        if len(x_sort) <= k:
            return np.nan

        diff = x_sort[k:] - x_sort[:-k]
        if diff.sum() == 0.0:
            return float(x_sort[0])

        diff[diff == 0.0] = np.nan

        return float(
            0.5
            * np.nansum((x_sort[k:] + x_sort[:-k]) / np.power(diff, p))
            / np.nansum(np.power(diff, -p))
        )
      
    @staticmethod
    def gastwirth_location(x: npt.NDArray) -> float:
        p33, p50, p66 = np.nanquantile(x, [1 / 3, 0.5, 2 / 3])
        return float(0.3 * p33 + 0.4 * p50 + 0.3 * p66)

@CentralTendency.route('/calculate_central_tendency', methods=['POST'])
def run_central_tendency():
    data = request.json
    raw_data = data.get('dataset', [])
    method = data.get('method', 'moors')
    
    x = np.array(raw_data, dtype=float)
    
    if len(x) == 0:
        return jsonify({"error": "Empty dataset"}), 400

    try:
        if method == 'midrange':
            result = CentralTendency.midrange(x)
        elif method == 'midhinge':
            result = CentralTendency.midhinge(x)
        elif method == 'trimean':
            result = CentralTendency.trimean(x)
        elif method == 'contraharmonic_mean':
            result = CentralTendency.contraharmonic_mean(x)
        elif method == 'hodges_lehmann_sen_location':
            result = CentralTendency.hodges_lehmann_sen_location(x)
        elif method == 'standard_trimmed_harrell_davis_quantile':
            result = CentralTendency.standard_trimmed_harrell_davis_quantile(x, q)
        elif method == 'half_sample_mode':
            result = CentralTendency.half_sample_mode(x)
        elif method == 'tau_location':
            result = CentralTendency.tau_location(x, c)
        elif method == 'grenanders_m':
            result = CentralTendency.grenanders_m(x, p, k)
        elif method == 'gastwirth_location':
            result = CentralTendency.gastwirth_location(x)
        else:
            return jsonify({"error": "Unknown method"}), 400
            
        return jsonify({"method": method, "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
