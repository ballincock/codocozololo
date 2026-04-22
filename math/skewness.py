import numpy as np
import numpy.typing as npt
from scipy import stats, integrate
from flask import Blueprint, request, jsonify

skewness_bp = Blueprint('skewness', __name__)

def half_sample_mode(x):
    x = np.sort(np.asarray(x))
    while len(x) >= 3:
        n = len(x)
        w = x[n//2:] - x[:n - n//2]
        i = np.argmin(w)
        x = x[i : i + n - n//2]
    return np.mean(x)

class Skewness:
    @staticmethod
    def pearson_mode_skew(x: npt.NDArray) -> float:
        mean = np.nanmean(x)
        mode = stats.mode(x, keepdims=True)[0][0]
        std = np.nanstd(x)
        return float((mean - mode) / std) if std != 0 else 0.0

    @staticmethod
    def bickel_mode_skew(x: npt.NDArray) -> float:
        mode = half_sample_mode(x)
        return float(np.nanmean(np.sign(np.asarray(x) - mode)))

    @staticmethod
    def pearson_median_skew(x: npt.NDArray) -> float:
        mean = np.nanmean(x)
        median = np.nanmedian(x)
        std = np.nanstd(x)
        return float(3.0 * (mean - median) / std) if std != 0 else 0.0

    @staticmethod
    def bowley_skew(x: npt.NDArray) -> float:
        q1, q2, q3 = np.nanquantile(x, [0.25, 0.5, 0.75])
        return float((q3 + q1 - 2 * q2) / (q3 - q1)) if (q3 - q1) != 0 else 0.0

    @staticmethod
    def kelly_skew(x: npt.NDArray) -> float:
        d1, d5, d9 = np.nanquantile(x, [0.1, 0.5, 0.9])
        return float((d9 + d1 - 2 * d5) / (d9 - d1)) if (d9 - d1) != 0 else 0.0

    @staticmethod
    def auc_skew_gamma(x: npt.NDArray, dp: float = 0.01) -> float:
        n = int(1 / dp)
        half_n = n // 2
        qs = np.nanquantile(x, np.r_[np.linspace(0, 1, n), 0.5])
        med = qs[-1]
        qs = qs[:-1]
        qs_low = qs[:half_n]
        qs_high = qs[-half_n:]
        skews = (qs_low + qs_high - 2 * med) / (qs_high - qs_low)
        return float(integrate.trapezoid(skews, dx=dp))

@skewness_bp.route('/calculate', methods=['POST'])
def run_skew():
    data = request.json
    raw_data = data.get('dataset', [])
    method = data.get('method', 'pearson_median')
    
    x = np.array(raw_data, dtype=float)
    if len(x) == 0:
        return jsonify({"error": "No data provided"}), 400

    try:
        if method == 'pearson_mode': res = Skewness.pearson_mode_skew(x)
        elif method == 'bickel': res = Skewness.bickel_mode_skew(x)
        elif method == 'pearson_median': res = Skewness.pearson_median_skew(x)
        elif method == 'bowley': res = Skewness.bowley_skew(x)
        elif method == 'kelly': res = Skewness.kelly_skew(x)
        elif method == 'auc_gamma': res = Skewness.auc_skew_gamma(x)
        else: return jsonify({"error": "Method not found"}), 400
        
        return jsonify({"result": res, "method": method})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
