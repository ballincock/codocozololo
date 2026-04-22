import numpy as np
import numpy.typing as npt
from scipy import stats
from flask import Blueprint, request, jsonify

Dispersion = Blueprint('Dispersion', __name__)

class Dispersion:
    @staticmethod
    def studentized_range(x: npt.NDArray) -> float:
        std = np.nanstd(x)
        maximum = np.nanmax(x)
        minimum = np.nanmin(x)
        return float((maximum - minimum) / std)
      
    @staticmethod
    def coefficient_of_lvariation(x: npt.NDArray) -> float:
        l1, l2 = stats.lmoment(x, order=[1, 2], nan_policy="omit")
        return float(l2 / l1)
      
    @staticmethod
    def coefficient_of_variation(x: npt.NDArray) -> float:
        return float(np.nanstd(x) / np.nanmean(x))
      
    @staticmethod
    def robust_coefficient_of_variation(x: npt.NDArray) -> float:
        med = np.nanmedian(x)
        med_abs_dev = np.nanmedian(np.abs(x - med))
        return float(1.4826 * med_abs_dev / med)
      
    @staticmethod
    def quartile_coefficient_of_dispersion(x: npt.NDArray) -> float:
        q1, q3 = np.nanquantile(x, [0.25, 0.75])
        return float(0.75 * (q3 - q1) / (q3 + q1))
      
    @staticmethod
    def fisher_index_of_dispersion(x: npt.NDArray) -> float:
        return float((len(x) - 1) * np.nanvar(x) / np.nanmean(x))
      
    @staticmethod
    def morisita_index_of_dispersion(x: npt.NDArray) -> float:
        x_sum = np.nansum(x)
        return float(len(x) * (np.nansum(np.square(x)) - x_sum) / (x_sum**2 - x_sum))
      
    @staticmethod
    def standard_quantile_absolute_deviation(x: npt.NDArray) -> float:
        med = np.nanmedian(x)
        n = len(x)
        k = 1.0 + 0.762 / n + 0.967 / n**2
        q = 0.6826894921370850  
        return float(k * np.nanquantile(np.abs(x - med), q=q))
      
    @staticmethod
    def shamos_estimator(x: npt.NDArray) -> float:
        product = np.meshgrid(x, x, sparse=True)
        return float(np.nanmedian(np.abs(product[0] - product[1])))
      
    @staticmethod
    def coefficient_of_range(x: npt.NDArray) -> float:
        min_ = np.nanmin(x)
        max_ = np.nanmax(x)
        return float((max_ - min_) / (max_ + min_))
      
    @staticmethod
    def cole_index_of_dispersion(x: npt.NDArray) -> float:
        return float(np.nansum(np.square(x)) / np.nansum(x) ** 2)
      
    @staticmethod
    def gini_mean_difference(x: npt.NDArray) -> float:
        n = len(x)
        product = np.meshgrid(x, x, sparse=True)
        return float(np.nansum(np.abs(product[0] - product[1])) / (n * (n - 1)))
      
    @staticmethod
    def inter_expectile_range(x: npt.NDArray) -> float:
        x = np.ravel(x)
        _x = _x[np.isfinite(_x)]
        if len(_x) <= 1:
            return np.nan
        return float(stats.expectile(_x, 0.75) - stats.expectile(_x, 0.25))

@Dispersion.route('/calculate_dispersion', methods=['POST'])
def run_stats():
    data = request.json
    raw_data = data.get('dataset', [])
    method = data.get('method', 'moors')
    
    x = np.array(raw_data, dtype=float)
    
    if len(x) == 0:
        return jsonify({"error": "Empty dataset"}), 400

    try:
        if method == 'studentized_range':
            result = Dispersion.studentized_range(x)
        elif method == 'coefficient_of_lvariation':
            result = Dispersion.coefficient_of_lvariation(x)
        elif method == 'coefficient_of_variation':
            result = Dispersion.coefficient_of_variation(x)
        elif method == 'robust_coefficient_of_variation':
            result = Dispersion.robust_coefficient_of_variation(x)
        elif method == 'quartile_coefficient_of_dispersion':
            result = Dispersion.quartile_coefficient_of_dispersion(x)
        elif method == 'fisher_index_of_dispersion':
            result = Dispersion.fisher_index_of_dispersion(x)
        elif method == 'peakedness':
            result = Dispersion.schmid_trede_peakedness(x)
        elif method == 'morisita_index_of_dispersion':
            result = Dispersion.morisita_index_of_dispersion(x)
        elif method == 'standard_quantile_absolute_deviation':
            result = Dispersion.standard_quantile_absolute_deviation(x)
        elif method == 'shamos_estimator':
            result = Dispersion.shamos_estimator(x)
        elif method == 'coefficient_of_range':
            result = Dispersion.coefficient_of_range(x)
        elif method == 'cole_index_of_dispersion':
            result = Dispersion.cole_index_of_dispersion(x)
        elif method == 'gini_mean_difference':
            result = Dispersion.gini_mean_difference(x)
        elif method == 'inter_expectile_range':
            result = Dispersion.inter_expectile_range(x)
        else:
            return jsonify({"error": "Unknown method"}), 400
            
        return jsonify({"method": method, "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
