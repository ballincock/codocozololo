import math  
from flask import Flask, request, jsonify, render_template,  Blueprint

occupational_sci = Blueprint('occupational_sci', __name__)

class OccupationalEngine:
    @staticmethod
    def run(data):
        def get_val(key):
            try:
                return float(data.get(key) or 0)
            except:
                return 0.0

        try:
            cid = int(data.get('cid', 1))
            step = int(data.get('step', 1))
        except:
            return [">> ERROR: Invalid Step/CID"]

        if cid == 1:
            if step == 1:
                pipe_dia = float(data.get('pipe_dia_in', 0) or 0)
                pipe_slope = float(data.get('pipe_slope_ft_ft', 0) or 0)
                n_roughness = 0.013 

                if pipe_dia > 0 and pipe_slope > 0:
                    radius_ft = (pipe_dia / 12) / 4
                    area = 3.1415 * ((pipe_dia / 12 / 2) ** 2)
                    velocity = (1.486 / n_roughness) * (radius_ft ** (2/3)) * (pipe_slope ** 0.5)
                    capacity_cfs = area * velocity
                    return [
                        f">> MODULE: PIPE CAPACITY",
                        f">> RESULT: {capacity_cfs:.2f} cfs"
                    ]
            
            if step == 2:
                p_length = float(data.get('p_length', 0) or 0)
                p_width = float(data.get('p_width', 0) or 0)
                p_depth = float(data.get('p_depth', 0) or 0)

                if p_length > 0 and p_width > 0 and p_depth > 0:
                    total_cf = p_length * p_width * p_depth
                    total_gallons = total_cf * 7.48
                    return [
                        f">> MODULE: POND VOLUME",
                        f">> RESULT: {total_cf:.0f} ft³ ({total_gallons:,.0f} gal"
                    ]

            if step == 3:
                v_head = float(data.get('v_head_ft', 0) or 0)
        
                if v_head > 0:
                    v_discharge = 2.5 * (v_head ** 2.5)
                    return [
                        f">> MODULE: V-Notch Weir",
                        f">> RESULT: {v_discharge:.2f} cfs"
                    ]

            if step == 4:
                drop_inches = float(data.get('drop_inches', 0) or 0)
                time_minutes = float(data.get('time_minutes', 0) or 0)
            
                if time_minutes > 0:
                    inf_rate = (drop_inches / time_minutes) * 60
                    return [
                        f">> MODULE: Infiltration Rate",
                        f">> RESULT: {inf_rate:.2f} in/hr"
                    ]
                else:
                    return [">> ERROR: Time must be greater than 0"]

            if step == 5:
                r_area = float(data.get('r_area_acres', 0) or 0)
                r_intensity = float(data.get('r_intensity_in_hr', 0) or 0)
                r_coeff = float(data.get('r_coeff', 0.9) or 0.9)
        
                if r_area > 0 and r_intensity > 0:
                    r_peak_q = r_coeff * r_intensity * r_area
                    return [
                        f">> MODULE: Quick Runoff",
                        f">> RESULT: {r_peak_q:.2f} cfs"
                    ]

            if step == 6:
                o_area = float(data.get('o_area_sqft', 0) or 0)
                o_head = float(data.get('o_head_ft', 0) or 0)
                if o_area > 0 and o_head > 0:
                    o_discharge = 0.62 * o_area * ((2 * 32.2 * o_head) ** 0.5)
                    return [
                        f">> MODULE: ORIFICE FLOW",
                        f">> RESULT: {o_discharge:.2f} cfs"
                    ]

            if step == 7:
                tc_length = float(data.get('tc_length_ft', 0) or 0)
                tc_slope = float(data.get('tc_slope_ft_ft', 0) or 0)
                if tc_length > 0 and tc_slope > 0:
                    tc_minutes = 0.0078 * (tc_length**0.77) * (tc_slope**-0.385)
                    return [
                        f">> MODULE: TIME OF CONCENTRATION",
                        f">> RESULT: {tc_minutes:.2f} minutes"
                    ]

            if step == 8:
                precip = float(data.get('precip_in', 0) or 0)
                cn_value = float(data.get('cn_value', 0) or 0)
                if precip > 0 and cn_value > 0:
                    s_retention = (1000 / cn_value) - 10
                    if precip > (0.2 * s_retention):
                        q_runoff = ((precip - 0.2 * s_retention)**2) / (precip + 0.8 * s_retention)
                    else:
                        q_runoff = 0
                    return [
                        f">> MODULE: NRCS RUNOFF DEPTH",
                        f">> RESULT: {q_runoff:.2f} inches"
                    ]

            if step == 9:
                b_width = float(data.get('b_width_ft', 0) or 0)
                flow_depth = float(data.get('flow_depth_ft', 0) or 0)
                side_slope = float(data.get('side_slope_z', 0) or 0) 
                ch_slope = float(data.get('ch_slope_ft_ft', 0) or 0)
                if flow_depth > 0 and ch_slope > 0:
                    area = (b_width + side_slope * flow_depth) * flow_depth
                    wetted_p = b_width + 2 * flow_depth * ((1 + side_slope**2)**0.5)
                    radius = area / wetted_p
                    velocity = (1.486 / 0.030) * (radius**(2/3)) * (ch_slope**0.5)
                    q_ditch = area * velocity
                    return [
                        f">> MODULE: DITCH CAPACITY",
                        f">> RESULT: {q_ditch:.2f} cfs"
                    ]


            if step == 10:
                v_fps = float(data.get('v_fps', 0) or 0)
                if v_fps > 0:
                    d50_in = ((v_fps**2) / (2 * 32.2 * (2.65 - 1) * (0.86**2))) * 12
                    return [
                        f">> MODULE: RIPRAP SIZING",
                        f">> RESULT: {d50_in:.1f} inch D50 stone"
                    ]


            if step == 11:
                q_in = float(data.get('q_peak_inflow', 0) or 0)
                q_out = float(data.get('q_allowable_out', 0) or 0)
                duration_min = float(data.get('storm_duration_min', 0) or 0)
                if q_in > q_out:
                    storage_cf = (q_in - q_out) * (duration_min * 60) * 0.5 
                    return [
                        f">> MODULE: EST. DETENTION STORAGE",
                        f">> RESULT: {storage_cf:.0f} ft³"
                    ]


            if step == 12:
                inlet_length = float(data.get('inlet_length_ft', 0) or 0)
                inlet_depth = float(data.get('inlet_depth_ft', 0) or 0)
                if inlet_length > 0 and inlet_depth > 0:
                    q_inlet = 3.0 * inlet_length * (inlet_depth ** 1.5)
                    return [
                        f">> MODULE: CURB INLET CAPACITY",
                        f">> RESULT: {q_inlet:.2f} cfs"
                    ]

            if step == 13:
                flow_cfs = float(data.get('flow_cfs', 0) or 0)
                p_dia_in = float(data.get('p_dia_in', 0) or 0)
                if flow_cfs > 0 and p_dia_in > 0:
                    p_area = 3.1415 * (((p_dia_in / 12) / 2) ** 2)
                    exit_v = flow_cfs / p_area
                    status = "SCOUR RISK" if exit_v > 5.0 else "SAFE"
                    return [
                        f">> MODULE: PIPE EXIT VELOCITY",
                        f">> RESULT: {exit_v:.2f} fps ({status})"
                    ]

            if step == 14:
                peak_q = float(data.get('peak_q_cfs', 0) or 0)
                settle_vel = float(data.get('settle_vel_fps', 0.0004) or 0.0004) 
                if peak_q > 0:
                    min_area_sqft = peak_q / settle_vel
                    return [
                        f">> MODULE: SEDIMENT BASIN AREA",
                        f">> RESULT: {min_area_sqft:,.0f} sq. ft."
                    ]

            if step == 15:
                n1_val = float(data.get('n_main', 0.013) or 0.013)
                p1_len = float(data.get('p_main_ft', 0) or 0)
                n2_val = float(data.get('n_side', 0.035) or 0.035)
                p2_len = float(data.get('p_side_ft', 0) or 0)
                if p1_len > 0 or p2_len > 0:
                    weighted_n = (((p1_len * (n1_val**1.5)) + (p2_len * (n2_val**1.5))) / (p1_len + p2_len))**(2/3)
                    return [
                        f">> MODULE: COMPOSITE ROUGHNESS",
                        f">> RESULT: {weighted_n:.4f} n"
                    ]


            if step == 16:
                r_coeff = float(data.get('r_coeff', 0) or 0)
                r_precip = float(data.get('r_precip_in', 0) or 0)
                r_acres = float(data.get('r_acres', 0) or 0)
                if r_coeff > 0 and r_precip > 0:
                    vol_cf = r_coeff * (r_precip / 12) * (r_acres * 43560)
                    return [
                        f">> MODULE: TOTAL RUNOFF VOL",
                        f">> RESULT: {vol_cf:,.0f} ft³"
                    ]


            if step == 17:
                w_width = float(data.get('w_width_ft', 0) or 0)
                w_head = float(data.get('w_head_ft', 0) or 0)
                if w_width > 0 and w_head > 0:
                    q_weir = 3.33 * (w_width - (0.2 * w_head)) * (w_head ** 1.5)
                    return [
                        f">> MODULE: RECTANGULAR WEIR",
                        f">> RESULT: {q_weir:.2f} cfs"
                    ]

            if step == 18:
                g_area = float(data.get('g_area_sqft', 0) or 0)
                g_head = float(data.get('g_head_ft', 0) or 0)
                g_clog = float(data.get('g_clog_factor', 0.5) or 0.5)
                if g_area > 0 and g_head > 0:
                    effective_area = g_area * (1 - g_clog)
                    q_grate = 0.67 * effective_area * ((2 * 32.2 * g_head) ** 0.5)
                    return [
                        f">> MODULE: GRATE INLET CAPACITY",
                        f">> RESULT: {q_grate:.2f} cfs"
                    ]

            if step == 19:
                p_dia = float(data.get('p_dia_in', 0) or 0)
                p_depth = float(data.get('p_depth_in', 0) or 0)
                p_slope = float(data.get('p_slope_ft_ft', 0) or 0)
                p_n = float(data.get('p_n_val', 0.013) or 0.013)
                if p_dia > 0 and p_depth > 0 and p_slope > 0:
                    r = (p_dia / 12) / 2
                    h = p_depth / 12
                    theta = 2 * (3.14159 / 180) * (57.2958 * (1 - (h/r))) 
                    area = (r**2) * (3.14159 - (theta - (0.5 * (theta * 2).sin() if hasattr(theta, 'sin') else 0))) 
                    rh_approx = (p_dia / 12) / 4 
                    vel = (1.486 / p_n) * (rh_approx ** (2/3)) * (p_slope ** 0.5)
                    q_partial = area * vel 
                    return [
                        f">> MODULE: PARTIAL PIPE FLOW",
                        f">> RESULT: {q_partial:.2f} cfs"
                    ]

            if step == 20:
                wq_area = float(data.get('wq_area_acres', 0) or 0)
                wq_imp = float(data.get('wq_imperv_pct', 0) or 0)
                wq_rain = float(data.get('wq_rainfall_in', 1.0) or 1.0)
                if wq_area > 0:
                    rv = 0.05 + (0.009 * wq_imp)
                    wqv_cf = (wq_rain / 12) * rv * (wq_area * 43560)
                    return [
                        f">> MODULE: WATER QUALITY VOL",
                        f">> RESULT: {wqv_cf:,.0f} ft³"
                    ]

            if step == 21:
                g_cross = float(data.get('gut_cross_slope', 0) or 0)
                g_long = float(data.get('gut_long_slope', 0) or 0)
                g_flow = float(data.get('gut_flow_cfs', 0) or 0)
                g_n = float(data.get('gut_n_val', 0.016) or 0.016)
                if g_cross > 0 and g_long > 0 and g_flow > 0:
                    spread = ((g_flow * g_n) / (0.56 * (g_cross**1.67) * (g_long**0.5))) ** 0.375
                    return [
                        f">> MODULE: GUTTER SPREAD",
                        f">> RESULT: {spread:.2f} ft width"
                    ]

            if step == 22:
                r = float(data.get('r_factor', 0) or 0)
                k = float(data.get('k_factor', 0) or 0)
                ls = float(data.get('ls_factor', 0) or 0)
                c = float(data.get('c_factor', 1.0) or 1.0)
                if r > 0 and k > 0 and ls > 0:
                    tons_per_acre = r * k * ls * c
                    return [
                        f">> MODULE: ANNUAL SOIL LOSS",
                        f">> RESULT: {tons_per_acre:.2f} tons/acre/yr"
                    ]
                    
            if step == 23:
                c_flow = float(data.get('c_flow_cfs', 0) or 0)
                c_dia_ft = float(data.get('c_dia_in', 0) or 0) / 12
                c_c = float(data.get('c_form_factor', 0.02) or 0.02)
                if c_flow > 0 and c_dia_ft > 0:
                    hw_depth = c_dia_ft * (c_c * (c_flow / (c_dia_ft**2.5))**2)
                    return [
                        f">> MODULE: CULVERT HEADWATER",
                        f">> RESULT: {hw_depth:.2f} ft depth"
                    ]

            if step == 24:
                s_l = float(data.get('s_length_ft', 0) or 0)
                s_n = float(data.get('s_n_val', 0) or 0)
                s_p = float(data.get('s_precip_in', 0) or 0)
                s_s = float(data.get('s_slope', 0) or 0)
                if s_l > 0 and s_s > 0:
                    tc_sheet = (0.007 * (s_n * s_l)**0.8) / ((s_p**0.5) * (s_s**0.4))
                    return [
                        f">> MODULE: SHEET FLOW Tc",
                        f">> RESULT: {tc_sheet * 60:.2f} minutes"
                    ]

            if step == 25:
                f_l = float(data.get('f_length_ft', 0) or 0)
                f_d = float(data.get('f_dia_in', 0) or 0) / 12
                f_v = float(data.get('f_vel_fps', 0) or 0)
                f_f = float(data.get('f_friction', 0.02) or 0.02)
                if f_l > 0 and f_d > 0:
                    h_loss = f_f * (f_l / f_d) * ((f_v**2) / (2 * 32.2))
                    return [
                        f">> MODULE: PRESSURE PIPE LOSS",
                        f">> RESULT: {h_loss:.2f} ft of head"
                    ]

            if step == 26:
                sw_d = float(data.get('sw_depth_ft', 0) or 0)
                sw_s = float(data.get('sw_slope_ft_ft', 0) or 0)
                if sw_d > 0 and sw_s > 0:
                    stress = 62.4 * sw_d * sw_s
                    risk = "HIGH (Lining Req)" if stress > 1.0 else "LOW (Grass OK)"
                    return [
                        f">> MODULE: SWALE SHEAR STRESS",
                        f">> RESULT: {stress:.2f} lb/sq.ft ({risk})"
                    ]

            if step == 27:
                hp_q = float(data.get('hp_flow_gpm', 0) or 0)
                hp_h = float(data.get('hp_head_ft', 0) or 0)
                hp_e = float(data.get('hp_eff', 0.75) or 0.75)
                if hp_q > 0 and hp_h > 0:
                    horsepower = (hp_q * hp_h) / (3960 * hp_e)
                    return [
                        f">> MODULE: PUMP HORSEPOWER",
                        f">> RESULT: {horsepower:.2f} HP"
                    ]
                    
            if step == 28:
                v1 = float(data.get('v1', 0) or 0)
                v2 = float(data.get('v2', 0) or 0)
                angle_i = float(data.get('angle_i', 0) or 0)
    
                if v1 > 0 and v2 > 0:
                    sin_r = (v2 / v1) * math.sin(math.radians(angle_i))
                    if -1 <= sin_r <= 1:
                        angle_r = math.degrees(math.asin(sin_r))
                        return [f">> MODULE: SEISMIC REFRACTION", f">> REFRACTED ANGLE: {angle_r:.2f}°"]
                    return [f">> MODULE: SEISMIC REFRACTION", f">> RESULT: Total Internal Reflection"]
                    
            if step == 29:
                k = float(data.get('k_perm', 0) or 0)
                a = float(data.get('area', 0) or 0)
                i = float(data.get('h_grad', 0) or 0)
                discharge = k * i * a
                return [f">> MODULE: DARCY'S LAW", f">> DISCHARGE (Q): {discharge:.3f} m³/day"]

            if step == 30:
                z = float(data.get('depth_m', 0) or 0)
                rho = float(data.get('rho_rock', 0) or 0)
                g = 9.81
                pressure_pa = rho * g * z
                pressure_mpa = pressure_pa / 10**6
                return [f">> MODULE: LITHOSTATIC PRESSURE", f">> PRESSURE: {pressure_mpa:.2f} MPa"]

            if step == 33:
                dist = float(data.get('dist_km', 0) or 0)
                age = float(data.get('crust_age', 0) or 0)
                if dist > 0 and age > 0:
                    rate = (dist / age) / 10 
                    return [f">> MODULE: TECTONIC SPREADING", f">> RATE: {rate:.2f} cm/year"]

            if step == 34:
                obs_g = float(data.get('observed_g', 0) or 0)
                h = float(data.get('elev_m', 0) or 0)
                rho = float(data.get('rho_crust', 2670) or 2670)
                bc = 0.00004193 * rho * h
                fac = 0.3086 * h
                return [f">> MODULE: GRAVITY ANOMALY", f">> TOTAL CORRECTION: {(fac - bc):.2f} mGal"]

            if step == 35:
                p_gpa = float(data.get('pressure_gpa', 0) or 0)
                rho = float(data.get('avg_rho', 2800) or 2800)
                if p_gpa > 0:
                    depth_m = (p_gpa * 10**9) / (rho * 9.81)
                    depth_km = depth_m / 1000
                    return [f">> MODULE: MAGMA DEPTH", f">> CALCULATED DEPTH: {depth_km:.2f} km"]

            if step == 36:
                m = float(data.get('mag', 0) or 0)
                energy_joules = 10**(4.8 + 1.5 * m)
                return [f">> MODULE: SEISMIC ENERGY", f">> ENERGY: {energy_joules:.2e} Joules"]

            if step == 37:
                d10 = float(data.get('d10_mm', 0) or 0)
                c = float(data.get('c_factor', 10) or 10)
                k = c * (d10 ** 2)
                return [f">> MODULE: HYDRAULIC COND.", f">> K-VALUE: {k:.3f} cm/s"]
                    
        return [">> ERROR: BRANCH NOT FOUND"]

