import numpy as np
import numpy.typing as npt
from scipy import stats
from flask import Blueprint, request, jsonify

Association = Blueprint('Association', __name__)

class Association:
    @staticmethod
    def _check_arrays(x: npt.NDArray, y: npt.NDArray) -> bool:
        _x = np.ravel(x)
        _y = np.ravel(y)
        if len(_x) != len(_y):
            warnings.warn(
                "Lengths of the inputs do not match, please check the arrays.", stacklevel=2
            )
            return True
        if len(_x) <= 1:
            warnings.warn(
                "Lengths of the inputs are too small, please check the arrays.",
                stacklevel=2,
            )
            return True
        if np.all(np.isclose(_x, np.nanmin(_x), equal_nan=False)) or np.all(
            np.isclose(_y, np.nanmin(_y), equal_nan=False)
        ):
            warnings.warn(
                "One of the input arrays is constant;"
                " the correlation coefficient is not defined.",
                stacklevel=2,
            )
            return True
        if np.any(np.isinf(_x)) or np.any(np.isinf(_y)):
            warnings.warn(
                "One of the input arrays contains inf, please check the array.",
                stacklevel=2,
            )
            return True
        if (np.isnan(_x).sum() >= len(_x) - 1) or (np.isnan(_y).sum() >= len(_y) - 1):
            warnings.warn(
                "One of the input arrays has too many missing values,"
                " please check the arrays.",
                stacklevel=2,
            )
            return True
        return False

    @staticmethod
    def _prep_arrays(x: npt.NDArray, y: npt.NDArray) -> tuple[npt.NDArray, npt.NDArray]:
        _x = np.ravel(x)
        _y = np.ravel(y)
        notnan = np.isfinite(_x) & np.isfinite(_y)
        _x = _x[notnan]
        _y = _y[notnan]
        return _x, _y

    @staticmethod
    def concordance_correlation(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        std_x = np.std(x, ddof=0)
        std_y = np.std(y, ddof=0)
        w = std_y / std_x
        v = (np.mean(x) - np.mean(y)) ** 2 / (std_x * std_y) ** 0.5
        x_a = 2 / (v**2 + w + 1 / w)
        p = np.corrcoef(x, y)[0][1]
        return float(p * x_a)

    @staticmethod
    def concordance_rate(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        n = len(x)
        mean_x = np.sum(x) / n
        mean_y = np.sum(y) / n
        sem_x = np.std(x, ddof=0) / n**0.5
        sem_y = np.std(y, ddof=0) / n**0.5
        return float(
            (
                np.sum((x >= mean_x + sem_x) & (y >= mean_y + sem_y))
                - np.sum((x <= mean_x - sem_x) & (y >= mean_y + sem_y))
                + np.sum((x <= mean_x - sem_x) & (y <= mean_y - sem_y))
                - np.sum((x >= mean_x + sem_x) & (y <= mean_y - sem_y))
            )
            / n
        )

    @staticmethod
    def symmetric_chatterjee_xi(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        return max(
            stats.chatterjeexi(x, y, nan_policy="omit")[0],
            stats.chatterjeexi(y, x, nan_policy="omit")[0],
        )

    @staticmethod
    def zhang_i(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        return float(
            min(
                1.0,
                max(
                    abs(stats.spearmanr(x, y, nan_policy="omit")[0]),
                    2.5**0.5 * symmetric_chatterjee_xi(x, y),
                ),
            )
        )

    @staticmethod
    def tanimoto_similarity(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        xy = np.mean(x * y)
        xx = np.mean(x**2)
        yy = np.mean(y**2)
        return float(xy / (xx + yy - xy))

    @staticmethod
    def blomqvist_beta(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        med_x = np.median(x)
        med_y = np.median(y)
        return float(np.mean(np.sign((x - med_x) * (y - med_y))))

    @staticmethod
    def fechner_correlation(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        avg_x = np.mean(x)
        avg_y = np.mean(y)
        return float(np.mean(np.sign(x - avg_x) * np.sign(y - avg_y)))

    @staticmethod
    def winsorized_correlation(x: npt.NDArray, y: npt.NDArray, k: float = 0.1) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        x_w = stats.mstats.winsorize(x, (k, k))
        y_w = stats.mstats.winsorize(y, (k, k))
        return float(np.corrcoef(x_w, y_w)[0, 1])

    @staticmethod
    def rank_minrelation_coefficient(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        n_sq = len(x) ** 2 + 1
        rank_x_inc = (stats.rankdata(x) ** 2) / n_sq - 0.5
        rank_y_inc = (stats.rankdata(y) ** 2) / n_sq - 0.5
        rank_y_dec = -(stats.rankdata(-y) ** 2) / n_sq + 0.5
        lower = np.sum((-rank_x_inc < rank_y_inc) * (rank_x_inc + rank_y_inc) ** 2)
        higher = np.sum((rank_x_inc > rank_y_dec) * (rank_x_inc - rank_y_dec) ** 2)
        return float((lower - higher) / (lower + higher))

    @staticmethod
    def tukey_correlation(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        s_x = gini_mean_difference(x)
        s_y = gini_mean_difference(y)
        x_norm = x / s_x
        y_norm = y / s_y
        coef = 0.25 * (
            gini_mean_difference(x_norm + y_norm) ** 2
            - gini_mean_difference(x_norm - y_norm) ** 2
        )
        return float(max(min(coef, 1.0), -1.0))

    @staticmethod
    def gaussain_rank_correlation(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        n = len(x)
        norm_factor = 1 / (n + 1)
        x_ranks_norm = stats.rankdata(x) * norm_factor
        y_ranks_norm = stats.rankdata(y) * norm_factor
        coef = np.sum(stats.norm.ppf(x_ranks_norm) * stats.norm.ppf(y_ranks_norm)) / np.sum(
            stats.norm.ppf(np.arange(1, n + 1) * norm_factor) ** 2
        )
        return float(max(min(coef, 1.0), -1.0))

    @staticmethod
    def quantile_correlation(x: npt.NDArray, y: npt.NDArray, q: float = 0.5) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        return float(
            np.mean((q - (y < np.quantile(y, q=q))) * (x - np.mean(x)))
            / (((q - q**2) * np.var(x)) ** 0.5)
        )

    @staticmethod
    def normalized_chatterjee_xi(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        return (
            stats.chatterjeexi(x, y, nan_policy="omit")[0]
            / stats.chatterjeexi(y, y, nan_policy="omit")[0]
        )

    @staticmethod
    def morisita_horn_similarity(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        mean_x = np.mean(x)
        mean_y = np.mean(y)
        return float(
            np.sum(2 * x * y) / np.sum(x**2 * mean_y / mean_x + y**2 * mean_x / mean_y)
        )

    @staticmethod
    def rank_divergence(x: npt.NDArray, y: npt.NDArray, a: float = 2.0) -> float:
        if _check_arrays(x, y):
            return np.nan
        x, y = _prep_arrays(x, y)
        if _check_arrays(x, y):
            return np.nan
        if a <= 0:
            msg = "Parameter a should be > 0."
            raise ValueError(msg)
        return float(
            (a + 1.0)
            / a
            * np.mean(
                np.abs(1.0 / stats.rankdata(x) ** a - 1.0 / stats.rankdata(y) ** a)
                ** (1.0 / (a + 1.0))
            )
        )

    @staticmethod
    def symmetric_normalized_chatterjee_xi(x: npt.NDArray, y: npt.NDArray) -> float:
        if _check_arrays(x, y):
            return np.nan
        return max(normalized_chatterjee_xi(x, y), normalized_chatterjee_xi(y, x))

@Association.route('/calculate_association', methods=['POST'])
def run_assoc():
    data = request.json
    raw_data = data.get('dataset', [])
    method = data.get('method', '_check_arrays')
    
    x = np.array(raw_data, dtype=float)
    
    if len(x) == 0:
        return jsonify({"error": "Empty dataset"}), 400

    try:
        if method == '_check_arrays':
            result = Association._check_arrays(x, y)
        elif method == '_prep_arrays':
            result = Association.prep_arrays(x, y)
        elif method == 'concordance_correlation':
            result = Association.concordance_correlation(x, y)
        elif method == 'concordance_rate':
            result = Association.concordance_rate(x, y)
        elif method == 'symmetric_chatterjee_xi':
            result = Association.symmetric_chatterjee_xi(x, y)
        elif method == 'zhang_i':
            result = Association.zhang_i(x, y)
        elif method == 'tanimoto_similarity':
            result = Association.tanimoto_similarity(x, y)
        elif method == 'blomqvist_beta':
            result = Association.blomqvist_beta(x, y)
        elif method == 'fechner_correlation':
            result = Association.fechner_correlation(x, y)
        elif method == 'winsorized_correlation':
            result = Association.winsorized_correlation(x, y)
        elif method == 'rank_minrelation_coefficient':
            result = Association.rank_minrelation_coefficient(x, y)
        elif method == 'tukey_correlation':
            result = Association.tukey_correlation(x, y)
        elif method == 'gaussain_rank_correlation':
            result = Association.gaussain_rank_correlation(x, y)
        elif method == 'quantile_correlation':
            result = Association.quantile_correlation(x, y)
        elif method == 'normalized_chatterjee_xi':
            result = Association.normalized_chatterjee_xi(x, y)
        elif method == 'morisita_horn_similarity':
            result = Association.morisita_horn_similarity(x, y)
        elif method == 'rank_divergence':
            result = Association.rank_divergence(x, y)
        elif method == 'symmetric_normalized_chatterjee_xi':
            result = Association.symmetric_normalized_chatterjee_xi(x, y)

        else:
            return jsonify({"error": "Unknown method"}), 400
            
        return jsonify({"method": method, "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
