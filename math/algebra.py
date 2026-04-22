import math
from flask import Flask, request, jsonify, Blueprint

Algebra = Blueprint('Algebra', __name__)

class Algebra:
    @staticmethod
    def add(a, b):
        if isinstance(a, list) and isinstance(b, list):
            return list(map(lambda m, n: m + n, a, b))
        return a + b

    @staticmethod
    def sub(a, b):
        try:
            if isinstance(a, list) and isinstance(b, list):
                return list(map(lambda m, n: m - n, a, b))
            return a - b
        except Exception:
            return None 

    @staticmethod
    def div(a, b):
        try:
            if isinstance(a, list) and isinstance(b, list):
                return list(map(lambda m, n: m / n, a, b))
            return a / b
        except Exception:
            return None

    @staticmethod
    def multiply(a, b):
        try:
            if isinstance(a, list) and isinstance(b, list):
                return list(map(lambda m, n: m * n, a, b))
            return a * b
        except Exception:
            return None

    @staticmethod
    def exp(x, n):
        if n < 0:
            return Algebra.exp(1/x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 1:
            return x * Algebra.exp(x**2, (n-1)//2)
        else:
            return Algebra.exp(x**2, n//2)

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Algebra.factorial(n - 1)

@Algebra.route('/add', methods=['POST'])
def route_add():
    data = request.json
    res = Algebra.add(data.get('a'), data.get('b'))
    return jsonify({"result": res})

@Algebra.route('/sub', methods=['POST'])
def route_sub():
    data = request.json
    res = Algebra.sub(data.get('a'), data.get('b'))
    return jsonify({"result": res})

@Algebra.route('/multiply', methods=['POST'])
def route_multiply():
    data = request.json
    res = Algebra.multiply(data.get('a'), data.get('b'))
    return jsonify({"result": res})

@Algebra.route('/div', methods=['POST'])
def route_div():
    data = request.json
    res = Algebra.div(data.get('a'), data.get('b'))
    return jsonify({"result": res})

@Algebra.route('/exp', methods=['POST'])
def route_exp():
    data = request.json
    res = Algebra.exp(data.get('x'), data.get('n'))
    return jsonify({"result": res})

@Algebra.route('/factorial', methods=['POST'])
def route_factorial():
    data = request.json
    res = Algebra.factorial(int(data.get('n', 0)))
    return jsonify({"result": res})