@occupational_sci.route('/get_fields')
def get_fields():
    try:
        step = int(request.args.get('step', 1))
        cid = int(request.args.get('cid', 1))
    except (ValueError, TypeError):
        step = 1
        cid = 1
        
    if cid == 1:
        if step == 1:
            return jsonify([
                {"id": "pipe_dia_in", "label": "Pipe Diameter (in)", "type": "number", "default": 0}, 
                {"id": "pipe_slope_ft_ft", "label": "Pipe slope (feet)", "type": "number", "default": 0}
            ])
        if step == 2:
            return jsonify([
                {"id": "p_length", "label": "Pond Length (ft)", "type": "number", "default": 0}, 
                {"id": "p_width", "label": "Pond Width (ft)", "type": "number", "default": 0}, 
                {"id": "p_depth", "label": "Pond Depth (ft)", "type": "number", "default": 0}
            ])
        if step == 3:
            return jsonify([{"id": "v_head_ft", "label": "V Head (ft)", "type": "number", "default": 0}])
        if step == 4:
            return jsonify([
                {"id": "drop_inches", "label": "Drop (in)", "type": "number", "default": 0}, 
                {"id": "time_minutes", "label": "Time (min)", "type": "number", "default": 0}
            ])
        if step == 5:
            return jsonify([
                {"id": "r_area_acres", "label": "R Area (acres)", "type": "number", "default": 0}, 
                {"id": "r_intensity_in_hr", "label": "R Intensity (Hr)", "type": "number", "default": 0}, 
                {"id": "r_coeff", "label": "R Coefficient", "type": "number", "default": 0.9}
            ])
        if step == 6:
            return jsonify([{"id": "o_area_sqft", "label": "Orafice Area (Sq. Ft)", "type": "number", "default": 0},
                {"id": "o_head_ft", "label": "Orafice Head (Ft.)", "type": "number", "default": 0}])

        if step == 7:
            return jsonify([{"id": "tc_length_ft", "label": "Time of Concentration Length (Ft)", "type": "number", "default": 0},
                {"id": "tc_slope_ft_ft", "label": "TOC Slope (Ft)", "type": "number", "default": 0}])
        if step == 8:
            return jsonify([{"id": "precip_in", "label": "Precipitation (in)", "type": "number", "default": 0},
                {"id": "cn_value", "label": "CN Value", "type": "number", "default": 0}])
        if step == 9:
            return jsonify([{"id": "b_width_ft", "label": "B Width (Ft)", "type": "number", "default": 0},
                {"id": "flow_depth_ft", "label": "Flow Depth (Ft)", "type": "number", "default": 0},
                {"id": "side_slope_z", "label": "Side Slope (z)", "type": "number", "default": 0},
                {"id": "ch_slope_ft_ft", "label": "CH Slope (Ft)", "type": "number", "default": 0}])
        if step == 10:
            return jsonify([{"id": "v_fps", "label": "Volume (Fps)", "type": "number", "default": 0}])
        if step == 11:
            return jsonify([{"id": "q_peak_inflow", "label": "Q Peak Inflow", "type": "number", "default": 0},
                {"id": "q_allowable_out", "label": "Q Allowable (out)", "type": "number", "default": 0},
                {"id": "storm_duration_min", "label": "Storm Duration (min)", "type": "number", "default": 0}])
        if step == 12:
            return jsonify([{"id": "inlet_length_ft", "label": "Inlet Length (Ft)", "type": "number", "default": 0},
                {"id": "inlet_depth_ft", "label": "Inlet Depth (Ft)", "type": "number", "default": 0}])
        if step == 13:
            return jsonify([{"id": "flow_cfs", "label": "Flow (CFS)", "type": "number", "default": 0},
                {"id": "p_dia_in", "label": "Pipe Diameter (in)", "type": "number", "default": 0}])
        if step == 14:
            return jsonify([{"id": "peak_q_cfs", "label": "Peak Q (Cfs)", "type": "number", "default": 0},
                {"id": "settle_vel_fps", "label": "Settle Velocity (Fps)", "type": "number", "default": 0}])
        if step == 15:
            return jsonify([{"id": "n_main", "label": "N Main", "type": "number", "default": 0},
                {"id": "p_main_ft", "label": "P Main (Ft)", "type": "number", "default": 0},
                {"id": "n_side", "label": "N Side", "type": "number", "default": 0},
                {"id": "p_side_ft", "label": "P Side (Ft)", "type": "number", "default": 0}])
        if step == 16:
            return jsonify([{"id": "r_coeff", "label": "R Coefficient", "type": "number", "default": 0},
                {"id": "r_precip_in", "label": "R Precipitation (in)", "type": "number", "default": 0},
                {"id": "r_acres", "label": "R Acres", "type": "number", "default": 0}])
        if step == 17:
            return jsonify([{"id": "w_width_ft", "label": "W Width (Ft)", "type": "number", "default": 0},
                {"id": "w_head_ft", "label": "W Head (Ft)", "type": "number", "default": 0}])
        if step == 18:
            return jsonify([
                {"id": "g_area_sqft", "label": "Clear Opening Area (Sq. Ft)", "type": "number", "default": 0},
                {"id": "g_head_ft", "label": "Depth of Water over Grate (Ft)", "type": "number", "default": 0},
                {"id": "g_clog_factor", "label": "Clogging Factor (0-1.0)", "type": "number", "default": 0.5}])
        if step == 19:
            return jsonify([
                {"id": "p_dia_in", "label": "Pipe Diameter (Inches)", "type": "number", "default": 12},
                {"id": "p_depth_in", "label": "Water Depth in Pipe (Inches)", "type": "number", "default": 6},
                {"id": "p_slope_ft_ft", "label": "Pipe Slope (ft/ft)", "type": "number", "default": 0.01},
                {"id": "p_n_val", "label": "Manning's n (0.013 default)", "type": "number", "default": 0.013}])
        if step == 20:
            return jsonify([
            {"id": "wq_area_acres", "label": "Drainage Area (Acres)", "type": "number", "default": 0},
                {"id": "wq_imperv_pct", "label": "Percent Impervious (0-100)", "type": "number", "default": 0},
                {"id": "wq_rainfall_in", "label": "Water Quality Rainfall (Inches)", "type": "number", "default": 1.0}])
        if step == 21:
            return jsonify([
                {"id": "gut_cross_slope", "label": "Street Cross Slope (ft/ft)", "type": "number", "default": 0.02},
                {"id": "gut_long_slope", "label": "Street Longitudinal Slope (ft/ft)", "type": "number", "default": 0.01},
                {"id": "gut_flow_cfs", "label": "Gutter Flow Rate (cfs)", "type": "number", "default": 0},
                {"id": "gut_n_val", "label": "Pavement Manning's n (0.016)", "type": "number", "default": 0.016}])
        if step == 22:
            return jsonify([
                {"id": "r_factor", "label": "Rainfall Erosivity (R)", "type": "number", "default": 0},
                {"id": "k_factor", "label": "Soil Erodibility (K)", "type": "number", "default": 0},
                {"id": "ls_factor", "label": "Slope Length/Steepness (LS)", "type": "number", "default": 0},
                {"id": "c_factor", "label": "Cover Management (C)", "type": "number", "default": 1.0}])
        if step == 23:
            return jsonify([
                {"id": "c_flow_cfs", "label": "Design Flow (cfs)", "type": "number", "default": 0},
                {"id": "c_dia_in", "label": "Culvert Diameter (Inches)", "type": "number", "default": 18},
                {"id": "c_form_factor", "label": "Inlet Coefficient (0.0098-0.03)", "type": "number", "default": 0.02}])
        if step == 24:
            return jsonify([
                {"id": "s_length_ft", "label": "Flow Length (max 300ft)", "type": "number", "default": 100},
                {"id": "s_n_val", "label": "Surface Manning n (e.g. 0.15 grass)", "type": "number", "default": 0.15},
                {"id": "s_precip_in", "label": "2-yr 24-hr Rainfall (Inches)", "type": "number", "default": 3.0},
                {"id": "s_slope", "label": "Land Slope (ft/ft)", "type": "number", "default": 0.02}])
        if step == 25:
            return jsonify([
                {"id": "f_length_ft", "label": "Pipe Length (Ft)", "type": "number", "default": 100},
                {"id": "f_dia_in", "label": "Inside Diameter (Inches)", "type": "number", "default": 4},
                {"id": "f_vel_fps", "label": "Velocity (fps)", "type": "number", "default": 5},
                {"id": "f_friction", "label": "Friction Factor (f)", "type": "number", "default": 0.02}])
        if step == 26:
            return jsonify([
                {"id": "sw_depth_ft", "label": "Design Flow Depth (Ft)", "type": "number", "default": 0},
                {"id": "sw_slope_ft_ft", "label": "Swale Slope (ft/ft)", "type": "number", "default": 0.01}])
        if step == 27:
            return jsonify([
                {"id": "hp_flow_gpm", "label": "Flow Rate (GPM)", "type": "number", "default": 100},
                {"id": "hp_head_ft", "label": "Total Dynamic Head (Ft)", "type": "number", "default": 50},
                {"id": "hp_eff", "label": "Pump Efficiency (0.1 - 0.9)", "type": "number", "default": 0.75}])\
        if step == 28:
            return [
                {"id": "v1", "label": "Velocity Layer 1 (m/s)", "type": "number", "default": 1500},
                {"id": "v2", "label": "Velocity Layer 2 (m/s)", "type": "number", "default": 2500},
                {"id": "angle_i", "label": "Incident Angle (degrees)", "type": "number", "default": 30}]
        if step == 29:
            return [
                {"id": "k_perm", "label": "Permeability (m/day)", "type": "number", "default": 10},
                {"id": "area", "label": "Cross Sectional Area (m²)", "type": "number", "default": 50},
                {"id": "h_grad", "label": "Hydraulic Gradient (dh/dl)", "type": "number", "default": 0.05}]
        if step == 30:
            return [
                {"id": "depth_m", "label": "Depth (meters)", "type": "number", "default": 1000},
                {"id": "rho_rock", "label": "Rock Density (kg/m³)", "type": "number", "default": 2700}]
        if step == 31:
            return [
                {"id": "grain_d", "label": "Grain Diameter (mm)", "type": "number", "default": 0.2},
                {"id": "rho_p", "label": "Particle Density (kg/m³)", "type": "number", "default": 2650},
                {"id": "fluid_visc", "label": "Fluid Viscosity (Pa·s)", "type": "number", "default": 0.001}]
        if step == 32:
            return [
                {"id": "parent_now", "label": "Parent Isotope (Atoms)", "type": "number", "default": 50},
                {"id": "daughter_now", "label": "Daughter Isotope (Atoms)", "type": "number", "default": 50},
                {"id": "half_life", "label": "Half-Life (Years)", "type": "number", "default": 1300000000}]
        if step == 33:
            return [
                {"id": "dist_km", "label": "Distance from Ridge (km)", "type": "number", "default": 100},
                {"id": "crust_age", "label": "Age of Crust (Million Years)", "type": "number", "default": 5}]
        if step == 34:
            return [
                {"id": "observed_g", "label": "Observed Gravity (mGal)", "type": "number", "default": 980.12},
                {"id": "elev_m", "label": "Elevation (meters)", "type": "number", "default": 500},
                {"id": "rho_crust", "label": "Average Density (kg/m³)", "type": "number", "default": 2670}]
        if step == 35:
            return [
                {"id": "pressure_gpa", "label": "Crystallization Pressure (GPa)", "type": "number", "default": 0.5},
                {"id": "avg_rho", "label": "Overburden Density (kg/m³)", "type": "number", "default": 2800}]
        if step == 36:
            return [
                {"id": "mag", "label": "Richter Magnitude (M)", "type": "number", "default": 6.0}]
        if step == 37:
            return [
                {"id": "d10_mm", "label": "Effective Grain Size (D10 in mm)", "type": "number", "default": 0.5},
                {"id": "c_factor", "label": "Hazen Coefficient (C)", "type": "number", "default": 10}]
    
    return jsonify([])

@occupational_sci.route('/run_calculation', methods=['POST'])
def run_calc():
    try:
        data = request.json  
        results = OccupationialEngine.run(data) 
        
        return jsonify(results)
      
    except Exception as e:
        print(f"CRITICAL ERROR: {e}") 
        return jsonify([">> SERVER ERROR", f">> {str(e)}"]), 500
